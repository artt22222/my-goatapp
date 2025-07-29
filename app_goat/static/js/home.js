// script.js
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
    
    // Add event listeners
    addEventListeners();
    
    // Initialize animations
    initializeAnimations();
});

function initializeApp() {
    console.log('DGOAT Dashboard initialized');
    
    // Add loading animation to stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
        card.classList.add('animate-in');
    });
}

function addEventListeners() {
    // Navigation menu interactions
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', handleNavClick);
    });
    
    // CTA button interaction
    const ctaButton = document.querySelector('.cta-button');
    if (ctaButton) {
        ctaButton.addEventListener('click', handleCTAClick);
    }
    
    // Stat cards hover effects
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
        card.addEventListener('mouseenter', handleStatCardHover);
        card.addEventListener('mouseleave', handleStatCardLeave);
    });
    
    // Research cards interactions
    const researchCards = document.querySelectorAll('.research-card');
    researchCards.forEach(card => {
        card.addEventListener('click', handleResearchCardClick);
    });
}



function handleCTAClick(event) {
    const button = event.currentTarget;
    
    // Add click animation
    button.style.transform = 'translateY(-2px) scale(0.95)';
    setTimeout(() => {
        button.style.transform = 'translateY(-2px) scale(1)';
    }, 150);
    
    // Show modal or redirect (placeholder)
    showNotification('เริ่มการวินิจฉัย...', 'success');
    
    console.log('CTA Button clicked - Start diagnosis');
}

function handleStatCardHover(event) {
    const card = event.currentTarget;
    const icon = card.querySelector('.stat-icon');
    
    // Add hover animation to icon
    if (icon) {
        icon.style.transform = 'rotate(10deg) scale(1.1)';
    }
}

function handleStatCardLeave(event) {
    const card = event.currentTarget;
    const icon = card.querySelector('.stat-icon');
    
    // Reset icon animation
    if (icon) {
        icon.style.transform = 'rotate(0deg) scale(1)';
    }
}

function handleResearchCardClick(event) {
    const card = event.currentTarget;
    const title = card.querySelector('h3').textContent;
    
    // Add click animation
    card.style.transform = 'translateY(-3px) scale(0.98)';
    setTimeout(() => {
        card.style.transform = 'translateY(-3px) scale(1)';
    }, 150);
    
    showNotification(`เปิดรายละเอียด: ${title}`, 'info');
    
    console.log('Research card clicked:', title);
}

function initializeAnimations() {
    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .animate-in {
            animation: fadeInUp 0.6s ease forwards;
        }
        
        .stat-icon {
            transition: transform 0.3s ease;
        }
        
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            z-index: 1000;
            animation: slideInRight 0.3s ease;
        }
        
        .notification.success {
            background: linear-gradient(135deg, #28a745, #20c997);
        }
        
        .notification.info {
            background: linear-gradient(135deg, #17a2b8, #007bff);
        }
        
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => {
        notification.remove();
    });
    
    // Create new notification
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Utility functions
function animateNumber(element, start, end, duration) {
    const range = end - start;
    const minTimer = 50;
    const stepTime = Math.abs(Math.floor(duration / range));
    const timer = stepTime < minTimer ? minTimer : stepTime;
    
    const startTime = new Date().getTime();
    const endTime = startTime + duration;
    
    function run() {
        const now = new Date().getTime();
        const remaining = Math.max((endTime - now) / duration, 0);
        const value = Math.round(end - (remaining * range));
        const suffix = element.dataset.suffix || '';
        
        element.textContent = value.toLocaleString() + suffix;
        
        if (value === end) {
            clearInterval(timer);
        }
    }
    
    const timer_id = setInterval(run, timer);
    run();
}

// Initialize number animations when page loads
window.addEventListener('load', function() {
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(element => {
        const finalNumber = parseInt(element.dataset.value);
        if (!isNaN(finalNumber)) {
            element.textContent = '0';
            setTimeout(() => {
                animateNumber(element, 0, finalNumber, 2000);
            }, 500);
        }
    });
});



// Export functions for potential module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initializeApp,
        addEventListeners,
        showNotification,
        animateNumber
    };
}