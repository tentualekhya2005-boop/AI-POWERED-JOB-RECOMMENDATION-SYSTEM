import json
import random
import math

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

remaining = [
    "Permutation", "DataInterpretation", "DirectionSense", "Syllogism",
    "Seating", "Puzzles", "VennDiagrams", "StatementConclusion", "CauseEffect",
    "ReadingComprehension", "SentenceCorrection", "ErrorDetection",
    "ParaJumbles", "FillBlanks", "MirrorImages", "PaperFolding", "FigureSeries",
    "EmbeddedFigures", "CubeDice"
]

def generate_plausible_options(topic, ans, x, y):
    if topic == "Permutation":
        a = int(ans)
        return [str(a), str(a+10), str(max(2, a-12)), str(a*2)]
    elif topic == "DataInterpretation":
        a = float(ans)
        return [str(a), str(a+2.5), str(a-1.5), str(a+5.0)]
    elif topic == "DirectionSense":
        a = float(ans)
        return [str(a), str(a+1), str(a+5), str(max(1.0, a-2))]
    elif topic == "Syllogism":
        return [ans, "True", "Cannot be determined", "Both True and False"]
    elif topic == "Seating":
        return [ans, "A", "C", "D"]
    elif topic == "Puzzles":
        return [str(ans), str(x), str(y), str(x+y)]
    elif topic == "VennDiagrams":
        a = int(ans)
        return [str(a), str(a+10), str(a-5), str(a+20)]
    elif topic == "StatementConclusion":
        return [ans, "Follows", "Does not follow", "Neither follows nor contradicts"]
    elif topic == "CauseEffect":
        return [ans, "Event B is the cause", "Both are independent causes", "Both are independent effects"]
    elif topic == "ReadingComprehension":
        return [ans, f"It describes the history of {x}", f"It argues against {x}", f"It highlights the failures of {x}"]
    elif topic == "SentenceCorrection":
        return [ans, "No error", f"{x} should be gone", f"{x} should be going"]
    elif topic == "ErrorDetection":
        return [ans, "No error", "are -> is", "incorrect -> incorrects"]
    elif topic == "ParaJumbles":
        return [ans, "1, 2, 3, 4", "4, 3, 2, 1", "3, 1, 4, 2"]
    elif topic == "FillBlanks":
        return [ans, "on", "in", "with"]
    elif topic == "MirrorImages":
        w = str(x)
        return [ans, w, w[1:]+w[0], w[:-1]]
    elif topic == "PaperFolding":
        a = int(ans)
        return [str(a), str(a+2), str(max(1, a-2)), str(a*2)]
    elif topic == "FigureSeries":
        return [ans, "Heptagon", "Octagon", "Nonagon"]
    elif topic == "EmbeddedFigures":
        return [ans, "Located in top quadrant", "Not present", "Located in center"]
    elif topic == "CubeDice":
        return [str(ans), str((int(ans)%6)+1), str((int(ans)+1)%6+1), str((int(ans)+2)%6+1)]
    return [str(ans), "Option A", "Option B", "Option C"]

general_q_templates = {
    "Permutation": ("In how many ways can {} distinct items be arranged in a row?", lambda x, y: math.factorial(x)),
    "DataInterpretation": ("Based on a pie chart showing {}% growth in Q1 and {}% in Q2, what is the average growth?", lambda x,y: (x+y)/2),
    "DirectionSense": ("A man walks {} km North, then {} km East. What is the shortest distance from the start?", lambda x,y: round(math.sqrt(x*x + y*y), 2)),
    "Syllogism": ("Statements: All Cats are Dogs. Some Dogs are {}s. Conclusion: Some Cats are {}s. Is this true?", lambda x,y: "False"),
    "Seating": ("If {} sits next to B, and B sits next to {}, who is exactly in the middle?", lambda x,y: "B"),
    "Puzzles": ("If 3 cats kill 3 rats in 3 minutes, how many minutes does it take {} cats to kill {} rats?", lambda x,y: 3),
    "VennDiagrams": ("If {} people play cricket, 30 play football, and 10 play both, how many play at least one?", lambda x,y: x+30-10),
    "StatementConclusion": ("Statement: The sky is cloudy. Conclusion: It will rain. Does the conclusion follow?", lambda x,y: "May or may not follow"),
    "CauseEffect": ("Event A: Heavy {} rainfall. Event B: Floods. Which is the cause?", lambda x,y: "Event A is the cause"),
    "ReadingComprehension": ("Based on the short passage about {}, what is the main theme?", lambda x,y: f"The central idea revolves around {x}"),
    "SentenceCorrection": ("Identify the grammatical error: 'He {} to the market yesterday.'", lambda x,y: f"{x} should be went"),
    "ErrorDetection": ("Find the error in the sentence: 'The datas regarding {} are incorrect.'", lambda x,y: "datas -> data"),
    "ParaJumbles": ("Arrange: 1. However 2. {} 3. was late 4. to school.", lambda x,y: "2, 3, 4, 1"),
    "FillBlanks": ("The wild dog barked ___ the stranger near the {}.", lambda x,y: "at"),
    "MirrorImages": ("What is the exact mirror image of the word '{}'?", lambda x,y: str(x)[::-1]),
    "PaperFolding": ("If a square paper is folded twice and {} hole(s) punched, how many holes appear when unfolded?", lambda x,y: x * 4),
    "FigureSeries": ("Circle, Triangle, Square, Pentagon, ?", lambda x,y: "Hexagon"),
    "EmbeddedFigures": ("Find the hidden {} shape in the complex pattern.", lambda x,y: "Located in the bottom quadrant"),
    "CubeDice": ("If 1 is opposite 6, and 2 is opposite 5, what is opposite {}?", lambda x,y: 7-x)
}

for t in remaining:
    qs = []
    template, logic = general_q_templates[t]
    for _ in range(100):
        if t in ["Permutation"]:
            x = random.randint(3, 6)
            y = 0
            ans = str(logic(x, y))
            q = template.format(x)
        elif t in ["DataInterpretation", "DirectionSense", "VennDiagrams"]:
            x = random.randint(10, 50)
            y = random.randint(10, 50)
            ans = str(logic(x, y))
            q = template.format(x, y)
        elif t in ["Puzzles", "PaperFolding"]:
            x = random.randint(2, 10)
            y = x
            ans = str(logic(x, y))
            q = template.format(x, y)
        elif t in ["CubeDice"]:
            x = random.choice([3, 4])
            ans = str(logic(x, 0))
            q = template.format(x)
        elif t in ["MirrorImages"]:
            words = ["WATER", "IMAGE", "LOGIC", "CLOCK", "PAPER"]
            x = random.choice(words)
            ans = str(logic(x, 0))
            q = template.format(x)
        elif t in ["Syllogism", "Seating", "ReadingComprehension", "SentenceCorrection", "ErrorDetection", "ParaJumbles", "FillBlanks", "EmbeddedFigures", "CauseEffect"]:
            words = ["Rat", "Bat", "Cat", "Mat", "Hat"]
            x = random.choice(words)
            ans = str(logic(x, 0))
            q = template.format(x, x)
        else:
            x, y = 0, 0
            ans = str(logic(0,0))
            q = template
            
        opts = list(set(generate_plausible_options(t, ans, x, y)))
        while len(opts) < 4:
            opts.append(opts[0] + " variant")
        opts = opts[:4]
        random.shuffle(opts)
        qs.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": "Solved based on standard logical reasoning rules."})
    quizzes[t] = qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
