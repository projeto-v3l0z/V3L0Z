const rocket = document.getElementById("scroll-to-top");

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
}

window.addEventListener("scroll", function () {
    if (window.scrollY > 500) {
        rocket.classList.add("show");
    } else {
        rocket.classList.remove("show");
    }
});

rocket.addEventListener("click", function () {
    audio.play();
    scrollToTop();
    rocket.classList.add("move");
    setTimeout(function () {
        rocket.classList.remove("move");
    }, 1000);
});