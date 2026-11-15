document.addEventListener("DOMContentLoaded", () => {
  const header = document.getElementById("siteHeader");
  const nav = document.getElementById("mainNav");
  const toggle = document.getElementById("menuToggle");

  /* ---------- Header shadow on scroll ---------- */
  const onScroll = () => header && header.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Mobile menu ---------- */
  if (nav && toggle) {
    const setOpen = (open) => {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    };
    toggle.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
    nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener("click", (e) => {
      if (nav.classList.contains("is-open") && !header.contains(e.target)) setOpen(false);
    });
  }

  /* ---------- Highlight the nav link for the section in view ---------- */
  if (nav && "IntersectionObserver" in window) {
    const links = new Map();
    nav.querySelectorAll('a[href^="#"]:not(.btn)').forEach((a) => links.set(a.getAttribute("href").slice(1), a));
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          links.forEach((a) => a.classList.remove("is-active"));
          const link = links.get(entry.target.id);
          if (link) link.classList.add("is-active");
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    links.forEach((_, id) => {
      const section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }

  /* ---------- Contact form: client-side validation, then a normal submit ---------- */
  const form = document.getElementById("contactForm");
  if (form) {
    const fieldOf = (input) => input.closest(".field");
    const check = (input) => {
      const ok = input.checkValidity() && (!input.required || input.value.trim() !== "");
      fieldOf(input).classList.toggle("has-error", !ok);
      return ok;
    };
    const inputs = form.querySelectorAll(".field input, .field textarea");

    inputs.forEach((input) => {
      input.addEventListener("blur", () => input.value && check(input));
      input.addEventListener("input", () => {
        if (fieldOf(input).classList.contains("has-error")) check(input);
      });
    });

    form.addEventListener("submit", (e) => {
      let firstInvalid = null;
      inputs.forEach((input) => {
        if (!check(input) && !firstInvalid) firstInvalid = input;
      });
      if (firstInvalid) {
        e.preventDefault();
        firstInvalid.focus();
        return;
      }
      const button = form.querySelector('button[type="submit"]');
      button.dataset.label = button.textContent;
      button.disabled = true;
      button.textContent = button.dataset.sendingLabel;
    });

    // If the server rejected the submission, bring the user straight to the form.
    const serverError = form.querySelector(".field.has-error input, .field.has-error textarea");
    if (serverError) {
      document.getElementById("contact").scrollIntoView();
      serverError.focus({ preventScroll: true });
    }
  }
});

// Re-enable the submit button if the page is restored from the back/forward cache.
window.addEventListener("pageshow", (e) => {
  if (!e.persisted) return;
  const button = document.querySelector('#contactForm button[type="submit"]');
  if (button && button.dataset.label) {
    button.disabled = false;
    button.textContent = button.dataset.label;
  }
});
