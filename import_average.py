import json
import re
import random

raw_text = """
1. Find the average of 10, 20, and 30.

Explanation:
Average = (Sum of observations) / (Number of observations)
= (10 + 20 + 30) / 3
= 60 / 3

Answer: 20

2. Find the average of 5, 15, 25, and 35.

Explanation:
Sum = 5 + 15 + 25 + 35 = 80
Average = 80 / 4

Answer: 20

3. Find the average of first five natural numbers.

Explanation:
Numbers: 1, 2, 3, 4, 5
Sum = 15
Average = 15 / 5

Answer: 3

4. The average of 4 numbers is 25. Find their total sum.

Explanation:
Sum = Average * Number of terms
= 25 * 4

Answer: 100

5. Find the average of 12, 18, 24.

Explanation:
Sum = 12 + 18 + 24 = 54
Average = 54 / 3

Answer: 18

6. Average of 6 numbers is 15. Find the total sum.

Explanation:
Sum = 15 * 6

Answer: 90

7. Find the average of 7, 14, 21, 28.

Explanation:
Sum = 70
Average = 70 / 4

Answer: 17.5

8. Find the average of 100, 200, and 300.

Explanation:
Sum = 600
Average = 600 / 3

Answer: 200

9. The average age of 5 students is 16 years. Find total age.

Explanation:
Total age = 16 * 5

Answer: 80

10. Find the average of 9, 11, 13, 15, 17.

Explanation:
Sum = 65
Average = 65 / 5

Answer: 13

11. Find the average of 20 and 40.

Explanation:
(20 + 40) / 2 = 60 / 2

Answer: 30

12. The average of 8 numbers is 12. Find the sum.

Explanation:
Sum = 8 * 12

Answer: 96

13. Find the average of 4, 8, 12, 16, 20.

Explanation:
Sum = 60
Average = 60 / 5

Answer: 12

14. The average marks of 3 subjects is 75. Find total marks.

Explanation:
Total = 75 * 3

Answer: 225

15. Find the average of 25, 35, 45.

Explanation:
Sum = 105
Average = 105 / 3

Answer: 35

16. Find the average of first 10 even numbers.

Explanation:
First 10 even numbers are 2 to 20.
Average = (First + Last) / 2
= (2 + 20) / 2

Answer: 11

17. Find the average of 14, 16, 18, 20.

Explanation:
Sum = 68
Average = 68 / 4

Answer: 17

18. The average salary of 5 workers is 8000. Find total salary.

Explanation:
Total = 8000 * 5

Answer: 40000

19. Find the average of 3, 6, 9, 12, 15.

Explanation:
Sum = 45
Average = 45 / 5

Answer: 9

20. Average of 9 numbers is 50. Find their total.

Explanation:
Total = 50 * 9

Answer: 450

21. Find the average of 22, 24, 26, 28, 30.

Explanation:
Sum = 130
Average = 130 / 5

Answer: 26

22. The average of 7 numbers is 18. Find their sum.

Explanation:
Sum = Average * Number
= 18 * 7

Answer: 126

23. Find the average of first 8 natural numbers.

Explanation:
Average of consecutive numbers = (First + Last) / 2
= (1 + 8) / 2

Answer: 4.5

24. The average of 5 subjects is 68. Find total marks.

Explanation:
Total = 68 * 5

Answer: 340

25. Find the average of 45, 55, 65, 75.

Explanation:
Sum = 240
Average = 240 / 4

Answer: 60

26. A batsman scored 40, 60, 80 in 3 matches. Find average score.

Explanation:
Sum = 180
Average = 180 / 3

Answer: 60

27. The average of 10 numbers is 25. If one number is removed, average becomes 24. Find removed number.

Explanation:
Original total = 10 * 25 = 250
New total = 9 * 24 = 216
Removed number = 250 - 216

Answer: 34

28. Find the average of first 12 odd numbers.

Explanation:
First 12 odd numbers are 1 to 23
Average = (1 + 23) / 2

Answer: 12

29. Average of 6 numbers is 40. One number is 50. Find average of remaining 5 numbers.

Explanation:
Total = 6 * 40 = 240
Remaining sum = 240 - 50 = 190
Average = 190 / 5

Answer: 38

30. Find the average of 18, 24, 30, 36.

Explanation:
Sum = 108
Average = 108 / 4

Answer: 27

31. Average age of 8 students is 20 years. Find total age.

Explanation:
Total age = 8 * 20

Answer: 160

32. Find the average of 11, 22, 33, 44, 55.

Explanation:
Sum = 165
Average = 165 / 5

Answer: 33

33. Average of 9 numbers is 35. Find total sum.

Explanation:
Total = 35 * 9

Answer: 315

34. Find the average of 2, 4, 6, 8, 10, 12.

Explanation:
Sum = 42
Average = 42 / 6

Answer: 7

35. Average salary of 12 employees is 15,000. Find total salary.

Explanation:
Total = 15000 * 12

Answer: 180000

36. Find average of first 20 natural numbers.

Explanation:
Average = (1 + 20) / 2

Answer: 10.5

37. Average of 4 consecutive even numbers is 27. Find largest number.

Explanation:
Numbers are 24, 26, 28, 30

Answer: 30

38. Average of 5 consecutive odd numbers is 21. Find smallest number.

Explanation:
Numbers are 17, 19, 21, 23, 25

Answer: 17

39. Find the average of 120, 140, 160.

Explanation:
Sum = 420
Average = 420 / 3

Answer: 140

40. Average of 15 numbers is 16. Find total sum.

Explanation:
Total = 15 * 16

Answer: 240

41. Average marks of 8 students is 72. Find total marks.

Explanation:
Total = 72 * 8

Answer: 576

42. Find average of 13, 17, 21, 25.

Explanation:
Sum = 76
Average = 76 / 4

Answer: 19

43. The average of 3 numbers is 45. If two numbers are 40 and 50, find third number.

Explanation:
Total = 45 * 3 = 135
Third number = 135 - (40 + 50)

Answer: 45

44. Find average of 6, 12, 18, 24, 30.

Explanation:
Sum = 90
Average = 90 / 5

Answer: 18

45. Average of 7 consecutive numbers is 50. Find middle number.

Explanation:
In consecutive numbers, average equals middle number.

Answer: 50

46. Average of first 15 even numbers.

Explanation:
First even = 2
15th even = 30
Average = (2 + 30) / 2

Answer: 16

47. Average of 9, 18, 27, 36, 45.

Explanation:
Sum = 135
Average = 135 / 5

Answer: 27

48. Average of 5 numbers is 32. Find total sum.

Explanation:
Total = 32 * 5

Answer: 160

49. Find average of 14, 28, 42, 56.

Explanation:
Sum = 140
Average = 140 / 4

Answer: 35

50. Average of 10 consecutive odd numbers is 40. Find largest number.

Explanation:
Largest = 40 + 9 = 49

Answer: 49
"""

blocks = re.split(r'\n(?=\d+\.\s)', '\n' + raw_text.strip())
blocks = [b.strip() for b in blocks if b.strip()]

parsed_questions = []

for block in blocks:
    # Match question
    q_match = re.search(r'\d+\.\s*(.*?)(?=\nExplanation:|\nAnswer:)', block, re.DOTALL)
    exp_match = re.search(r'Explanation:\s*(.*?)(?=\nAnswer:)', block, re.DOTALL)
    ans_match = re.search(r'Answer:\s*(.*)', block)
    
    if q_match and ans_match:
        q_text = q_match.group(1).strip()
        ans_text = ans_match.group(1).strip()
        exp_text = exp_match.group(1).strip() if exp_match else "Solved mathematically."
        
        # Generate generic wrong options
        if '.' in ans_text:
            ans_num = float(ans_text)
            opts = [ans_text, str(ans_num + 2.5), str(max(1, ans_num - 2.5)), str(round(ans_num * 1.5, 1))]
        elif ans_text.isdigit():
            ans_num = int(ans_text)
            opts = [ans_text, str(ans_num + 10), str(max(1, ans_num - 5)), str(ans_num * 2)]
        else:
            opts = [ans_text, ans_text + " (Approx)", "10", "12"]
            
        opts = list(set(opts))
        while len(opts) < 4:
            opts.append(str(float(opts[-1]) + random.randint(1, 5)) if '.' in opts[-1] else str(int(opts[-1]) + random.randint(1, 5)))
        opts = opts[:4]
        random.shuffle(opts)
        
        parsed_questions.append({
            "q": q_text,
            "options": opts,
            "ans": opts.index(ans_text),
            "exp": exp_text.replace('\n', '<br>')
        })

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

quizzes['Average'] = parsed_questions

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")

print(f"Successfully loaded {len(parsed_questions)} questions into Average.")
