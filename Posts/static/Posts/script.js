const hamburgerClick = document.getElementById("hamburgerIcon");
let recentPostContainer = document.getElementById("postContainerId");
let recentPostContainerState = true;

hamburgerClick.addEventListener("click", function (event) {
  event.preventDefault();
  if (window.innerWidth < 992) {
    recentPostContainerState = !recentPostContainerState;
    recentPostContainer.style.display = recentPostContainerState
      ? "none"
      : "flex";
  }
});
