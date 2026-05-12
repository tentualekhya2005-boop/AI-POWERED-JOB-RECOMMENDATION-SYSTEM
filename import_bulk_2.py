import json
import re
import random

raw_text = """
# 1. Time and Work (50 Questions)

## Formula

Work = Efficiency * Time

1. A completes a work in 10 days. 1 day work?
   Explanation: 1/10
   Answer: 1/10

2. B completes work in 20 days. 1 day work?
   Explanation: 1/20
   Answer: 1/20

3. A and B together complete work in 5 days.
   Explanation: 1 day work = 1/5
   Answer: 1/5

4. A completes work in 12 days and B in 18 days. Together?
   Explanation: 1/12 + 1/18 = 5/36
   Time = 36/5
   Answer: 7.2 days

5. A does work in 15 days. Total work?
   Explanation: Assume LCM value.
   Answer: 15 units

6. A completes work in 8 days. One day work?
   Explanation: Reciprocal of days.
   Answer: 1/8

7. B completes work in 25 days. One day work?
   Explanation: 1/25
   Answer: 1/25

8. A and B together complete work in 4 days.
   Explanation: One day work = 1/4
   Answer: 1/4

9. A completes work in 6 days, B in 3 days. Together?
   Explanation: 1/6 + 1/3 = 1/2
   Answer: 2 days

10. A takes 20 days. Total work?
    Explanation: Assume total work = 20 units.
    Answer: 20 units

11. A completes work in 16 days. One day work?
    Answer: 1/16

12. B completes work in 40 days.
    Answer: 1/40

13. A and B complete work in 8 days.
    Answer: 1/8 work/day

14. A=12 days, B=6 days. Together?
    Explanation: 1/12 + 1/6 = 1/4
    Answer: 4 days

15. A completes work in 30 days.
    Answer: 1/30

16. A and B together finish work in 3 days.
    Answer: 1/3 work/day

17. A=18 days, B=9 days.
    Explanation: 1/18 + 1/9 = 1/6
    Answer: 6 days

18. A alone takes 24 days.
    Answer: 1/24

19. B alone takes 36 days.
    Answer: 1/36

20. Together complete in 12 days.
    Answer: 1/12

21. A=5 days, B=10 days.
    Explanation: 1/5 + 1/10 = 3/10
    Time = 10/3
    Answer: 3.33 days

22. A=14 days.
    Answer: 1/14

23. B=21 days.
    Answer: 1/21

24. A and B complete in 7 days.
    Answer: 1/7

25. A=9 days, B=18 days.
    Explanation: 1/9 + 1/18 = 1/6
    Answer: 6 days

26. A alone finishes in 11 days.
    Answer: 1/11

27. B alone finishes in 22 days.
    Answer: 1/22

28. A and B complete work in 2 days.
    Answer: 1/2

29. A=15 days, B=30 days.
    Explanation: 1/15 + 1/30 = 1/10
    Answer: 10 days

30. A completes work in 50 days.
    Answer: 1/50

31. B completes work in 100 days.
    Answer: 1/100

32. A and B together complete in 20 days.
    Answer: 1/20

33. A=7 days, B=14 days.
    Answer: 14/3 days

34. A alone takes 13 days.
    Answer: 1/13

35. B alone takes 26 days.
    Answer: 1/26

36. Together complete in 9 days.
    Answer: 1/9

37. A=4 days, B=12 days.
    Explanation: 1/4 + 1/12 = 1/3
    Answer: 3 days

38. A alone takes 60 days.
    Answer: 1/60

39. B alone takes 15 days.
    Answer: 1/15

40. Together complete in 6 days.
    Answer: 1/6

41. A=8 days, B=24 days.
    Explanation: 1/8 + 1/24 = 1/6
    Answer: 6 days

42. A alone takes 32 days.
    Answer: 1/32

43. B alone takes 16 days.
    Answer: 1/16

44. Together complete in 5 days.
    Answer: 1/5

45. A=10 days, B=5 days.
    Explanation: 1/10 + 1/5 = 3/10
    Answer: 10/3 days

46. A alone takes 45 days.
    Answer: 1/45

47. B alone takes 90 days.
    Answer: 1/90

48. Together complete in 15 days.
    Answer: 1/15

49. A=6 days, B=8 days.
    Explanation: 1/6 + 1/8 = 7/24
    Answer: 24/7 days

50. A alone takes 27 days.
    Answer: 1/27

# 2. Time Speed Distance (50 Questions)

## Formula

Speed = Distance / Time

1. 120 km in 2 hours.
   Explanation: 120/2
   Answer: 60 km/h

2. 150 km in 3 hours.
   Answer: 50 km/h

3. Distance at 80 km/h for 4 hrs.
   Answer: 320 km

4. Time for 200 km at 50 km/h.
   Answer: 4 hrs

5. Convert 72 km/h to m/s.
   Answer: 20 m/s

6. Convert 54 km/h to m/s.
   Answer: 15 m/s

7. Convert 10 m/s to km/h.
   Answer: 36 km/h

8. Distance at 40 km/h for 5 hrs.
   Answer: 200 km

9. Speed for 300 km in 6 hrs.
   Answer: 50 km/h

10. Time for 180 km at 60 km/h.
    Answer: 3 hrs

11. Distance at 90 km/h for 2 hrs.
    Answer: 180 km

12. Time for 400 km at 80 km/h.
    Answer: 5 hrs

13. Speed for 240 km in 4 hrs.
    Answer: 60 km/h

14. Convert 18 km/h to m/s.
    Answer: 5 m/s

15. Convert 25 m/s to km/h.
    Answer: 90 km/h

16. Distance at 70 km/h for 3 hrs.
    Answer: 210 km

17. Speed for 500 km in 10 hrs.
    Answer: 50 km/h

18. Time for 360 km at 90 km/h.
    Answer: 4 hrs

19. Distance at 55 km/h for 2 hrs.
    Answer: 110 km

20. Speed for 150 km in 5 hrs.
    Answer: 30 km/h

21. Time for 100 km at 25 km/h.
    Answer: 4 hrs

22. Distance at 65 km/h for 4 hrs.
    Answer: 260 km

23. Speed for 600 km in 12 hrs.
    Answer: 50 km/h

24. Convert 90 km/h to m/s.
    Answer: 25 m/s

25. Convert 20 m/s to km/h.
    Answer: 72 km/h

26. Distance at 100 km/h for 5 hrs.
    Answer: 500 km

27. Time for 450 km at 90 km/h.
    Answer: 5 hrs

28. Speed for 160 km in 2 hrs.
    Answer: 80 km/h

29. Distance at 35 km/h for 6 hrs.
    Answer: 210 km

30. Time for 240 km at 80 km/h.
    Answer: 3 hrs

31. Speed for 420 km in 7 hrs.
    Answer: 60 km/h

32. Convert 108 km/h to m/s.
    Answer: 30 m/s

33. Convert 15 m/s to km/h.
    Answer: 54 km/h

34. Distance at 45 km/h for 8 hrs.
    Answer: 360 km

35. Time for 600 km at 75 km/h.
    Answer: 8 hrs

36. Speed for 90 km in 1.5 hrs.
    Answer: 60 km/h

37. Distance at 85 km/h for 2 hrs.
    Answer: 170 km

38. Time for 720 km at 90 km/h.
    Answer: 8 hrs

39. Speed for 250 km in 5 hrs.
    Answer: 50 km/h

40. Distance at 95 km/h for 3 hrs.
    Answer: 285 km

41. Convert 36 km/h to m/s.
    Answer: 10 m/s

42. Convert 12 m/s to km/h.
    Answer: 43.2 km/h

43. Time for 350 km at 70 km/h.
    Answer: 5 hrs

44. Speed for 480 km in 8 hrs.
    Answer: 60 km/h

45. Distance at 120 km/h for 2 hrs.
    Answer: 240 km

46. Time for 150 km at 30 km/h.
    Answer: 5 hrs

47. Speed for 200 km in 4 hrs.
    Answer: 50 km/h

48. Distance at 75 km/h for 6 hrs.
    Answer: 450 km

49. Time for 540 km at 60 km/h.
    Answer: 9 hrs

50. Convert 144 km/h to m/s.
    Answer: 40 m/s

# 3. Simple and Compound Interest (50 Questions)

1. SI on 1000 at 10% for 2 yrs.
   Explanation: (1000*10*2)/100
   Answer: 200

2. SI on 5000 at 5% for 3 yrs.
   Answer: 750

3. SI on 2000 at 8% for 2 yrs.
   Answer: 320

4. SI on 3000 at 6% for 5 yrs.
   Answer: 900

5. SI on 1500 at 4% for 2 yrs.
   Answer: 120

6. CI on 1000 at 10% for 2 yrs.
   Answer: 210

7. CI on 2000 at 5% for 2 yrs.
   Answer: 205

8. Amount on 5000 at 10% for 1 yr.
   Answer: 5500

9. SI on 2500 at 12% for 2 yrs.
   Answer: 600

10. CI on 4000 at 5% for 2 yrs.
    Answer: 410

11. SI on 800 at 15% for 1 yr.
    Answer: 120

12. SI on 6000 at 7% for 3 yrs.
    Answer: 1260

13. CI on 10000 at 10% for 2 yrs.
    Answer: 2100

14. Amount on 3000 at 5% for 2 yrs.
    Answer: 3307.5

15. SI on 7000 at 9% for 2 yrs.
    Answer: 1260

16. CI on 1500 at 10% for 2 yrs.
    Answer: 315

17. SI on 1200 at 5% for 4 yrs.
    Answer: 240

18. SI on 900 at 8% for 3 yrs.
    Answer: 216

19. Amount on 2500 at 12% for 1 yr.
    Answer: 2800

20. CI on 5000 at 10% for 2 yrs.
    Answer: 1050

21. SI on 4000 at 6% for 2 yrs.
    Answer: 480

22. SI on 3500 at 10% for 3 yrs.
    Answer: 1050

23. CI on 6000 at 5% for 2 yrs.
    Answer: 615

24. Amount on 4500 at 8% for 2 yrs.
    Answer: 5248.8

25. SI on 10000 at 4% for 5 yrs.
    Answer: 2000

26. CI on 2000 at 10% for 3 yrs.
    Answer: 662

27. SI on 5500 at 6% for 2 yrs.
    Answer: 660

28. SI on 6500 at 7% for 3 yrs.
    Answer: 1365

29. Amount on 8000 at 5% for 2 yrs.
    Answer: 8820

30. CI on 3000 at 8% for 2 yrs.
    Answer: 499.2

31. SI on 9000 at 10% for 1 yr.
    Answer: 900

32. SI on 7500 at 12% for 2 yrs.
    Answer: 1800

33. Amount on 2000 at 15% for 1 yr.
    Answer: 2300

34. CI on 1000 at 20% for 2 yrs.
    Answer: 440

35. SI on 15000 at 5% for 2 yrs.
    Answer: 1500

36. SI on 2500 at 9% for 4 yrs.
    Answer: 900

37. Amount on 5000 at 6% for 3 yrs.
    Answer: 5955.08

38. CI on 4000 at 10% for 2 yrs.
    Answer: 840

39. SI on 3200 at 7% for 5 yrs.
    Answer: 1120

40. SI on 1100 at 10% for 3 yrs.
    Answer: 330

41. Amount on 7000 at 8% for 2 yrs.
    Answer: 8164.8

42. CI on 9000 at 5% for 2 yrs.
    Answer: 922.5

43. SI on 4500 at 11% for 2 yrs.
    Answer: 990

44. SI on 2400 at 6% for 3 yrs.
    Answer: 432

45. Amount on 10000 at 12% for 2 yrs.
    Answer: 12544

46. CI on 3500 at 10% for 2 yrs.
    Answer: 735

47. SI on 2700 at 8% for 5 yrs.
    Answer: 1080

48. SI on 1800 at 5% for 4 yrs.
    Answer: 360

49. Amount on 6000 at 7% for 2 yrs.
    Answer: 6869.4

50. CI on 2500 at 10% for 2 yrs.
    Answer: 525

"""

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

import re

# Split raw_text directly into lines and parse
lines = raw_text.split('\n')
current_topic = None
parsed = []

def save_current():
    global current_topic, parsed
    if current_topic and len(parsed) > 0:
        quizzes[current_topic] = parsed
        print(f"Loaded {len(parsed)} questions into {current_topic}")
    parsed = []

for i in range(len(lines)):
    line = lines[i].strip()
    if line.startswith('# 1. Time and Work'):
        save_current()
        current_topic = 'TimeWork'
    elif line.startswith('# 2. Time Speed'):
        save_current()
        current_topic = 'TimeSpeed'
    elif line.startswith('# 3. Simple and Compound'):
        save_current()
        current_topic = 'Interest'
    elif re.match(r'^\d+\.', line):
        # Found a question!
        q_text = re.sub(r'^\d+\.\s*', '', line)
        ans_text = ""
        exp_text = "Solved using standard formulas."
        
        # Look ahead for Answer and Explanation
        j = i + 1
        while j < len(lines) and not re.match(r'^\d+\.', lines[j].strip()) and not lines[j].strip().startswith('#'):
            nxt = lines[j].strip()
            if nxt.startswith('Explanation:'):
                exp_text = nxt.replace('Explanation:', '').strip()
            elif nxt.startswith('Answer:'):
                ans_text = nxt.replace('Answer:', '').strip()
            j += 1
            
        if ans_text:
            opts = [ans_text]
            if '/' in ans_text:
                parts = ans_text.split('/')
                if len(parts) == 2 and parts[1].split(' ')[0].isdigit():
                    num = int(parts[1].split(' ')[0])
                    opts.extend([f"{parts[0]}/{num+2}", f"{parts[0]}/{max(2, num-2)}", f"{parts[0]}/{num+5}"])
            elif 'km/h' in ans_text or 'm/s' in ans_text or 'hrs' in ans_text:
                val_str = ans_text.split(' ')[0]
                unit = ' '.join(ans_text.split(' ')[1:])
                if val_str.replace('.','').isdigit():
                    val = float(val_str) if '.' in val_str else int(val_str)
                    opts.extend([f"{val+10} {unit}", f"{max(5, val-10)} {unit}", f"{val+15} {unit}"])
            elif ans_text.replace('.', '').isdigit():
                val = float(ans_text) if '.' in ans_text else int(ans_text)
                opts.extend([str(val+10), str(max(1, val-10)), str(val*2)])
            
            opts = list(set(opts))
            while len(opts) < 4:
                opts.append(opts[0] + " variant")
            opts = opts[:4]
            random.shuffle(opts)
            
            parsed.append({
                "q": q_text,
                "options": opts,
                "ans": opts.index(ans_text),
                "exp": exp_text
            })

save_current()

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
