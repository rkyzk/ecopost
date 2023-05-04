$(document).ready(function(){
  var ButtonValue;

  // Confirm before deleting the post
  const DELETE_POST = "Are you sure you want to delete your post?  You won't be able to retrieve the draft."
  $('#delete-form').submit(function(e) {
    return confirm(DELETE_POST);
  });

  // Confirm before deleting comment
  const DELETE_COMMENT = "Are you sure you want to delete your comment?"
  $('#delete-comment').submit(function() {
    return confirm(DELETE_COMMENT);
  })

  // Confirm before submitting posts
  const SUBMIT_POST = "After submiiting your post, you won't be able to" +
                      " update or delete it.  Would you like to proceed?"
  $('.submit-post').click(function() {
      ButtonValue = $(this).val();
      console.log(ButtonValue)
  })
  $('.submit-post-form').submit(function() {
    if(ButtonValue == 'complete') {
      return confirm(SUBMIT_POST);
    }
  })
});