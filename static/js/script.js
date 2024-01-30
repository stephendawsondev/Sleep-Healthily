document.addEventListener("DOMContentLoaded", () => {
  const navbarToggler = document.querySelector(".navbar-toggler");
  const navbarTogglerIcon = navbarToggler.querySelector("i");

  navbarToggler.addEventListener("click", () => {
    if (navbarToggler.getAttribute("aria-expanded") === "true") {
      navbarTogglerIcon.classList.remove("fa-times");
      navbarTogglerIcon.classList.add("fa-bars");
    } else {
      navbarTogglerIcon.classList.remove("fa-bars");
      navbarTogglerIcon.classList.add("fa-times");
    }
  });
});
