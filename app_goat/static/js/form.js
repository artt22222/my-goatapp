document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form"); 
    const submitBtn = document.querySelector(".submit-btn"); 
    const checkboxes = document.querySelectorAll('input[name="symptoms[]"]');
    const summaryBox = document.getElementById("summary-box");
    const selectedList = document.getElementById("selected-symptoms");

    checkboxes.forEach(cb => {
        cb.addEventListener("change", updateSummary);
    });

    function updateSummary() {
        selectedList.innerHTML = "";
        const selected = [...checkboxes].filter(cb => cb.checked).map(cb => cb.value);

        if (selected.length > 0) {
            summaryBox.style.display = "block";
            selected.forEach(symptom => {
                const li = document.createElement("li");
                li.textContent = symptom;
                selectedList.appendChild(li);
            });
        } else {
            summaryBox.style.display = "none";
        }
    }

    form.addEventListener("submit", function (e) {
        const selected = document.querySelectorAll("input[name='symptoms[]']:checked");
        if (selected.length < 3) {
            e.preventDefault();
            submitBtn.textContent = "⚠ เลือกอย่างน้อย 3 อาการ";
            submitBtn.style.backgroundColor = "red";
        } else {
            submitBtn.textContent = "🔍 ส่งข้อมูลวินิจฉัย";
            submitBtn.style.backgroundColor = "green";
        }
    });
});
