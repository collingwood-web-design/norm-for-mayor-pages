/**
 * ==========================================================================
 * main.js — Minimal JavaScript for static GitHub Pages site
 * ==========================================================================
 *
 * PURPOSE:
 *   Keep JS tiny. This site is HTML/CSS-first. Only add scripts when
 *   plain HTML cannot solve the problem.
 *
 * CURRENT FEATURES:
 *   1. Mobile navigation toggle (auto-closes when a nav link is tapped)
 *   2. Dynamic copyright year in footer
 *   3. Gallery carousel (Dogs R Us–style CSS crossfade)
 *   4. (Placeholder) Contact / subscribe forms — wire before launch
 *
 * NO BUILD STEP REQUIRED — this file loads directly in the browser.
 * ==========================================================================
 */

(function () {
  "use strict";

  /* -----------------------------------------------------------------------
   * Mobile navigation
   * Toggles .site-nav--open on #site-nav when hamburger is clicked
   * ----------------------------------------------------------------------- */
  var navToggle = document.getElementById("site-nav-toggle");
  var siteNav = document.getElementById("site-nav");

  if (navToggle && siteNav) {
    function closeNav() {
      siteNav.classList.remove("site-nav--open");
      navToggle.setAttribute("aria-expanded", "false");
    }

    navToggle.addEventListener("click", function () {
      var isOpen = siteNav.classList.toggle("site-nav--open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    var navLinks = siteNav.querySelectorAll("#site-nav-menu a");
    navLinks.forEach(function (link) {
      link.addEventListener("click", closeNav);
    });
  }

  /* -----------------------------------------------------------------------
   * Footer year — avoids hard-coding year in every HTML file
   * ----------------------------------------------------------------------- */
  var yearEl = document.getElementById("footer-year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* -----------------------------------------------------------------------
   * Contact form — posts to FormSubmit (norm@norm4mayor.ca)
   * Set _next from the current origin so preview and live both work.
   * ----------------------------------------------------------------------- */
  var contactForms = document.querySelectorAll("#contact-form, #donations-contact-form");
  contactForms.forEach(function (contactForm) {
    var nextInput = contactForm.querySelector('input[name="_next"]');
    if (nextInput) {
      var thankYouPath = nextInput.getAttribute("data-thank-you-path") || "thank-you.html";
      nextInput.value =
        window.location.origin +
        window.location.pathname.replace(/[^/]*$/, "") +
        thankYouPath;
    }
    contactForm.addEventListener("submit", function (event) {
      if (!contactForm.getAttribute("action")) {
        event.preventDefault();
        alert(
          "Contact form is not yet connected. Set the form action URL in HTML before launch."
        );
      }
    });
  });

  /* Prefill contact subject from lawn-sign CTA */
  document.querySelectorAll("[data-prefill-subject]").forEach(function (link) {
    link.addEventListener("click", function () {
      var subject = link.getAttribute("data-prefill-subject");
      var subjectInput = document.getElementById("footer-subject");
      if (subjectInput && subject) {
        subjectInput.value = subject;
      }
    });
  });
  /* -----------------------------------------------------------------------
   * Gallery carousel — CSS keyframe crossfade (Dogs R Us style)
   * Slides animate in CSS; JS only syncs dots / pause / jump.
   * ----------------------------------------------------------------------- */
  function initCarousel(carousel) {
    var slides = Array.prototype.slice.call(carousel.querySelectorAll(".home-carousel__slide"));
    var dots = Array.prototype.slice.call(carousel.querySelectorAll(".home-carousel__dot"));
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var slotMs = 4000;
    var cycleMs = slotMs * slides.length;
    var startedAt = performance.now();
    var resumeTimer = null;
    var pauseDepth = 0;

    function syncDots(index) {
      dots.forEach(function (dot, i) {
        var active = i === index;
        dot.classList.toggle("is-active", active);
        dot.setAttribute("aria-selected", active ? "true" : "false");
      });
    }

    function currentIndex() {
      if (!slides.length) return 0;
      var elapsed = (performance.now() - startedAt) % cycleMs;
      if (elapsed < 0) elapsed += cycleMs;
      return Math.floor(elapsed / slotMs) % slides.length;
    }

    function tick() {
      syncDots(currentIndex());
    }

    function pause() {
      pauseDepth += 1;
      if (pauseDepth === 1) {
        carousel.classList.add("is-paused");
      }
    }

    function resume() {
      pauseDepth = Math.max(0, pauseDepth - 1);
      if (pauseDepth === 0) {
        carousel.classList.remove("is-paused");
      }
    }

    function jumpTo(index) {
      if (!slides.length || reduceMotion) {
        syncDots(index);
        return;
      }
      var n = ((index % slides.length) + slides.length) % slides.length;
      startedAt = performance.now() - n * slotMs;
      slides.forEach(function (slide, i) {
        var delaySec = ((i - n + slides.length) % slides.length) * (slotMs / 1000);
        slide.style.animation = "none";
        void slide.offsetWidth;
        slide.style.animation = "";
        slide.style.animationDelay = delaySec + "s";
        slide.style.opacity = i === n ? "1" : "";
      });
      syncDots(n);
    }

    if (!reduceMotion && slides.length > 1) {
      window.setInterval(tick, 250);
      carousel.addEventListener("mouseenter", pause);
      carousel.addEventListener("mouseleave", resume);
      carousel.addEventListener("focusin", pause);
      carousel.addEventListener("focusout", resume);
    }

    dots.forEach(function (dot) {
      dot.addEventListener("click", function () {
        var index = parseInt(dot.getAttribute("data-slide"), 10);
        if (isNaN(index)) return;
        jumpTo(index);
        if (resumeTimer) window.clearTimeout(resumeTimer);
        carousel.classList.add("is-paused");
        pauseDepth = 1;
        resumeTimer = window.setTimeout(function () {
          pauseDepth = 0;
          carousel.classList.remove("is-paused");
        }, slotMs);
      });
    });

    syncDots(0);
  }

  document.querySelectorAll(".home-carousel").forEach(initCarousel);
})();
