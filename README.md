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

