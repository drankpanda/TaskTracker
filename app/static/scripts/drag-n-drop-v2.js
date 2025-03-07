function dragStart(ev) {
    ev.dataTransfer.effectAllowed = "move";
    this.classList.add("dragging");
}

function dragEnd(ev) {
    ev.preventDefault();
    this.classList.remove("dragging");
    if (ev.dataTransfer.dropEffect == "none") {
        let expandedDropzones = document.getElementsByClassName("expanding");
        if (expandedDropzones.length != 0) {
            // Only one dropzone can be expanding in the moment
            expandedDropzones[0].classList.remove("expanding");
        }
    }
}

function dragEnter(ev) {
    this.classList.add("expanding");
}

function dragOver(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move";
}

function dragLeave(ev) {
    this.classList.remove("expanding");
}

function addDropzoneListeners(dropzone) {
    dropzone.addEventListener("dragenter", dragEnter);
    dropzone.addEventListener("dragover", dragOver);
    dropzone.addEventListener("dragleave", dragLeave);
    dropzone.addEventListener("drop", dragDrop);
}

function dragDrop(ev) {
    this.classList.remove("expanding");
    let dragging = document.getElementsByClassName("dragging")[0];
    
    if (
        !(this.previousElementSibling === dragging) &&
        !(this === dragging.previousElementSibling)
    ) {
        let duration = 400;

        let draggingPrevDropzone = dragging.previousElementSibling;
        $(draggingPrevDropzone).css({transition: "none"}).slideUp(duration, () => {
            $(draggingPrevDropzone).remove();
        })
        
        let newDropzone = dragging.nextElementSibling.cloneNode(true);
        addDropzoneListeners(newDropzone);
        $(newDropzone).insertBefore(this);
        $(newDropzone).slideToggle(0);
        $(newDropzone).slideToggle(duration);

        let html = document.getElementsByTagName("html")[0];
        let fontSize = parseInt(window.getComputedStyle(html)["fontSize"]);
        let vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
        let leftOffset = Math.min(2 * fontSize, 0.03 * vw);
        $(dragging).animate({
            opacity: "toggle",
            height: "toggle",
            paddingTop: "toggle",
            paddingBottom: "toggle",
            left: `-=${leftOffset}`
        }, duration, () => {
            $(dragging).insertBefore(this);
        });
        $(dragging).animate({
            opacity: "toggle",
            height: "toggle",
            paddingTop: "toggle",
            paddingBottom: "toggle",
            left: `+=${leftOffset}`
        }, duration);
    }
}

const draggables = document.querySelectorAll(".draggable");
const dropzones = document.querySelectorAll(".dropzone");

draggables.forEach((draggable) => {
    draggable.addEventListener("dragstart", dragStart);
    draggable.addEventListener("dragend", dragEnd);
});

dropzones.forEach((dropzone) => {
    if (dropzone.classList.contains("move")) {
        addDropzoneListeners(dropzone);
    }
});
