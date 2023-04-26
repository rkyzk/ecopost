// Confirm before deleting the post
const DELETE_POST = "Are you sure you want to delete your post?  You won't be able to retrieve the draft."
$('.delete_post').click(function() {
return confirm(DELETE_POST);
});

// Confirm before deleting comment
const DELETE_COMMENT = "Are you sure you want to delete your comment?"
$('.delete_comment').click(function() {
return confirm(DELETE_COMMENT);
})