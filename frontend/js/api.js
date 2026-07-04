/* SkyFarm Solutions – API client */

const API_BASE = "";

async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.error || `Request failed (${response.status})`);
  }

  return data;
}

const api = {
  getPlants: () => apiRequest("/api/plants"),
  recommendPlants: (body) =>
    apiRequest("/api/plants/recommend", { method: "POST", body: JSON.stringify(body) }),
  calculateSpace: (body) =>
    apiRequest("/api/space/calculate", { method: "POST", body: JSON.stringify(body) }),
  checkSoil: (body) =>
    apiRequest("/api/soil/check", { method: "POST", body: JSON.stringify(body) }),
  getTips: (category = "all") =>
    apiRequest(`/api/tips?category=${encodeURIComponent(category)}`),
};
