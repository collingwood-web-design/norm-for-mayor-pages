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
 *   1. Mobile navigation toggle
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
    navToggle.addEventListener("click", function () {
      var isOpen = siteNav.classList.toggle("site-nav--open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
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
   * The 2022 WordPress site used Formidable Forms with inquiry types:
   *   GENERAL INQUIRY | REQUEST A LAWN SIGN | DONATIONS | VOLUNTEER
   * ----------------------------------------------------------------------- */
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      // Remove this block once a real action URL is configured
      if (!contactForm.getAttribute("action")) {
        event.preventDefault();
        alert(
          "Contact form is not yet connected. Set the form action URL in HTML before launch."
        );
      }
    });
  }
})();
