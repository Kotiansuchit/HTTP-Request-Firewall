# HTTP-Request-Firewall
# Spring Exploit Defender 🔐

A lightweight Python-based HTTP firewall designed to detect and block malicious HTTP POST requests, specifically targeting Spring4Shell-style exploits.

---

## 📌 Project Overview

**Spring Exploit Defender** acts as a simple yet effective layer of protection against known Spring4Shell attack patterns by inspecting incoming POST requests and blocking those that contain suspicious payloads.

This project includes:
- A custom firewall server built with Python's `http.server` module.
- Signature-based detection for malicious request patterns.
- A test client to simulate both malicious and clean HTTP requests.

---

## 🛠 Features

- 🚫 Blocks known Spring4Shell attack strings.
- ✅ Allows clean and safe HTTP requests.
- 🔍 Scans headers and body content.
- 🧪 Includes a client script to test the firewall.
- 🔐 Helps in learning and simulating basic web application security.

---

