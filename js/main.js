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
 *   3. (Placeholder) Contact form — wire to Formspree/Netlify Forms later
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

  /* Subscribe form placeholder */
  var subscribeForm = document.getElementById("subscribe-form");
  if (subscribeForm) {
    subscribeForm.addEventListener("submit", function (event) {
      if (!subscribeForm.getAttribute("action") || subscribeForm.getAttribute("action") === "#") {
        event.preventDefault();
        alert("Newsletter signup is not yet connected. Add a mailing-list action URL before launch.");
      }
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
   * Contact form placeholder
   * TODO: Replace with real form handler before launch.
   * Options for static hosting:
   *   - Formspree (https://formspree.io)
   *   - Netlify Forms (if deploying via Netlify instead)
   *   - GitHub Pages + external serverless function
   *
   * Legacy site used WordPress Formidable with inquiry types:
   *   GENERAL INQUIRY | REQUEST A LAWN SIGN | DONATIONS | VOLUNTEER
   * ----------------------------------------------------------------------- */
  var contactForms = document.querySelectorAll("#contact-form, #donations-contact-form");
  contactForms.forEach(function (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      if (!contactForm.getAttribute("action")) {
        event.preventDefault();
        alert(
          "Contact form is not yet connected. Set the form action URL in HTML before launch."
        );
      }
    });
  });
})();
