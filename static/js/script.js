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
for (btn of button) {
  btn.addEventListener("click", function(){
    let posts = this.nextElementSibling;
    if (this.textContent == 'Show more') {
      this.textContent = 'Show less'
      posts.classList.remove('hide');
      posts.classList.add('show');      
    } else {
      this.textContent = 'Show more'
      posts.classList.remove('show');
      posts.classList.add('hide');     
    }
  });
}

// Clicking 'Show less' button will hide posts.
let hideButton = document.getElementsByClassName('hide-posts');
for (hideBtn of hideButton) {
  hideBtn.addEventListener("click", function(){
    let posts = this.parentElement;
    posts.previousElementSibling.textContent = 'Show more'
    posts.classList.remove('show');
    posts.classList.add('hide');
  });
}
