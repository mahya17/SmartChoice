from project import calculate_scores, rank_alternatives


def test_calculate_scores():
    criteria = {
        "Cost": 0.5,
        "Quality": 0.5
    }

    alternatives = {
        "Option A": {
            "Cost": 8,
            "Quality": 6
        },
        "Option B": {
            "Cost": 6,
            "Quality": 9
        }
    }

    scores = calculate_scores(criteria, alternatives)

    assert scores["Option A"] == 7.0
    assert scores["Option B"] == 7.5


def test_rank_alternatives():
    scores = {
        "Option A": 7.0,
        "Option B": 7.5,
        "Option C": 6.2
    }

    ranked = rank_alternatives(scores)

    assert ranked[0][0] == "Option B"
    assert ranked[1][0] == "Option A"
    assert ranked[2][0] == "Option C"


def test_rank_alternatives_values():
    scores = {
        "X": 5.0,
        "Y": 10.0
    }

    ranked = rank_alternatives(scores)

    assert ranked[0][1] >= ranked[1][1]
