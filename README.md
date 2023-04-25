# Ecopost

## Overview:

This application offers a platform where individuals around the world can share their stories on what they are doing to save the environment.  Many people feel helpless, thinking that individuals cannot do so much.  Here, visitors can read posts written by others, leave comments and write their own stories.  Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope. 

## User Stories

**As a visitor I can ...**
- easily understand what the site is meant for and how I can use it.

**As a visitor/member I can ...**
- take a look at many excerpts and then have access to detailed pages so that I can first have an overview of what kind of stories are posted and read the entire content of the posts that interest me.
- search posts by title, author, keywords, published dates and popularity (number of likes) so I can easily access the kind of posts I am looking for.

**As a member I can ...**
- post comments on stories so I can express my thoughts.
- ‘like’ posts so I can show my appreciation for the post.
- write my own story so I can share my experience with other users.
- save drafts so I don't have to finish my drafts at one sitting.
- edit saved drafts.
- delete my drafts.
- edit my comments.
- delete my comments.
- have a quick access to posts and drafts I wrote, posts I commented on as well as posts I bookmarked.

**As admin I can ...**
- evaluate drafts submitted by users so admin can publish only appropriate posts.
- make it easy for readers to find posts that are interesting for them so that they enjoy their experience at the site.
- make sure that users can update or delete their posts only before they submit their drafts.
- make sure that users can’t update or delete posts or comments written by other users.
- make sure that users can access only to their own ‘My Page,’ but not others’.

## Features in Nutshell:
Users can see lists of excerpts from
-	featured stories
-	posts published in the previous 7 days
-	popular stories of all time
-	posts written by them
-	posts commented by them
-	posts bookmarked by them
Users can read the entire content of the post
Users can search stories by title, authors and other factors
Users can sign up to become members
Members can like and bookmark posts
Members can leave comments for the posts
Members can edit and delete comments
Members can write their own stories and submit them for evaluation
Members can update or delete their posts before submitting them

## Notes on the Design 
The overall appearance is kept simple and clean in order to avoid interfering with various colors that the featured images will bring in.

**About the Colors**
- The background is kept white.
- Beige, green and blue are used for titles, navigation and links since these colors are the colors of soil, the ocean, the sky and plants, which suits the theme of the site.
- In order to offer some originality, I used greenish blue and greenish beige instead of typical blue and beige.

**About the Fonts**
- Montserrat was used for headings because it is stylish and gives a pleasant contrast to the rest when used sparingly.
- For the content Lato is used since it is readable and familiar to users. 

## Detailed Look at Each Part and Function

### Navigation (common to all pages)
- The logo of the website is located on the left side of the navigation bar.
- A clover is chosen for the logo because it’s a widely liked symbol and is associated with good luck and hope, giving a friendly and positive impression.   
- On the right side, links to other pages are provided.
- Logged-in users will find links to ‘Home,’ ‘Search,’ ‘Write Stories,’ ‘My Page’ and ‘Log out.’
- Other users will find links to ‘Home,’ ‘Search,’ ‘Become a Member,’ and ‘Log in.’
- These terms clear indicates what these linked pages will present.
- Only 'My Page' may not be clear for first-time visitors, but if they navigate to the page, they will see lists of posts that are grouped with clearly labeled categories, so there shouldn't be any confusion. 

### Footer (common to all pages)

### Home Page

**Heading**
- The heading at the center states the title of this website ‘ecopost.’
- A graphic of earth is placed on the right side.
- This graphic serves as a reminder that we want to protect this beautiful planet.  

**Introduction**
- Below the heading an introductory paragraph explains what the site is for and how to use it.
- The paragraph encourages users to take part in the blog. 
- The first sentence addresses the problem that many people share – that they feel helpless, thinking individuals cannot do much to save the environment, and that is meant to establish immediate connection with the visitors.
- Then the rest of the paragraph offers a possible solution to the users' helpless feeling, inviting them to read the posts and connect with others.    
- The paragraph aims to capture readers’ interests and motivates them to participate in this app in a welcoming and concise manner. 

**Featured Stories Section**
- Among the posts that are submitted in the week, managers of the site will choose three ‘featured stories’ that are most likely to capture readers’ interests and will display in this section.  
- The featured image, title, author, published date and the excerpt will be shown, so that users can have a general idea of what each post is about.
- Each excerpt has a link that says ‘Read the full story,’ which will take users to the detail page that shows the full content of the post.
- Presenting a few featured stories on the home page has advantages: it removes from the visitors the stress of having to choose what to read and also increases the chance of users liking the site and wanting to revisit it.  

**Links to More Post Articles**
- At the bottom of the page, links to ‘More stories from this week’ and ‘Readers’ favorite stories of all time’ are provided.
- This invites users to explore more post articles.  

### "More Stories from This Week" and Readers' Favorite Stories of All Time"
- 'More Stories from This Week' will show a list of post articles published in the previous 7 days except the featured stories.
- "Readers' Favorite Stories of All Time" shows a list of post articles that are liked more times than others.
- I made this page 'Readers' Favorite Stories of All Time' since interesting posts are worth reading regardless to how old they are.
- The managers can set the number of likes above which posts are going to be included on this page.
- Each page will show 6 posts, and if there are more than 6 posts, the posts will be paginated.

### Detail Page
- 


### Write Stories
- Here logged-in members can write their own stories they woudl like to share.
- The fields are: title, content, featured image (optional), cateogry (select box), city, country (select box)
- if no image is uploaded as featured image, a default graphic image will be applied for the post.
- Users can click on 'save' to save drafts so they can edit them later, or click 'submit' to submit the articles.
- In this setting, if the article is submitted, it will be evaluated by the managers of the site  (revise)
- If submit button is clicked, a confirmation dialog box will tell users that they will not be able to edit or delete the post once submitted.

### Update Post
- Authors of the posts can update their own drafts before submission.
- They can update the post by writing over prepopulated fields or uploading a new image.
- They can 'save' the change , 'submit' the post, or 'cancel' updating.

### Delete Post
- Authors of the posts can delete their own drafts before submission by clicking the delete button on "Detail page.'
- A confirmation dialog will ask if users really want to proceed.
!! - If 'yes' is clicked the post will be deleted from the database, and the users is redirected to the home page.

### Update and Delete Comment
- The writer of the comment can update or delete their comment by clicking on the edit icon or the trash bin idon right by their comment on 'Detail Page.'
- If edited, the comment will be labeled with a note 'edited' so as to avoid possible confusion.
- If deleted, a note will say 'Comment deleted' in place of the comment, again in order to avoid confusion.  

### Search Stories
- Users can search post articles by title, author, keywords, published dates, number of likes, cities, countries and categories.
- They can enter one or more fields and click on search.
- The search result will be displayed below the search form.



### Control  ----?
- Some pages of this app are equipped with UserRequiredMixin and UserPassesTestMixin so they are accessible only for certain users and will send 403 errors if others attempt to reach the pages.
- 'Write Stories' can be accessed only by logged in members.
- 'Update Post' can be accessed only by the author of the post when he/she is logged in.
- 'Update Comment' can be accessed only by the writer of the comment when he/she is logged in.
- 'My Page' is accessible only by the user   ??  when he/she is logged in.

**other forms of control**
- Besides the two Mixin,   control access by displaying elements of html depending on the conditions.
- Update and delete buttons are displayed only when the user is the one who wrote the posts or the comments.



crispy forms are used.
allauth is used.  Login, Sign out, Sign up pages


\

bugs

* Post couldn't be created through add_story.html.  Integrity error.  Set slugify and worked.
* When posts are made on the admin panel, they have p tags (<p> and </p>) around the content and 
that appears on the page.  --> still need to fix.


log in user id =2, click on my page and got
Reverse for 'post_detail' with arguments '('',)' not found.

search.html
Reverse for 'post_detail' with arguments '('',)' not found.
The word 'search' was recognized as slug.  changed the url from '<slug:slug>/post_detail' to 'detail/<slug:slug>'
and search.html was rendered.

urls.py
'/detail/' added slash at the end and the issue was resolved.

test_views 
can_add_post didn't created a post.  logged in the user and was able to create a post.

add-story bottom confirm submit JS not working 

post-detail footer appears in the middle if content is small



https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests

my page how to get parameter id to test user == id



turn navbar to hamburger menu
https://stackoverflow.com/questions/70370519/how-can-i-turn-my-navbar-into-hamburger-menu-for-mobile-using-responsive-design

