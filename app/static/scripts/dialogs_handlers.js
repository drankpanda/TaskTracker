let openAddDialogBtn = document.getElementById("open-add-task-dialog");
let closeAddDialogBtn = document.getElementById("close-add-task-dialog")
let addDialog = document.getElementById("add-dialog-blur");

openAddDialogBtn.addEventListener("click", () => {
    addDialog.classList.add("enabled");
});

closeAddDialogBtn.addEventListener("click", (ev) => {
    ev.preventDefault();
    addDialog.classList.remove("enabled");
});
