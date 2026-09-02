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
 *   4. Policy materials lightbox (image overlays with next/prev)
 *   5. (Placeholder) Contact / subscribe forms — wire before launch
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

  /* -----------------------------------------------------------------------
   * Policy materials lightbox — image gallery overlays (PDFs stay as links)
   * ----------------------------------------------------------------------- */
  function initMaterialsLightbox(root) {
    var thumbs = Array.prototype.slice.call(
      root.querySelectorAll("a.policy-materials__thumb")
    ).filter(function (link) {
      return /\.(jpe?g|png|gif|webp)(\?|#|$)/i.test(link.getAttribute("href") || "");
    });

    if (!thumbs.length) return;

    var items = thumbs.map(function (link) {
      var img = link.querySelector("img");
      var figure = link.closest("figure");
      var caption = figure ? figure.querySelector("figcaption") : null;
      return {
        src: link.getAttribute("href"),
        alt: img ? img.getAttribute("alt") || "" : "",
        caption: caption ? caption.textContent.trim() : ""
      };
    });

    var overlay = document.createElement("div");
    overlay.className = "policy-lightbox";
    overlay.setAttribute("hidden", "");
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Concept drawing viewer");
    overlay.innerHTML =
      '<button type="button" class="policy-lightbox__close" aria-label="Close">&times;</button>' +
      '<button type="button" class="policy-lightbox__nav policy-lightbox__nav--prev" aria-label="Previous drawing">&lsaquo;</button>' +
      '<button type="button" class="policy-lightbox__nav policy-lightbox__nav--next" aria-label="Next drawing">&rsaquo;</button>' +
      '<div class="policy-lightbox__stage">' +
      '<img class="policy-lightbox__image" alt="" />' +
      '<p class="policy-lightbox__caption"></p>' +
      '<p class="policy-lightbox__counter" aria-live="polite"></p>' +
      "</div>";
    document.body.appendChild(overlay);

    var imageEl = overlay.querySelector(".policy-lightbox__image");
    var captionEl = overlay.querySelector(".policy-lightbox__caption");
    var counterEl = overlay.querySelector(".policy-lightbox__counter");
    var closeBtn = overlay.querySelector(".policy-lightbox__close");
    var prevBtn = overlay.querySelector(".policy-lightbox__nav--prev");
    var nextBtn = overlay.querySelector(".policy-lightbox__nav--next");
    var activeIndex = 0;
    var lastFocus = null;

    function show(index) {
      activeIndex = ((index % items.length) + items.length) % items.length;
      var item = items[activeIndex];
      imageEl.src = item.src;
      imageEl.alt = item.alt;
      captionEl.textContent = item.caption;
      counterEl.textContent = activeIndex + 1 + " / " + items.length;
      counterEl.hidden = items.length < 2;
      prevBtn.hidden = items.length < 2;
      nextBtn.hidden = items.length < 2;
    }

    function open(index) {
      lastFocus = document.activeElement;
      show(index);
      overlay.removeAttribute("hidden");
      document.body.classList.add("policy-lightbox-open");
      closeBtn.focus();
    }

    function close() {
      overlay.setAttribute("hidden", "");
      document.body.classList.remove("policy-lightbox-open");
      imageEl.removeAttribute("src");
      if (lastFocus && typeof lastFocus.focus === "function") {
        lastFocus.focus();
      }
    }

    thumbs.forEach(function (link, index) {
      link.addEventListener("click", function (event) {
        event.preventDefault();
        open(index);
      });
    });

    closeBtn.addEventListener("click", close);
    prevBtn.addEventListener("click", function () {
      show(activeIndex - 1);
    });
    nextBtn.addEventListener("click", function () {
      show(activeIndex + 1);
    });

    overlay.addEventListener("click", function (event) {
      if (event.target === overlay) close();
    });

    document.addEventListener("keydown", function (event) {
      if (overlay.hasAttribute("hidden")) return;
      if (event.key === "Escape") {
        event.preventDefault();
        close();
      } else if (event.key === "ArrowLeft") {
        event.preventDefault();
        show(activeIndex - 1);
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        show(activeIndex + 1);
      }
    });
  }

  document.querySelectorAll(".policy-materials").forEach(initMaterialsLightbox);
})();
