document.addEventListener("DOMContentLoaded", function () {
    const body = document.querySelector('body');
    const sidebar = document.querySelector('.sidebar');
    const toggle = document.querySelector(".toggle");
    const modeText = document.querySelector(".mode-text");

    toggle.addEventListener("click", () => {
        sidebar.classList.toggle("close");
    });

    const searchBtn = document.querySelector(".search-box");

    searchBtn.addEventListener("click", () => {
        sidebar.classList.remove("close");
    });

    const modeSwitch = document.querySelector(".toggle-switch");

    modeSwitch.addEventListener("click", () => {
        body.classList.toggle("dark");
        modeText.innerText = body.classList.contains("dark") ? "Light mode" : "Dark mode";
    });
});
