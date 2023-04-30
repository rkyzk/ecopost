// Confirm before deleting the post
const DELETE_POST = "Are you sure you want to delete your post?  You won't be able to retrieve the draft."
$('.delete-post').click(function() {
  return confirm(DELETE_POST);
});

// Confirm before deleting comment
const DELETE_COMMENT = "Are you sure you want to delete your comment?"
$('.delete-comment').click(function() {
  return confirm(DELETE_COMMENT);
})

// Confirm before submitting posts
const SUBMIT_POST = "After submiiting your post, you won't be able to" +
                    "update or delete it.  Would you like to proceed?"
$('.submit-post').click(function() {
  return confirm(SUBMIT_POST);
})