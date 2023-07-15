const mainMenu = document.querySelector(".mainMenu");
const closeMenu = document.querySelector(".closeMenu");
const openMenu = document.querySelector(".openMenu");
const navLinks = document.querySelectorAll(".link");

const show = () => {
  mainMenu.style.display = "flex";
  mainMenu.style.top = "0";
};

const close = () => {
  mainMenu.style.top = "-100%";
};

openMenu.addEventListener("click", show);
closeMenu.addEventListener("click", close);
navLinks.forEach((link) => link.addEventListener("click", close));

if (localStorage.getItem("cookiesAccepted") === null) {
  setTimeout(function () {
    let cookies = document.querySelector("#cookies");
    cookies.classList.remove("d-none");
  });
}

function closeCookies() {
  let cookies = document.querySelector("#cookies");
  cookies.classList.add("d-none");
  localStorage.setItem("cookiesAccepted", true);
}
