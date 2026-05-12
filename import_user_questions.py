import json
import re
import random

raw_text = """
1. What is the HCF of 12 and 18?

Explanation:
Factors of 12 -> 1, 2, 3, 4, 6, 12
Factors of 18 -> 1, 2, 3, 6, 9, 18
Highest common factor = 6

Answer: 6

2. What is the LCM of 4 and 6?

Explanation:
Multiples of 4 -> 4, 8, 12...
Multiples of 6 -> 6, 12...
Least common multiple = 12

Answer: 12

3. Is 37 a prime number?

Explanation:
37 has only 2 factors: 1 and 37.

Answer: Yes

4. Find the remainder when 25 is divided by 4.

Explanation:
25 = 4 x 6 + 1

Answer: 1

5. What is the HCF of 16 and 24?

Explanation:
Common factors are 1, 2, 4, 8.
Highest = 8

Answer: 8

6. Find the LCM of 8 and 12.

Explanation:
Multiples of 8 -> 8, 16, 24...
Multiples of 12 -> 12, 24...
LCM = 24

Answer: 24

7. Is 51 divisible by 3?

Explanation:
5 + 1 = 6
6 is divisible by 3.

Answer: Yes

8. Find the remainder when 49 is divided by 5.

Explanation:
49 = 5 x 9 + 4

Answer: 4

9. Find the HCF of 20 and 30.

Explanation:
Common factors -> 1, 2, 5, 10
Highest = 10

Answer: 10

10. Find the LCM of 5 and 7.

Explanation:
Both are prime numbers.
LCM = 5 x 7

Answer: 35

11. Is 91 a prime number?

Explanation:
91 = 7 x 13
So it has more than 2 factors.

Answer: No

12. Find the remainder when 78 is divided by 6.

Explanation:
78 / 6 = 13 remainder 0

Answer: 0

13. What is the HCF of 9 and 27?

Explanation:
Common factors -> 1, 3, 9
Highest = 9

Answer: 9

14. Find the LCM of 9 and 15.

Explanation:
Multiples of 9 -> 9, 18, 27, 36, 45
Multiples of 15 -> 15, 30, 45
LCM = 45

Answer: 45

15. Is 121 a prime number?

Explanation:
121 = 11 x 11

Answer: No

16. Find the remainder when 100 is divided by 9.

Explanation:
100 = 9 x 11 + 1

Answer: 1

17. Find the HCF of 14 and 35.

Explanation:
Common factors -> 1, 7
Highest = 7

Answer: 7

18. Find the LCM of 10 and 15.

Explanation:
Multiples of 10 -> 10, 20, 30
Multiples of 15 -> 15, 30
LCM = 30

Answer: 30

19. Is 2 a prime number?

Explanation:
2 has exactly two factors: 1 and 2.

Answer: Yes

20. Find the remainder when 67 is divided by 8.

Explanation:
67 = 8 x 8 + 3

Answer: 3

21. Find the HCF of 84 and 126.
Explanation:
84 = 2^2 x 3 x 7
126 = 2 x 3^2 x 7
Common factors = 2 x 3 x 7
Answer: 42

22. Find the LCM of 24 and 36.
Explanation:
24 = 2^3 x 3
36 = 2^2 x 3^2
LCM = 2^3 x 3^2
Answer: 72

23. Find the remainder when 2^35 is divided by 7.
Explanation:
2^3 = 8 = 1 (mod 7)
2^35 = (2^3)^11 x 2^2
= 1^11 x 4
Answer: 4

24. Find the number of factors of 72.
Explanation:
72 = 2^3 x 3^2
Number of factors = (3+1)(2+1)
Answer: 12

25. Find the greatest 4-digit number divisible by 18.
Explanation:
Largest 4-digit number = 9999
9999 / 18 gives remainder 9
9999 - 9 = 9990
Answer: 9990

26. Find the smallest number divisible by 12, 15, and 20.
Explanation:
Find LCM:
12 = 2^2 x 3
15 = 3 x 5
20 = 2^2 x 5
LCM = 2^2 x 3 x 5
Answer: 60

27. Find the remainder when 17^2 is divided by 5.
Explanation:
17 = 2 (mod 5)
2^2 = 4
Answer: 4

28. Find the HCF of 96 and 144.
Explanation:
96 = 2^5 x 3
144 = 2^4 x 3^2
Common = 2^4 x 3
Answer: 48

29. Find the LCM of 14, 21, and 28.
Explanation:
14 = 2 x 7
21 = 3 x 7
28 = 2^2 x 7
LCM = 2^2 x 3 x 7
Answer: 84

30. How many prime numbers are between 1 and 20?
Explanation:
2, 3, 5, 7, 11, 13, 17, 19
Answer: 8

31. Find the remainder when 10^5 is divided by 3.
Explanation:
10 = 1 (mod 3)
1^5 = 1
Answer: 1

32. Find the smallest prime number.
Explanation:
Prime numbers start from 2.
Answer: 2

33. Find the greatest number dividing 45 and 75 completely.
Explanation:
HCF of 45 and 75
Answer: 15

34. Find the least number divisible by 8, 12, and 15.
Explanation:
LCM = 2^3 x 3 x 5
Answer: 120

35. Find the remainder when 7^4 is divided by 5.
Explanation:
7 = 2 (mod 5)
2^4 = 16 = 1
Answer: 1

36. Find the sum of factors of 18.
Explanation:
Factors: 1, 2, 3, 6, 9, 18
Sum = 39
Answer: 39

37. Find the number of factors of 100.
Explanation:
100 = 2^2 x 5^2
Factors = (2+1)(2+1)
Answer: 9

38. Find the remainder when 81 is divided by 7.
Explanation:
81 = 7 x 11 + 4
Answer: 4

39. Find the HCF of 45, 60, and 75.
Explanation:
Common highest factor = 15
Answer: 15

40. Find the LCM of 18 and 24.
Explanation:
18 = 2 x 3^2
24 = 2^3 x 3
LCM = 2^3 x 3^2
Answer: 72

41. Find the unit digit of 3^45.
Explanation:
Unit digits cycle: 3, 9, 7, 1
45 mod 4 = 1
Answer: 3

42. Find the unit digit of 7^52.
Explanation:
Cycle: 7, 9, 3, 1
52 mod 4 = 0
Answer: 1

43. Find the remainder when 125 is divided by 9.
Explanation:
125 = 9 x 13 + 8
Answer: 8

44. Find the smallest number exactly divisible by 6 and 8.
Explanation:
LCM of 6 and 8
Answer: 24

45. Find the greatest 3-digit number divisible by 7.
Explanation:
999 / 7 remainder 5
999 - 5
Answer: 994

46. Find the number of even factors of 24.
Explanation:
Factors: 2, 4, 6, 8, 12, 24
Answer: 6

47. Find the product of HCF and LCM of 18 and 24.
Explanation:
HCF = 6
LCM = 72
6 x 72
Answer: 432

48. Find the remainder when 999 is divided by 11.
Explanation:
999 = 11 x 90 + 9
Answer: 9

49. Find the smallest multiple of 13 greater than 200.
Explanation:
13 x 15 = 195
13 x 16 = 208
Answer: 208

50. Find the unit digit of 2^100.
Explanation:
Cycle: 2, 4, 8, 6
100 mod 4 = 0
Answer: 6
"""

# Parse the text block into questions
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
        if ans_text == "Yes":
            opts = ["Yes", "No", "Cannot be determined", "None of the above"]
        elif ans_text == "No":
            opts = ["No", "Yes", "Cannot be determined", "None of the above"]
        elif ans_text.isdigit():
            ans_num = int(ans_text)
            opts = [ans_text, str(ans_num + 2), str(max(1, ans_num - 2)), str(ans_num * 2)]
            opts = list(set(opts))
            while len(opts) < 4:
                opts.append(str(int(opts[-1]) + random.randint(1, 5)))
        else:
            opts = [ans_text, ans_text + " (Approx)", "10", "12"]
            
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

# Replace Number System with EXACTLY these 50 questions
quizzes['NumberSystem'] = parsed_questions

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")

print(f"Successfully loaded {len(parsed_questions)} questions into Number System.")
