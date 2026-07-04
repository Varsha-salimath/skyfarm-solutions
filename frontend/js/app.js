/* SkyFarm Solutions – Frontend application */

const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

navToggle?.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", open);
});

navLinks?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
  });
});

function showError(elementId, message) {
  const el = document.getElementById(elementId);
  if (el) {
    el.textContent = message;
    el.hidden = false;
  }
}

function hideError(elementId) {
  const el = document.getElementById(elementId);
  if (el) el.hidden = true;
}

function setLoading(button, loading) {
  if (!button) return;
  button.disabled = loading;
  button.dataset.originalText ??= button.textContent;
  button.textContent = loading ? "Loading…" : button.dataset.originalText;
}

// Space Planner
document.getElementById("space-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  hideError("space-error");
  const btn = e.target.querySelector('button[type="submit"]');
  setLoading(btn, true);

  try {
    const data = await api.calculateSpace({
      length: parseFloat(document.getElementById("length").value),
      width: parseFloat(document.getElementById("width").value),
      layout: document.getElementById("layout-type").value,
    });

    document.getElementById("space-summary").textContent = data.summary;
    document.getElementById("space-suggestions").innerHTML =
      data.suggestions.map((s) => `<li>${s}</li>`).join("");
    document.getElementById("space-result").hidden = false;
    window.animateResult?.("space-result");
  } catch (err) {
    showError("space-error", err.message);
    document.getElementById("space-result").hidden = true;
  } finally {
    setLoading(btn, false);
  }
});

// Plant Recommendations
document.getElementById("plant-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  hideError("plant-error");
  const btn = e.target.querySelector('button[type="submit"]');
  setLoading(btn, true);

  try {
    const data = await api.recommendPlants({
      sunlight: document.getElementById("sunlight").value,
      season: document.getElementById("season").value,
      soil: document.getElementById("soil-pref").value,
    });

    const list = document.getElementById("plant-list");
    if (data.plants.length === 0) {
      list.innerHTML =
        '<p class="empty-message">No exact matches. Try adjusting sunlight or soil — many plants are adaptable with minor amendments.</p>';
    } else {
      list.innerHTML = data.plants
        .map(
          (p) => `
        <div class="plant-card">
          <span class="plant-emoji">${p.emoji}</span>
          <div class="plant-info">
            <h5>${p.name}</h5>
            <p>${p.care}</p>
          </div>
        </div>`
        )
        .join("");
    }
    document.getElementById("plant-result").hidden = false;
    window.animateResult?.("plant-result");
    window.animatePlantCards?.();
  } catch (err) {
    showError("plant-error", err.message);
    document.getElementById("plant-result").hidden = true;
  } finally {
    setLoading(btn, false);
  }
});

// Soil Checker
document.getElementById("soil-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  hideError("soil-error");
  const btn = e.target.querySelector('button[type="submit"]');
  setLoading(btn, true);

  try {
    const data = await api.checkSoil({
      plant: document.getElementById("plant-select").value,
      soil: document.getElementById("your-soil").value,
    });

    const verdictEl = document.getElementById("soil-verdict");
    verdictEl.textContent = data.verdict;
    verdictEl.className = `soil-verdict soil-verdict--${data.status}`;
    document.getElementById("soil-advice").textContent = data.advice;
    document.getElementById("soil-result").hidden = false;
    window.animateResult?.("soil-result");
  } catch (err) {
    showError("soil-error", err.message);
    document.getElementById("soil-result").hidden = true;
  } finally {
    setLoading(btn, false);
  }
});

// Gardening Tips
const tipsGrid = document.getElementById("tips-grid");
const filterBtns = document.querySelectorAll(".tip-filter-btn");

function renderTips(tips) {
  tipsGrid.innerHTML = tips
    .map(
      (t) => `
    <article class="tip-card">
      <span class="tip-card-tag">${t.category}</span>
      <h4>${t.title}</h4>
      <p>${t.body}</p>
    </article>`
    )
    .join("");
}

async function loadTips(category = "all") {
  hideError("tips-error");
  tipsGrid.innerHTML = '<p class="loading-message">Loading tips…</p>';

  try {
    const data = await api.getTips(category);
    renderTips(data.tips);
    window.animateTipCards?.();
  } catch (err) {
    tipsGrid.innerHTML = "";
    showError("tips-error", err.message);
  }
}

filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    filterBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    loadTips(btn.dataset.category);
  });
});

// Load plants for soil checker dropdown and hero stat
async function initPlants() {
  const select = document.getElementById("plant-select");
  const statPlants = document.getElementById("stat-plants");

  try {
    const plants = await api.getPlants();
    select.innerHTML = plants
      .map((p) => `<option value="${p.id}">${p.name}</option>`)
      .join("");
    if (statPlants) statPlants.textContent = `${plants.length}+`;
  } catch {
    select.innerHTML = `
      <option value="tomato">Tomato</option>
      <option value="basil">Basil</option>
      <option value="lettuce">Lettuce</option>
      <option value="carrot">Carrot</option>
    `;
  }
}

initPlants();
loadTips();
