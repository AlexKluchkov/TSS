/*const burger = document.getElementById('burger');
const menu = document.getElementById('menu');

burger.addEventListener('click', () => {
    menu.classList.toggle('active');
});
*/

document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('burger');
    const menu = document.getElementById('menu');
    const overlay = document.getElementById('overlay');

    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        menu.classList.toggle('active');
        overlay.classList.toggle('active');
    });

    overlay.addEventListener('click', () => {
        burger.classList.remove('active');
        menu.classList.remove('active');
        overlay.classList.remove('active');
    });
});