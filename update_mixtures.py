import json
import random

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

# Mixtures and Alligations
qs = []
for _ in range(100):
    cost_cheap = random.randint(10, 30)
    cost_dear = random.randint(40, 80)
    mix_price = random.randint(cost_cheap + 5, cost_dear - 5)
    
    # Using alligation rule: Ratio = (cost_dear - mix_price) : (mix_price - cost_cheap)
    r1 = cost_dear - mix_price
    r2 = mix_price - cost_cheap
    
    ans = f"{r1}:{r2}"
    opts = list(set([ans, f"{r2}:{r1}", f"{r1+1}:{r2}", f"{r1}:{r2+1}", f"{r1+2}:{r2-1}"]))
    if ans not in opts[:4]: opts[0] = ans
    opts = opts[:4]
    random.shuffle(opts)
    
    q = f"In what ratio must a grocer mix two varieties of pulses costing ${cost_cheap}/kg and ${cost_dear}/kg so that the worth of the mixture is ${mix_price}/kg?"
    exp = f"By rule of alligation: Ratio = (Dearer Price - Mixture Price) : (Mixture Price - Cheaper Price) = ({cost_dear} - {mix_price}) : ({mix_price} - {cost_cheap}) = {ans}."
    
    qs.append({"q": q, "options": opts, "ans": opts.index(ans), "exp": exp})

quizzes['Mixtures'] = qs

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
