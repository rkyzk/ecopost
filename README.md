# Ecopost

## CONTENTS

* [Overview](#overview)
* [User Stories](#user-stories)
* [Features in Nutshell](#features-in-nutshell)
* [Wireframes](#wireframes)
* [Notes on Design](#notes-on-design)
* [Each Part and Function in Detail](#each-part-and-function-in-detail)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
- - -

## Overview

This application offers a platform where individuals around the world can share their stories on what they are doing to save the environment.  Many people feel helpless, thinking that individuals cannot do so much.  Here, visitors can read posts written by others, leave comments and write their own stories.  Users can connect with others who are concerned about the environmental crisis, get motivated to take actions, or at least find some hope. 

![ecopost in different screen sizes]()

## User Stories

User stories can be found [here.](https://github.com/users/rkyzk/projects/5/views/1?layout=board)

## Features in Nutshell:
Users can see lists of excerpts from
-	featured stories
-	posts published in the previous 7 days
-	popular stories of all time
-	posts written by them
-	posts commented by them
-	posts bookmarked by them

Users can read the entire content of the posts<br>
Users can search stories by title, authors and other factors<br>
Users can sign up to become members<br>
Members can like and bookmark posts<br>
Members can leave comments for the posts<br>
Members can write their own stories and submit them for evaluation<br>
Members can edit and delete comments<br>
Members can update or delete their posts before submitting them<br>

## Wireframes
Wireframes for the app can be found [here.](https://wireframe.cc/pro/pp/873798723651976)
Please click on "Homepage" in the upper left corner to see wireframes of each page of the app.

## Notes on Design 
The overall appearance is kept simple and clean in order to avoid interfering with various colors that the featured images will bring in.

**About the Colors**
- Beige, green and blue are used for titles and navigation links. These colors are the colors of soil, the ocean, the sky and plants, so they suit the theme of the site.

**About the Fonts**
- Montserrat Alternates was used for headings because it's stylish and stands out from the rest when used sparingly.
- For the content Lato is used since it's readable and familiar to users. 

## Each Part and Function in Detail

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

### Notes on Other Pages
- “Become a Member” (sign up page), “log in” and “sign out” pages were taken from allauth.
- The pages were styled with my own css to match other pages.
- Line 42 in login.html was modified in order to display a note:
  'Email admin@ecopost.com if you've forgotten your password.' since setting a system to
  reset passwords is beyond this current project.

### Access Control
**By Desgin**
- Only logged-in users will find links to ‘Write Stories’ and ‘My Page’ in the navigation bar so other users can’t get to the page via the links.  
- Update and Delete buttons for posts and comments appear only if the user is the writer of the posts or of the comments.  Others can’t get to update pages or delete posts and comments through buttons.
- Update and Delete buttons for posts will appear only if the posts are in draft states (before submission).

**LoginRequiredMixin and UserPassestestMixin**
- In addition to access control mentioned above, in order to prevent users from getting to certain pages by entering URLs or accessing view functions (delete posts and comments), LoginRequiredMixin and/or UserPassestestMixin are used.
- ‘Write Stories’ has LoginRequiredMixin, so users who are not logged in will be sent to a 403 error page.
- ‘Update Post,’ ‘Update Comment’ and ‘Delete Comment’ views are controlled by LoginRequiredMixin and UserPassestestMixin, which checks if the user is the writer of the posts or the comments, other users will be sent to a 403 error page.
- Additionally, since posts should not be updated or deleted once submitted, the program is written to send a 403 page if users try to get to update page of a post that’s been submitted.
- Delete Posts view function has a program at line 149 in views.py to test if the user is the author of the post and that the post hasn’t been submitted and otherwise sends a 403.  Here Mixins are not used, since the post will be deleted before the test_func is run, which throws an error (explained also in bugs section.)

- - -
## Automated Testing
Automated tests can be found in test_models.py, test_forms.py and test_views.py

Line index of views tested in test_views.py
- PostListView line 86-156
- AddStoryView line 159-291
- PostLikeView line 294-308
- BookmarkView line 311-316
- UpdateCommentView line 328-359
- DeleteCommentView line 362-367
- UpdatePostView line 370-521
- DeletePostView line 524-554
- MoreStoriesView line 557-568
- PopularStoriesView line 571
- MyPageView line

## Manual Testing
I conducted manual testing for the aspects that weren't covered in automated testing.

### Testing User Stories

No. | Goals | How they are achieved | 
|:---| :--- | :--- | 
||**First Time Visitors**||   
|1| Understand what the site is for and how to use it. | An introductory paragraph on the home page describes what the site is for and how to use it. | 
|2| Become a member. | An introductory paragraph on the home page invites users to become a member.  In addition, a link to sign up page is displayed in the navbar. | 
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
|13| Quick access to one's own posts and other posts |‘My page’ displays lists of posts written, commented and bookmarked by the user.|
||||
||**Admin**||
|14| Select posts to be published | Posts’ status is set to ‘Submitted’ when users submit their drafts, and they will not be displayed in public.  Only when admin changes the status to ‘Published,’ the posts will be publicized. |
|15| Let users see the most interesting posts |Three featured stories chosen by admin will be displayed on the home page, where the users will see immediately when they visit the site. |
|16| Allow users to update or delete posts only before submission | Update and Delete buttons for posts appear only if posts are in ‘draft’ status.  In addition, trying to update or delete posts that have been submitted will display a 403 error page.|
|17| Allow only the author to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the user who is logged in as the author of the posts and comments to update or delete their writings. |
|18|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |

### Testing Features
As preparatory steps for the following tests:
1. create a user with username "testuser", an email "test@ecopost.com" and a password "gR48NmYr1"
2. Log in as "testuser"
3. make 10 posts with the following field values:
title: blog 1, blog 2, blog 3, blog 4, blog 5, blog 6, blog 7, blog 8, blog 9, blog 10
content: (for all of them): test content
city: Dublin
country: Ireland
4. go to admin panel.
5. publish blog 1-10 one by one in the order.
6. set featured_flag True for blog 1-3.
7. go to "Detail Page" of blog 4-10 and click on like button

#### Testing common features in all pages
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|19.|Logo link|Go to “Search Stories”|Click on the logo|Redirected to the home page|Redirected to the home page|pass|2023/4/29|
|||||||||
||**Navigation links**|||||||
|20|”Home”|Go to “Search Stories” page|Click on “Home”|Redirected to ”Home"|Redirected to ”Home”|pass|2023/4/29|
|21|”Search stories”|Go to “Home”|Click on “Search Stories”|Redirected to ”Search Stories”|Redirected to ”Search Stories”|pass|2023/4/29|
|22|”Become a Member”|Log out if you haven't.  Go to “Home” page|Click on “Become a Member”|Redirected to ”Become a Member” | Redirected to “Become a Member”|pass|2023/4/29|
|23|”Log in”|Go to “Home” page|Click on “Log in”|Redirected to ”Log in”|Redirected to “Log in”|pass|2023/4/29|
|8|”Write Stories”|Log in and go to “Home” page|Click on “Write Stories”|Redirected to ” Write Stories”|Redirected to ” Write Stories”|pass|2023/4/29|
|9|”My Page”|Go to “Home” page|Click on “My Page”|Redirected to ”My Page”|Redirected to “My Page”|pass|2023/4/29|
|10|”Log out”|Go to “Home” page|Click on “Log out”|Redirected to ”Log out”|Redirected to “Log out”|pass|2023/4/29|

**Testing hamburger menu for screen sizes below 700px**<br>
*Conduct test no. and consecutively without any actions in between*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||Hamburger menu| set the window size to 690px | click on the hamburger menu | the Menu box opens |the Menu box opens| pass|2023/4/30|
||Hamburger menu| --| click on the hamburger menu for the second time | the Menu box closes |the Menu box closes| pass|2023/4/30|
|||||||||
||**links in the footer**||||||
|11|link to facebook|Go to “Home” page|Click on the facebook icon|Redirected to facebook site|Redirected to facebook site| pass|2023/4/29|
|12|link to twitter|Go to “Home” page|Click on the twitter icon|Redirected to twitter site|Redirected to twitter site| pass|2023/4/29|
|13|link to instagram|Go to “Home” page|Click on the instagram icon|Redirected to instagram site|Redirected to instagram site| pass|2023/4/29|
|||||||||
||**The flash messages**||||||
|| setTimeout function in line 2-6 of script.js | log out | log in as testuser | Redirected to the home page.  The message "Successfully signed in as testuser" will show up and disappear after 5 seconds. |Redirected to the home page.  The message "Successfully signed in as testuser" shows up and disappears after 5 seconds.| pass|2023/4/30|

#### Testing features on individual pages
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||**“Home” Page**||||||||
|14|link ”become a member” in the introduction |Go to “Home”|Click on the link|Redirected to "Become a member."| Redirected to "Become a member."|pass|2023/4/29|
|14|link ”Read the full story” at the bottom of "blog 3" |Go to “Home”|Click on the link|Detail page of "blog 3" will be displayed.| Detail page of "blog 3" is displayed.|pass|2023/4/29|
|15|link ”Read the full story” at the bottom of "blog 2" |Go to “Home”|Click on the link|Detail page of "blog 2" will be displayed.| Detail page of "blog2" is displayed.|pass|2023/4/29|
|16|link ”Read the full story” at the bottom of "blog1" |Go to “Home”|Click on the link|Detail page of "blog 1" will be displayed.| Detail page of "blog 1" is displayed.|pass|2023/4/29|
|17|link ”More stories from this week” |Go to “Home” page|Click on the link|Redirected to “More stories from this week”| Redirected to “More stories from this week”|pass|2023/4/30|
|18|link ”Readers’ favorite stories of all time” |Go to “Home” page|Click on the link|Redirected to ”Readers’ favorite stories of all time” |Redirected to ”Readers’ favorite stories of all time”|pass|2023/4/30|
|||||||||
||**"Detail Page"**|||||||
||link to "Become a Member"|Log out|Click on the link on the right side of the comments section|Redirected to "Sign up" page|Redirected to "Sign up" page|pass|2023/5/1|
||link to "Sign in"|--|Click on the link|Redirected to "Sign in" page|Redirected to "Sign in" page|pass|2023/5/1|

*Testing validation messages on Leave Comments section on “Detail Page”*
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|49|Leave the comment text box empty| Log in as testuser and go to "Detail Page" page of "blog 1"| click on 'Submit' under comment field | A message says "Please fill out this field"| A message says "Please fill out this field"| pass|2023/4/30|

*Testing buttons to update/delete comments*
Conduct test no. consecutively.
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||Update comment button|Log in as testuser and go to "Detail Page" of "blog 1." Enter "test comment" in the text box and click on 'Submit' | Click on the update icon next to the comment.|"Update Comment" page will be displayed.|"Update Comment" page will be displayed.|pass|2023/5/2 
||Delete comment button|Log in as testuser and go to "Detail Page" of "blog 1." | Click on the trash bin icon next to the comment.|Confirmation dialog "Are you sure you want to delete your comment?" will show up. |Confirmation dialog "Are you sure you want to delete your comment?" shows up. |pass|2023/5/2 |
|||||||||
||**"More Stories"**|Conduct test. no   consecutively||||||
||link 'NEXT' if paginated|--|Click on NEXT|The second page is displayed.|The second page is displayed.|pass|2023/5/2|
||link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|2023/5/2|
||content of the page|--|Go to "More Stories"| Blog 5-10 are displayed in the descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in the descending order and blog 4 is displayed on the second page.|pass|2023/5/2|
||**"Popular Stories"**|Conduct test. no   consecutively||||||
||link 'NEXT' if paginated|--|Click on NEXT|The second page is displayed.|The second page is displayed.|pass|2023/5/2|
||link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|2023/5/2|
||content of the page|--|Go to "Popular Stories"| Blog 5-10 are displayed in the descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in the descending order and blog 4 is displayed on the second page.|pass|2023/5/2|
||Check if the right posts will be listed.|Log in as testuser and create a new post with title 'blog 11.' Publish the post on the admin panel.|Go to "Detail Page" of blog 11 and 'like' the post.|'blog 11' will be displayed on 'Popular Stories' page.|'blog 11' is not shown immediately after it is made. When I stopped the server and reran it, blog 11 appeared on the page.|fail|2023/5/5|

**"Search Stories" page**
As preparatory steps:
1. log in as testuser
2. Make a post
title: blog test search
content: content
city: Berlin
country: Germany

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||Enter letters in the field "Liked more than" field|Enter 'a' in the field|Click on 'Search'|'a' won't be shown in the input box, and a message "Please enter at least one field." will appear in "Search Results" section.|'a' isn't shown in the input box, and a message "Please enter at least one field." appears in "Search Results" section.|pass|2023/5/2|
||test search by country|--|Enter 'Germany' for country.  Click on 'Search'|'blog test search' will be displayed under Search Results|'blog test search' is displayed under Search Results|pass|2023/5/4|

*Testing case sensitivity
As preparatory steps for test no. :
- Create users "John" and "susan" 
- log in as "John," and on "Write Stories" page, make two posts:
1. title: 'Gray Cat'; content: 'test'; city: 'lowercased city'; country: 'Afghanistan'
2. title: 'white cat'; content: 'test'; city: 'Capitalized City'; country: 'Afghanistan'
- log in as "susan" and make one post:
title: 'Brown Dog'; content: 'test'; city: 'test'; country: 'Afghanistan'

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||get capitalized title - contains|go to "Search" page. | Enter 'gray cat' for title, select 'contains,' click on 'Search'|Blog "Gray Cat" will be displayed.|Blog "Gray Cat" is displayed.|pass|2023/5/2|
||get capitalized title - is exactly |go to "Search" page. | Enter 'gray cat' for title, select 'is exactly,' click on 'Search'|Blog "Gray Cat" will be displayed.|Blog "Gray Cat" is displayed.|pass|2023/5/2|
||get lowercased title - contains|go to "Search" page. | Enter 'White Cat' for title, select 'contains,' click on 'Search'|Blog "white cat" will be displayed.|Blog "white cat" is displayed.|pass|2023/5/2|
||get lowercased title - is exactly |go to "Search" page. | Enter 'White Cat' for title, select 'is exactly,' click on 'Search'|Blog "white cat" will be displayed.|Blog "white cat" is displayed.|pass|2023/5/2|
||get capitalized author - contains|go to "Search" page. | Enter 'john' for author, select 'contains,' click on 'Search'|Blogs "Gray Cat" and "white cat" will be displayed.|Blogs "Gray Cat" and "white cat" are displayed.|pass|2023/5/2|
||get capitalized author - is exactly |go to "Search" page. | Enter 'john' for author, select 'is exactly,' click on 'Search'|Blog "Brown Dog" will be displayed.|Blog "Brown Dog" is displayed.|pass|2023/5/2|
||get lowercased author - contains|go to "Search" page. | Enter 'Susan' for author, select 'contains,' click on 'Search'|Blog "Brown Dog" will be displayed.|Blog "Brown Dog" is displayed.|pass|2023/5/2|
||get lowercased title - is exactly |go to "Search" page. | Enter 'Susan' for author, select 'is exactly,' click on 'Search'|Blog "Brown Dog" will be displayed.|Blog "Brown Dog" is displayed.|pass|2023/5/2|
||get capitalized city - contains|go to "Search" page. | Enter 'capitalized city' for city, select 'contains,' click on 'Search'|Blog "white cat" will be displayed.|Blog "white cat" are displayed.|pass|2023/5/2|
||get capitalized city - is exactly |go to "Search" page. | Enter 'capitalized city' for city, select 'is exactly,' click on 'Search'|Blog "white cat" will be displayed.|Blog "white cat" is displayed.|pass|2023/5/2|
||get lowercased city - contains|go to "Search" page. | Enter 'Lowercased City' for city, select 'contains,' click on 'Search'|Blog "Gray Cat" will be displayed.|Blog "Gray Cat" is displayed.|pass|2023/5/2|
||get lowercased city - is exactly |go to "Search" page. | Enter 'Lowercased City' for city, select 'is exactly,' click on 'Search'|Blog "Gray Cat" will be displayed.|Blog "Gray Cat" is displayed.|pass|2023/5/2|

**Testing "Write Stories" page**
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|37|Leave all fields empty| -- | click on 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |2023/4/30|
|38|Leave all fields empty| -- | click on 'submit' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |2023/4/30|
|39|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click on 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |2023/4/30|
|40|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click on 'submit' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|2023/4/30|
|41|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click on 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the content | pass|2023/4/30|
|42|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click on 'submit' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|2023/4/30|
|41|Leave city empty | Enter 'test title 1' for title, 'content' for content, select 'Afghanistan' for country | click on 'save' | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|2023/4/30|
|42|Leave city empty | Enter "test title 1" for title, 'content' for content, select 'Afghanistan' for country | click on 'submit' | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|2023/4/30|
|41|Select nothing for country | Enter "test title 1" for title, 'content' for content, 'test city' for city | click on 'save' | A message says "Please select an item in the list" for the country" | A message says "Please fill out this list" for the country" | pass|2023/4/30|
|42|Select nothing for country | Enter 'test title 1' for title, 'content' for content, 'test city' for city | click on 'submit' | A message says "Please select an item in the list" for the country | A message says "Please fill out this list" for the country | pass|2023/4/30|
|100|enter spaces | enter spaces in 'title,' 'content' and 'city'| click on 'save' | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |2023/4/30|
|101|enter spaces | enter spaces in 'title,' 'content' and 'city'| click on 'submit' | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |2023/4/30|
|102|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country| click on 'save' | A message says "Please fill out this field" for the title | A message says "This field is required." appears for title, content and city | fail |2023/4/30|
|103|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country (Go on to test no. without any actions.)| click on 'submit' | A message says "Please fill out this field" for the title | Confimation dialog before submitting posts appears | fail |2023/4/30|
|103|confirmation dialog - cancel|--|Click on 'cancel' | The dialog disappears. | The dialog disappears. | pass |2023/5/4|
|103|confirmation dialog - ok|--|Click on 'Submit' and 'OK' in the dialog | Message 'This field is required' will be displayed for title, content and city. | Message 'This field is required' will be displayed for title, content and city. | pass |2023/5/4|

**Testing transformation of images during upload** ("Write Stories" and "Update Stories")
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||code in line 32-41 in models.py|Go to ‘Write Stories.’ Enter ‘test image transformation’ for title, ‘content’ for content, ‘test’ for city, ‘Afghanistan’ for country, upload ‘test_transformation.jpg,’ and click on ‘Save’|Inspect the photo| The photo will be cropped to 510 x 340 px. The photo shows the face and the torso of the person (testing the function “gravity: ‘auto’”)  The file size is significantly reduced.|The photo was cropped to 510 x 340px. The photo shows the face and the torso of the person. The file size was reduced from 1.5MB to 33.0kB.|pass|2023/5/4|
||**Test jquery code to confirm before submitting posts**|Conduct test no.  consecutively.||||||
||confirmation dialog|Enter 'test title 1' for title, 'content' for content, 'test city' for city, select 'Afghanistan' for country|click 'Submit'|A confirmation box appears and says, "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?"|A confirmation box appears and says, "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?"| pass|2023/5/2|
||confirmation dialog-cancel|--|Click on 'Cancel' in the dialog|The dialog disappears, and no change has been made to the page.|The dialog disappears, and no change has been made to the page.| pass|2023/5/23|
||confirmation dialog-ok|Enter 'test title 1' for title, 'content' for content, 'test city' for city, select 'Afghanistan' for country. Click on 'Submit'|Click on 'OK' in the dialog|Redirected to "Detail Page" of the blog "test title 1," and the flash message says "Your post has been submitted." |Redirected to "Detail Page" of the blog "test title 1," and the flash message says "Your post has been submitted."| pass|2023/5/2|

**Testing "Update Stories"**
As preparation for tests no 43-48: 
- Log in as testuser, go to "Write Stories," enter "test title 2" for title, "content" for the content, "test city" for city, select 'Afghanistan' for country.
- click "Save"
- go to "My page" and click on the link "Read the full story" of the blog "test title 2"
- click on "Update" 

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|43|Make all fields empty| delete prepopulated title, content, city and unselect the country | click on 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |2023/4/30|
|44|Make all fields empty| delete prepopulated title and content, city and unselect the country | click on 'submit' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|2023/4/30|
|44|Make all fields empty| delete prepopulated title and content, city and unselect the country | click on 'cancel' | Redirected to "detail page" | A message says "Please fill out this field" for the title | fail|2023/5/2|
|45|Make title field empty | delete the title but keep the other fields populated | click on 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|2023/4/30|
|46|Make title field empty | delete the title but keep the other fields populated| click on 'submit' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|2023/4/30|
|46|Make title field empty | delete the title but keep the other fields populated| click on 'cancel' | Redirected to "detail page" | A message says "Please fill out this field" for the title | fail|2023/5/2|
|47|Make content field empty | delete the content but keep the other fields populated | click on 'save' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|2023/4/30|
|48|Make content field empty | delete the content but keep the other fields populated | click on 'submit' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|2023/4/30|
|48|Make content field empty | delete the content but keep the other fields populated | click on 'cancel' | Redirected to "detail page" | A message says "Please fill out this field" for the content | fail|2023/5/2|
|47|Make city field empty | delete the content but keep the other fields populated | click on 'save' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city | pass|2023/4/30|
|48|Make city field empty | delete the content but keep the other fields populated | click on 'submit' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city| pass|2023/4/30|
|48|Make city field empty | delete the content but keep the other fields populated | click on 'cancel' | Redirected to "detail page" | A message says "Please fill out this field" for city |fail|2023/5/2|
|47|Unselect country | unselect the country  | click on 'save' | A message says "Please fill out this field" for the country | "Please select an item in the list" for the country | pass|2023/4/30|
|48|Unselect country | unselect the country | click on 'submit' | A message says "Please fill out this field" for the country | "Please select an item in the list" for the country | pass|2023/4/30|
|48|Unselect country | unselect the country | click on 'cancel' | Redirected to "detail page" | "Please select an item in the list" for the country. Unselect country. | fail|2023/5/2|
|100|enter spaces. Unselect country. | Enter spaces in 'title,' 'content,' 'city' and unselect country| click on 'save' | A message says "Please fill out this field" for the title | "Please select an item in the list" for the country | fail |2023/4/30|
|101|enter spaces. Unselect country. | Enter spaces in 'title,' 'content,' 'city' and unselect country| click on 'submit' | A message says "Please fill out this field" for the title | "Please select an item in the list" for the country | fail |2023/4/30|
|102|enter spaces. Unselect country. | Enter spaces in 'title,' 'content,' 'city' and unselect the country | click on 'cancel' | Redirected to "detail page" | "Please select an item in the list" for the country | fail|2023/5/2|
|103|enter spaces (leave country selected) | enter spaces in 'title,' 'content,' 'city'| click on 'save' | A message says "Please fill out this field" for the title | An error message "This field is required" for the country" appears for title, content and city. | fail |2023/4/30|
|103|enter spaces | enter spaces in 'title,' 'content,' 'city' | click on 'submit' (Go on to test no. without any other actions.) | A message says "Please fill out this field" for the title | Confirmation dialog asking if users really want to submit the post shows up. | fail |2023/5/2| 
|103|confirmation dialog - cancel|--|Click on 'cancel' | The dialog disappears. | The dialog disappears. | pass |2023/5/4|
|103|confirmation dialog - ok|--|Click on 'Submit' and 'OK' in the dialog | Message 'This field is required' will be displayed for title, content and city. | Message 'This field is required' will be displayed for title, content and city. | pass |2023/5/4|
|103|enter spaces | enter spaces in 'title,' 'content,' 'city'| click on 'cancel' | Redirected to "detail page" | An error message "This field is required" for the country" appears for title, content and city. |fail|2023/5/2|
||**Test jquery code to confirm before submitting posts**|Conduct test no.  consecutively.||||||
||confirmation dialog|change the title to 'test title 2 updated' |click on 'Submit'|A confirmation box appears and says, "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?"|A confirmation box appears and says, "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?"| pass|2023/5/3|
||confirmation dialog-cancel||Click on 'Cancel' in the dialog|The dialog disappears. Redirected to "Detail Page." The title reads 'test title 2' |The dialog disappears. Redirected to "Detail Page." The title reads 'test title 2'| pass|2023/5/3|
||confirmation dialog-ok|Click on 'Submit'|Click on 'OK' in the dialog|Redirected to "Detail Page." of blog "test title 2," the title has changed to 'test title 2 updated,' and the flash message says "You submitted your post. We'll contact you when evaluation is done." |Redirected to "Detail Page." of blog "test title 2," the title has changed to 'test title 2 updated,' and the flash message says "You submitted your post. We'll contact you when evaluation is done."| pass|2023/5/3|
||||||||
||**Testing confirmation dialog before deleting posts**|Write a story and save. Conduct no. without any actions in between.|||||||
||Confirmation dialog |Go to the "Detail Page" of the draft, and click on "Delete"|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft."Write a story and save.|Go to the "Detail Page" of the draft, and click on "Delete"|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft."|pass|2023/5/3|
||Confirmation dialog - cancel|--|Click on 'Cancel'|The dialog diappears, and "Detail Page" remains unchanged.|The dialog diappears and the "Detail Page" remains unchanged.|pass|2023/5/3|
||Confirmation dialog - ok|--|Click on 'Ok'|Redirected to "home." A flash message, "Your draft has been deleted." appears.|Redirected to "home." A flash message, "Your draft has been deleted." appears.|pass|2023/5/3|

**Testing “Update Comments”**
As preparation for test no. 50, 
1.	log in as testuser
2.	On the home page, click on the link “Read the full story” of the blog “blog 1”
4.	Enter “test comment” in the leave comments section and click on “Submit”
5.	Click on the update comment icon

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|50|Leave the text box empty| delete the prepopulated comment | click on 'Submit' | A message says "Please fill out this field"|  A message says "Please fill out this field"| pass|2023/4/30|
|||||||||
||**Testing confirmation dialog before deleting comments**|Log in as testuser, go to "Detail Page" of "blog 1." Conduct no. without any actions in between.|||||||
||Confirmation dialog |--|Click on the trash bin icon next to the comment 'test comment'|A confirmation dialog appears.|A confirmation dialog appears.|pass|2023/5/3|
||Confirmation dialog - cancel|--|Click on 'Cancel'|The dialog diappears, and "Detail Page" remains unchanged.|The dialog diappears and "Detail Page" remains unchanged.|pass|2023/5/3|
||Confirmation dialog - ok|Click on the trash bin icon.|Click on 'OK' in the dialog.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|pass|2023/5/3|

**Testing "My Page"**
As preparation for tests no. 53-62, 
1. sign up as a new user testuser3
2. go to "Write Stories" page, and make 4 new posts with the titles: blog 11, blog 12, blog 13, blog 14.
3. go to admin panel and publish the 4 posts one by one in the ascending order.
4. go to detail page of the 4 posts and bookmark them.
5. enter "test comment" as comment in all 4 posts and click on "submit"

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||**"Written by me" section**|||||||
||The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|2023/5/23|
||The layout|--| Click on "Show more" | blog 11 appears. | blog 11 appears.|pass|2023/5/23|
||**"Commented by me" section**|||||||
||The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|2023/5/23|
||The layout|--| Click on "Show more" | blog 11 appears. | blog 11 appears.|pass|2023/5/23|
||**"Bookmarked by me" section**|||||||
||The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|2023/5/23|
||The layout in "Bookmarked by me"|--| Click on "Show more" | In "Bookmarked by me"  section, blog 14, blog 13, blog 12 appear in the order, and the "Show more" button is shown. | In "Bookmarked by me"  section, blog 14, blog 13, blog 12 appear in the order, and the "Show more" button is shown.|pass|2023/5/23|
|||||||||
||**Show more/less buttons in "Written by me" section**|||||||
|53|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|2023/4/30|
|54|"Show less" button (upper) | -- |Click on "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|2023/4/30|
|54|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-114) says "Show more" |pass|2023/4/30|
||**Show more/less buttons in "Commented by me" section**|||||||
|53|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|2023/4/30|
|54|"Show less" button (upper) | -- |Click on "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|2023/4/30|
|54|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-114) says "Show more" |pass|2023/4/30|
||**Show more/less buttons in "Bookmarked by me" section**|||||||
|53|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|2023/4/30|
|54|"Show less" button (upper) | -- |Click on "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|2023/4/30|
|54|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-114) says "Show more" |pass|2023/4/30|

**Testing if clicking on show more & show less buttons in different sections doesn't disrupt the functions**<br>
As preparation
1. click on "Show more" in "Written by me"
2. click on "Show more" in "Commented by me"
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|62|Show more/less buttons across different sections | -- |Click on "Show less" in "Commented by me" (One below the fourth post)| "blog 11" in "Commented by me" will disappear. The upper button in "Commented by me" will say "Show more" | "blog 11" in "Commented by me" disappears. The upper button in "Commented by me" section says "Show more" | pass|2023/4/30|

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||**"Become a Member" page**|||||||
||link “sign in” | Go to “Become a Member” page | Click on the link | Redirected to the log in page| Redirected to the log in page |pass|2023/4/30|
||**"Sign up" page**|||||||
|19|leave all fields empty| --|click “Sign up” button|A validation error message says “Please fill out this field for the username field| A validation error message says “Please fill out this field” for the username field |pass|2023/4/30|
|20|Leave the second password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the first password field |click “Sign up” button|A validation error message says “Please fill out this field” for the second password field| A validation error message says “Please fill out this field” for the second password field |pass|2023/4/30|
|21|Leave the first password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the second password field |click “Sign up” button|A validation error message says “Please fill out this field” for the first password field.| A validation error message says “Please fill out this field” for the first password field. |pass|2023/4/30|
|22|Leave email empty|Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|Redirected to “Home” page and the message says “Successfully signed in as testuser1” | Redirected to “Home” page and the message says “Successfully signed in as testuser1” |pass|2023/4/30|
|23|Leave username empty|Enter “def@test.com” for the email; “swUf8LcR” for the two password fields; |click on “Sign up” button|A validation error message says “Please fill out this field” for the username field| A validation error message says “Please fill out this field” for the username field |pass|2023/4/30|
|24|Use already registered username| Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation message says “A user with that username already exists”| A validation message says “A user with that username already exists”| pass|2023/4/30|
|25|Use already registered email| Enter “testuser2” for the username; "test@ecopost.com” for the email; “swUf8LcR” for the two password fields |click “Sign up” button|A validation message says “A user is already registered with this email address.”| A validation message says “A user is already registered with this email address.”| pass|2023/4/30|
|26|Use common password| Enter “testuser2” for the username; “def@test.com” for the email; “password” for the two password fields |click “Sign up” button |A validation message says “This password is too common.”| A validation message says “This password is too common.”| pass|2023/4/30|
|27|enter two different passwords| Enter “testuser2” for the username; “def@test.com” for the email; “rDw74kRmW” for the first password field; “Adr49PwTeB” for the second password field |click “Sign up” button|A validation message says “You must type the same password each time.”| A validation message says A validation message says “You must type the same password each time.”| pass|2023/4/30|
|28|Enter all appropriate data| Enter “testuser2”; “def@test.com” for email; “swUf8LcR” for both password fields| click on“Sign up” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser2” | Redirected to “Home” page, and a message says “Successfully signed in as testuser2”| pass|2023/4/30|
||**"Sign up" page**|||||||
|29|link “sign up”|Go to “Log in” page|Click on the link|Redirected to the sign up page| Redirected to the sign page |pass|2023/4/30|
||**"Log in" page**|||||||
|30|Enter all appropriate data| Enter “testuser”; “test@ecopost.com” for email; “gR48NmYr1” for both password fields| click on“Sign in” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser” | Redirected to “Home” page, and a message says “Successfully signed in as testuser”| pass|2023/4/30|
|31|Leave username empty| Enter “gR48NmYr1” for password| click “Sign in” button|A message says "Please fill out this field" for username | A message says "Please fill out this field" for username| pass|2023/4/30|
|32|Leave password empty| Enter “testuser” for username| click “Sign in” button|A message says "Please fill out this field" for password| A message says "Please fill out this field" for password| pass|2023/4/30|
|33|Enter wrong password| Enter “testuser” for username; "wrongpw" for password | click “Sign in” button|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|2023/4/30|
|34|Enter wrong username| Enter “testuser2” for username; "gR48NmYr1" for password | click “Sign in” button|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|2023/4/30|
|35|Remember me function| Enter “testuser” for username; "gR48NmYr1" for password; put a check for "Remember me" and sign in. Log out and go back to the log in page| Enter "testuser" for username | The password will be automatically filled out. | The password is not automatically filled out. | fail|2023/4/30|
||**"Sign out" page**|||||||
|36|“Sign out” button|Log in as "testuser." Click on "Log out" in the navigation bar. |Click on "Sign out"|Redirected to "Home" page, and the flash message says, "You have signed out." | Redirected to "Home" page, and the flash message says, "You have signed out." |pass|2023/4/30|

### Test summary

- "Remember me" function in the test no. 35.
For log in systems in general, clicking on the check box "Remember me" prepopulates the password for the user when the same user tries to log in the next time.  But as recorded, the password doesn't get filled out automatically. It doesn't cause a serious problem for the function of the site, so as of May, 2023, I will leave it as it is.  It needs to be fixed in the future.

- test no.  <br>
When spaces are entered for the title, content and city, and the country is unselected, clicking 'Save' or 'Submit' will display the validation message for the country.
When spaces are entered for the title, content and city while the country is selected, clicking 'Save' will display a message 'This field is required.' for the title, content and city.  Clicking 'Submit' in this case will cause the confirmation dialog to appear.

In above cases validation is not displayed as expected.  Especially, in cases as in test no.    it would be strange for users to see a confirmation dialog, click on 'OK' for submitting the draft and then to see validation messages.  I added a
validate function in line 20-25 in script.js, and that took care of the cases in which spaces are entered as well.  I repeated test no. :

 Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||validation messages on "Write Stories"|Enter 'test validation' for titel, 'content' for content, 'test' for city, 'Afghanistan' for country|Click on 'Submit'| Validation messages appear |Validation message 'This field is required' appears for the title, content and city.|pass|2023/5/5|
||validation messages on "Update Stories"|Make a draft and save.  Go to "Detail Page" of the blog.  Delete values in the title, content and city and insert spaces. |Click on 'Submit'| Validation messages appear |Validation message 'This field is required' appears for the title, content and city.|pass|2023/5/5|


Adding a validate function in line 20-25 in script.js didn't change the results for test no.  .
It seems that the program to display the validation message for country field is fired even before I can capture with jquery.
I wasn't able to fix this issue but in the future I will 



"update post" page
tests   failed, because the Django form error messages appeared before redirection.  If 'Cancel' button is clicked, the user should be promptly redirected to "detail page."  I used anchor tag and href attribute to redirect to "Detail Page" (line 16 in "update_post.html") and repeated the tests:  
 
 Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|44|Make all fields empty| delete prepopulated title and content, city and unselect the country | click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" | pass|2023/5/2|
|46|Make title field empty | delete the title but keep the other fields populated| click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" | pass|2023/5/2|
|48|Make content field empty | delete the content but keep the other fields populated | click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" | pass|2023/5/2|
|48|Make city field empty | delete the content but keep the other fields populated | click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" |pass|2023/5/2|
|48|Unselect country | unselect the country | click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" | pass|2023/5/2|
|102|enter spaces. Unselect country. | Enter spaces in 'title,' 'content,' 'city' and unselect the country | click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" | pass|2023/5/2|
|103|enter spaces | enter spaces in 'title,' 'content,' 'city'| click on 'cancel' | Redirected to "detail page" | Redirected to "detail page" |pass|2023/5/2|

Test no.   
Refer to 

- - -
## Bugs

1. For “Update Stories” I was using View class instead of UpdateView class.  When I updated posts, if the post had a featured image originally, and if I updated other fields (but not the image) and saved the change, the image was lost.<br><br>**Solution:** I rewrote “Update Stories” using UpdateView class and the issue was resolved.

2. “Search Stories” page didn’t get displayed.  An error page appeared with the message “Reverse for 'post_detail' with arguments '('',)' not found.”<br><br>**Solution:** I was forgetting a slash at the end of the url in urls.py, so I changed the url from ‘search_story’ to ‘search_story/,’ and the issue was resolved.

3. On “Write Stories” and “Update Stories” pages, if I left the fields empty and clicked on ‘Submit’, the confirmation dialog showed up instead of the validation error message.In this case, the validation message should appear, and only if there are no validation messages to be displayed, the dialog should appear.<br><br>
**Solution:** This happened because I set the dialog to appear when ‘Submit’ button was clicked.
I changed the code so that the dialog appears when the form will be submitted.  I also had to target specifically the events in which 'Submit' is clicked, so I rewrote code as after line 17 in dialog.js.
The issue was resolved for cases in which fields are left empty or the country is unselected.  The problem remains, when spaces are entered for the title, content or city as discussed in 'Manual Testing' section.  I will fix the issue in the future.  

4. On “Write Stories” and “Update Stories” pages, the following steps resulted in an unexpected outcome:
Fill out all required fields, click on ‘Submit,’ click on ‘Cancel’ in the dialog, click on ‘Save’
-> a confirmation dialog before form submission showed up.
What happened was: when ‘Submit’ was clicked, the value ‘complete’ was stored in the variable ‘ButtonValue.’  When ‘Save’ was clicked, since the value of ‘ButtonValue’ was ‘complete,’ the confirm function in line 24 in script.js was fired.<br>
**Solution:** I added the class name ‘btn-submit’ to 'Save' button as well, so when ‘Save’ button is clicked, value ‘draft’ will be stored in ButtonValue, which will not fire the confirm function.  

## Aspects to be improved in the future:
- As discussed in “Manual Testing” and “Bugs” sections, the mechanism to display validation messages for PostForm needs to be improved.
- Remember me function on “Log in” page also needs to be fixed.
- Currently on "Search Stories" page, if users click on 'Search,' they will have to scroll down to see the results.  I need to design the page so they will find the search results easily.
- In addition, I will make Contact page where users can write and submit messages to admin.
- I also want to make the system to update comments simpler.  I plan to display a small input box for updating comments where the comment is displayed, since a comment form shouldn't need a whole another page.

## Credits:
Many thanks to my mentor Jubril Akolade and tutors at Code Institute for their dedicated support and encouragement.<br>
For this application, I used the Code Institute's 'Code Star' project as a starting point.

Code snippets that were taken from 'Code Star' are as follows:

- The code to display 3 excerpts of posts in a row 
{% if forloop.counter|divisibleby:3 %}
was used in “More Stories,” “Popular Stories” and “My Page.” 

- The code to paginate post lists was used in lines 39-53 in “More Stories” and “Popular Stories.”

- The code to display “Comments” and “Leave Comments” sections was used on “Detail Page.”

- The code to display the heart and the number of likes was used in “More Stories,” “Popular Stories” and “Detail Page”

- The code to ‘like’ posts was used in line 61-63, 89-91 in “PostDetail” view in views.py.
 It was also used in ‘bookmark’ function in line 66-68, 93-95 in “PostDetail” view in views.py.

- The code to post comments was used in line 96-103 in PostLike View in views.py

Other sources for code snippets taken in this project:
- The code to display links to social networks (lines in 68-87 in base.html) was taken from “Love Running” project.

- The code for turning the navbar to a hamburger menu (lines 9-19 in script.js & lines 21-45 in base.html) was taken from the following site:
https://stackoverflow.com/questions/70370519/how-can-i-turn-my-navbar-into-hamburger-menu-for-mobile-using-responsive-design

- For the code for search system, I took basic ideas from the following youtube video:


- The code to display confirmation dialog when ‘Submit’ is clicked (line 17-25 in dialog.js) is taken from the following site:



- The code to log in a testuser (lines  in test_views.py) was taken from the following site:
https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests

## Media used

Logo image: clover 
https://www.freepik.com/free-vector/watercolor-background-earth-day-with-natural-elements_1069886.htm#query=earth%20plants%20free&position=24&from_view=search&track=ais

Heading image: blue earth
https://www.freepik.com/free-vector/watercolor-background-earth-day-with-natural-elements_1069886.htm#query=earth%20plants%20free&position=24&from_view=search&track=ais

Default featured image
https://www.freepik.com/free-vector/background-zoom_8764554.htm#page=5&query=nature%20graphics&position=24&from_view=search&track=ais

test_transformation
https://www.pexels.com/photo/city-fashion-man-people-15839341/




