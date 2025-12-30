const API = "https://patient-management-system-fastapi.onrender.com";

async function fetchJSON(url, options = {}) {
  const res = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options
  });
  if (!res.ok) {
    const err = await res.json();
    throw err.detail || "Something went wrong";
  }
  return res.json();
}
