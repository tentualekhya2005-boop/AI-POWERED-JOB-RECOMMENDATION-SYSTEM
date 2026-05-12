import json
import random
import math

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

# remove 'const massiveQuizData = ' and ';'
json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

# Generate 100 Mensuration questions
mensuration_qs = []
for i in range(100):
    shape = random.choice(['circle', 'square', 'rectangle', 'cylinder', 'sphere'])
    if shape == 'circle':
        r = random.randint(2, 20)
        area = int(math.pi * r * r)
        opts = list(set([area, area+random.randint(10,50), area-random.randint(10,50), area+100]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(200, 300))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the approximate area of a circle with radius {r}?"
        exp = f"Area = pi * r^2 = 3.14 * {r}^2 = {area} (approx)"
        ans = opts.index(area)
    elif shape == 'square':
        side = random.randint(5, 50)
        area = side * side
        opts = list(set([area, area+random.randint(5,25), area-random.randint(5,25), area+50]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(100, 200))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the area of a square with side {side}?"
        exp = f"Area = side * side = {side} * {side} = {area}"
        ans = opts.index(area)
    elif shape == 'rectangle':
        l = random.randint(10, 50)
        b = random.randint(5, 40)
        area = l * b
        opts = list(set([area, area+random.randint(10,50), area-random.randint(10,50), area+100]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(150, 250))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the area of a rectangle with length {l} and breadth {b}?"
        exp = f"Area = length * breadth = {l} * {b} = {area}"
        ans = opts.index(area)
    elif shape == 'cylinder':
        r = random.randint(2, 10)
        h = random.randint(5, 20)
        vol = int(math.pi * r * r * h)
        opts = list(set([vol, vol+random.randint(50,150), vol-random.randint(50,150), vol+300]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(400, 500))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the approximate volume of a cylinder with radius {r} and height {h}?"
        exp = f"Volume = pi * r^2 * h = 3.14 * {r}^2 * {h} = {vol} (approx)"
        ans = opts.index(vol)
    else: # sphere
        r = random.randint(2, 10)
        vol = int((4/3) * math.pi * (r**3))
        opts = list(set([vol, vol+random.randint(50,150), vol-random.randint(50,150), vol+300]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(400, 500))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the approximate volume of a sphere with radius {r}?"
        exp = f"Volume = 4/3 * pi * r^3 = 1.33 * 3.14 * {r}^3 = {vol} (approx)"
        ans = opts.index(vol)

    mensuration_qs.append({
        "q": q,
        "options": [str(o) for o in opts],
        "ans": ans,
        "exp": exp
    })

quizzes['Mensuration'] = mensuration_qs

# Generate 100 Number System questions
number_system_qs = []
for i in range(100):
    t = random.choice(['lcm', 'hcf', 'divisibility'])
    if t == 'lcm':
        a = random.randint(2, 15)
        b = random.randint(2, 15)
        # compute lcm
        lcm = (a * b) // math.gcd(a, b)
        opts = list(set([lcm, lcm+a, lcm+b, lcm*2]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(20, 50))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the LCM of {a} and {b}?"
        exp = f"The lowest common multiple of {a} and {b} is {lcm}."
        ans = opts.index(lcm)
    elif t == 'hcf':
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        hcf = math.gcd(a, b)
        opts = list(set([hcf, hcf+1, hcf+2, hcf+3]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(4, 10))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the HCF (Highest Common Factor) of {a} and {b}?"
        exp = f"The highest common factor that divides both {a} and {b} is {hcf}."
        ans = opts.index(hcf)
    else:
        # divisibility
        num = random.randint(100, 999)
        rem = num % 3
        opts = list(set([rem, (rem+1)%3, (rem+2)%3, 3]))
        while len(opts) < 4: opts.append(opts[0] + random.randint(4, 10))
        opts = opts[:4]
        random.shuffle(opts)
        q = f"What is the remainder when {num} is divided by 3?"
        exp = f"Sum of digits of {num} modulo 3 gives the remainder. {num} % 3 = {rem}."
        ans = opts.index(rem)

    number_system_qs.append({
        "q": q,
        "options": [str(o) for o in opts],
        "ans": ans,
        "exp": exp
    })

quizzes['NumberSystem'] = number_system_qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
