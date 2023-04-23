# General Overview:

This application offers a platform where individuals around the world can share their stories on what they are doing to save the environment.  Many people feel helpless, thinking that individuals cannot do so much.  Here, visitors can read posts written by others, leave comments and write their own stories.  Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope. 

## User Stories

**As a visitor I want to ...**
- be able to easily understand what the site is meant for and how I can use it.

**As a visitor/member I want to ...**
- take a look at many excerpts and then have access to detailed pages so that I can first have an overview of what kind of stories are posted and read the entire content of the posts that interest me.
- be able to search posts by title, author, keywords, published dates and popularity (number of likes) so I can easily access the kind of posts I am looking for.

**As a member I wan to ...**
- be able to post comments on stories so I can express my thoughts.
- be able to ‘like’ posts so I can show my appreciation for the post.
- be able to write my own story so I can share my experience with other users.
- be able to save drafts so I don't have to finish my drafts at one sitting.
- be able to edit saved drafts.
- be able to delete my drafts.
- be able to edit my comments.
- be able to delete my comments.
- have a quick access to 1. posts and drafts I wrote, 2. posts I commented on and 3. posts I bookmarked.

**As admin I want to ...**
- be able to evaluate drafts submitted by users so admin can publish only posts that are appropriate.
- display posts that seem to particularly interest readers on the home page as featured stories so that visitors are likely to read them first and will enjoy the website.
- make sure that users can update or delete their posts only before they submit their drafts.
- make sure that users can’t update or delete posts or comments written by other users.
- make sure that users can access only to their own ‘My Page,’ but not others’.


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

