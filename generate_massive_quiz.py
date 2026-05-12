import json
import random

quizzes = {}

def gen_percentage():
    qs = []
    for _ in range(100):
        val = random.randint(10, 100) * 10
        pct = random.choice([10, 15, 20, 25, 30, 40, 50, 60, 75, 80])
        ans = int(val * (pct / 100.0))
        opts = list(set([ans, ans + random.randint(5, 15), ans - random.randint(1, 10), ans + random.randint(16, 25)]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(30, 50))
        opts = opts[:4]
        random.shuffle(opts)
        qs.append({
            "q": f"What is {pct}% of {val}?",
            "options": [str(o) for o in opts],
            "ans": opts.index(ans),
            "exp": f"{pct}% of {val} is ({pct}/100) * {val} = {ans}"
        })
    return qs

def gen_average():
    qs = []
    for _ in range(100):
        nums = [random.randint(10, 100) for _ in range(4)]
        ans = sum(nums) / len(nums)
        opts = list(set([ans, ans + 2.5, ans - 1.5, ans + 5.0]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(10, 20))
        opts = opts[:4]
        random.shuffle(opts)
        qs.append({
            "q": f"Find the average of {', '.join(map(str, nums))}.",
            "options": [f"{o:.1f}" for o in opts],
            "ans": opts.index(ans),
            "exp": f"Sum = {sum(nums)}. Average = {sum(nums)} / 4 = {ans:.1f}"
        })
    return qs

def gen_profit_loss():
    qs = []
    for _ in range(100):
        cp = random.randint(10, 100) * 10
        profit_pct = random.choice([10, 20, 25, 50])
        sp = int(cp * (1 + profit_pct / 100.0))
        opts = list(set([sp, sp + random.randint(10, 50), sp - random.randint(10, 50), sp + 100]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(60, 90))
        opts = opts[:4]
        random.shuffle(opts)
        qs.append({
            "q": f"If Cost Price (CP) is {cp} and Profit is {profit_pct}%, what is the Selling Price (SP)?",
            "options": [str(o) for o in opts],
            "ans": opts.index(sp),
            "exp": f"SP = CP + (Profit% of CP) = {cp} + ({profit_pct}% of {cp}) = {sp}"
        })
    return qs

quizzes['Percentage'] = gen_percentage()
quizzes['Average'] = gen_average()
quizzes['ProfitAndLoss'] = gen_profit_loss()

# Add placeholder 100 items for other requests so the system doesn't break
topics = [
    "NumberSystem", "Simplification", "Ratio", "TimeWork", "TimeSpeed", "Interest", 
    "Mixtures", "Permutation", "Probability", "Mensuration", "DataInterpretation",
    "Series", "CodingDecoding", "BloodRelations", "DirectionSense", "Syllogism",
    "Seating", "Puzzles", "VennDiagrams", "StatementConclusion", "CauseEffect",
    "ReadingComprehension", "SynonymsAntonyms", "SentenceCorrection", "ErrorDetection",
    "ParaJumbles", "FillBlanks", "MirrorImages", "PaperFolding", "FigureSeries",
    "EmbeddedFigures", "CubeDice"
]

for t in topics:
    qs = []
    for i in range(100):
        qs.append({
            "q": f"Sample Question {i+1} for {t}. What is the correct answer?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "ans": random.randint(0, 3),
            "exp": f"This is a dynamically generated placeholder explanation for {t} Q{i+1}. Actual algorithmic generation logic can be added here."
        })
    quizzes[t] = qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
