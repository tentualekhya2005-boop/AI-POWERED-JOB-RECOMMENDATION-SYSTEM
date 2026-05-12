import json
import re

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

def get_difficulty_score(q_obj):
    # Try to extract numbers from the question text. Larger numbers = harder to compute.
    # If no numbers, use string length. Longer reading = harder to comprehend.
    numbers = re.findall(r'\d+', q_obj['q'])
    if numbers:
        score = sum(float(n) for n in numbers)
        # add a small factor for string length just to break ties
        score += len(q_obj['q']) * 0.1
    else:
        score = len(q_obj['q'])
    return score

for topic, qs in quizzes.items():
    # Sort the 100 questions by their calculated difficulty score
    qs.sort(key=get_difficulty_score)
    quizzes[topic] = qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
