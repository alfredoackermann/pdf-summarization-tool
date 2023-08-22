document.addEventListener("DOMContentLoaded", function() {
  const pdfFileInput = document.getElementById("pdfFile");
  const summarizeButton = document.getElementById("summarizeButton");
  const summaryContainer = document.getElementById("summaryContainer");
  const summaryText = document.getElementById("summaryText");
  const loadingIndicator = document.getElementById("loadingIndicator");

  summarizeButton.addEventListener("click", async function() {
      const file = pdfFileInput.files[0];
      if (!file) {
          alert("Please select a PDF file.");
          return;
      }

      // Disable the button and show loading indicator
      summarizeButton.disabled = true;
      loadingIndicator.style.display = "block";

      const formData = new FormData();
      formData.append("file", file);

      try {
          const response = await fetch("/summarize", {
              method: "POST",
              body: formData,
          });

          const data = await response.json();
          if (response.ok) {
              summaryText.textContent = data.summary;
              summaryContainer.style.display = "block";
          } else {
              alert("Error summarizing PDF.");
          }
      } catch (error) {
          console.error("An error occurred:", error);
          alert("An error occurred. Please try again.");
      } finally {
        // Re-enable the button and hide loading indicator
        summarizeButton.disabled = false;
        loadingIndicator.style.display = "none";
    }
  });
});
