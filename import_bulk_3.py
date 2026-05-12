import json
import re
import random

raw_text = """
Mixtures and Alligations – 50 Questions with Answers

A milkman mixes 10 L water in 40 L milk. Find water percentage.
Answer: 20%

Ratio of milk and water is 5:2 in 35 L mixture. Find water quantity.
Answer: 10 L

A trader mixes rice worth ₹40/kg and ₹60/kg in ratio 2:3. Find mean price.
Answer: ₹52/kg

20 L solution contains 25% acid. Find acid quantity.
Answer: 5 L

A mixture has alcohol and water in ratio 7:3. Find alcohol percentage.
Answer: 70%

How much water added to 50 L milk to make water 20%?
Answer: 12.5 L

Two varieties of tea ₹30/kg and ₹50/kg mixed equally. Find average price.
Answer: ₹40/kg

Ratio of sugar and water is 4:1 in 25 kg solution. Find sugar quantity.
Answer: 20 kg

60 L mixture contains 40% milk. Find milk quantity.
Answer: 24 L

Rice worth ₹80/kg and ₹100/kg mixed in ratio 1:2. Find mixture price.
Answer: ₹93.33/kg

A solution has 30% alcohol in 90 L. Find alcohol quantity.
Answer: 27 L

40 kg mixture has milk and water in ratio 3:1. Find water quantity.
Answer: 10 kg

25 L water added to 75 L milk. Find milk percentage.
Answer: 75%

Tea of ₹40/kg and ₹60/kg mixed in ratio 3:2. Find mean price.
Answer: ₹48/kg

A container has 80 L mixture with 25% water. Find water quantity.
Answer: 20 L

Ratio of acid and water is 9:1. Find water percentage.
Answer: 10%

100 kg mixture contains 15% salt. Find salt quantity.
Answer: 15 kg

Two oils ₹120/L and ₹150/L mixed equally. Find mixture price.
Answer: ₹135/L

A solution has milk and water ratio 11:4. Find milk percentage.
Answer: 73.33%

50 L mixture contains 10% alcohol. Find water quantity.
Answer: 45 L

Rice worth ₹20/kg and ₹30/kg mixed equally. Find average cost.
Answer: ₹25/kg

40 L milk diluted with 10 L water. Find water percentage.
Answer: 20%

A mixture contains 60% acid in 50 L. Find acid quantity.
Answer: 30 L

Tea priced ₹80/kg and ₹120/kg mixed in ratio 1:1. Find mean price.
Answer: ₹100/kg

A solution has water and alcohol ratio 2:3. Find alcohol percentage.
Answer: 60%

25 kg sugar solution has 20% sugar. Find sugar quantity.
Answer: 5 kg

Milk and water ratio is 4:5. Find milk percentage.
Answer: 44.44%

90 L solution contains 30% water. Find water quantity.
Answer: 27 L

Rice ₹40/kg and ₹50/kg mixed in ratio 2:1. Find mixture cost.
Answer: ₹43.33/kg

60 kg mixture contains 25% salt. Find salt quantity.
Answer: 15 kg

A mixture has alcohol and water ratio 5:4. Find water percentage.
Answer: 44.44%

Tea worth ₹100/kg and ₹140/kg mixed equally. Find average price.
Answer: ₹120/kg

120 L mixture contains 20% milk. Find milk quantity.
Answer: 24 L

Acid solution 40 L contains 10% acid. Find acid quantity.
Answer: 4 L

Oil ₹50/L and ₹70/L mixed in ratio 3:2. Find mixture price.
Answer: ₹58/L

80 kg mixture has sugar and water ratio 7:1. Find sugar quantity.
Answer: 70 kg

50 L mixture contains 80% milk. Find water quantity.
Answer: 10 L

Two metals ₹200/kg and ₹300/kg mixed equally. Find mean price.
Answer: ₹250/kg

Water and alcohol ratio is 1:4. Find alcohol percentage.
Answer: 80%

200 kg solution contains 15% acid. Find acid quantity.
Answer: 30 kg

Rice ₹25/kg and ₹35/kg mixed equally. Find average price.
Answer: ₹30/kg

A mixture has milk and water ratio 9:11. Find milk percentage.
Answer: 45%

100 L mixture contains 60% alcohol. Find alcohol quantity.
Answer: 60 L

Tea worth ₹90/kg and ₹110/kg mixed equally. Find mean price.
Answer: ₹100/kg

70 kg solution contains 20% sugar. Find sugar quantity.
Answer: 14 kg

Water added to 30 L milk becomes 25% water. Find water added.
Answer: 10 L

Acid and water ratio is 3:7. Find acid percentage.
Answer: 30%

Oil ₹40/L and ₹60/L mixed in ratio 1:2. Find mean price.
Answer: ₹53.33/L

90 L solution contains 50% water. Find water quantity.
Answer: 45 L

A mixture contains milk and water ratio 2:1. Find milk percentage.
Answer: 66.67%

Permutation and Combination – 50 Questions with Answers

Find 5!
Answer: 120

Find permutation of 5 objects taken 2 at a time.
Answer: 20

Find combination of 5 objects taken 2 at a time.
Answer: 10

Find 6P3.
Answer: 120

Find 6C2.
Answer: 15

Number of ways to arrange 4 books.
Answer: 24

Number of ways to arrange letters of CAT.
Answer: 6

Find 7C1.
Answer: 7

Find 7P1.
Answer: 7

Find 8C2.
Answer: 28

Find 8P2.
Answer: 56

Arrange 5 people in a row.
Answer: 120

Find 10C3.
Answer: 120

Find 10P2.
Answer: 90

Number of ways to select 2 students from 6.
Answer: 15

Number of arrangements of DOG.
Answer: 6

Find 9C4.
Answer: 126

Find 9P2.
Answer: 72

Find 4C2.
Answer: 6

Find 4P2.
Answer: 12

Find 11C1.
Answer: 11

Find 11P1.
Answer: 11

Arrange 6 books on shelf.
Answer: 720

Find 5C3.
Answer: 10

Find 5P3.
Answer: 60

Number of ways to arrange BAT.
Answer: 6

Find 12C2.
Answer: 66

Find 12P2.
Answer: 132

Select 3 students from 7.
Answer: 35

Find 13C1.
Answer: 13

Find 13P1.
Answer: 13

Arrange 7 people.
Answer: 5040

Find 8C3.
Answer: 56

Find 8P3.
Answer: 336

Number of arrangements of SUN.
Answer: 6

Find 14C2.
Answer: 91

Find 14P2.
Answer: 182

Find 15C1.
Answer: 15

Find 15P1.
Answer: 15

Arrange 3 books.
Answer: 6

Find 6C3.
Answer: 20

Find 6P3.
Answer: 120

Find 9C2.
Answer: 36

Find 9P3.
Answer: 504

Number of arrangements of MAP.
Answer: 6

Find 16C2.
Answer: 120

Find 16P2.
Answer: 240

Find 7C2.
Answer: 21

Find 7P2.
Answer: 42

Arrange letters of PEN.
Answer: 6

Probability – 50 Questions with Answers

Probability of getting head in one toss.
Answer: 1/2

Probability of getting tail in one toss.
Answer: 1/2

Probability of getting 3 on dice.
Answer: 1/6

Probability of even number on dice.
Answer: 1/2

Probability of odd number on dice.
Answer: 1/2

Probability of prime number on dice.
Answer: 1/2

Probability of number greater than 4 on dice.
Answer: 1/3

Probability of red card from deck.
Answer: 1/2

Probability of king from deck.
Answer: 1/13

Probability of ace from deck.
Answer: 1/13

Probability of face card from deck.
Answer: 3/13

Probability of drawing heart.
Answer: 1/4

Probability of getting 6 on dice.
Answer: 1/6

Probability of getting number less than 3.
Answer: 1/3

Probability of getting head twice.
Answer: 1/4

Probability of getting tail twice.
Answer: 1/4

Probability of sum 7 in two dice.
Answer: 1/6

Probability of sum 12 in two dice.
Answer: 1/36

Probability of black card.
Answer: 1/2

Probability of queen from deck.
Answer: 1/13

Probability of vowel from word “CAT”.
Answer: 1/3

Probability of consonant from “DOG”.
Answer: 2/3

Probability of getting odd number >3.
Answer: 1/3

Probability of getting multiple of 3 on dice.
Answer: 1/3

Probability of getting 2 heads in 3 tosses.
Answer: 3/8

Probability of getting at least one head in 2 tosses.
Answer: 3/4

Probability of non-face card.
Answer: 10/13

Probability of not getting 6.
Answer: 5/6

Probability of blue ball from 5 blue, 5 red.
Answer: 1/2

Probability of red ball from 2 red, 3 blue.
Answer: 2/5

Probability of getting even prime on dice.
Answer: 1/6

Probability of drawing spade.
Answer: 1/4

Probability of getting number <5.
Answer: 2/3

Probability of sum 5 in two dice.
Answer: 1/9

Probability of getting head and tail.
Answer: 1/2

Probability of getting at least one 6 in two dice.
Answer: 11/36

Probability of drawing jack.
Answer: 1/13

Probability of getting 1 or 2 on dice.
Answer: 1/3

Probability of getting even number less than 5.
Answer: 1/3

Probability of drawing diamond.
Answer: 1/4

Probability of drawing black king.
Answer: 1/26

Probability of getting two heads.
Answer: 1/4

Probability of getting no head in 2 tosses.
Answer: 1/4

Probability of getting sum 2 in dice.
Answer: 1/36

Probability of selecting even number from 1–10.
Answer: 1/2

Probability of selecting odd number from 1–10.
Answer: 1/2

Probability of getting number divisible by 2 on dice.
Answer: 1/2

Probability of selecting vowel from “APPLE”.
Answer: 2/5

Probability of getting head in 3 tosses exactly once.
Answer: 3/8

Probability of drawing ace of spades.
Answer: 1/52

Mensuration – 50 Questions with Answers

Area of square side 4 cm.
Answer: 16 cm²

Perimeter of square side 5 cm.
Answer: 20 cm

Area of rectangle 6x4.
Answer: 24 cm²

Perimeter of rectangle 6x4.
Answer: 20 cm

Area of circle radius 7 cm.
Answer: 154 cm²

Circumference of circle radius 7 cm.
Answer: 44 cm

Area of triangle base 10 cm, height 8 cm.
Answer: 40 cm²

Volume of cube side 3 cm.
Answer: 27 cm³

TSA of cube side 2 cm.
Answer: 24 cm²

Volume of cuboid 2x3x4.
Answer: 24 cm³

Curved surface area of cylinder r=7, h=10.
Answer: 440 cm²

Volume of cylinder r=7, h=10.
Answer: 1540 cm³

Area of square side 9 cm.
Answer: 81 cm²

Perimeter of square side 12 cm.
Answer: 48 cm

Area of rectangle 8x5.
Answer: 40 cm²

Perimeter of rectangle 8x5.
Answer: 26 cm

Area of circle radius 14 cm.
Answer: 616 cm²

Circumference radius 14 cm.
Answer: 88 cm

Area triangle b=12, h=6.
Answer: 36 cm²

Volume cube side 5 cm.
Answer: 125 cm³

TSA cube side 4 cm.
Answer: 96 cm²

Volume cuboid 5x4x3.
Answer: 60 cm³

CSA cylinder r=3, h=7.
Answer: 132 cm²

Volume cylinder r=3, h=7.
Answer: 198 cm³

Area square side 15 cm.
Answer: 225 cm²

Perimeter square side 16 cm.
Answer: 64 cm

Area rectangle 9x2.
Answer: 18 cm²

Perimeter rectangle 9x2.
Answer: 22 cm

Area circle radius 21 cm.
Answer: 1386 cm²

Circumference radius 21 cm.
Answer: 132 cm

Area triangle b=20, h=5.
Answer: 50 cm²

Volume cube side 6 cm.
Answer: 216 cm³

TSA cube side 6 cm.
Answer: 216 cm²

Volume cuboid 6x5x4.
Answer: 120 cm³

CSA cylinder r=5, h=8.
Answer: 251.2 cm²

Volume cylinder r=5, h=8.
Answer: 628 cm³

Area square side 20 cm.
Answer: 400 cm²

Perimeter square side 7 cm.
Answer: 28 cm

Area rectangle 11x3.
Answer: 33 cm²

Perimeter rectangle 11x3.
Answer: 28 cm

Area circle radius 10 cm.
Answer: 314 cm²

Circumference radius 10 cm.
Answer: 62.8 cm

Area triangle b=15, h=4.
Answer: 30 cm²

Volume cube side 8 cm.
Answer: 512 cm³

TSA cube side 8 cm.
Answer: 384 cm²

Volume cuboid 7x6x5.
Answer: 210 cm³

CSA cylinder r=4, h=9.
Answer: 226.08 cm²

Volume cylinder r=4, h=9.
Answer: 452.16 cm³

Area square side 25 cm.
Answer: 625 cm²

Circumference radius 28 cm.
Answer: 176 cm

Data Interpretation – 50 Questions with Answers

Total of 20, 30, 40?
Answer: 90

Average of 10, 20, 30?
Answer: 20

Highest number among 15, 40, 25?
Answer: 40

Lowest number among 12, 9, 18?
Answer: 9

Difference between 80 and 45?
Answer: 35

Percentage of 25 out of 100?
Answer: 25%

Average of 5,10,15,20?
Answer: 12.5

Sum of 12,13,14?
Answer: 39

Increase from 50 to 75?
Answer: 25

Percentage increase from 50 to 75?
Answer: 50%

Average of 2,4,6,8?
Answer: 5

Total of 100,200,300?
Answer: 600

Difference between 90 and 35?
Answer: 55

Highest among 11,22,33?
Answer: 33

Lowest among 44,55,22?
Answer: 22

Average of 7,14,21?
Answer: 14

Sum of 9,8,7,6?
Answer: 30

Percentage of 40 out of 200?
Answer: 20%

Increase from 80 to 100?
Answer: 20

Percentage increase from 80 to 100?
Answer: 25%

Average of 25,35,45?
Answer: 35

Total of 18,22,30?
Answer: 70

Difference between 120 and 75?
Answer: 45

Highest among 91,81,71?
Answer: 91

Lowest among 15,10,20?
Answer: 10

Average of 16,18,20?
Answer: 18

Sum of 11,22,33,44?
Answer: 110

Percentage of 15 out of 60?
Answer: 25%

Increase from 40 to 60?
Answer: 20

Percentage increase from 40 to 60?
Answer: 50%

Average of 3,6,9?
Answer: 6

Total of 14,16,18?
Answer: 48

Difference between 150 and 100?
Answer: 50

Highest among 99,88,77?
Answer: 99

Lowest among 35,25,15?
Answer: 15

Average of 12,24,36?
Answer: 24

Sum of 50,60,70?
Answer: 180

Percentage of 30 out of 120?
Answer: 25%

Increase from 90 to 120?
Answer: 30

Percentage increase from 90 to 120?
Answer: 33.33%

Average of 8,16,24?
Answer: 16

Total of 5,15,25,35?
Answer: 80

Difference between 200 and 140?
Answer: 60

Highest among 45,55,65?
Answer: 65

Lowest among 100,80,60?
Answer: 60

Average of 14,28,42?
Answer: 28

Sum of 13,26,39?
Answer: 78

Percentage of 45 out of 90?
Answer: 50%

Increase from 70 to 98?
Answer: 28

Percentage increase from 70 to 98?
Answer: 40%
"""

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

topics = re.split(r'\n(?=[A-Za-z\s]+– 50 Questions)', '\n' + raw_text.strip())

for topic_block in topics:
    if not topic_block.strip(): continue
    lines = topic_block.strip().split('\n')
    
    topic_header = lines[0].strip()
    if 'Mixtures' in topic_header: key = 'Mixtures'
    elif 'Permutation' in topic_header: key = 'Permutation'
    elif 'Probability' in topic_header: key = 'Probability'
    elif 'Mensuration' in topic_header: key = 'Mensuration'
    elif 'Data Interpretation' in topic_header: key = 'DataInterpretation'
    else: continue
    
    blocks = re.split(r'\n\n+', '\n'.join(lines[1:]).strip())
    parsed = []
    
    for block in blocks:
        if 'Answer:' not in block: continue
        parts = block.split('Answer:')
        q_text = parts[0].strip()
        ans_text = parts[1].strip()
        
        opts = [ans_text]
        if '%' in ans_text:
            num = float(ans_text.replace('%','')) if '.' in ans_text else int(ans_text.replace('%',''))
            opts.extend([f"{num+10}%", f"{max(1, num-5)}%", f"{num*2}%"])
        elif '/' in ans_text:
            num = int(ans_text.split('/')[1]) if ans_text.split('/')[1].isdigit() else 2
            opts.extend([f"1/{num+1}", f"1/{num+2}", f"1/{max(1, num-1)}"])
        elif any(c.isdigit() for c in ans_text):
            nums = re.findall(r'\d+', ans_text)
            if nums:
                val = int(nums[0])
                unit = ans_text.replace(nums[0], '').strip()
                opts.extend([f"{val+10} {unit}".strip(), f"{max(1, val-5)} {unit}".strip(), f"{val*2} {unit}".strip()])
                
        opts = list(set(opts))
        while len(opts) < 4:
            opts.append(opts[0] + " variant")
        opts = opts[:4]
        random.shuffle(opts)
        
        parsed.append({
            "q": q_text,
            "options": opts,
            "ans": opts.index(ans_text),
            "exp": "Solved using standard formulas."
        })
        
    quizzes[key] = parsed
    print(f"Loaded {len(parsed)} questions into {key}")

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
