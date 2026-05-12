import json
import random
import math

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

# 1. Simple & Compound Interest
interest_qs = []
for _ in range(100):
    if random.choice(['SI', 'CI']) == 'SI':
        P = random.randint(10, 100) * 100
        R = random.randint(5, 20)
        T = random.randint(2, 10)
        SI = int((P * R * T) / 100)
        opts = list(set([SI, SI + 100, SI - 100, SI + 200, SI + 500]))
        if SI not in opts[:4]:
            opts[0] = SI
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the Simple Interest on a principal of {P} at a rate of {R}% per annum for {T} years?"
        exp = f"SI = (P * R * T) / 100 = ({P} * {R} * {T}) / 100 = {SI}."
        ans = opts.index(SI)
    else:
        P = random.randint(1, 10) * 1000
        R = random.choice([5, 10, 20])
        T = random.choice([2, 3])
        CI = int(P * ((1 + R/100.0)**T)) - P
        opts = list(set([CI, CI + 100, CI - 100, CI + 200, CI + 500]))
        if CI not in opts[:4]:
            opts[0] = CI
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the Compound Interest on a principal of {P} at a rate of {R}% per annum for {T} years compounded annually?"
        exp = f"Amount = P(1 + R/100)^T = {P}(1 + {R}/100)^{T} = {CI + P}. CI = Amount - P = {CI}."
        ans = opts.index(CI)
    interest_qs.append({"q": q, "options": [str(o) for o in opts], "ans": ans, "exp": exp})
quizzes['Interest'] = interest_qs

# 2. Time and Work
timework_qs = []
for _ in range(100):
    a_days = random.randint(10, 30)
    b_days = random.randint(15, 40)
    days = round((a_days * b_days) / (a_days + b_days), 2)
    opts = list(set([days, round(days + 2, 2), round(days - 2, 2), round(days + 5, 2)]))
    if days not in opts[:4]:
        opts[0] = days
    opts = opts[:4]
    random.shuffle(opts)
    q = f"A can do a piece of work in {a_days} days and B can do it in {b_days} days. How long will they take if they work together?"
    exp = f"Total work = {a_days * b_days} units. A's efficiency = {b_days}, B's efficiency = {a_days}. Together = {a_days + b_days}. Time = Work/Efficiency = {days} days."
    ans = opts.index(days)
    timework_qs.append({"q": q, "options": [str(o) for o in opts], "ans": ans, "exp": exp})
quizzes['TimeWork'] = timework_qs

# 3. Time, Speed, Distance
timespeed_qs = []
for _ in range(100):
    speed_kmh = random.choice([36, 54, 72, 90, 108])
    time_sec = random.randint(10, 30)
    speed_ms = speed_kmh * (5/18)
    dist = int(speed_ms * time_sec)
    opts = list(set([dist, dist + 50, dist - 50, dist + 100, dist + 20]))
    if dist not in opts[:4]:
        opts[0] = dist
    opts = opts[:4]
    random.shuffle(opts)
    q = f"A train traveling at {speed_kmh} km/hr crosses a pole in {time_sec} seconds. What is the length of the train?"
    exp = f"Speed in m/s = {speed_kmh} * (5/18) = {speed_ms} m/s. Distance (length) = Speed * Time = {speed_ms} * {time_sec} = {dist} meters."
    ans = opts.index(dist)
    timespeed_qs.append({"q": q, "options": [str(o) for o in opts], "ans": ans, "exp": exp})
quizzes['TimeSpeed'] = timespeed_qs

# 4. Simplification & Approx
simplification_qs = []
for _ in range(100):
    a = random.randint(10, 50)
    b = random.randint(2, 10)
    c = random.randint(5, 20)
    ans = (a * b) + c
    opts = list(set([ans, ans + 10, ans - 10, ans + 5, ans - 5]))
    if ans not in opts[:4]:
        opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    q = f"Simplify: ({a} x {b}) + {c} = ?"
    exp = f"Using BODMAS: Multiplication first: {a} x {b} = {a*b}. Then addition: {a*b} + {c} = {ans}."
    idx = opts.index(ans)
    simplification_qs.append({"q": q, "options": [str(o) for o in opts], "ans": idx, "exp": exp})
quizzes['Simplification'] = simplification_qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
