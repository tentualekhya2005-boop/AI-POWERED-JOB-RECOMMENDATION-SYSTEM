import json
import re
import random

raw_text = """
# 2. Simplification
1. 25 + 15 * 2 = 55
2. 100 / 5 + 8 = 28
3. 12 * 3 - 10 = 26
4. (18 + 6) / 3 = 8
5. 7^2 + 3^2 = 58
6. 64 / 8 * 2 = 16
7. 15 + 20 / 4 = 20
8. 5 * (6 + 4) = 50
9. 81 / 9 + 7 = 16
10. 9 * 9 - 20 = 61
11. Approximate 49.8 + 20.2 = 70
12. Approximate 199 / 5 = 40
13. sqrt(144) + 6 = 18
14. 45 - 18 / 3 = 39
15. 2^3 + 5 = 13
16. (25 * 4) / 5 = 20
17. Approximate 398 + 201 = 600
18. 72 / (3 * 4) = 6
19. 14 + 6 * 5 = 44
20. 90 - 8^2 = 26
21. Approximate 999 + 499 = 1500
22. (16 / 4)^2 = 16
23. 120 / 10 * 3 = 36
24. 5 + 4 * 7 - 3 = 30
25. Approximate 49 * 19 = 1000
26. sqrt(225) - 5 = 10
27. 6^3 / 9 = 24
28. Approximate 802 / 4 = 200
29. (9 + 3) * 2 = 24
30. 7 * 8 + 12 / 3 = 60
31. 50% of 200 = 100
32. 36 / 6 * 2 = 12
33. 144 / 12 = 12
34. 15^2 = 225
35. 8^2 - 10 = 54
36. 1000 / 25 = 40
37. 72 + 28 = 100
38. 13 * 13 = 169
39. 500 - 275 = 225
40. 45 / 5 + 7 = 16
41. 16 * 6 = 96
42. 125 / 5 = 25
43. 3^3 + 4^2 = 43
44. 84 / 7 = 12
45. 150 + 350 = 500
46. sqrt(81) + 9 = 18
47. 17 * 6 = 102
48. 96 / 12 = 8
49. 24^2 = 576
50. 9^3 = 729

# 3. Percentage
1. 10% of 200 = 20
2. 25% of 400 = 100
3. 50% of 80 = 40
4. 5% of 500 = 25
5. 20% of 150 = 30
6. 75% of 200 = 150
7. 15% of 300 = 45
8. 30% of 90 = 27
9. 12% of 250 = 30
10. 40% of 500 = 200
11. Increase 200 by 10% = 220
12. Decrease 400 by 20% = 320
13. 60 is what percent of 240? = 25%
14. 45 is what percent of 90? = 50%
15. 72 is what percent of 120? = 60%
16. 18% of 600 = 108
17. 35% of 700 = 245
18. Increase 500 by 25% = 625
19. Decrease 1000 by 10% = 900
20. 80% of 250 = 200
21. 150% of 40 = 60
22. 200% of 70 = 140
23. 90% of 90 = 81
24. 33% of 300 = 99
25. 66% of 150 = 99
26. 12.5% of 80 = 10
27. 5% of 960 = 48
28. 17% of 200 = 34
29. 22% of 50 = 11
30. 45% of 80 = 36
31. 110% of 90 = 99
32. 125% of 200 = 250
33. 250 increased by 20% = 300
34. 300 decreased by 15% = 255
35. 75 is what percent of 300? = 25%
36. 48 is what percent of 60? = 80%
37. 96 is what percent of 120? = 80%
38. 150 reduced by 20% = 120
39. 500 increased by 5% = 525
40. 14% of 350 = 49
41. 32% of 125 = 40
42. 18% of 450 = 81
43. 9% of 900 = 81
44. 55% of 200 = 110
45. 44% of 50 = 22
46. 27% of 300 = 81
47. 19% of 100 = 19
48. 2% of 2500 = 50
49. 7% of 700 = 49
50. 95% of 200 = 190

# 4. ProfitAndLoss
1. CP=100 SP=120 Profit=20
2. CP=200 SP=180 Loss=20
3. Profit% on CP100 SP120 = 20%
4. Loss% on CP200 SP150 = 25%
5. CP=500 Profit20% SP=600
6. SP of CP300 Loss10% = 270
7. Profit on CP250 SP300 = 50
8. Loss on CP400 SP350 = 50
9. Profit% on CP50 SP75 = 50%
10. Loss% on CP80 SP60 = 25%
11. SP for 25% profit on 200 = 250
12. SP for 20% loss on 500 = 400
13. Profit if CP150 SP210 = 60
14. Loss if CP700 SP650 = 50
15. Profit% if CP1000 SP1200 = 20%
16. Loss% if CP600 SP540 = 10%
17. Marked price1000 discount10% SP=900
18. MP500 discount20% SP=400
19. CP250 profit40% SP=350
20. CP800 loss25% SP=600
21. Profit on CP90 SP120 = 30
22. Loss on CP350 SP300 = 50
23. Profit% on CP150 SP180 = 20%
24. Loss% on CP400 SP320 = 20%
25. CP100 profit50% SP=150
26. CP200 loss15% SP=170
27. MP600 discount25% SP=450
28. MP1000 discount30% SP=700
29. Profit on CP75 SP90 = 15
30. Loss on CP500 SP450 = 50
31. Profit% on CP250 SP300 = 20%
32. Loss% on CP100 SP90 = 10%
33. SP for CP400 profit25% = 500
34. SP for CP900 loss20% = 720
35. Profit if CP700 SP910 = 210
36. Loss if CP1200 SP1000 = 200
37. MP800 discount5% SP=760
38. MP400 discount50% SP=200
39. Profit% on CP60 SP72 = 20%
40. Loss% on CP1000 SP850 = 15%
41. Profit on CP550 SP660 = 110
42. Loss on CP750 SP675 = 75
43. CP500 profit10% SP=550
44. CP300 loss5% SP=285
45. Profit% on CP125 SP150 = 20%
46. Loss% on CP240 SP216 = 10%
47. MP2000 discount10% SP=1800
48. Profit if CP100 SP130 = 30
49. Loss if CP450 SP360 = 90
50. SP for CP1000 profit15% = 1150

# 5. Ratio
1. Ratio 10:20 = 1:2
2. Ratio 15:45 = 1:3
3. 4:8 = 1:2
4. 25:100 = 1:4
5. Divide 60 in ratio1:2 = 20,40
6. Divide 90 in ratio2:3 = 36,54
7. 3/4 proportion to 6/x => x=8
8. 5:10 = 1:2
9. Ratio 18:24 = 3:4
10. Ratio 49:56 = 7:8
11. Divide100 in ratio3:2 = 60,40
12. Divide80 in ratio1:3 = 20,60
13. 2:5 = x:20 => x=8
14. 7:14 = 1:2
15. Ratio 45:60 = 3:4
16. 8:12 = 2:3
17. Divide120 in ratio2:1 = 80,40
18. 4:x = 8:16 => x=8
19. Ratio 9:27 = 1:3
20. Ratio 21:28 = 3:4
21. Divide150 in ratio4:1 = 120,30
22. 3:6 = 5:x => x=10
23. Ratio 16:20 = 4:5
24. 10:15 = 2:3
25. Divide200 in ratio3:5 = 75,125
26. Ratio 32:48 = 2:3
27. 6:x = 12:24 => x=12
28. Ratio 14:49 = 2:7
29. Divide90 in ratio4:5 = 40,50
30. 2:8 = 1:4
31. Ratio 81:108 = 3:4
32. Divide72 in ratio1:2:3 = 12,24,36
33. 7:21 = 1:3
34. Ratio 24:36 = 2:3
35. Divide180 in ratio2:4 = 60,120
36. 5:x = 15:45 => x=15
37. Ratio 35:49 = 5:7
38. Ratio 54:81 = 2:3
39. Divide140 in ratio3:4 = 60,80
40. Ratio 100:250 = 2:5
41. 4:5 = x:25 => x=20
42. Ratio 63:84 = 3:4
43. Divide96 in ratio1:5 = 16,80
44. Ratio 44:55 = 4:5
45. 9:x = 27:81 => x=27
46. Ratio 72:90 = 4:5
47. Divide110 in ratio6:5 = 60,50
48. Ratio 48:60 = 4:5
49. 12:18 = 2:3
50. Ratio 30:45 = 2:3
"""

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()
json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

topics = raw_text.strip().split('# ')
for topic_block in topics:
    if not topic_block.strip(): continue
    lines = topic_block.strip().split('\n')
    
    # Get topic key
    topic_header = lines[0].strip()
    if 'Simplification' in topic_header: key = 'Simplification'
    elif 'Percentage' in topic_header: key = 'Percentage'
    elif 'ProfitAndLoss' in topic_header: key = 'ProfitAndLoss'
    elif 'Ratio' in topic_header: key = 'Ratio'
    else: continue
    
    parsed_questions = []
    
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        # strip '1. ', '2. ', etc
        match = re.match(r'\d+\.\s*(.*)', line)
        if match:
            clean_line = match.group(1)
        else:
            clean_line = line
            
        if '=' in clean_line or '=>' in clean_line:
            # Handle '=> x=8' type splits
            if '=>' in clean_line:
                q_part, ans_part = clean_line.rsplit('=>', 1)
                q_text = q_part.strip() + " => ?"
                ans_text = ans_part.replace('x=', '').strip()
            else:
                q_part, ans_part = clean_line.rsplit('=', 1)
                q_text = q_part.strip() + " = ?"
                ans_text = ans_part.strip()
                
            # generate options
            if ans_text.isdigit():
                num = int(ans_text)
                opts = [ans_text, str(num+10), str(max(1, num-5)), str(num*2)]
            elif '%' in ans_text:
                num = int(ans_text.replace('%', ''))
                opts = [ans_text, f"{num+5}%", f"{max(1, num-10)}%", f"{num*2}%"]
            elif ',' in ans_text:
                opts = [ans_text, ans_text.replace(ans_text.split(',')[0], str(int(ans_text.split(',')[0])+10)), "10,20", "50,50"]
            elif ':' in ans_text:
                opts = [ans_text, "1:5", "2:5", "3:5"]
            else:
                opts = [ans_text, ans_text+" (approx)", "10", "20"]
                
            opts = list(set(opts))
            while len(opts) < 4: opts.append(opts[0] + " variant")
            opts = opts[:4]
            random.shuffle(opts)
            
            parsed_questions.append({
                "q": q_text,
                "options": opts,
                "ans": opts.index(ans_text),
                "exp": f"Calculated as requested: {clean_line}"
            })
            
    quizzes[key] = parsed_questions
    print(f"Loaded {len(parsed_questions)} questions into {key}")

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
