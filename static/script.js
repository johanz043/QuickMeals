function showLoader() {
    document.getElementById("loading").style.display = "block";
}

function toggleDetails(card) {
    const details = card.querySelector(".recipe-details");
    details.style.display =
        details.style.display === "block" ? "none" : "block";
}

document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("imageInput");
    const scanBtn = document.getElementById("scanBtn");

    imageInput.addEventListener("change", function () {
        scanBtn.disabled = imageInput.files.length === 0;
    });
});