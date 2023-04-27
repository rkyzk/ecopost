// Let messages appear for 3 seconds
setTimeout(function() {
    let messages =document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// For mobile devices, clicking the hamburger icon will display the menu.
const menu = document.querySelector(".nav-menu");
let open;
function openMenu() {
  if (open) {
    menu.style.display = "none";
    open = false;
  } else if (!open) {
    menu.style.display = "block";
    open = true;
  }
}

// Clicking 'Show more' button will display more posts.
let button = document.getElementsByClassName('show-posts');
console.log(button)
for (btn in button) {
  btn.addEventListener("click", function(){
    let myPosts = this.nextElementSibling;
    if (showPostsButton.textContent == 'Show more') {
      myPosts.classList.remove('hide');
      myPosts.classList.add('show');
      this.textContent = 'Show less'
    } else {
      myPosts.classList.remove('show');
      myPosts.classList.add('hide');
      this.textContent = 'Show more'
    }
  });
}

// Clicking 'Show less' button will hide posts.
let hideButton = document.getElementsByClassName('hide-posts');
hideButton.addEventListener("click", function(){
  let myPosts = this.parentElement;
  myPosts.classList.remove('show');
  myPosts.classList.add('hide');
  myPosts.previousElementSibling.textContent = 'Show more'
})

module.exports = { openMenu };