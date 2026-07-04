/* SkyFarm Solutions – Animation controller */

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

function motionAllowed() {
  return !prefersReducedMotion.matches;
}

/* ── Floating particles ── */
function createParticles(container, count, type) {
  if (!motionAllowed() || !container) return;

  const fragment = document.createDocumentFragment();
  for (let i = 0; i < count; i++) {
    const p = document.createElement("span");
    p.className = `particle particle--${type}`;
    p.style.left = `${Math.random() * 100}%`;
    p.style.top = `${Math.random() * 100}%`;
    p.style.setProperty("--drift-x", `${(Math.random() - 0.5) * 120}px`);
    p.style.setProperty("--drift-y", `${-80 - Math.random() * 40}vh`);
    p.style.setProperty("--drift-rot", `${Math.random() * 360}deg`);
    p.style.animationDuration = `${18 + Math.random() * 22}s`;
    p.style.animationDelay = `${Math.random() * 20}s`;
    fragment.appendChild(p);
  }
  container.appendChild(fragment);
}

function initAtmosphere() {
  const layer = document.getElementById("particles-layer");
  if (!layer) return;
  createParticles(layer, 12, "leaf");
  createParticles(layer, 18, "pollen");
}

function initSoilParticles() {
  const layer = document.getElementById("soil-particles");
  if (!layer) return;
  createParticles(layer, 8, "soil");
}

/* ── Scroll reveal ── */
function initScrollReveal() {
  const targets = document.querySelectorAll(".animate-on-scroll, .stagger-children");
  if (!targets.length) return;

  if (!motionAllowed()) {
    targets.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );

  targets.forEach((el) => observer.observe(el));
}

/* ── Parallax on scroll ── */
function initParallax() {
  if (!motionAllowed()) return;

  const layers = document.querySelectorAll("[data-parallax]");
  if (!layers.length) return;

  let ticking = false;

  function update() {
    const scrollY = window.scrollY;
    layers.forEach((layer) => {
      const speed = parseFloat(layer.dataset.parallax) || 0.3;
      const rect = layer.closest("section")?.getBoundingClientRect();
      if (rect && rect.bottom > 0 && rect.top < window.innerHeight) {
        const offset = (scrollY - (layer.closest("section")?.offsetTop || 0)) * speed;
        layer.style.transform = `translate3d(0, ${offset}px, 0)`;
      }
    });
    ticking = false;
  }

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        requestAnimationFrame(update);
        ticking = true;
      }
    },
    { passive: true }
  );
  update();
}

/* ── Button ripple ── */
function initButtonRipples() {
  document.querySelectorAll(".btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!motionAllowed()) return;
      const rect = btn.getBoundingClientRect();
      btn.style.setProperty("--ripple-x", `${((e.clientX - rect.left) / rect.width) * 100}%`);
      btn.style.setProperty("--ripple-y", `${((e.clientY - rect.top) / rect.height) * 100}%`);
      btn.classList.remove("ripple");
      void btn.offsetWidth;
      btn.classList.add("ripple");
      setTimeout(() => btn.classList.remove("ripple"), 600);
    });
  });
}

/* ── Form submit pulse ── */
function initFormAnimations() {
  document.querySelectorAll("form.tool-card").forEach((form) => {
    form.addEventListener("submit", () => {
      if (!motionAllowed()) return;
      form.querySelectorAll(".form-row").forEach((row, i) => {
        row.classList.remove("form-submitted");
        void row.offsetWidth;
        row.style.animationDelay = `${i * 0.05}s`;
        row.classList.add("form-submitted");
        setTimeout(() => row.classList.remove("form-submitted"), 600);
      });
    });
  });
}

/* ── Re-trigger result animations ── */
window.animateResult = function (elementId) {
  const el = document.getElementById(elementId);
  if (!el || el.hidden) return;
  el.hidden = false;
  if (!motionAllowed()) return;
  el.style.animation = "none";
  void el.offsetWidth;
  el.style.animation = "";
};

window.animatePlantCards = function () {
  if (!motionAllowed()) return;
  document.querySelectorAll(".plant-card").forEach((card, i) => {
    card.style.animation = "none";
    card.style.animationDelay = `${0.05 + i * 0.07}s`;
    void card.offsetWidth;
    card.style.animation = "";
  });
};

window.animateTipCards = function () {
  if (!motionAllowed()) return;
  document.querySelectorAll(".tip-card").forEach((card, i) => {
    card.style.animation = "none";
    card.style.animationDelay = `${0.05 + i * 0.05}s`;
    void card.offsetWidth;
    card.style.animation = "";
  });
};

/* ── Init ── */
function init() {
  initAtmosphere();
  initSoilParticles();
  initScrollReveal();
  initParallax();
  initButtonRipples();
  initFormAnimations();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}

prefersReducedMotion.addEventListener("change", () => {
  if (!motionAllowed()) {
    document.querySelectorAll(".animate-on-scroll, .stagger-children").forEach((el) => {
      el.classList.add("is-visible");
    });
  }
});
