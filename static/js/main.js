document.addEventListener("DOMContentLoaded", function () {
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Contact form handler (if you add one later)
  const form = document.getElementById("contactForm");
  const response = document.getElementById("responseMessage");
  if (form && response) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      response.textContent = "Thanks for your message! We'll get back to you soon.";
      form.reset();
    });
  }

  // Auto-start testimonial carousel (Bootstrap)
  const carousel = document.querySelector("#testimonialCarousel");
  if (carousel) {
    const bsCarousel = new bootstrap.Carousel(carousel, {
      interval: 4000,
      ride: "carousel",
      pause: false
    });
  }

  // Calendly widget is already embedded via HTML — no JS needed unless you want popup mode
});

function toggleMenu() {
      const menu = document.getElementById('menu');
      const icon = document.getElementById('menuIcon');
      const nav_bar = document.getElementById('navbar');

      menu.classList.toggle('show');
      icon.classList.toggle('open');
      nav_bar.classList.toggle('bg_change');
    }


document.querySelectorAll('.menu-overlay a').forEach(link => {
  link.addEventListener('click', () => {
    document.getElementById('menu').classList.remove('show');
    document.getElementById('menuIcon').classList.remove('open');
    document.getElementById('navbar').classList.remove('bg_change');
  });
});