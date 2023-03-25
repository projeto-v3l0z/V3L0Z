const carousel = document.querySelector("#carouselExampleIndicators");
const listGroup = document.querySelector("#projetosFeitos");

carousel.addEventListener("slide.bs.carousel", function (event) {
    const items = listGroup.children;
    const activeIndex = event.to;

    for (let i = 0; i < items.length; i++) {
        if (i === activeIndex) {
            items[i].classList.add("active");
        } else {
            items[i].classList.remove("active");
        }
    }
});