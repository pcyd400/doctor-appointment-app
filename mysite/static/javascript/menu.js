//for menu burger
const burgerIcon=document.querySelector('#burger');
const navbarMenu=document.querySelector('#nav-links');

burgerIcon.addEventListener('click', ()=>{
    navbarMenu.classList.toggle('is-active');
});