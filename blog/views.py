from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta
from django.core.exceptions import PermissionDenied
from .forms import PostForm, CommentForm
from .models import Post, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(featured_flag=True).order_by("-created_on")[:3]
    template_name = "index.html"


class AddStory(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "add_story.html"
    form_class = PostForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        message = 'Your draft has been saved.'
        if 'submit' in self.request.POST.keys():
            form.instance.status = 1
            message = 'Your story has been submitted for evaluation.'
        form.save()
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(AddStory, self).form_valid(form)


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm(),
            },
        )


    def post(self, request, slug, *args, **kwargs):
        post = Post.objects.filter(slug=slug)[0]
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.commenter = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted.')
        else:
            comment_form = CommentForm()
            messages.add_message(request, messages.SUCCESS, "Error occuered.  Your comment was not saved.")
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Bookmark(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.bookmark.filter(id=request.user.id).exists():
            post.bookmark.remove(request.user)
        else:
            post.bookmark.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):

    model = Post
    template_name = "update_post.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        message = 'The change has been saved.'
        if 'submit' in self.request.POST.keys():
            form.instance.status = 1
            message = 'Your story has been submitted for evaluation.'
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(UpdatePost, self).form_valid(form)


    def test_func(self):
        slug = self.request.GET.get('update_post')
        post = get_object_or_404(Post, slug=slug)
        return post.author == self.request.user
            

class DeletePost(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.author == self.request.user:
            post.delete()
            message = 'Your draft has been deleted.'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse('home'))
        else:     
            raise PermissionDenied()   


# def update_comment(request):
#     # if request is json
#     if request.method == "GET":
#         id = request.GET['id']
#         comment = get_object_or_404(Comment, id=id)
#         response = {
#             'comment' : comment.body,
#         }
#         return JsonResponse(response)



class UpdateComment(LoginRequiredMixin, UserPassesTestMixin, View):


    def get(self, request, id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=id)
        comment_form = CommentForm(instance=comment)
        slug = comment.post.slug

        return render(
            request,
            "update_comment.html",
            {
                "comment_form": comment_form
            }
        )


    def post(self, request, id, *args, **kwargs):

        comment = get_object_or_404(Comment, id=id)
        comment_form = CommentForm(self.request.POST, instance=comment)
        updated = comment_form.save(commit=False)
        updated.commneter = request.user
        updated.comment_status = 1
        slug = comment.post.slug
        if comment_form.is_valid():
            updated.save()
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


    def test_func(self):
        if self.request == 'GET':
            id = self.kwargs.get('id')
            comment = get_object_or_404(Comment, id)
            return comment.commenter == self.request.user
        return True


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, View):

    def post(self, request, id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=id)
        comment.comment_status = 2
        comment.save()
        slug = comment.post.slug
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    
    def test_func(self):
        id = self.kwargs.get('id')
        comment = get_object_or_404(Comment, id=id)
        return comment.commenter == self.request.user
       


# class MyPage(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):

#     model = Post
#     template_name = "my_page.html"


#     def get_context_data(self, *args, **kwargs):
#         context = super(MyPage, self).get_context_data(*args, **kwargs)
#         id = self.kwargs.get('pk')
#         my_posts = [Post.objects.filter(author=id)]
#         if len(my_posts) > 3:
#             my_posts, my_posts_hidden = [my_posts[:3], my_posts[3:]]
#         comments = Comment.objects.filter(commenter__id=id)
#         commented_posts = [comment.post for comment in comments]
#         # remove duplicates
#         commented_posts = list(dict.fromkeys(commented_posts))
#         if len(commented_posts) > 3:
#             commented_posts, commented_posts_hidden = [commented_posts[:3],
#                                                        commented_posts[3:]]
#         all_posts = Post.objects.all()
#         bookmarked_posts = []
#         for post in all_posts:
#             if post.bookmark.filter(id=id).exists():
#                 bookmarked_posts.append(post)
#         if len(bookmarked_posts) > 3:
#             bookmarked_posts, bookmarked_posts_hidden = [
#                 bookmarked_posts[:3], bookmarked_posts[3:] 
#             ]
#         context = {
#             'my_posts': my_posts,
#             'commented_posts': commented_posts,
#             'bookmarked_posts': bookmarked_posts 
#         }
#         return context

    # def get(self, request, id, *args, **kwargs):
    #     my_posts = Post.objects.filter(author=id)  
    #     comments = Comment.objects.filter(commenter__id=id)
    #     commented_posts = [comment.post for comment in comments]
        # remove duplicates
        # commented_posts = list(dict.fromkeys(commented_posts))
        # this can be made more concise
        # return render(
        #     request,
        #     "my_page.html",
        #     {
        #         "my_posts": my_posts,
        #         "commented_posts": commented_posts,
        #         "bookmarked_posts": bookmarked_posts
        #     },
        # )


    # def test_func(self):
    #     return self.kwargs.get('pk') == self.request.user.id


class MyPage(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk, *args, **kwargs):     
        my_posts = Post.objects.filter(author=pk)  
        comments = Comment.objects.filter(commenter__id=pk)
        commented_posts = [comment.post for comment in comments]
        # remove duplicates
        commented_posts = list(dict.fromkeys(commented_posts))
        # this can be made more concise
        all_posts = Post.objects.all()
        bookmarked_posts = []
        for post in all_posts:
            if post.bookmark.filter(id=request.user.id).exists():
                bookmarked_posts.append(post)

        return render(
            request,
            "my_page.html",
            {
                "my_posts": my_posts,
                "commented_posts": commented_posts,
                "bookmarked_posts": bookmarked_posts
            },
        )


    def test_func(self):
        return self.kwargs.get('pk') == self.request.user.id


class Search(View):
    def get(self, request, *args, **kwargs):
        category_choices = Post._meta.get_field('category').choices
        categories = [cat[1] for cat in category_choices]
        region_choices = Post._meta.get_field('region').choices
        regions = [region[1] for region in region_choices]

        posts = Post.objects.filter(status=2)

        title_query = request.GET.get('title_input')
        title_filter_type = request.GET.get('title_filter')
        author_query = request.GET.get('author_input')
        author_filter_type = request.GET.get('author_filter')
        kw_query_list = [request.GET.get('keyword_1'),
                         request.GET.get('keyword_2'),
                         request.GET.get('keyword_3')
                    ]
        min_liked_query = request.GET.get('liked_count_min')
        pub_date_min_query = request.GET.get('date_min')
        pub_date_max_query = request.GET.get('date_max')
        category = request.GET.get('category')
        region = request.GET.get('region')
        qs = []
        query_lists = []

        if title_query != '' and title_query is not None:  
            if title_filter_type == "contains":
                qs_title = posts.filter(title__icontains=title_query)
            else:
                qs_title = posts.filter(title__exact=title_query)
            if qs_title != []:
                query_lists.append(qs_title)

        if author_query != '' and author_query is not None:
            if author_filter_type == "contains":
                qs_author = posts.filter(author__username__icontains=author_query)
            else:
                qs_author = posts.filter(author__username__exact=author_query)
            if qs_author != []:
                query_lists.append(qs_author)

        for kw in kw_query_list:
            if kw != '' and kw is not None:
                qs = posts.filter(Q(title__icontains=kw) | Q(content__icontains=kw))
                query_lists.append(qs)

        if min_liked_query != '' and min_liked_query is not None:
            print('hello liked')
            qs_liked = [post for post in posts if (post.number_of_likes()>=int(min_liked_query))]
            print(qs_liked)
            if qs_liked != []:
                query_lists.append(qs_liked)

        if pub_date_min_query != '' and pub_date_min_query is not None:
            min_date_str = pub_date_min_query
            min_date = datetime.strptime(min_date_str, '%Y-%m-%d')
            qs_min_pub_date = posts.filter(published_on__date__gte=min_date)
            query_lists.append(qs_min_pub_date)

        if pub_date_max_query != '' and pub_date_max_query is not None:
            max_date_str = pub_date_max_query
            max_date = datetime.strptime(max_date_str, '%Y-%m-%d')
            qs_max_pub_date = posts.filter(published_on__date__lte=max_date)
            query_lists.append(qs_max_pub_date)

        if region != 'Choose...':
            qs_region = [post for post in posts if post.get_region_display() == region]
            query_lists.append(qs_region)
        if category != 'Choose...':
            qs_category = [post for post in posts if post.get_category_display() == category]
            query_lists.append(qs_category)

        if query_lists != []:
            qs = query_lists[0]

        if len(query_lists) > 1:
            i = 0
            for i in range(len(query_lists) - 1):
                qs = [post for post in query_lists[i] if post in query_lists[i+1]]
                i += 1 
            
        search_clicked = False
        if 'search' in self.request.GET:
            search_clicked = True  
        context = {
            'categories': categories,
            'regions': regions,
            'queryset': qs,
            'search_clicked': search_clicked
        }
        return render(request, "search.html", context)


class MoreStories(generic.ListView):
    model = Post
    template_name = "more_stories.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(MoreStories, self).get_context_data(**kwargs)
        filterargs = {
            'status': 2,
            'published_on__date__gte': datetime.utcnow() - timedelta(days=7),
            'featured_flag': False
            }
        posts = Post.objects.filter(**filterargs).order_by("-published_on")
        context['object_list'] = Post.objects.filter(**filterargs).order_by("-published_on")
        return context
