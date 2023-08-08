import random

extendedText = [
    "Subscribe = Happiness",
    "Like = Happy",
    "Like + Sub = Excitement",
    "Sub + Like = Enjoyment",
    "Like + Comment = Love",
    "Sub + Share = Joy",
    "Share = Wonderful",
    "Subscribe = Amazing",
    "Like = Awesome",
    "Comment = Fantastic",
    "Sub + Comment = Thanks",
    "Comment = Charming",
    "Sub + Comment = Appreciation",
    "Sub + Share = Happiness",
    "Share = Excitement",
    "Sub + Like + Comment = Admiration",
    "Sub + Like + Share = Elation",
    "Sub + Share + Comment = Enthusiasm",
    "Like + Share = Grateful",
    "Like + Share + Comment = Bliss",
    "Share + Comment = Pleasure",
    "Subscribe + Like = Appreciation",
    "Subscribe + Comment = Delight",
    "Subscribe + Share = Elated",
    "Like + Subscribe + Comment = Enjoyment",
    "Like + Subscribe + Share = Happiness",
    "Share + Like = Motivated",
    "Share + Like + Comment = Satisfaction"
]


def Text_maker():
    return f"{random.choice(extendedText)}"
