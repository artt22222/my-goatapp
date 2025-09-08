 // Animate progress bars on load
        window.addEventListener('load', function() {
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach((bar, index) => {
                setTimeout(() => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 100);
                }, index * 200);
            });
        });

        // Show more info function
        function showMoreInfo(diseaseName) {
            alert(`แสดงข้อมูลเพิ่มเติมเกี่ยวกับ ${diseaseName}`);
            // You can replace this with actual navigation or modal logic
        }

        // Add click animations to cards
        document.querySelectorAll('.disease-card').forEach(card => {
            card.addEventListener('click', function(e) {
                if (!e.target.classList.contains('more-info-btn')) {
                    this.style.transform = 'scale(0.98)';
                    setTimeout(() => {
                        this.style.transform = '';
                    }, 150);
                }
            });
        });

        function toggleOthers() {
        const div = document.getElementById("others");
        div.style.display = div.style.display === "none" ? "block" : "none";
}