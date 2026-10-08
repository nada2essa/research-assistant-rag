def route_question(question):

    question = question.lower().strip()

    if (
        question.startswith("summarize")
        or question.startswith("summary")
        or question.startswith("summarise")
    ):
        return "SUMMARY"

    return "QUESTION"