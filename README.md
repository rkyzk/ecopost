# Ecopost

## Overview:

This application offers a platform where individuals around the world can share their stories on what they are doing to save the environment.  Many people feel helpless, thinking that individuals cannot do so much.  Here, visitors can read posts written by others, leave comments and write their own stories.  Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope. 

![ecopost in different screen sizes]()

## User Stories

User stories can be found [here](https://github.com/users/rkyzk/projects/5/views/1?layout=board)

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
- The full content of the post is presented.
- At the top left, the title, author, region and published dates are stated.
- At the top right the featured image is shown.
- The full text of the blog is presented below the title and the image.
- If the post is in ‘draft’ state, and if the user is the author of the post, update and delete buttons are provided below the post content.
- If the post has been published, comments are displayed on the bottom left.
- The comments are listed in the order of oldest to newest (?) so that users can follow the conversation.
- If users are logged in, they will see a comment form on the right side of the comments so they can leave comments.
- For users who haven’t logged in, a note will say ‘Want to leave comments?  Log in or Become a member,’ which includes links to log-in and sign-up pages.

**Additional Functions on Detail Page**
- By clicking on the heart below the featured image, users can like the post, or undo that action.
- Similarly, by clicking on the book sign next to the heart, users can bookmark the post, or undo the action.
- Bookmarked posts can be found on ‘My Page.’ 
- The like function is an important element of this app since it offers opportunities for interaction among users--readers can express their appreciation for the articles, and the authors will feel rewarded. 
- The bookmark function is also a useful function because users can easily find the posts at later times. 

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

### Delete Post Function (no page)
- Authors of the posts can delete their own drafts before submission by clicking the delete button on "Detail page.'
- A confirmation dialog will ask if users really want to proceed.
!! - If 'yes' is clicked the post will be deleted from the database, and the users is redirected to the home page.

### Update and Delete Comment (Delete comment has no page)
- The writer of the comment can update or delete their comment by clicking on the edit icon or the trash bin idon right by their comment on 'Detail Page.'
- If edited, the comment will be labeled with a note 'edited' so as to avoid possible confusion.
- If deleted, a note will say 'Comment deleted' in place of the comment, again in order to avoid confusion.  

### Search Stories
- Users can search post articles by title, author, keywords, published dates, number of likes, cities, countries and categories.
- They can enter one or more fields and click on search to get search results.
- The search result will be displayed below the search form.
- If no input was made or only spaces are entered, a note will say, 'Please enter at least one field.'
- If no match was found, a note will say, 'No matching results found'

### Notes on other pages
- “Become a Member” (sign up page), “log in” and “sign out” pages were taken from allauth.
- The pages were styled with my own css to match other pages.
- Line 42 in login.html was modified in order to display a note:
  'Email admin@ecopost.com if you've forgotten your password.' since setting a system to
  reset passwords is beyond this current project.

### Notes on form validation
- I used crispy forms and its validation system will display messages if the form is not valid.

**"Write Stories" and "Update Post" pages**
- If the title or the content, or both are empty, and ‘save’ or ‘submit’ button is clicked, the validation error message will say, ‘Please fill out this field’ for the first required field that’s left empty.
- Since Post model requires the title to be unique, if an existing title is entered, a validation message will say, ‘Post with this Title already exists.’

**Comment form on “Detail Page” and on “Update Comment” page**
- If form is submitted while the body of the comment is empty, the validation error message will say, ‘Please fill out this field.’

### Access Control
**By Desgin**
- Only logged-in users will see links to ‘Write Stories,’ and ‘My Page,’ so other users can’t get to the page via links.  
- Update and Delete buttons for posts and comments appear only if the user is the writer of the posts or of the comments.  Others can’t get to update pages or delete posts and comments through buttons.
- Update and Delete buttons for posts will appear only if the posts are in draft states (before submission).

**LoginRequiredMixin and UserPassestestMixin**
- In addition to access control mentioned above, in order to prevent users from getting to certain pages by entering URLs or accessing view functions (delete posts and comments), LoginRequiredMixin and/or UserPassestestMixin are used.
- ‘Write Stories’ has LoginRequiredMixin, so users who are not logged in will be sent to a 403 error page.
- ‘Update Post,’ ‘Update Comment’ and ‘Delete Comment’ views are controlled by LoginRequiredMixin and UserPassestestMixin, which checks if the user is the writer of the posts or the comments, other users will be sent to a 403 error page.
- Additionally, since posts should not be updated or deleted once submitted, the program is written to send a 403 page if users try to get to update page of a post that’s been submitted.
- Delete Posts view function has a program at line 149 in views.py to test if the user is the author of the post and that the post hasn’t been submitted and otherwise sends a 403.  Here Mixins are not used, since the post will be deleted before the test_func is run, which throws an error (explained also in bugs section.)

- - -
## MANUAL TESTING

### Testing User Stories

No. | Goals | How they are achieved | 
|:---| :--- | :--- | 
||**First Time Visitors**||   
|1| Understand what the site is for and how to use it. | An introductory paragraph on the home page describes what the site is for and how to use it. | 
|2| Become a member. | The introduction on the home page invites new users to become a member and offers a link. Another link to sign up page is displayed also on the navbar. | 
|3| Excerpts are listed. | Three featured stories chosen by editors are displayed on the home page for quick access.  Also the pages “More Stories from this Week” and “Readers’ Favorite Stories of All Time” provide lists of posts that are likely to interest visitors.|
|4| Search posts | On “Search Stories” page users can search posts by various factors.  The link to the page is provided in the navbar regardless to the users’ log-in status. | 
||||  
||**Members**||
|5| Leave comments | On “Detailed page” logged-in members are able to post comments.
|6| ‘Like’ posts | Logged-in members are able to click on the heart sign to ‘like’ posts.  Clicking the heart again will undo the action.|
|7| Write posts | On ‘Write Stories’ page users can write their own posts and submit them.  The posts will be published if admin of the site approves of them. |
|8| Save posts | By clicking ‘Save’ button on ‘Write stories’ page users can save their drafts for editing later on. |
|9| Edit posts | By clicking ‘Update’ button on “Detail Page,” users can update their drafts. |
|10|Delete posts | By clicking ‘Delete’ button on “Detailed Page,” they can delete their drafts. |
|11| Edit comments | By clicking edit icon, users can update their comments. |
|12| Delete comments | By clicking trash bin icon, users can delete their comments. |
|13| Quick access to one's own posts and other posts | ‘My page’ displays lists of posts written, commented and bookmarked by the user. |
||||
||**Admin**||
|14| Select posts to be published | Posts’ status is set to ‘Submitted’ when users submit their drafts, and they will not be displayed in public.  Only when admin changes the status to ‘Published,’ the posts will be publicized. |
|15| Let users see the most interesting posts |Three featured stories chosen by admin will be displayed on the home page, where the users will see immediately when they visit the site. |
|16| Allow users to update or delete posts only before submission | Update and Delete buttons for posts appear only if posts are in ‘draft’ status.  In addition, trying to update or delete posts that have been submitted will display a 403 error page.|
|17| Allow only the author to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the user who is logged in as the author of the posts and comments to update or delete their writings. |
|18|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |

### Testing Features

|Test No.|Feature|Preparation Steps if any|Test Steps|Expected results|Actual results|Pass/Fail|Date|Test conducted by|
||Logo|||||||
|1.|Logo|Go to “Search Stories”|Click on the logo|Redirected to the home page|Redirected to the home page|pass|2023/4/29|Reiko Yazaki|
||**Navigation links**|||||||
||Test the active page is underlined|||||||
|2|”Home”|Go to the home page|Check which link is underlined|”Home” is underlined|”Home” is underlined |pass|2023/4/29|Reiko Yazaki|
|3|”Search Stories”|Go to “Search Stories” page|Check which link is underlined|”Search Stories” is underlined|”Search Stories” is underlined |pass|2023/4/29|Reiko Yazaki|
|4|”Become A Member”|Go to “Become A Member” page|Check which link is underlined|” Become A Member” is underlined|” Become A Member” is underlined |pass|2023/4/29|Reiko Yazaki|
|5|”Log in”|Go to “Log in” page|Check which link is underlined|” Log in” is underlined|” Log in” is underlined |pass|2023/4/29|Reiko Yazaki|
|6|”Write Stories”|Log in and go to “Write Stories” page|Check which link is underlined|” Write Stories” is underlined|”Write Stories” is underlined |pass|2023/4/29|Reiko Yazaki|
|Notes||Stay logged in for tests no. 7-13||||||
|7|”Write Stories”|Go to “Write Stories” page|Check which link is underlined|” 
Write Stories” is underlined|”Write Stories” is underlined |pass|2023/4/29|Reiko Yazaki|
|8|”My Page”|Go to “My Page”|Check which link is underlined|” My Page” is underlined|” My Page” is underlined |pass|2023/4/29|Reiko Yazaki|
|9|”Log out”|Go to “My Page”|Check which link is underlined|”Log out” is underlined|”Log out” is underlined |pass|2023/4/29|Reiko Yazaki|
||Test the link will redirect to the right page |||||||
|10|”Home”|Go to “Search Stories” page|Click on “Home”|Redirected to ”Home | Redirected to ”Home”|pass|2023/4/29|Reiko Yazaki|
|11|”Search stories”|Go to “Home”|Click on “Search Stories”|Redirected to ”Search Stories” | Redirected to ”Search Stories”|pass|2023/4/29|Reiko Yazaki|
|12|”Write Stories”|Go to “Home”|Click on “Write Stories”|Redirected to ” Write Stories” | Redirected to ” Write Stories”|pass|2023/4/29|Reiko Yazaki|
|12|”My Page”|Go to “Home”|Click on “My Page”|Redirected to ”My Page” | Redirected to “My Page”|pass|2023/4/29|Reiko Yazaki|
|13|”Log out”|Go to “Home” |Click on “Log out”|Redirected to ”Log out” | Redirected to “Log out”|pass|2023/4/29|Reiko Yazaki|
|14|”Become a Member”|Log out and go to “Home”|Click on “Become a Member”|Redirected to ” Become a Member” | Redirected to “Become a Member”|pass|2023/4/29|Reiko Yazaki|
|15|”Log in”|Go to “Home”|Click on “Log in”|Redirected to ”Log in”| Redirected to “Log in”|pass|2023/4/29|Reiko Yazaki|

- - -


## Wireframes
Wireframes for the app can be found [here](https://wireframe.cc/pro/pp/873798723651976)



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

