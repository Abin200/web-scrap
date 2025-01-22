document.addEventListener("DOMContentLoaded", function () {
    const jobFilter = document.getElementById("jobFilter");
    const jobTableBody = document.getElementById("jobTableBody");

    // Add event listener for the filter dropdown
    jobFilter.addEventListener("change", function () {
        const filterValue = jobFilter.value.toLowerCase();

        // Get all rows from the table body
        const rows = jobTableBody.getElementsByTagName("tr");

        // Loop through rows and filter them
        for (const row of rows) {
            const jobTitle = row.getElementsByTagName("td")[0].innerText.toLowerCase();
            if (filterValue === "all" || jobTitle.includes(filterValue)) {
                row.style.display = ""; // Show row
            } else {
                row.style.display = "none"; // Hide row
            }
        }
    });
});
