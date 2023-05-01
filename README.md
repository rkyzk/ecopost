# Ecopost

## Overview:

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

Users can read the entire content of the post<br>
Users can search stories by title, authors and other factors<br>
Users can sign up to become members<br>
Members can like and bookmark posts<br>
Members can leave comments for the posts<br>
Members can edit and delete comments<br>
Members can write their own stories and submit them for evaluation<br>
Members can update or delete their posts before submitting them<br>

## Notes on the Design 
The overall appearance is kept simple and clean in order to avoid interfering with various colors that the featured images will bring in.

**About the Colors**
- The background is white.
- Beige, green and blue are used for titles and navigation links. These colors are the colors of soil, the ocean, the sky and plants, so they suit the theme of the site.

**About the Fonts**
- Montserrat was used for headings because it's stylish and stands out from the rest when used sparingly.
- For the content Lato is used since it's readable and familiar to users. 

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
|13| Quick access to one's own posts and other posts | ‘My page’ displays lists of posts written, commented and bookmarked by the user. |
||||
||**Admin**||
|14| Select posts to be published | Posts’ status is set to ‘Submitted’ when users submit their drafts, and they will not be displayed in public.  Only when admin changes the status to ‘Published,’ the posts will be publicized. |
|15| Let users see the most interesting posts |Three featured stories chosen by admin will be displayed on the home page, where the users will see immediately when they visit the site. |
|16| Allow users to update or delete posts only before submission | Update and Delete buttons for posts appear only if posts are in ‘draft’ status.  In addition, trying to update or delete posts that have been submitted will display a 403 error page.|
|17| Allow only the author to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the user who is logged in as the author of the posts and comments to update or delete their writings. |
|18|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |

### Testing Features

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|1.|Logo|Go to “Search Stories”|Click on the logo|Redirected to the home page|Redirected to the home page|pass|2023/4/29|
|py|**Navigation links**|||||||
|3|Test each link will redirect to the right page |||||||
|4|”Home”|Go to “Search Stories” page|Click on “Home”|Redirected to ”Home|Redirected to ”Home”|pass|2023/4/29|
|5|”Search stories”|Go to “Home”|Click on “Search Stories”|Redirected to ”Search Stories”|Redirected to ”Search Stories”|pass|2023/4/29|
|6|”Become a Member”|Log out if you haven't.  Go to “Home” page|Click on “Become a Member”|Redirected to ”Become a Member” | Redirected to “Become a Member”|pass|2023/4/29|
|7|”Log in”|Go to “Home” page|Click on “Log in”|Redirected to ”Log in”|Redirected to “Log in”|pass|2023/4/29|
|8|”Write Stories”|Log in and go to “Home” page|Click on “Write Stories”|Redirected to ” Write Stories”|Redirected to ” Write Stories”|pass|2023/4/29|
|9|”My Page”|Go to “Home” page|Click on “My Page”|Redirected to ”My Page”|Redirected to “My Page”|pass|2023/4/29|
|10|”Log out”|Go to “Home” page|Click on “Log out”|Redirected to ”Log out”|Redirected to “Log out”|pass|2023/4/29|
||**links in the footer**||||||
|11|link to facebook|Go to “Home” page|Click on the facebook icon|Redirected to facebook site|Redirected to facebook site| pass|2023/4/29|
|12|link to twitter|Go to “Home” page|Click on the twitter icon|Redirected to twitter site|Redirected to twitter site| pass|2023/4/29|
|13|link to instagram|Go to “Home” page|Click on the instagram icon|Redirected to instagram site|Redirected to instagram site| pass|2023/4/29|

**Testing "Home" page specifically"**
*Note:*
As preparatory steps for tests no. 14-16, if no featured stories have been created, follow the steps below:
1. log in
2. go to “Write Stories” 
3. make 3 posts
4. go to admin panel
5. set featured flag True for all 3 posts.

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||links on “Home”||||||||
|14|link ”Read the full story” at the bottom of the first excerpt |Go to “Home”|Click on the link|Detail page of the post will be displayed.| Detail page of the post will be displayed.|pass|2023/4/29|
|15|link ”Read the full story” at the bottom of the second excerpt |Go to “Home”|Click on the link|Detail page of the post will be displayed.| Detail page of the post will be displayed.|pass|2023/4/29|
|16|link ”Read the full story” at the bottom of the third excerpt |Go to “Home”|Click on the link|Detail page of the post will be displayed.| Detail page of the post will be displayed.|pass|2023/4/29|
|17|link ”More stories from this week” at the bottom of the third excerpt |Go to “Home” page|Click on the link|Redirected to “More stories from this week”| Redirected to “More stories from this week”|pass|2023/4/30|
|18|link ”Readers’ favorite stories of all time” at the bottom of the third excerpt |Go to “Home” page|Click on the link|Redirected to ”Readers’ favorite stories of all time” Redirected to ”Readers’ favorite stories of all time”|pass|2023/4/30|

#### "Become a Member" page

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
||link “sign in” | Go to “Become a Member” page | Click on the link | Redirected to the log in page| Redirected to the log in page |pass|2023/4/30|

- Testing sign up function and validation messages

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|19|leave all fields empty| --|click “Sign up” button|A validation error message says “Please fill out this field for the username field| A validation error message says “Please fill out this field” for the username field |pass|2023/4/30|
|20|Leave the second password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the first password field |click “Sign up” button|A validation error message says “Please fill out this field” for the second password field| A validation error message says “Please fill out this field” for the second password field |pass|2023/4/30|
|21|Leave the first password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the second password field |click “Sign up” button|A validation error message says “Please fill out this field” for the first password field.| A validation error message says “Please fill out this field” for the first password field. |pass|2023/4/30|
|22|Leave email empty|Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|Redirected to “Home” page and the message says “Successfully signed in as testuser1” | Redirected to “Home” page and the message says “Successfully signed in as testuser1” |pass|2023/4/30|
|23|Leave username empty|Enter “def@test.com” for the email; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation error message says “Please fill out this field” for the username field| A validation error message says “Please fill out this field” for the username field |pass|2023/4/30|
|24|Use already registered username| Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation message says “A user with that username already exists”| A validation message says “A user with that username already exists”| pass|2023/4/30|
|25|Use already registered email| Enter “testuser2” for the username; “abc@test.com” for the email; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation message says “A user is already registered with this email address.”| A validation message says “A user is already registered with this email address.”| pass|2023/4/30|
|26|Use common password| Enter “testuser2” for the username; “def@test.com” for the email; “password” for the first password field; “password” for the second password field |click “Sign up” button|A validation message says “This password is too common.”| A validation message says “This password is too common.”| pass|2023/4/30|
|27|enter two different passwords| Enter “testuser2” for the username; “def@test.com” for the email; “rDw74kRmW” for the first password field; “Adr49PwTeB” for the second password field |click “Sign up” button|A validation message says “You must type the same password each time.”| A validation message says A validation message says “You must type the same password each time.”| pass|2023/4/30|
|28|Enter all appropriate data| Enter “testuser2”; “def@test.com” for email; “swUf8LcR” for both password fields| click on“Sign up” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser2” | Redirected to “Home” page, and a message says “Successfully signed in as testuser2”| pass|2023/4/30|

### Log in page
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|29|link “sign up”|Go to “Log in” page|Click on the link|Redirected to the sign up page| Redirected to the sign page |pass|2023/4/30|

**Testing log-in function and validation messages**
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|30|Enter all appropriate data| Enter “testuser2”; “def@test.com” for email; “swUf8LcR” for both password fields| click on“Sign in” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser2” | Redirected to “Home” page, and a message says “Successfully signed in as testuser2”| pass|2023/4/30|
|31|Leave username empty| Enter “swUf8LcR” for password| click “Sign in” button|A message says "Please fill out this field" for username | A message says "Please fill out this field" for username| pass|2023/4/30|
|32|Leave password empty| Enter “testuser2” for username| click “Sign in” button|A message says "Please fill out this field" for password| A message says "Please fill out this field" for password| pass|2023/4/30|
|33|Enter wrong password| Enter “testuser2” for username; "wrongpw" for password | click “Sign in” button|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|2023/4/30|
|34|Enter wrong username| Enter “testuser3” for username; "swUf8LcR" for password | click “Sign in” button|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|2023/4/30|
|35|Remember me function| Enter “testuser2” for username; "swUf8LcR" for password; put a check for "Remember me" and sign in. Log out and go back to the log in page| Enter "testuser2" and see if the password will be automatically filled | The password will be automatically filled | The password is not filled out. | fail|2023/4/30|

### Log out page
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|36|“Sign out” button|Log in, click on "Log out"|Click on "Sign out"|Redirected to "Home" page| Redirected to "Home" page |pass|2023/4/30|

### Validation messages on "Write Stories" (Functions other than the validation messages are tested in automated testing. )

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|37|Leave all fields empty| -- | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|38|Leave all fields empty| -- | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|39|Leave title empty | Enter "content" for content | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|40|Leave title empty | Enter "content" for content | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|41|Leave content empty | Enter "test title 1" for title | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the content | pass|2023/4/30|
|42|Leave content empty | Enter "test title 1" for title | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the content | pass|2023/4/30|

### Validation messages on "Update Stories" (Functions other than the validation messages are tested in automated testing. )
As preparation for tests no 43-48.  
- Log in, go to "Write Stories," enter "test title 1" for title; "content" for the content
- click "Save"
- go to "My page" and click on the link "Read the full story" of the blog "test title 1"
- click "Update" 

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|43|Leave all fields empty| delete prepopulated title and content | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|44|Leave all fields empty| delete prepopulated title and content | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|45|Leave title empty | delete the title | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|46|Leave title empty | delete the title | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the title | pass|2023/4/30|
|47|Leave content empty | delete the content | click on 'save' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the content | pass|2023/4/30|
|48|Leave content empty | delete the content | click on 'submit' | A message says "Please fill out this field" for the title |  A message says "Please fill out this field" for the content | pass|2023/4/30|

### Validation messages on Leave Comments section on “Detail Page”
As preparation for test no. 49, 
1.	log in as testuser2
2.	go to “My Page”
3.	Click on the link “Read the full story” of the blog “test title 1”

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|49|Leave the field empty| -- | click on 'Submit' | A message says "Please fill out this field"|  A message says "Please fill out this field"| pass|2023/4/30|

### Validation messages on “Update Comments”
As preparation for test no. 50, 
1.	log in as testuser2
2.	go to “My Page”
3.	Click on the link “Read the full story” of the blog “test title 1”
4.	Enter “test comment” in the leave comments section and click on “Submit”
5.	Click on the update comment icon

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|50|Leave the text box empty| delete the prepopulated comment | click on 'Submit' | A message says "Please fill out this field"|  A message says "Please fill out this field"| pass|2023/4/30|

### Testing JaveScript in script.js
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|51| code in ln 9-19 | set the window size to 690px | click on the hamburger menu | the Menu box opens |the Menu box opens| pass|2023/4/30|
|52| code in ln 2-6 | log out | log in as testuser2 | Redirected to the home page, and the message "Successfully signed in as testuser2" will be displayed.  The message disappears after 3 seconds. |Redirected to the home page, and the message "Successfully signed in as testuser2" is displayed.  The message disappears after 3 seconds.| pass|2023/4/30|

As preparation for tests no. 53-62, 
1. log in as testuser2
2. make 4 posts
3. go to admin panel and publish the posts
4. go to detail page of the posts and bookmark them.
5. enter comments "test comment" and click on "submit"

**Testing show more and show less buttons in "Written by me" section**
Conduct test no. 53-55 consecutively without taking any other steps than written items.
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|53| code in ln 22-36 | -- |Click on "Show more"| The fouth post is displayed. The label of the clicked button will change to "Show less" | The fouth post is displayed.  The clicked button says "Show less"| pass|2023/4/30|
|54| code in ln 22-36 | -- |Click on "Show less" (The upper of the two "Show less" buttons)| The fouth post will disappear. The clicked button will say "Show more" | The fouth post is displayed.  The clicked button says "Show more" | pass|2023/4/30|
|55| code in ln 22-36 | click on "Show more" in "Commented by me" |Click on "Show less" (One below the fourth post)| The fouth post will disappear. The upper button will say "Show more" | The fouth post disappears.  The upper button says "Show more" | pass|2023/4/30|

**Testing show more and show less buttons in "Commented by me" section**
Conduct test no. 56-58 consecutively without taking any other steps than written items.
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|56| code in ln 22-36 | -- |Click on "Show more"| The fouth post is displayed. The label of the clicked button will change to "Show less" | The fouth post is displayed.  The clicked button says "Show less"| pass|2023/4/30|
|57| code in ln 22-36 | -- |Click on "Show less" (The upper of the two "Show less" buttons)| The fouth post will disappear. The clicked button will say "Show more" | The fouth post is displayed.  The clicked button says "Show more" | pass|2023/4/30|
|58| code in ln 22-36 | click on "Show more" in "Commented by me" |Click on "Show less" (One below the fourth post)| The fouth post will disappear. The upper button will say "Show more" | The fouth post disappears.  The upper button says "Show more" | pass|2023/4/30|

**Testing show more and show less buttons in "Bookmarked by me" section**
Conduct test no. 59-61 consecutively without taking any other steps than written items.
Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|59| code in ln 22-36 | -- |Click on "Show more"| The fouth post is displayed. The label of the clicked button will change to "Show less" | The fouth post is displayed.  The clicked button says "Show less"| pass|2023/4/30|
|60| code in ln 22-36 | -- |Click on "Show less" (The upper of the two "Show less" buttons)| The fouth post will disappear. The clicked button will say "Show more" | The fouth post is displayed.  The clicked button says "Show more" | pass|2023/4/30|
|61| code in ln 22-36 | click on "Show more" in "Bookmarked by me" |Click on "Show less" (One below the fourth post)| The fouth post will disappear. The upper button will say "Show more" | The fouth post disappears.  The upper button says "Show more" | pass|2023/4/30|

**Testing if clicking on show more & show less buttons in different sections don't disrupt the functions**
As preparation
1. click on "Show more" in "Written by me"
2. click on "Show more" in "Commented by me"
|62|code in ln 22-36 | -- |Click on "Show less" in "Commented by me" (One below the fourth post)| The fouth post of "Commented by me" will disappear. The upper button in "Commented by me" section will say "Show more" | The fouth post of "Commented by me" disappears. The upper button in "Commented by me" section says "Show more"  | pass|2023/4/30|

### Testing JaveScript in dialog.js
As preparation
1. log in as testuser2
2. make a post titled "test blog 1" and click on save
3. make a post titled "test blog 2" and submit
4. go to admin panel and publish "test blog 2"
5. go to detail page of test blog 2, and leave comment "test comment" and submit

Test No.| Test condition | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|59| code in ln 2-5 | go to detail page of test blog 1 | click on delete | a dialog box will show up and say "Are you sure you want to delete your post?  You won't be able to retrieve the draft." | The message "Are you sure you want to delete your post?  You won't be able to retrieve the draft." shows up in a dialog box| pass|2023/4/30|
|60| code in ln 8-11 | go to detail page of test blog 2 | click on the trash bin icon of the comment "test comment" | a dialog box will show up and say "Are you sure you want to delete your comment?" | The message "Are you sure you want to delete your comment?" shows up in a dialog box| pass|2023/4/30|
|61| code in ln 14-18 | go to "My page" click on the link "Read the full story" of "test blog 1" | Click on "Submit" | a dialog box will show up and say "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?" | The message "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?" shows up in a dialog box| pass|2023/4/30|
|62| code in ln 14-18 | go to "Write Stories." Enter "test blog 3" for title; "content" for "content" | Click on "Submit" | a dialog box will show up and say "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?" | The message "After submiiting your post, you won't be able to update or delete it.  Would you like to proceed?" shows up in a dialog box| pass|2023/4/30|

### Test summary
All features are functioning normally except for "Remember me" function in the test no. 35.
in general clicking on the check box "Remember me" prepopulates the password for the user when the same user tries to logs in the next time.  But as the test result suggests, the password doesn't get prepopulated. It needs to be fixed in the future.

- - -

## Wireframes
Wireframes for the app can be found [here.](https://wireframe.cc/pro/pp/873798723651976)
Please click on "Homepage" in the upper left corner to see wireframes of each page of the app.



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

