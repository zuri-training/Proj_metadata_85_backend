// toggling nav menu
const burger = document.querySelector('.burger-menu');
const ul = document.querySelector('nav ul');
const nav = document.querySelector('nav');
const navBarBtns = document.querySelector('.signup-link');
// The burger variable select the hamburger menu bars
// The ul variable selects the list items (the nav links altogether)
// The nav variable selects the container itself (the nav element). Now, next is toggle the nav ul.show class when the user clicks the hamburger menu bar.
burger.addEventListener('click', () => {
    ul.classList.toggle('show');
});
burger.addEventListener('click', () => {
    navBarBtns.classList.toggle('show');
});
//To close Hamburger menu when a link is click >>Select navlinks
const navLink = document.querySelectorAll('.nav-link');
navLink.forEach((link) =>
    link.addEventListener('click', () => {
        ul.classList.remove('show');
    })
);
const navBtn = document.querySelectorAll('.nav-btn');
navBtn.forEach((btn) =>
    btn.addEventListener('click', () => {
        navBarBtns.classList.remove('show');
    })
);