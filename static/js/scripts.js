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
let showPostsButton = document.getElementById('show-my-posts');
showPostsButton.addEventListener("click", function(){
  let myPosts = document.getElementById('my-posts');
  myPosts.classList.remove('hide');
  myPosts.classList.add('show');
  let showMoreBtn = document.getElementById('show-my-posts');
  showMoreBtn.textContent = 'Show less'
})

// Clicking 'Show less' button will hide posts.
let hideButton = document.getElementById('hide-my-posts');
hideButton.addEventListener("click", function(){
  let myPosts = document.getElementById('my-posts');
  myPosts.classList.remove('show');
  myPosts.classList.add('hide');
  let showMoreBtn = document.getElementById('show-my-posts');
  showMoreBtn.textContent = 'Show more'
})

modle.exports = buttonClick;