# SmartChoice

## About the Project

SmartChoice is my final project for **CS50P (Introduction to Programming with Python)**.

I built this project to make comparing different options a little easier. The idea came from a simple question: when there are several options to choose from, how can we make a decision based on what actually matters to us?

With SmartChoice, the user can define their own criteria, decide how important each criterion is, and then give each option a score. The program uses these values to calculate a final score and rank the options.

For example, it could be used to compare different cities, products, universities, job offers, or pretty much anything that can be evaluated using several criteria.

The project is written entirely in **Python** and runs in the **command line (CLI)**.

---

## How It Works

The program guides the user through a few steps:

1. Enter the criteria that matter for the decision.
2. Give each criterion a weight based on its importance.
3. Enter the options that you want to compare.
4. Give each option a score for every criterion.
5. The program calculates a weighted score for each option.
6. The options are ranked from the highest score to the lowest.
7. The best-scoring option is displayed at the end.

The main calculation is based on:

```text
Final Score = sum(score × weight)
