# 💰 Who Wants to Be a Millionaire? (CLI Game)

A lightweight, interactive command-line interface (CLI) trivia game built in Python, inspired by the iconic television show *"Who Wants to Be a Millionaire?"*. Players test their general knowledge across a series of increasingly challenging questions to achieve the ultimate high score.

## 🎮 Features
* **Extensive Question Bank:** Features 20 unique, multi-disciplinary questions ranging from geography and science to pop culture and history.
* **High-Stakes Scoring Mechanics:** Earn 100,000 points for every correct answer. 
* **Sudden-Death Logic:** A single incorrect answer ends the game immediately, preserving the tense, high-stakes spirit of the original game show.
* **Case-Insensitive Input Handling:** Automatically processes user input to accept both lowercase and uppercase selections seamlessly.

## 📂 Data Structure & Logic
The game utilizes a structured, modular **matrix (list of lists)** array pattern to bundle questions, multiple-choice options, and corresponding answer keys together securely:

```python
questions = [
    ["What is the capital of France?", "A] PARIS", "B] LONDON", "C] BERLIN", "D] MADRID", "A"],
    ...
]
