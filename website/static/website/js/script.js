const mainMenu = document.querySelector(".mainMenu");
const closeMenu = document.querySelector(".closeMenu");
const openMenu = document.querySelector(".openMenu");

const show = () => {
  mainMenu.style.display = "flex";
  mainMenu.style.top = "0";
};

const close = () => {
  mainMenu.style.top = "-100%";
};

openMenu.addEventListener("click", show);
closeMenu.addEventListener("click", close);
