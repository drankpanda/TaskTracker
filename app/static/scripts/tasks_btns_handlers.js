// Add new task button
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

// Editting modes (edit or delete)
let currentMode = document.getElementById("editting-mode");
let applyBtn = document.getElementById("apply-changes");

function toggleEdittingMode(ev) {
    let currentModeClass;
    let currentModeStr;
    let previousModeClass;
    let previousModeStr;
    let applyBtnText;
    let confirmMsg;

    if (ev.currentTarget == editToggleBtn) {
        currentModeClass = "edit-mode";
        currentModeStr = "редактирования";
        previousModeClass = "delete-mode";
        previousModeStr = "удаления";
        applyBtnText = "Сохранить изменения";
        confirmMsg = "Все несохранённые данные будут потеряны! Вы уверены, что хотите выйти из режима редактирования?";
    } else {
        currentModeClass = "delete-mode";
        currentModeStr = "удаления";
        previousModeClass = "edit-mode";
        previousModeStr = "редактирования";
        applyBtnText = "Удалить выбранное";
        confirmMsg = "Операция удаления не будет завершена! Вы уверены, что хотите выйти из режима удаления?";
    }

    if (applyBtn.classList.contains(previousModeClass)) {
        alert(`Сначала завершите операцию ${previousModeStr}.`);
        return;
    }
    if (!applyBtn.classList.contains(currentModeClass)) {
        applyBtn.classList.add(currentModeClass);
        applyBtn.innerHTML = applyBtnText;
        currentMode.innerHTML = `Режим ${currentModeStr}`;
        openAddDialogBtn.disabled = true;
    } else if (confirm(confirmMsg)) {
        applyBtn.classList.remove(currentModeClass);
        applyBtn.innerHTML = "";
        currentMode.innerHTML = "";
        openAddDialogBtn.disabled = false;
    }
}

// Edit mode
let editToggleBtn = document.getElementById("toggle-edit-mode");
editToggleBtn.addEventListener("click", toggleEdittingMode);

// Delete mode
let deleteToggleBtn = document.getElementById("toggle-delete-mode");
deleteToggleBtn.addEventListener("click", toggleEdittingMode);
