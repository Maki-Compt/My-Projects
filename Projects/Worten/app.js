
var btn_next = document.querySelector(".right-arrow")
var btn_prev = document.querySelector(".left-arrow")
var slider = document.querySelector(".slides")
var menu = document.querySelector(".menu")

var collapsble_menu = document.querySelector(".collapsble-menu")
var collapsble_menu_close_btn = document.querySelector(".x-close")
var bg_black = document.querySelector(".black-background ")
var caroussels = document.querySelectorAll(".caroussel-1")
var index = 0

// Caroussel Buttons

function caroussel_foward() {
    
    if (index > -600) {

        index -= 100

        slider.style.transform = `translateX(${index}%)`

    }
    
}

function caroussel_backwards() {
    
    if (index < 0) {
    
        index += 100

        slider.style.transform = `translateX(${index}%)`

    }
    
}

btn_next.addEventListener("click", () => {
    
    caroussel_foward()

})

btn_prev.addEventListener("click", () => {

    caroussel_backwards()

})

// Collapsble Menu

function close_collapsble_menu() {
    
    collapsble_menu.style.transform = `translateX(-370px)`
    document.documentElement.style.overflowY = "visible" 
    bg_black.style.display = "none"

}

menu.addEventListener("click", ()=> {

    collapsble_menu.style.transform = `translateX(0px)`
    bg_black.style.display = "block"
    document.documentElement.style.overflowY = "hidden" 

    collapsble_menu.style.opacity = "100%"

})

collapsble_menu_close_btn.addEventListener("click", () => {
    
    close_collapsble_menu()
})


bg_black.addEventListener("click", () => {
    close_collapsble_menu()
})



