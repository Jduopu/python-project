# 🎬 Movie Recommendation Engine

A Python-based project that fetches real-time movie data from The Movie Database (TMDb) API and recommends movies based on genre or mood.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Objective](#objective)
- [System Architecture](#system-architecture)
- [Features](#features)
- [API Reference](#api-reference)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## 🧠 Overview

This project allows users to input a mood or genre (like "comedy" or "thriller") and receive a curated list of movie recommendations. It integrates directly with the TMDb API to ensure real-time accuracy and updated film data.

---

## 🎯 Objective

- Build a simple CLI application that demonstrates how to fetch and parse movie data from an external API.
- Help users discover new films based on personalized genre input.
- Practice clean software architecture, modular design, and API consumption.

---

## 🏗️ System Architecture

- `main.py`: User interface and execution flow
- `api_handler.py`: Abstracts logic for talking to TMDb API
- `config.py`: Keeps sensitive info separate from logic

---

## ✅ Features

- Search movies by genre, mood, or keyword
- Fetch movie details (rating, overview, release date, runtime)
- Clean CLI interaction
- Modular code for easy scaling or GUI integration

---

## 🔌 API Reference

**Base URL**: `https://api.themoviedb.org/3`  
**Authentication**: Uses `API Key (v3 auth)`

Endpoints used:
- `/search/movie`: Returns a list of movies based on a search query
- `/movie/{movie_id}`: Returns detailed information about a specific movie

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jduopu/python-project.git
   cd python-project
2. **Set Up environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Set your API key**
   ```bash
   API_KEY = "your_tmdb_api_key"
   BASE_URL = "https://api.themoviedb.org/3"

---

## 🚀 Usage ##

- python main.py

---

## 📁 File Structure ##
```bash
├── main.py
├── config.py
├── requirements.txt
└── libraries/
    ├── api_handler.py
    ├── requests.py
    └── json.py
```
## 🐛 Known Issues ##
- Results may not always return 5 movies (depends on TMDb data).

- Some movies may lack overviews or ratings.

## 🚧 Future Improvements ##
- Add support for filtering by year or language

- Include poster images using image URLs

- Implement a GUI version

- Save past searches and favorites locally

- Add genre list to help guide user input

## 🙌 Credits ##
Created by Jon Duopu
Powered by TMDb API

## 📄 License ##
This project is licensed under the MIT License — see LICENSE for details.
