function getDropTarget(container, x, y) {
    const draggables = [...container.querySelectorAll(".draggable:not(.dragging)")];

    for (const draggable of draggables) {
        const draggableRect = draggable.getBoundingClientRect();
        const offsetX = Math.min(50, draggableRect.width * 0.25);
        const offsetY = Math.min(50, draggableRect.height * 0.25);

        if (y > draggableRect.top + offsetY && y < draggableRect.bottom - offsetY
            && x > draggableRect.left + offsetX && x < draggableRect.right - offsetX) {
            return draggable;
        }
    }
    return null;
}

function swapNodes(n1, n2) {
    let p1 = n1.parentNode;
    let p2 = n2.parentNode;
    let i1, i2;

    if ( !p1 || !p2 || p1.isEqualNode(n2) || p2.isEqualNode(n1) ) return;

    for (let i = 0; i < p1.children.length; i++) {
        if (p1.children[i].isEqualNode(n1)) {
            i1 = i;
        }
    }
    for (let i = 0; i < p2.children.length; i++) {
        if (p2.children[i].isEqualNode(n2)) {
            i2 = i;
        }
    }

    if ( p1.isEqualNode(p2) && i1 < i2 ) {
        i2++;
    }
    p1.insertBefore(n2, p1.children[i1]);
    p2.insertBefore(n1, p2.children[i2]);
}

function dragStart(ev) {
    ev.dataTransfer.effectAllowed = "move";
    ev.target.classList.add("dragging");
}

function dragEnd(ev) {
    ev.preventDefault();
    ev.target.classList.remove("dragging");
}

function dragOver(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move";

    const dragging = document.querySelector(".dragging");
    const dropTarget = getDropTarget(ev.currentTarget, ev.clientX, ev.clientY);

    if (dropTarget) {
        swapNodes(dragging, dropTarget);
    } else if (!ev.currentTarget.querySelector(".draggable:not(.dragging)")) {
        ev.currentTarget.appendChild(dragging);
    }
}

const draggables = document.querySelectorAll(".draggable")
const dndContainers = document.querySelectorAll(".dnd-container")

draggables.forEach((draggable) => {
    draggable.addEventListener("dragstart", dragStart);
    draggable.addEventListener("dragend", dragEnd);
});

dndContainers.forEach((container) => {
    if (container.classList.contains("move")) {
        container.addEventListener("dragover", dragOver);
    }
});
