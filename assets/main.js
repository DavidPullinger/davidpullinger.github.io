e = document.getElementById("scroll-indicator")
window.addEventListener("scroll", () => {
    // decrease opacity of scroll indicator, according to its distance from top
    // use an exponential function rather than just linear so it is opaque for longer
    e.style.opacity = (Math.exp(2*e.getBoundingClientRect().top/window.innerHeight)-1)
})
