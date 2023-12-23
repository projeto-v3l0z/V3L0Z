var nav = document.querySelector("nav");

window.addEventListener("scroll", () => {
  if (window.pageYOffset > 50) {
    nav.classList.add("bg-dark", "shadow");
  } else {
    nav.classList.remove("bg-dark", "shadow");
  }
});
