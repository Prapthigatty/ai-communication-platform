async function analyzeText() {
  const text = document.getElementById("textInput").value.trim();

  if (!text) {
    alert("Please enter some text to analyze.");
    return;
  }

  const response = await fetch("https://ai-communication-backend.onrender.com/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await response.json();

  document.getElementById("result").classList.remove("hidden");

  document.getElementById("tone").innerText = data.tone;
  document.getElementById("confidence").innerText = data.confidence_score;
  document.getElementById("professionalism").innerText = data.professionalism_score;

  const insightsList = document.getElementById("insights");
  insightsList.innerHTML = "";
  data.insights.forEach(item => {
    const li = document.createElement("li");
    li.innerText = item;
    insightsList.appendChild(li);
  });

  document.getElementById("rewrite").innerText = data.rewrite_suggestion;
}
function toggleTheme() {
  document.body.classList.toggle("dark");

  const isDark = document.body.classList.contains("dark");
  localStorage.setItem("theme", isDark ? "dark" : "light");

  document.getElementById("themeToggle").innerText =
    isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
}

// Load saved theme
window.onload = () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark");
    document.getElementById("themeToggle").innerText = "☀️ Light Mode";
  }
};
