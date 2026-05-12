import json
import re
import random

raw_text = """
========================================
1. SERIES (NUMBER & ALPHABET)
========================================

1. 2, 4, 8, 16, ?
2. 5, 10, 20, 40, ?
3. 1, 4, 9, 16, ?
4. 3, 6, 12, 24, ?
5. 7, 14, 21, 28, ?
6. A, C, E, G, ?
7. Z, X, V, T, ?
8. B, D, F, H, ?
9. 11, 22, 33, 44, ?
10. 100, 90, 80, 70, ?
11. 1, 8, 27, 64, ?
12. M, O, Q, S, ?
13. 13, 26, 39, 52, ?
14. 9, 18, 27, 36, ?
15. A, D, G, J, ?
16. 81, 27, 9, 3, ?
17. 6, 12, 18, 24, ?
18. P, R, T, V, ?
19. 15, 30, 45, 60, ?
20. 4, 9, 14, 19, ?


========================================
2. CODING–DECODING
========================================

1. If CAT = DBU, then DOG = ?
2. If PEN = QFO, then BOX = ?
3. If SUN = TVO, then BAT = ?
4. If CAR = DBS, then MAP = ?
5. If RED = SFE, then BLUE = ?
6. If KING = LJOH, then QUEEN = ?
7. If APPLE = BQQMF, then MANGO = ?
8. If BOOK = CPPL, then NOTE = ?
9. If FAN = GBO, then HAT = ?
10. If COLD = DPME, then WARM = ?
11. If BIRD = CJSE, then FISH = ?
12. If ROAD = SPBE, then PATH = ?
13. If HAND = IBOE, then FOOT = ?
14. If GOLD = HPME, then SILVER = ?
15. If GAME = HBNF, then PLAY = ?
16. If CUP = DVQ, then GLASS = ?
17. If STAR = TUBS, then MOON = ?
18. If DAY = EBZ, then NIGHT = ?
19. If HOME = IPNF, then HOUSE = ?
20. If CODE = DPEF, then DATA = ?


========================================
3. BLOOD RELATIONS
========================================

1. A is the son of B. B is the daughter of C. How is A related to C?
2. P is the mother of Q. Q is the brother of R. How is P related to R?
3. X is the father of Y. Y is the sister of Z. How is X related to Z?
4. A is the brother of B. B is the mother of C. How is A related to C?
5. D is the daughter of E. E is the wife of F. How is D related to F?
6. R is the son of T. T is the sister of M. How is M related to R?
7. K is the mother of L. L is the father of M. How is K related to M?
8. A is the husband of B. C is the son of A. How is B related to C?
9. P is the uncle of Q. How can Q be related to P?
10. X is the grandfather of Y. How is Y related to X?
11. R is the father of S. S is the mother of T. How is R related to T?
12. A is the aunt of B. How is B related to A?
13. C is the brother of D. D is the daughter of E. How is C related to E?
14. M is the father of N. N is the brother of O. How is M related to O?
15. P is the daughter of Q. Q is the son of R. How is P related to R?
16. T is the wife of U. V is the daughter of T. How is U related to V?
17. X is the son of Y. Y is the husband of Z. How is Z related to X?
18. A is the mother of B. B is the father of C. How is A related to C?
19. D is the sister of E. E is the son of F. How is D related to F?
20. G is the grandfather of H. How is H related to G?


========================================
4. DIRECTION SENSE TEST
========================================

1. Ravi walks 10 m north and then 5 m east. Which direction is he from the start?
2. A man walks south, then turns left. Which direction is he facing?
3. Priya moves east and turns right. Which direction now?
4. Ram walks north, turns right, then right again. Which direction now?
5. A person walks west and turns left. Which direction now?
6. Arun walks 5 m north and 5 m south. Where is he now?
7. If you face east and turn left, which direction do you face?
8. If you face south and turn right, which direction do you face?
9. A man moves north, east, south. Final direction?
10. Ravi walks east, then north. Which direction from start?
11. A girl walks west and turns right. Which direction now?
12. Facing north, turn left twice. Which direction?
13. Facing east, turn right twice. Which direction?
14. A boy walks south, then east. Which direction from start?
15. Facing west, turn left. Which direction?
16. Facing north, turn right. Which direction?
17. A person walks east, west. Final position?
18. Facing south, turn left. Which direction?
19. Facing west, turn right. Which direction?
20. A man walks north, then west. Which direction from start?


========================================
5. SYLLOGISM
========================================

1. All cats are animals. Some animals are pets. Conclusion?
2. All apples are fruits. All fruits are healthy. Conclusion?
3. Some boys are players. All players are fit. Conclusion?
4. All pens are stationery. Some stationery are books. Conclusion?
5. All cars are vehicles. Some vehicles are bikes. Conclusion?
6. All roses are flowers. Some flowers fade quickly. Conclusion?
7. All students study. Ravi is a student. Conclusion?
8. Some birds can fly. Penguin is a bird. Conclusion?
9. All tables are furniture. Some furniture is wooden. Conclusion?
10. All lions are animals. Some animals are dangerous. Conclusion?
11. All mangoes are fruits. Fruits are sweet. Conclusion?
12. Some teachers are strict. All strict people are disciplined. Conclusion?
13. All books contain pages. Some pages are colored. Conclusion?
14. All mobiles are gadgets. Some gadgets are expensive. Conclusion?
15. Some doctors are surgeons. All surgeons are educated. Conclusion?
16. All rivers contain water. Ganga is a river. Conclusion?
17. All dogs bark. Tommy is a dog. Conclusion?
18. Some flowers are red. Roses are flowers. Conclusion?
19. All fish swim. Shark is a fish. Conclusion?
20. Some students are intelligent. Intelligent people work hard. Conclusion?


========================================
6. SEATING ARRANGEMENT
========================================

1. A sits left of B. Who is right of A?
2. P sits between Q and R. Who is in middle?
3. M is right of N. Who is left of M?
4. S sits next to T. Who is beside S?
5. A, B, C sit in row. B in middle. Who is left?
6. P is left of Q and right of R. Who is middle?
7. X sits opposite Y in circle. Who faces X?
8. A sits between B and C. Who are neighbors of A?
9. D sits right of E. Who is left of D?
10. F sits next to G. Who is beside G?
11. K sits left of L. L sits left of M. Who is middle?
12. P faces north. Q sits right of P. Where is Q?
13. A sits opposite B. Who faces A?
14. T is between U and V. Who is middle?
15. R sits left of S. S sits left of T. Who is rightmost?
16. C sits next to D. D next to E. Who is between?
17. M sits opposite N. Who faces M?
18. A left of B, B left of C. Who is center?
19. P next to Q. Q next to R. Who is between?
20. S opposite T. T opposite U impossible or not?


========================================
7. PUZZLES
========================================

1. If all roses are flowers and some flowers fade, are some roses fading?
2. A clock shows 3:15. Angle between hands?
3. Which month has 28 days?
4. What comes once in a minute, twice in a moment?
5. I speak without mouth. What am I?
6. What has keys but no locks?
7. Which number replaces ? : 2, 6, 12, 20, ?
8. A farmer has 17 sheep; all but 9 die. How many left?
9. What gets wetter as it dries?
10. Which weighs more: 1 kg iron or 1 kg cotton?
11. What has hands but cannot clap?
12. If today is Monday, what day after 10 days?
13. Complete: JFMAMJJASOND
14. Which number is odd: 2,4,6,9,10?
15. What has a neck but no head?
16. Which comes next: 1,1,2,3,5,8, ?
17. What begins with T ends with T and has tea in it?
18. How many sides in triangle?
19. Which is smallest prime number?
20. Which letter comes after K?


========================================
8. VENN DIAGRAMS
========================================

1. Can all dogs be animals?
2. Can fruits and vegetables overlap?
3. Are all squares rectangles?
4. Can teachers and singers overlap?
5. Are all roses flowers?
6. Can boys and students overlap?
7. Are all apples fruits?
8. Can cars and electric vehicles overlap?
9. Are all birds animals?
10. Can doctors and writers overlap?
11. Are all laptops computers?
12. Can fish and pets overlap?
13. Are all pens stationery?
14. Can students and athletes overlap?
15. Are all bananas fruits?
16. Can mobiles and cameras overlap?
17. Are all cows animals?
18. Can flowers and gifts overlap?
19. Are all buses vehicles?
20. Can books and notebooks overlap?


========================================
9. STATEMENT & CONCLUSION
========================================

1. Statement: All students passed. Conclusion: Ravi passed.
2. Statement: Some cars are red. Conclusion: All cars are red.
3. Statement: All birds fly. Conclusion: Sparrow flies.
4. Statement: No cats are dogs. Conclusion: Dogs are not cats.
5. Statement: Some apples are sweet. Conclusion: All apples sweet.
6. Statement: All teachers educated. Conclusion: Ram teacher educated.
7. Statement: Some boys play cricket. Conclusion: All boys play cricket.
8. Statement: All fish swim. Conclusion: Shark swims.
9. Statement: No pen is pencil. Conclusion: Pencil not pen.
10. Statement: Some flowers red. Conclusion: Roses red.
11. Statement: All buses vehicles. Conclusion: Bus vehicle.
12. Statement: Some fruits sour. Conclusion: Mango sour.
13. Statement: All doctors trained. Conclusion: Ravi doctor trained.
14. Statement: No birds mammals. Conclusion: Mammals not birds.
15. Statement: Some students intelligent. Conclusion: All intelligent students.
16. Statement: All rivers contain water. Conclusion: Ganga water.
17. Statement: Some mobiles expensive. Conclusion: All mobiles expensive.
18. Statement: All laptops computers. Conclusion: Laptop computer.
19. Statement: Some teachers strict. Conclusion: All teachers strict.
20. Statement: All books useful. Conclusion: English book useful.


========================================
10. CAUSE & EFFECT
========================================

1. Heavy rain -> floods. Cause or effect?
2. Fever -> infection.
3. Power cut -> darkness.
4. Hard work -> success.
5. Smoking -> health problems.
6. Exercise -> fitness.
7. Lack of sleep -> tiredness.
8. Pollution -> global warming.
9. Rain -> wet roads.
10. Overeating -> obesity.
11. Practice -> improvement.
12. Earthquake -> building damage.
13. Carelessness -> accidents.
14. Deforestation -> climate change.
15. Studying -> good marks.
16. Traffic jam -> delay.
17. Fire -> smoke.
18. Stress -> headache.
19. Drinking water -> hydration.
20. Virus -> disease.

LOGICAL REASONING – ANSWERS

ANswers 1. SERIES (NUMBER & ALPHABET)

1. 32
2. 80
3. 25
4. 48
5. 35
6. I
7. R
8. J
9. 55
10. 60
11. 125
12. U
13. 65
14. 45
15. M
16. 1
17. 30
18. X
19. 75
20. 24


2. CODING–DECODING

1. EPH
2. CPY
3. CBU
4. NBQ
5. CMV F
6. RVFFO
7. NBOHP
8. OPUF
9. IBU
10. XBSN
11. GJTI
12. QBUI
13. GPPU
14. TJMWFS
15. QMBZ
16. HMBTT
17. NPPO
18. OJHIU
19. IPVTF
20. EBUB


3. BLOOD RELATIONS

1. Grandson
2. Mother
3. Father
4. Uncle
5. Daughter
6. Uncle
7. Grandmother
8. Mother
9. Nephew/Niece
10. Grandchild
11. Grandfather
12. Nephew/Niece
13. Son
14. Father
15. Granddaughter
16. Father
17. Mother
18. Grandmother
19. Daughter
20. Grandchild


4. DIRECTION SENSE TEST

1. North-East
2. East
3. South
4. South
5. South
6. Starting point
7. North
8. West
9. South
10. North-East
11. North
12. South
13. West
14. South-East
15. South
16. East
17. Starting point
18. East
19. North
20. North-West


5. SYLLOGISM

1. No definite conclusion
2. Apples are healthy
3. Some boys may be fit
4. No definite conclusion
5. No definite conclusion
6. No definite conclusion
7. Ravi studies
8. Penguin is a bird
9. Some furniture may be tables
10. Some lions may be dangerous
11. Mangoes are sweet
12. Some teachers are disciplined
13. Some books may have colored pages
14. Some mobiles may be expensive
15. Some doctors are educated
16. Ganga contains water
17. Tommy barks
18. Roses may be red
19. Shark swims
20. Some students work hard


6. SEATING ARRANGEMENT

1. B
2. P
3. N
4. T
5. A
6. P
7. Y
8. B and C
9. E
10. F
11. L
12. Right side of P
13. B
14. T
15. T
16. D
17. N
18. B
19. Q
20. Impossible


7. PUZZLES

1. Cannot be determined
2. 7.5°
3. All months
4. Letter M
5. Echo
6. Piano
7. 30
8. 9
9. Towel
10. Both equal
11. Clock
12. Thursday
13. No next letter
14. 9
15. Bottle
16. 13
17. Teapot
18. 3
19. 2
20. L


8. VENN DIAGRAMS

1. Yes
2. Yes
3. Yes
4. Yes
5. Yes
6. Yes
7. Yes
8. Yes
9. Yes
10. Yes
11. Yes
12. Yes
13. Yes
14. Yes
15. Yes
16. Yes
17. Yes
18. Yes
19. Yes
20. Yes


9. STATEMENT & CONCLUSION

1. Cannot be determined
2. False
3. True
4. True
5. False
6. True
7. False
8. True
9. True
10. Cannot be determined
11. True
12. Cannot be determined
13. True
14. True
15. False
16. True
17. False
18. True
19. False
20. True


10. CAUSE & EFFECT

1. Rain = Cause, Flood = Effect
2. Infection = Cause, Fever = Effect
3. Power cut = Cause, Darkness = Effect
4. Hard work = Cause, Success = Effect
5. Smoking = Cause, Health problems = Effect
6. Exercise = Cause, Fitness = Effect
7. Lack of sleep = Cause, Tiredness = Effect
8. Pollution = Cause, Global warming = Effect
9. Rain = Cause, Wet roads = Effect
10. Overeating = Cause, Obesity = Effect
11. Practice = Cause, Improvement = Effect
12. Earthquake = Cause, Building damage = Effect
13. Carelessness = Cause, Accidents = Effect
14. Deforestation = Cause, Climate change = Effect
15. Studying = Cause, Good marks = Effect
16. Traffic jam = Cause, Delay = Effect
17. Fire = Cause, Smoke = Effect
18. Stress = Cause, Headache = Effect
19. Drinking water = Cause, Hydration = Effect
20. Virus = Cause, Disease = Effect
"""

# Extract Q and A parts
q_part, a_part = raw_text.split('LOGICAL REASONING – ANSWERS')

import collections

def parse_section(text):
    data = collections.defaultdict(list)
    current_topic = None
    
    for line in text.split('\n'):
        line = line.strip()
        if not line: continue
        if line.startswith('='): continue
        
        # Checking for topics
        if '1. SERIES' in line: current_topic = 'SeriesAlphabet'; continue
        if '2. CODING' in line: current_topic = 'CodingDecoding'; continue
        if '3. BLOOD RELATIONS' in line: current_topic = 'BloodRelations'; continue
        if '4. DIRECTION SENSE' in line: current_topic = 'DirectionSense'; continue
        if '5. SYLLOGISM' in line: current_topic = 'Syllogism'; continue
        if '6. SEATING ARRANGEMENT' in line: current_topic = 'SeatingArrangement'; continue
        if '7. PUZZLES' in line: current_topic = 'Puzzles'; continue
        if '8. VENN DIAGRAMS' in line: current_topic = 'VennDiagrams'; continue
        if '9. STATEMENT & CONCLUSION' in line: current_topic = 'StatementConclusion'; continue
        if '10. CAUSE & EFFECT' in line: current_topic = 'CauseEffect'; continue
        if 'ANswers 1. SERIES' in line: current_topic = 'SeriesAlphabet'; continue
        
        if current_topic and re.match(r'^\d+\.', line):
            content = re.sub(r'^\d+\.\s*', '', line)
            data[current_topic].append(content)
            
    return data

questions = parse_section(q_part)
answers = parse_section(a_part)

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

for topic in questions.keys():
    qs = questions[topic]
    ans = answers[topic]
    
    parsed = []
    for i in range(min(len(qs), len(ans))):
        q_text = qs[i]
        ans_text = ans[i]
        
        # generate generic options
        opts = [ans_text]
        if ans_text == 'True' or ans_text == 'False':
            opts = ['True', 'False']
        elif ans_text == 'Yes' or ans_text == 'No':
            opts = ['Yes', 'No', 'Maybe', 'Cannot be determined']
        elif ans_text == 'Cannot be determined':
            opts = ['True', 'False', 'Cannot be determined', 'None of these']
        else:
            opts.extend([f"Alternative {ans_text}", f"Variant {ans_text}", f"Opposite {ans_text}"])
            
        opts = list(set(opts))
        while len(opts) < 4:
            opts.append(opts[0] + " variant " + str(len(opts)))
        opts = opts[:4]
        if ans_text not in opts: opts[0] = ans_text
        random.shuffle(opts)
        
        parsed.append({
            "q": q_text,
            "options": opts,
            "ans": opts.index(ans_text),
            "exp": "Solved logically."
        })
    
    quizzes[topic] = parsed
    print(f"Loaded {len(parsed)} questions into {topic}")

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
