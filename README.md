# VGC Closed Team Sheet (CTS) Predictor

A strategic forecasting tool built for the *Pokémon Champions* ranked ladder. This engine helps competitive VGC players reduce cognitive load during Team Preview by analyzing information asymmetry in Closed Team Sheet (CTS) formats.

## 🚀 Features

- **Meta Inference Engine:** Automatically estimates probabilities for opponent items, abilities, and movesets based on weighted regional usage statistics.
- **Synergy & Counter Matrix:** Cross-references the enemy's 6 Pokémon against your own to evaluate type advantages, speed tiers, and core meta role threats (e.g., Tailwind, Trick Room, Intimidate).
- **"Bring 4" Simulator:** Evaluates the mathematically safest 4-Pokémon combination (Leads and Backs) to counter the opponent's most probable team selection.

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3.x
- **Data Source:** Static JSON database compiled from current meta usage statistics.
- **Interface:** Command Line Interface (CLI) / Planned transition to a Streamlit web app.

## 📦 Getting Started

### Prerequisites
- Python 3.10+ installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
