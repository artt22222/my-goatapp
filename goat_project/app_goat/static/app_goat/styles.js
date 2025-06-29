
  document.addEventListener('DOMContentLoaded', function () {
    const goatImages = document.querySelectorAll('.goat-image');

    goatImages.forEach(image => {
      image.addEventListener('click', () => {
        // ลบคลาส active ออกจากทุกภาพ
        goatImages.forEach(img => img.classList.remove('active'));

        // ใส่ active เฉพาะรูปที่คลิก
        image.classList.add('active');
      });
    });
  });