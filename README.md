# 🗓 Date Intelligence Engine

A Python CLI tool that generates a structured cultural and personality
profile for any date — covering multiple calendar systems, zodiac, and
historical facts.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Features

- Multi-calendar output — Gregorian, Islamic (Hijri), Hindu (Shaka)
- Zodiac sign with element and personality traits
- "On This Day" — historical facts for the given date
- Clean structured output, built for future web/API integration

---

## Installation

```bash
git clone https://github.com/haroon-hasan110/date-intelligence-engine.git
cd date-intelligence-engine
pip install hijri-converter
python main.py
```

---

## Project Structure

date-intelligence-engine/
├── main.py            → controller, output formatter
├── validators.py      → input validation
├── calendar_utils.py  → Gregorian info
├── islamic.py         → Hijri conversion
├── hindu.py           → Shaka calendar
├── zodiac.py          → zodiac + personality
└── history.py         → "On This Day" facts

---

## Sample Output

![Output](https://github.com/user-attachments/assets/cf4f0507-3f92-4e1b-a940-a673d6ed6a9d)

---

## Roadmap

- [ ] Chinese Zodiac support
- [ ] Moon phase on birth date
- [ ] Flask web API
- [ ] PWA (Progressive Web App)

---

## Author

**Haroon Hasan** — FY AI & ML Student
[GitHub](https://github.com/haroon-hasan110)
