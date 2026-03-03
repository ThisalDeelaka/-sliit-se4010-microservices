const express = require("express");

const app = express();
const PORT = process.env.PORT || 8081;

app.use(express.json());

const items = [];
let idCounter = 1;

app.get("/items", (req, res) => {
  res.status(200).json(items);
});

app.post("/items", (req, res) => {
  const { name } = req.body || {};

  if (!name || typeof name !== "string") {
    return res.status(400).json({ message: "Invalid payload. 'name' is required." });
  }

  const item = {
    id: idCounter++,
    name
  };

  items.push(item);
  return res.status(201).json(item);
});

app.get("/items/:id", (req, res) => {
  const id = parseInt(req.params.id, 10);
  const item = items.find((i) => i.id === id);

  if (!item) {
    return res.status(404).json({ message: "Item not found" });
  }

  return res.status(200).json(item);
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`item-service listening on port ${PORT}`);
});
