// EstateFlow - Main JavaScript

// Smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Auto-hide alerts after 5 seconds
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    }, 5000);
});

// Form validation for inquiry form
const inquiryForm = document.querySelector('form[action*="inquiry"]');
if (inquiryForm) {
    inquiryForm.addEventListener('submit', function(e) {
        const name = this.querySelector('#name').value.trim();
        const email = this.querySelector('#email').value.trim();
        const phone = this.querySelector('#phone').value.trim();
        const message = this.querySelector('#message').value.trim();

        if (!name || !email || !phone || !message) {
            e.preventDefault();
            alert('Please fill in all fields.');
            return false;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            e.preventDefault();
            alert('Please enter a valid email address.');
            return false;
        }

        const phoneRegex = /^[\d\-\(\)\s\+]{10,}$/;
        if (!phoneRegex.test(phone)) {
            e.preventDefault();
            alert('Please enter a valid phone number.');
            return false;
        }
    });
}

// Add active class to current navigation item
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = location.pathname;
    const menuItems = document.querySelectorAll('.nav-link');

    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });
});

// Fade in animation for cards on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.property-card, .feature-box, .value-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    observer.observe(el);
});

// Format currency display
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Search box functionality
const searchForm = document.querySelector('form[action*="properties"]');
if (searchForm) {
    const inputs = searchForm.querySelectorAll('input[type="text"], select');
    inputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchForm.submit();
            }
        });
    });
}

// Property filter dropdown change handler
const filterSelects = document.querySelectorAll('.filter-card select');
filterSelects.forEach(select => {
    select.addEventListener('change', function() {
        // Auto-submit filter form if needed
        const form = this.closest('form');
        if (form && form.id === 'filterForm') {
            // Optional: Uncomment to auto-submit
            // form.submit();
        }
    });
});

// Image lazy loading fallback
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                }
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
}

// Tooltip initialization
document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(el => {
        new bootstrap.Tooltip(el);
    });
});

// Modal form handler
document.querySelectorAll('form[data-confirm]').forEach(form => {
    form.addEventListener('submit', function(e) {
        const message = this.getAttribute('data-confirm');
        if (!confirm(message)) {
            e.preventDefault();
        }
    });
});

// Navbar active link indicator on scroll
window.addEventListener('scroll', function() {
    let current = '';
    const sections = document.querySelectorAll('section');

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Initialize popovers
document.addEventListener('DOMContentLoaded', function() {
    const popovers = document.querySelectorAll('[data-bs-toggle="popover"]');
    popovers.forEach(el => {
        new bootstrap.Popover(el);
    });
});

// Console message for fun
console.log('%cEstateFlow', 'font-size: 24px; font-weight: bold; color: #d4af37;');
console.log('%cPremium Real Estate Platform', 'font-size: 14px; color: #1a1a2e;');
console.log('Welcome to EstateFlow!');
