import csv

# Expected probability for p1 to win vs. p2
def expected(p1, p2):
    probability = 1 / (1 + 10 ** ( (p2 - p1) / 400) )
    return probability

# New rating of p after facing a team of o1 - o5
def newRating(p, acs, o1, o2, o3, o4, o5, outcome):
    # Get all expected matchups (0.00 to 1.00)
    match1 = expected(p, o1)
    match2 = expected(p, o2)
    match3 = expected(p, o3)
    match4 = expected(p, o4)
    match5 = expected(p, o5)

    # Calculate rating change depending on W/L
    K = acs / 10
    if (outcome == "win"):
        elodiff = K * (5 - match1 - match2 - match3 - match4 - match5)
    if (outcome == "loss"):
        elodiff = (K - 40) * (match1 + match2 + match3 + match4 + match5)

    return p + round(elodiff)
