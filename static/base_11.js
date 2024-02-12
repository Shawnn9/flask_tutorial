
document.addEventListener("DOMContentLoaded", function () {
    const body = document.querySelector('body');
    const sidebar = body.querySelector('nav');
    const toggle = body.querySelector(".toggle");

    toggle.addEventListener("click", () => {
      console.log("Toggle clicked");
      sidebar.classList.toggle("close");
    });

    const searchBtn = body.querySelector(".search-box");

    searchBtn.addEventListener("click", () => {
      sidebar.classList.remove("close");
    });

    const modeSwitch = body.querySelector(".toggle-switch");
    const modeText = body.querySelector(".mode-text");

    modeSwitch.addEventListener("click", () => {
      body.classList.toggle("dark");
      modeText.innerText = body.classList.contains("dark") ? "Light mode" : "Dark mode";
    });
  });
