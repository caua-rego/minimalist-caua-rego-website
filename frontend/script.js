// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('click', () => {
    body.classList.toggle('light-theme');
    // Save theme preference to localStorage
    if (body.classList.contains('light-theme')) {
        localStorage.setItem('theme', 'light');
    } else {
        localStorage.setItem('theme', 'dark');
    }
});

// Load saved theme preference
window.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('light-theme');
    }
    // Initial fade-in for the page content
    document.body.classList.add('page-loaded');

    const currentPage = window.location.pathname;
    if (currentPage === '/profile' || currentPage === '/repositories') {
        document.body.classList.add('header-not-fixed');
    }
});

// Page Transition Animations
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', function(e) {
        const targetUrl = this.href; // Get the URL from the link

        // Only apply transition if navigating to a different page
        if (targetUrl !== window.location.href) {
            e.preventDefault(); // Prevent default navigation immediately

            document.body.classList.remove('page-loaded'); // Start fade-out
            document.body.classList.add('page-exiting');

            // Listen for the end of the fade-out transition
            document.body.addEventListener('transitionend', function handler() {
                document.body.removeEventListener('transitionend', handler);
                window.location.href = targetUrl; // Navigate to the new page
            });
        }
    });
});


// Cursor Follower Animation
const cursorFollower = document.getElementById('cursor-follower');

document.addEventListener('mousemove', (e) => {
    cursorFollower.style.left = `${e.clientX}px`;
    cursorFollower.style.top = `${e.clientY}px`;
});

// Add hover effect for interactive elements (e.g., links, buttons, main text)
document.addEventListener('mouseover', (e) => {
    const target = e.target;
    const isInteractive = target.tagName === 'A' ||
                          target.tagName === 'BUTTON' ||
                          target.closest('nav') ||
                          target.closest('form') ||
                          target.closest('.page h1') ||
                          target.closest('.page p');

    if (isInteractive) {
        cursorFollower.classList.add('text-hover');
    } else {
        cursorFollower.classList.remove('text-hover');
    }
});

document.addEventListener('mouseout', (e) => {
    const target = e.target;
    const isInteractive = target.tagName === 'A' ||
                          target.tagName === 'BUTTON' ||
                          target.closest('nav') ||
                          target.closest('form') ||
                          target.closest('.page h1') ||
                          target.closest('.page p');

    if (isInteractive) {
        // Check if we are still hovering over an interactive element after mouseout
        // This prevents flickering when moving between closely spaced interactive elements
        if (!e.relatedTarget || (!e.relatedTarget.tagName === 'A' &&
                                !e.relatedTarget.tagName === 'BUTTON' &&
                                !e.relatedTarget.closest('nav') &&
                                !e.relatedTarget.closest('form') &&
                                !e.relatedTarge.closest('.page h1') &&
                                !e.relatedTarget.closest('.page p'))) {
            cursorFollower.classList.remove('text-hover');
        }
    }
});

// Contact Form Submission
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = document.getElementById('contactName').value;
        const email = document.getElementById('contactEmail').value;
        const message = document.getElementById('contactMessage').value;

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, message }),
            });

            const data = await response.json();

            if (response.ok) {
                formMessage.style.color = 'green';
                contactForm.reset(); // Clear the form
            } else {
                formMessage.style.color = 'red';
            }
            formMessage.textContent = data.message;
        } catch (error) {
            console.error('Error submitting contact form:', error);
            formMessage.style.color = 'red';
            formMessage.textContent = 'An unexpected error occurred. Please try again.';
        }
    });
}

const header = document.querySelector('header');
document.addEventListener('mousemove', (e) => {
    if (document.body.classList.contains('header-not-fixed')) {
        if (e.clientY < 100) {
            header.classList.add('visible');
        } else {
            header.classList.remove('visible');
        }
    }
});

particlesJS('particles-js', 
{
  "particles": {
    "number": {
      "value": 80,
      "density": {
        "enable": true,
        "value_area": 800
      }
    },
    "color": {
      "value": "#ffffff"
    },
    "shape": {
      "type": "circle",
      "stroke": {
        "width": 0,
        "color": "#000000"
      },
      "polygon": {
        "nb_sides": 5
      },
      "image": {
        "src": "img/github.svg",
        "width": 100,
        "height": 100
      }
    },
    "opacity": {
      "value": 0.5,
      "random": false,
      "anim": {
        "enable": false,
        "speed": 1,
        "opacity_min": 0.1,
        "sync": false
      }
    },
    "size": {
      "value": 3,
      "random": true,
      "anim": {
        "enable": false,
        "speed": 40,
        "size_min": 0.1,
        "sync": false
      }
    },
    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#ffffff",
      "opacity": 0.4,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 6,
      "direction": "none",
      "random": false,
      "straight": false,
      "out_mode": "out",
      "bounce": false,
      "attract": {
        "enable": false,
        "rotateX": 600,
        "rotateY": 1200
      }
    }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": {
      "onhover": {
        "enable": true,
        "mode": "repulse"
      },
      "onclick": {
        "enable": true,
        "mode": "push"
      },
      "resize": true
    },
    "modes": {
      "grab": {
        "distance": 400,
        "line_linked": {
          "opacity": 1
        }
      },
      "bubble": {
        "distance": 400,
        "size": 40,
        "duration": 2,
        "opacity": 8,
        "speed": 3
      },
      "repulse": {
        "distance": 200,
        "duration": 0.4
      },
      "push": {
        "particles_nb": 4
      },
      "remove": {
        "particles_nb": 2
      }
    }
  },
  "retina_detect": true
}
);
