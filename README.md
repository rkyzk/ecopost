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

