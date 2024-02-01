document.addEventListener("DOMContentLoaded", () => {
  handleDeleteButton();
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

// Scroll to top button script
//Get the button
let scrollToTopButton = document.getElementById("btn-scroll-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopButton.style.display = "block";
  } else {
    scrollToTopButton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
scrollToTopButton.addEventListener("click", scrollToTop);

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// Starry night script
function init() {
  const styles = ["animate4", "animate1", "animate2", "animate3"];
  const scales = ["scale1", "scale2", "scale3"];
  const opacities = [
    "opacity1",
    "opacity1",
    "opacity1",
    "opacity2",
    "opacity2",
    "opacity3",
  ];

  const rand = (min, max) => Math.floor(Math.random() * (max - min)) + min;

  let stars = "";
  const count = 60;
  const widthWindow = window.innerWidth;
  const heightWindow = window.innerHeight;

  for (let i = 0; i < count; i++) {
    stars += `<span class='star ${styles[rand(0, 4)]} ${opacities[rand(0, 6)]} 
              ${scales[rand(0, 3)]}' style='animation-delay: .${rand(
      0,
      9
    )}s; left: 
              ${rand(0, widthWindow)}px; top: ${rand(
      0,
      heightWindow
    )}px;'></span>`;
  }

  const skies = document.querySelectorAll(".sky");

  skies.forEach((sky) => (sky.innerHTML = stars));
}

window.onload = init;
window.onresize = init;

/**
 * Check for delete profile button and add
 * event listener to display modal
 * @returns {void}
 */
const handleDeleteButton = () => {
  if (!document.querySelector(".delete-link")) return;
  const deleteButtons = document.querySelectorAll(".delete-link");
  const deleteModal = document.getElementById("delete-modal");
  const deleteConfirmButton = document.querySelector(".delete-confirm-button");
  const deleteCancelButton = document.querySelector(".delete-cancel-button");
  let currentDeleteForm = null;

  if (deleteButtons.length === 0 || !deleteModal) return;

  for (const deleteButton of deleteButtons) {
    deleteButton.addEventListener("click", (event) => {
      event.preventDefault();
      try {
        if (!(deleteButton.parentElement instanceof HTMLFormElement)) return;
        const formId = deleteButton.parentElement.getAttribute("id");
        if (formId) {
          currentDeleteForm = document.getElementById(formId);
        }

        // @ts-ignore
        deleteModal.showModal();
      } catch (error) {
        console.error(error);
      }
    });
  }

  if (deleteConfirmButton) {
    deleteConfirmButton.addEventListener("click", () => {
      if (currentDeleteForm instanceof HTMLFormElement) {
        currentDeleteForm.submit();
      }
    });
  }

  if (deleteCancelButton && deleteModal) {
    deleteCancelButton.addEventListener("click", (event) => {
      event.preventDefault();
      // @ts-ignore
      deleteModal.close();
    });
  }
};
