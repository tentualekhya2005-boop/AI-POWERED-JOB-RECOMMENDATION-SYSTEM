import json
import random
import math

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

# 1. Permutations
perms = []
objects = ["books on a shelf", "people in a line", "cars in a parking lot", "paintings on a wall", "distinct letters in a word"]
for _ in range(100):
    t = random.randint(1, 3)
    if t == 1:
        # P(n, n) = n!
        n = random.randint(4, 9)
        obj = random.choice(objects)
        ans = math.factorial(n)
        q = f"In how many ways can {n} {obj} be arranged?"
    else:
        # P(n, r) = n! / (n-r)!
        n = random.randint(5, 15)
        r = random.randint(2, 4)
        ans = math.factorial(n) // math.factorial(n - r)
        obj = random.choice(["students", "candidates", "players", "colors"])
        q = f"In how many ways can {r} {obj} be chosen and arranged from a group of {n} {obj}?"
        
    opts = list(set([ans, ans+10, max(2, ans-12), ans*2, ans + random.randint(1, 5)*10]))
    if ans not in opts[:4]:
        opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    perms.append({"q": q, "options": [str(o) for o in opts], "ans": opts.index(ans), "exp": "Using standard permutation formulas P(n,r) = n! / (n-r)!"})

quizzes['Permutation'] = perms


# 2. Seating Arrangement
seats = []
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ian", "Jack", "Kevin", "Liam"]
for _ in range(100):
    subset = random.sample(names, 5)
    p1, p2, p3, p4, p5 = subset
    q = f"Five friends {p1}, {p2}, {p3}, {p4}, and {p5} are sitting in a row facing north. {p1} is at the extreme left. {p5} is at the extreme right. {p2} sits immediately to the right of {p1}. {p4} sits immediately to the left of {p5}. Who is sitting exactly in the middle?"
    ans = p3
    opts = [p1, p2, p3, p4]
    random.shuffle(opts)
    seats.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": f"The arrangement from left to right is {p1}, {p2}, {p3}, {p4}, {p5}."})

quizzes['Seating'] = seats

# 3. Cube and Dice
cubes = []
for _ in range(100):
    faces = [1,2,3,4,5,6]
    random.shuffle(faces)
    p1 = (faces[0], faces[1])
    p2 = (faces[2], faces[3])
    p3 = (faces[4], faces[5])
    
    target = random.choice(faces)
    if target in p1: ans = p1[0] if target == p1[1] else p1[1]
    elif target in p2: ans = p2[0] if target == p2[1] else p2[1]
    else: ans = p3[0] if target == p3[1] else p3[1]
    
    q = f"In a certain dice configuration, if {p1[0]} is opposite {p1[1]}, and {p2[0]} is opposite {p2[1]}, what number is opposite {target}?"
    opts = [ans, faces[random.randint(0,5)], faces[random.randint(0,5)], faces[random.randint(0,5)]]
    opts = list(set(opts))
    while len(opts) < 4:
        opts.append(random.randint(7, 15))
    opts = opts[:4]
    random.shuffle(opts)
    cubes.append({"q": q, "options": [str(o) for o in opts], "ans": opts.index(ans), "exp": "By mapping the given opposite faces, we can deduce the remaining pair."})
    
quizzes['CubeDice'] = cubes

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
