from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import PostForm, PhotoForm, CommentForm
from .models import Post, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(featured_flag=True).order_by("-created_on")
    template_name = "index.html"


class AddStory(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        """Post an empty form for writing a new post """
        return render(
            request,
            "add_story.html",
            {
                "post_form": PostForm(),
                "photo_form": PhotoForm()
            }
        )

    
    def post(self, request, *args, **kwargs):
        """Save or submit a new post"""
        post_form = PostForm(self.request.POST)
        photo_form = PhotoForm(self.request.POST, self.request.FILES)
        if post_form.is_valid() and photo_form.is_valid():
            post_form.instance.author = self.request.user
            photo = photo_form.save(commit=False)
            post_form.instance.featured_image = photo.image
            if 'submit' in self.request.POST.keys():
                post_form.instance.status = 1
                post_form.save()
                messages.add_message(self.request, messages.SUCCESS, 'Your draft has been submitted.')
            else:
                post_form.save()
                messages.add_message(self.request, messages.SUCCESS, 'Your draft has been saved.')    
        else:
            print("error occured")
        return render(
            request,
            "add_story.html",
            {
                "post_form": PostForm(),
                "photo_form": PhotoForm()
            }
        )


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
            comment_form.instance.email = request.user.email
            comment_form.instance.commenter = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, message.SUCCESS, 'Your comment has been submitted.')
        else:
            comment_form = CommentForm()
            messages.add_message(request, message.SUCCESS, "Error occuered.  Your comment was not saved.")
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


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        # Not Working at all
        # if post.status == 2:
        #     messages.add_message(self.request, messages.INFO, "You can't update a post that's been published.")
        #     return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        original_data = {
                            "title": post.title,
                            "content": post.content,
                            "region": post.region,
                            "category": post.category,
                        }

        image = post.featured_image.image

        return render(
            request,
            "update_post.html",
            {
                "post_form": PostForm(initial=original_data),
                "photo_form": PhotoForm(image),
                "post": post
            }
        )


    def test_func(self):
        print(dir(self.request.GET.values))
        return True

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post_form = PostForm(self.request.POST, instance=post)
        photo_form = PhotoForm(self.request.POST, self.request.FILES)
        
        if post_form.is_valid() and photo_form.is_valid:
            post_form.instance.author = self.request.user
            photo = photo_form.save(commit=False)
            # if photo.image is None:
            #     post_form.instance.featured_image = post.featured_image
            # else:
            post_form.instance.featured_image = photo.image

            if 'submit' in self.request.POST.keys():
                post_form.instance.status = 1
                post_form.save()
                messages.add_message(self.request, messages.SUCCESS, 'Your draft has been submitted.')
            else:
                post_form.save()
                messages.add_message(self.request, messages.SUCCESS, 'Your draft has been saved.')

        else:
            messages.add_message(self.request, messages.INFO, "Error occured.  The change hasn't been saved.")
            print ("non", post_form.non_field_errors())   
            field_errors = [(field.label, field.errors) for field in post_form]
            print ("field", field_errors)
            print (post_form.errors)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))