import json
import random
import string
import math

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

# Ratio
qs = []
for _ in range(100):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    while a == b: b = random.randint(2, 9)
    mult = random.randint(5, 50)
    total = (a + b) * mult
    ans = a * mult
    opts = list(set([ans, ans+10, ans-10, b*mult]))
    if ans not in opts[:4]: opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    q = f"A sum of ${total} is divided in the ratio {a}:{b}. What is the first part?"
    exp = f"First part = {a}/({a}+{b}) * {total} = {ans}."
    qs.append({"q": q, "options": [str(o) for o in opts], "ans": opts.index(ans), "exp": exp})
quizzes['Ratio'] = qs

# Probability
qs = []
for _ in range(100):
    red = random.randint(3, 10)
    blue = random.randint(3, 10)
    total = red + blue
    ans = f"{red}/{total}"
    opts = list(set([ans, f"{blue}/{total}", f"{red-1}/{total}", f"{red+1}/{total}"]))
    if ans not in opts[:4]: opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    q = f"A bag contains {red} red balls and {blue} blue balls. If one ball is drawn at random, what is the probability it is red?"
    exp = f"P(Red) = Red / Total = {red} / {total}."
    qs.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": exp})
quizzes['Probability'] = qs

# Series (Number Series)
qs = []
for _ in range(100):
    start = random.randint(2, 10)
    diff = random.randint(2, 8)
    seq = [start + i*diff for i in range(5)]
    ans = seq[-1]
    seq_str = ", ".join(map(str, seq[:-1])) + ", ?"
    opts = list(set([ans, ans+diff, ans-diff, ans+1]))
    if ans not in opts[:4]: opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    q = f"Find the missing number in the series: {seq_str}"
    exp = f"The series increases by a constant difference of {diff}. Next term = {seq[-2]} + {diff} = {ans}."
    qs.append({"q": q, "options": [str(o) for o in opts], "ans": opts.index(ans), "exp": exp})
quizzes['Series'] = qs

# Coding-Decoding
qs = []
for _ in range(100):
    word = "".join(random.choices(string.ascii_uppercase, k=4))
    shift = random.randint(1, 5)
    coded = "".join(chr(((ord(c)-65+shift)%26)+65) for c in word)
    opts = [coded]
    for _ in range(3):
        fake_shift = shift + random.randint(1,3)
        opts.append("".join(chr(((ord(c)-65+fake_shift)%26)+65) for c in word))
    random.shuffle(opts)
    coded_apple = "".join(chr(((ord(c)-65+shift)%26)+65) for c in "APPLE")
    q = f"If in a certain code, 'APPLE' is written as '{coded_apple}', how is '{word}' written in that code?"
    exp = f"Each letter is shifted forward by {shift} positions in the alphabet."
    qs.append({"q": q, "options": opts, "ans": opts.index(coded), "exp": exp})
quizzes['CodingDecoding'] = qs

# Synonyms
syn_pairs = [("Abundant", "Plentiful"), ("Candid", "Frank"), ("Obscure", "Unclear"), ("Tenacious", "Persistent"), ("Diligent", "Hardworking"), ("Lucid", "Clear"), ("Ephemeral", "Short-lived"), ("Pragmatic", "Practical"), ("Amiable", "Friendly"), ("Mitigate", "Reduce")]
qs = []
for _ in range(100):
    word, ans = random.choice(syn_pairs)
    fakes = [p[1] for p in syn_pairs if p[0] != word]
    opts = [ans] + random.sample(fakes, 3)
    random.shuffle(opts)
    q = f"Choose the synonym for the word: '{word}'"
    exp = f"'{word}' means {ans}."
    qs.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": exp})
quizzes['SynonymsAntonyms'] = qs

# Blood Relations
names = ["John", "Mary", "David", "Sarah", "Michael", "Emma"]
rels = [("father", "son"), ("mother", "daughter"), ("brother", "sister"), ("uncle", "nephew")]
qs = []
for _ in range(100):
    p1 = random.choice(names)
    p2 = random.choice(names)
    while p1 == p2: p2 = random.choice(names)
    rel1, rel2 = random.choice(rels)
    ans = rel2
    opts = ["son", "daughter", "brother", "sister", "uncle", "nephew", "father", "mother"]
    if ans in opts: opts.remove(ans)
    options = [ans] + random.sample(opts, 3)
    random.shuffle(options)
    q = f"Pointing to {p1}, {p2} said, 'He is the {rel1} of my {rel2}.' How is {p1} related to {p2}?"
    exp = f"By drawing the family tree, the relationship resolves to {ans}."
    qs.append({"q": q, "options": options, "ans": options.index(ans), "exp": exp})
quizzes['BloodRelations'] = qs

remaining = [
    "Permutation", "DataInterpretation", "DirectionSense", "Syllogism",
    "Seating", "Puzzles", "VennDiagrams", "StatementConclusion", "CauseEffect",
    "ReadingComprehension", "SentenceCorrection", "ErrorDetection",
    "ParaJumbles", "FillBlanks", "MirrorImages", "PaperFolding", "FigureSeries",
    "EmbeddedFigures", "CubeDice"
]

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
            ans = str(logic(0,0))
            q = template
            
        opts = list(set([ans, "Option 2", "Option 3", "Option 4", "Option 5"]))
        if ans not in opts[:4]: opts[0] = ans
        opts = opts[:4]
        random.shuffle(opts)
        qs.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": "Solved based on standard logical reasoning rules."})
    quizzes[t] = qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
