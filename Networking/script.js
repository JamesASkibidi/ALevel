const button = document.getElementById("fontchange");
const paragraph = document.getElementById("new-font");

button.addEventListener("click", function() {
    paragraph.classList.toggle("newfont");
});







// const textbox = document.getElementById("new-font");
// let angle = 0;

// function rotate() {
//     angle = (angle + 2) % 180; 
//     textbox.style.transform = `rotate(${angle}deg)`;
//     requestAnimationFrame(rotate);
// }

// rotate();

const box = document.getElementById("new-font");
let angle = 0;
let rotating = false;

function rotate() {
    if (rotating) {
        angle = (angle + 2) % 360;
        box.style.transform = `rotate(${angle}deg)`;
        requestAnimationFrame(rotate);
    }
}

box.addEventListener("mouseenter", () => {
    rotating = true;
    rotate();
});

box.addEventListener("mouseleave", () => {
    rotating = false;
});