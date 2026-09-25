def main():
    print("=== Decision Support System ===")

    criteria = get_criteria()
    alternatives = get_alternatives(criteria)
    scores = calculate_scores(criteria, alternatives)
    ranked = rank_alternatives(scores)

    print("\n--- Final Ranking ---")
    for rank, (name, score) in enumerate(ranked, start=1):
        print(f"{rank}. {name} - Score: {score:.2f}")

    print(f"\n✅ Best Choice: {ranked[0][0]}")


def get_criteria():
    criteria = {}
    count = int(input("How many criteria do you want to define? "))

    for i in range(count):
        name = input(f"Enter name of criterion {i + 1}: ")
        weight = float(input(f"Enter weight for '{name}' (e.g. 0.3): "))
        criteria[name] = weight

    return criteria


def get_alternatives(criteria):
    alternatives = {}
    count = int(input("\nHow many alternatives do you want to compare? "))

    for i in range(count):
        name = input(f"\nEnter name of alternative {i + 1}: ")
        alternatives[name] = {}

        for criterion in criteria:
            score = float(
                input(f"Score for '{name}' on '{criterion}' (0–10): ")
            )
            alternatives[name][criterion] = score

    return alternatives


def calculate_scores(criteria, alternatives):
    final_scores = {}

    for alternative, scores in alternatives.items():
        total = 0
        for criterion, weight in criteria.items():
            total += scores[criterion] * weight
        final_scores[alternative] = total

    return final_scores


def rank_alternatives(scores):
    return sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )


if __name__ == "__main__":
    main()
