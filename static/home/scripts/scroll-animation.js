// seleciona todos os elementos que possuem o atributo 'data-animation'
const animatedElements = document.querySelectorAll("[data-animation]");

// função que verifica se um elemento está dentro da área visível da página
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom - 200 <=
        (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <=
        (window.innerWidth || document.documentElement.clientWidth)
    );
}

// função que aplica a classe 'animate' nos elementos que estão dentro da área visível da página
function animateElements() {
    for (let i = 0; i < animatedElements.length; i++) {
        const el = animatedElements[i];
        if (isElementInViewport(el)) {
            el.classList.add("animate");
        }
    }
}

// adiciona um evento de rolagem na página
window.addEventListener("scroll", function () {
    // remove o evento de rolagem depois que todos os elementos foram animados
    if (!animatedElements.length) {
        window.removeEventListener("scroll", this);
        return;
    }

    animateElements();

    // remove os elementos já animados da lista de elementos
    for (let i = 0; i < animatedElements.length; i++) {
        const el = animatedElements[i];
        if (el.classList.contains("animate")) {
            animatedElements.splice(i, 1);
            i--;
        }
    }
});