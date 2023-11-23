scroller = document.getElementById("scroll-indicator")
overlay = document.getElementById("overlay")
window.addEventListener("scroll", () => {
    // decrease opacity of scroll indicator, according to its distance from top
    // use an exponential function rather than just linear so it is opaque for longer
    scroller.style.opacity = (Math.exp(2*scroller.getBoundingClientRect().top/window.innerHeight)-1)
})

const toggleImageFullscreen = (e) => {
    // get image, based on the target of the click
    // if its the overlay, we need to get the image by its id
    // otherwise, we can just use the target of the click event
    e.preventDefault();
    image = (e.target == overlay) ? document.getElementById("fullScreenImage") : e.target

    // toggle image and overlay fullscreen properties
    image.classList.toggle("full-screen")
    overlay.classList.toggle("hidden")

    // finally, based on if we are hiding or showing the image
    // (i.e. it has an id)
    // we set or remove it's id
    if (image.id){
        image.removeAttribute("id");
    }
    else {
        image.id = "fullScreenImage";
    }
}
