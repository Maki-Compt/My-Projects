
// Variables!
const slider = document.querySelector(".pop-up-left-slider")
const right_arrow = document.querySelector(".right-key")
const left_arrow = document.querySelector(".left-key")

const left_arrow_some_items = document.querySelector(".items-nav-bar-left")
const right_arrow_some_items = document.querySelector(".items-nav-bar-right")
const wrapper = document.querySelector(".some-items-bottom")

const left_arrow_some_items_promo = document.querySelector(".sm-promo-btn-left")
const right_arrow_some_items_promo = document.querySelector(".sm-promo-btn-rigth")
const wrapper_promo = document.querySelector(".sm-promo")

const test_promp_1 = document.querySelector(".some-items")
const test_promp = document.querySelector(".sm-2")

const nav_bar_promo = document.querySelector(".items-nav-bar")
const nav_bar_promo_tends = document.querySelector(".tends")

var index = 0

const scrollPixels = 200;
const scrollPixels_promo = 200;

// Some items 1 Scroll Behaviour! 

test_promp_1.addEventListener("mouseenter", ()=> {
    nav_bar_promo.style.opacity = "1"
})

test_promp_1.addEventListener("mouseleave", ()=> {
    nav_bar_promo.style.opacity = "0"
})

right_arrow_some_items.addEventListener("click", ()=> {
    
    wrapper.scrollBy({ left: scrollPixels, behavior: "smooth" });
})

left_arrow_some_items.addEventListener("click", ()=> {    
    wrapper.scrollBy({ left: -scrollPixels, behavior: "smooth" });
})


// Some items 2 Scroll Behaviour! 

test_promp.addEventListener("mouseenter", ()=> {
    nav_bar_promo_tends.style.opacity = "1"
})

test_promp.addEventListener("mouseleave", ()=> {
    nav_bar_promo_tends.style.opacity = "0"
})

left_arrow_some_items_promo.addEventListener("click", () => {
    wrapper_promo.scrollBy({ left: -scrollPixels_promo, behavior: "smooth" });
})

right_arrow_some_items_promo.addEventListener("click", () => {
    wrapper_promo.scrollBy({ left: scrollPixels_promo, behavior: "smooth" });
})




// Caroussel Behaviour

right_arrow.addEventListener("click", () => {

    if (index != -500) {
        index -= 100
    } else {
        index = -500
    }

    slider.style.transform = `translateX(${index}%)`
})


left_arrow.addEventListener("click", () => {

    if (index != 0) {
        index += 100
    } else {
        index = 0
    }
    
    slider.style.transform = `translateX(${index}%)`
})



