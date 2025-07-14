
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    addEventListeners();
    initializeAnimations();
});

function initializeApp() {
    console.log('DGOAT About Page initialized');
    
    // Add entrance animations
    setTimeout(() => {
        const textContent = document.querySelector('.text-content');
        const imageGallery = document.querySelector('.image-gallery');
        
        if (textContent) {
            textContent.classList.add('slide-in-left');
        }
        
        if (imageGallery) {
            imageGallery.classList.add('slide-in-right');
        }
    }, 300);
}

function addEventListeners() {
    // Navigation menu interactions
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', handleNavClick);
    });
    
    // Navigation dots interactions
    const dots = document.querySelectorAll('.dot');
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => handleDotClick(index));
    });
    
    // Image gallery interactions
    const imageCards = document.querySelectorAll('.image-card');
    imageCards.forEach(card => {
        card.addEventListener('click', handleImageClick);
    });
    
    // Add parallax effect to background decorations
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('mousemove', handleMouseMove);
}

function handleNavClick(event) {
    
    
    // Remove active class from all nav items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    // Add active class to clicked item
    event.currentTarget.classList.add('active');
    
    // Add click animation
    const item = event.currentTarget;
    item.style.transform = 'translateX(10px)';
    setTimeout(() => {
        item.style.transform = 'translateX(5px)';
    }, 150);
    
    console.log('Navigation clicked:', event.currentTarget.textContent.trim());
}

function handleDotClick(index) {
    // Remove active class from all dots
    document.querySelectorAll('.dot').forEach(dot => {
        dot.classList.remove('active');
    });
    
    // Add active class to clicked dot
    document.querySelectorAll('.dot')[index].classList.add('active');
    
    // Animate content change (placeholder)
    animateContentChange(index);
    
    console.log('Dot clicked:', index);
}

function handleImageClick(event) {
    const card = event.currentTarget;
    
    // Add click animation
    card.style.transform = 'scale(1.1)';
    setTimeout(() => {
        card.style.transform = 'scale(1)';
    }, 200);
    
    // Show image modal (placeholder)
    showImageModal(card.querySelector('img').src);
    
    console.log('Image clicked');
}

function handleScroll() {
    const scrollY = window.scrollY;
    const circles = document.querySelectorAll('.circle');
    
    circles.forEach((circle, index) => {
        const speed = 0.5 + (index * 0.2);
        circle.style.transform = `translateY(${scrollY * speed}px)`;
    });
}

function handleMouseMove(event) {
    const { clientX, clientY } = event;
    const { innerWidth, innerHeight } = window;
    
    const moveX = (clientX / innerWidth) * 20 - 10;
    const moveY = (clientY / innerHeight) * 20 - 10;
    
    const dotsPattern = document.querySelector('.dots-pattern');
    if (dotsPattern) {
        dotsPattern.style.transform = `translateY(-50%) translate(${moveX}px, ${moveY}px)`;
    }
}

function animateContentChange(index) {
    const textContent = document.querySelector('.text-content');
    const imageGallery = document.querySelector('.image-gallery');
    
    // Fade out
    textContent.style.opacity = '0.7';
    imageGallery.style.opacity = '0.7';
    
    // Content change logic here (placeholder)
    setTimeout(() => {
        // Fade in
        textContent.style.opacity = '1';
        imageGallery.style.opacity = '1';
        
        // Update content based on index
        updateContent(index);
    }, 300);
}

function updateContent(index) {
    const contents = [
        {
            title: "เกี่ยวกับเรา",
            subtitle: "การผสมผสาน<br>ความรู้และนวัตกรรม.",
            text: "เรามีแนวทางการวิจัยที่ผสมผสานความรู้จากการแพทย์สัตว์ดั้งเดิมและเทคโนโลยีล้ำสมัย เพื่อพัฒนาโซลูชันที่เหมาะสมที่สุดสำหรับการดูแลสุขภาพแพะ และเพิ่มประสิทธิภาพในการเลี้ยงแพะเพื่อการผลิตที่ยั่งยืน"
        },
        {
            title: "ภารกิจของเรา",
            subtitle: "ยกระดับสุขภาพแพะ<br>ด้วยการวินิจฉัยที่รวดเร็วและแม่นยำ",
            text: "เรามุ่งมั่นที่จะส่งเสริมสุขภาพของแพะด้วยการวิจัยที่ครบวงจร และการใช้โซลูชันที่ทันสมัยเพื่อพัฒนาคุณภาพชีวิตของแพะ พร้อมทั้งการป้องกันโรคและเพิ่มผลผลิตในฟาร์ม"
        },
        {
            title: "วิสัยทัศน์ของเรา",
            subtitle: "การเป็นผู้นำในด้านการดูแลสุขภาพแพะ",
            text: "เราตั้งเป้าหมายที่จะเป็นแหล่งข้อมูลชั้นนำในด้านสุขภาพและการป้องกันโรคแพะในเอเชียตะวันออกเฉียงใต้ เพื่อให้เกษตรกรได้รับประโยชน์จากความรู้และเทคโนโลยีใหม่ๆ ในการดูแลสัตว์เลี้ยงอย่างมีประสิทธิภาพ"
        },
        {
            title: "ทีมงานของเรา",
            subtitle: "ผู้เชี่ยวชาญที่ทุ่มเทเพื่อสุขภาพแพะ",
            text: "ทีมงานของเราประกอบไปด้วยสัตวแพทย์ที่มีประสบการณ์ นักวิจัยที่มีความเชี่ยวชาญ และผู้เชี่ยวชาญด้านเทคโนโลยี ที่ทำงานร่วมกันเพื่อพัฒนาโซลูชันที่ทันสมัยในการดูแลสุขภาพแพะให้ดียิ่งขึ้น"
        }
    ];
    
    const content = contents[index];
    const titleElement = document.querySelector('.about-title');
    const subtitleElement = document.querySelector('.about-subtitle');
    const textElement = document.querySelector('.about-text p');
    
    if (titleElement) titleElement.textContent = content.title;
    if (subtitleElement) subtitleElement.innerHTML = content.subtitle;
    if (textElement) textElement.textContent = content.text;
}

function showImageModal(imageSrc) {
    // Create modal overlay
    const modal = document.createElement('div');
    modal.className = 'image-modal';
    modal.innerHTML = `
        <div class="modal-overlay">
            <div class="modal-content">
                <button class="modal-close">&times;</button>
                <img src="${imageSrc}" alt="Large view" />
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Add modal styles
    const style = document.createElement('style');
    style.textContent = `
        .image-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1000;
            animation: fadeIn 0.3s ease;
        }
        
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .modal-content {
            position: relative;
            max-width: 80%;
            max-height: 80%;
        }
        
        .modal-content img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 10px;
        }
        
        .modal-close {
            position: absolute;
            top: -40px;
            right: -40px;
            width: 30px;
            height: 30px;
            background: white;
            border: none;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    `;
    document.head.appendChild(style);
    
    // Add close event listeners
    modal.querySelector('.modal-close').addEventListener('click', () => {
        modal.remove();
        style.remove();
    });
    
    modal.querySelector('.modal-overlay').addEventListener('click', (e) => {
        if (e.target === e.currentTarget) {
            modal.remove();
            style.remove();
        }
    });
}

function initializeAnimations() {
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1
    });
    
    // Observe elements for animation
    const elementsToAnimate = document.querySelectorAll('.about-title, .about-subtitle, .about-text, .image-card');
    elementsToAnimate.forEach(el => {
        observer.observe(el);
    });
    
    // Auto-rotate navigation dots
    let currentDot = 0;
    setInterval(() => {
        currentDot = (currentDot + 1) % 4;
        handleDotClick(currentDot);
    }, 5000);
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Export functions for potential module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initializeApp,
        addEventListeners,
        handleNavClick,
        handleDotClick,
        showImageModal
    };
}