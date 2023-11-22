scroller = document.getElementById("scroll-indicator")
overlay = document.getElementById("overlay")
window.addEventListener("scroll", () => {
    // decrease opacity of scroll indicator, according to its distance from top
    // use an exponential function rather than just linear so it is opaque for longer
    scroller.style.opacity = (Math.exp(2*scroller.getBoundingClientRect().top/window.innerHeight)-1)
})

const enlargeImage = (e) => {
    e.target.classList.toggle("full-screen")
    overlay.classList.toggle("hidden");
}
