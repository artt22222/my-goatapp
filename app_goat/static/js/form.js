document.addEventListener("DOMContentLoaded", function () {
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
        const selected = [...checkboxes].filter(cb => cb.checked);

        if (selected.length > 0) {
            summaryBox.style.display = "block";

            selected.forEach(cb => {
                // ดึงข้อความจาก label ที่ผูกกับ checkbox
                const label = document.querySelector(`label[for="${cb.id}"]`);
                const symptomText = label ? label.textContent : cb.value;

                const li = document.createElement("li");
                li.textContent = symptomText;
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
