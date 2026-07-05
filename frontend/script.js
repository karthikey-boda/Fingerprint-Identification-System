const voterId = document.getElementById("voter_id");
const fingerprint = document.getElementById("fingerprint");
const preview = document.getElementById("preview");
const uploadBtn = document.getElementById("uploadBtn");
const result = document.getElementById("result");

// Preview image
fingerprint.addEventListener("change", function () {

    const file = this.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
    }

});

// Upload
uploadBtn.addEventListener("click", async function (event) {

    event.preventDefault();

    // Validation
    if (voterId.value.trim() === "") {
        alert("Please enter Voter ID.");
        return;
    }

    if (fingerprint.files.length === 0) {
        alert("Please upload a fingerprint.");
        return;
    }

    result.innerHTML = "Processing...";

    const formData = new FormData();

    formData.append("voter_id", voterId.value.trim());
    formData.append("fingerprint", fingerprint.files[0]);

    try {

        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.status === "found") {

            result.innerHTML = `
                <h2 style="color:green;">✅ Fingerprint Found</h2>

                <p><b>Registered Voter ID:</b> ${data.voter_id}</p>

                <p><b>Similarity:</b> ${data.similarity}%</p>
            `;

        }

        else if (data.status === "enrolled") {

            result.innerHTML = `
                <h2 style="color:blue;">✅ New Fingerprint Enrolled</h2>

                <p><b>Voter ID:</b> ${data.voter_id}</p>
            `;

        }

        else if (data.status === "duplicate") {

            result.innerHTML = `
                <h2 style="color:red;">
                    ${data.message}
                </h2>
            `;

        }

        else {

            result.innerHTML = `
                <h2 style="color:red;">
                    ${data.message}
                </h2>
            `;

        }

    }

    catch (error) {

        console.error(error);

        result.innerHTML = `
            <h2 style="color:red;">
                Failed to connect to server.
            </h2>
        `;

    }

});