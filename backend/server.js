const express = require("express");
const mysql = require("mysql");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// 🔗 MySQL Connection
const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root", // 👈 CHANGE if different
    database: "traffic_db"
});

db.connect(err => {
    if (err) {
        console.log("❌ DB Error:", err);
        return;
    }
    console.log("✅ MySQL Connected!");
});

// 🚦 API with advanced features
app.get("/traffic", (req, res) => {
    db.query("SELECT * FROM traffic_data ORDER BY id DESC LIMIT 4", (err, result) => {
        if (err) {
            res.send(err);
        } else {
            const response = {
                traffic: result,
                emergency: Math.random() > 0.7 ? "🚑 Ambulance Incoming" : null,
                greenCorridor: Math.random() > 0.8 ? "ACTIVE" : "OFF"
            };
            res.json(response);
        }
    });
});

// 🚀 Start server
app.listen(5000, () => {
    console.log("🚀 Server running at http://localhost:5000");
});
