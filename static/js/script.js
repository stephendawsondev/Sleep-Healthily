document.addEventListener("DOMContentLoaded", () => {
  handleDeleteButton();
  displayToastMessage();
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

/**
 * Scroll to top button function
 * @returns {void}
 */
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

/**
 * Function to initialise the stars animation for
 * the hero and newsletter sections
 * @returns {void}
 */
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
 * Check for delete buttons and add event listener to display modal
 * @returns {void}
 */
const handleDeleteButton = () => {
  const deleteButtons = document?.querySelectorAll(".delete-link");
  const deleteModal = document?.getElementById("delete-modal");
  const deleteModalForm = deleteModal?.querySelector("form");
  const deleteModalMessage = deleteModal?.querySelector(
    "#delete-modal-message"
  );
  const deleteCancelButton = deleteModal?.querySelector(
    ".delete-cancel-button"
  );

  if (deleteButtons.length === 0 || !deleteModal) return;

  deleteButtons.forEach((deleteButton) => {
    deleteButton.addEventListener("click", (event) => {
      event.preventDefault();

      // Determine if the delete button is for a review or a product
      const isReview = deleteButton.classList.contains("delete-review-link");

      // Determine if link is a blog post link
      const isBlogPost = deleteButton.classList.contains(
        "blog-post__delete-link"
      );

      const isProfile = deleteButton.classList.contains("profile-delete-link");

      const isComment = deleteButton.classList.contains("comment-action-link");

      let message = "Are you sure you want to delete this item?";

      if (isReview) {
        message = "Are you sure you want to delete this review?";
      } else if (isProfile) {
        message = "Are you sure you want to delete your account?";
      } else if (isBlogPost) {
        message = "Are you sure you want to delete this blog post?";
      } else if (isComment) {
        message = "Are you sure you want to delete this comment?";
      } else {
        message = "Are you sure you want to delete this product?";
      }

      // Update the modal message
      deleteModalMessage.textContent = message;

      // Update the form action to the href of the delete button
      deleteModalForm.setAttribute("action", deleteButton.getAttribute("href"));

      // Show the modal
      deleteModal.showModal();
    });
  });

  // Handle the cancel button click
  if (deleteCancelButton) {
    deleteCancelButton.addEventListener("click", (event) => {
      event.preventDefault();
      deleteModal.close();
    });
  }
};

/**
 * Display toast messages
 * @returns {void}
 */
function displayToastMessage() {
  if (!document.querySelector(".toast")) return;
  const toast = document.querySelector(".toast");
  toast.classList.add("show");
  dismissToast();
}

/**
 * Function to add event listener to the
 * toast close button to dismiss the toast
 * @returns {void}
 */
function dismissToast() {
  const toastCloseButton = document.querySelector("[data-dismiss='toast']");
  if (toastCloseButton) {
    toastCloseButton.addEventListener("click", () => {
      const toast = document.querySelector(".toast");
      toast.classList.remove("show");
      toast.remove();
    });
  }
}
