const express = require("express");
const bodyParser = require("body-parser");
const { spawn } = require("child_process");
const cors = require("cors");

// ✅ Define app BEFORE using it
const app = express();
const PORT = process.env.PORT || 5000;

// ✅ Setup CORS with specific origin
app.use(
  cors({
    origin: "https://gen-seo-frontend.vercel.app", // replace with your frontend domain
  })
);

app.use(bodyParser.json());

// ✅ Helper to call Python scripts
function runPython(script, input, res) {
  const python = spawn("python", [script, input]);

  let data = "";
  python.stdout.on("data", (chunk) => {
    data += chunk.toString();
  });

  python.stderr.on("data", (err) => {
    console.error("Python error:", err.toString());
  });

  python.on("close", () => {
    try {
      const parsed = JSON.parse(data);
      res.json(parsed);
    } catch (error) {
      res.status(500).json({ error: "Failed to parse Python response" });
    }
  });
}

// ✅ API Routes
app.post("/api/keyword", (req, res) => {
  const { keyword } = req.body;
  runPython("keyword_generator.py", keyword, res);
});

app.post("/api/title", (req, res) => {
  const { keyword } = req.body;
  runPython("title_generator.py", keyword, res);
});

app.post("/api/topic", (req, res) => {
  const { title } = req.body;
  runPython("topic_generator.py", title, res);
});

app.post("/api/content", (req, res) => {
  const { topic } = req.body;

  const python = spawn("python", ["content_generator.py", topic]);

  let data = "";
  python.stdout.on("data", (chunk) => {
    data += chunk.toString();
  });

  python.stderr.on("data", (err) => {
    console.error("Python error:", err.toString());
  });

  python.on("close", (code) => {
    try {
      const parsed = JSON.parse(data);
      const content = parsed.content;
      const keyword = topic.toLowerCase();
      const keywordCount = (
        content.toLowerCase().match(new RegExp(keyword, "g")) || []
      ).length;
      const score = keywordCount > 0 ? Math.min(100, keywordCount * 20) : 0;

      res.json({ content, seoScore: score });
    } catch (err) {
      res.status(500).json({ error: "Failed to parse Python response" });
    }
  });
});

// ✅ Start the server
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
