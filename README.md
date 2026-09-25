# Decision Support System

https://youtu.be/DXDovX0FzWA
---

## Description

This project is my final project for **CS50P (Introduction to Programming with Python)**. I built a simple **Decision Support System** that helps users compare different options and choose the best one based on their own priorities.

The idea behind this project is very straightforward. Instead of making decisions based on guesswork, the user defines what criteria are important to them, assigns a weight to each criterion, and then scores each option based on those criteria. The program calculates a final score for every option and ranks them from best to worst.

The entire project is written in **Python** and works through the **command line (CLI)**. I intentionally avoided using external libraries or graphical interfaces so that the logic stays clear and the project remains fully compatible with the CS50 Codespace environment.

---

## How the Program Works

* First, the user enters the criteria they want to use for comparison.
* Each criterion is given a weight to show how important it is.
* Then, the user enters several alternatives to compare.
* Each alternative is scored for every criterion using a numeric value.
* The program calculates a weighted total score for each alternative.
* Finally, all alternatives are ranked, and the best option is displayed.

The scoring formula used in the program is:

```
Final Score = sum(score × weight)
```

---

## Project Structure

The project folder contains two main files:

* **project.py**
  This file contains the main logic of the program, including user input, score calculation, and ranking of alternatives.

* **test_project.py**
  This file includes unit tests written with **pytest**. These tests check that score calculations and rankings work correctly.

---

## Design Decisions

* **Command-Line Interface:**
  I chose a CLI to keep the project simple and focused on core programming concepts.

* **Pure Python:**
  No external libraries were used so the program remains easy to understand and maintain.

* **Testable Functions:**
  The main logic is split into separate functions, which makes testing and debugging easier.

* **Real-World Use Case:**
  This system can be used for many real-life decisions, such as choosing a city, a product, or comparing job offers.

---

## How to Run

To run the program:

```bash
python project.py
```

To run the tests:

```bash
pytest
```

---

