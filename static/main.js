document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".btn-delete");

    deleteButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            const confirmed = confirm("Êtes-vous sûr de vouloir supprimer cette tâche ?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});

const searchInput = document.getElementById("search");
if (searchInput) {
    searchInput.addEventListener("input", () => {
        const filter = searchInput.value.toLowerCase();
        const rows = document.querySelectorAll(".todo-row");

        rows.forEach(row => {
            const title = row.querySelector(".todo-title").textContent.toLowerCase();
            row.style.display = title.includes(filter) ? "" : "none";
        });
    });
}

