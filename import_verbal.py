import json
import re
import random

raw_text = """
# 1. Reading Comprehension (50 Questions)

## Passage 1

Technology has changed the way people communicate. Earlier, letters were used, but now instant messaging and video calls are common. Communication has become faster and easier.

1. What replaced letters mostly?
   Answer: Instant messaging and video calls

2. Communication has become?
   Answer: Faster and easier

3. What is the passage about?
   Answer: Technology and communication

4. Earlier people used?
   Answer: Letters

5. Modern communication includes?
   Answer: Video calls

## Passage 2

Exercise is important for good health. Regular exercise improves fitness, reduces stress, and increases energy.

6. What improves fitness?
   Answer: Regular exercise

7. Exercise reduces?
   Answer: Stress

8. Exercise increases?
   Answer: Energy

9. Passage is about?
   Answer: Benefits of exercise

10. Good health requires?
    Answer: Exercise

## Passage 3

Trees are essential for life. They provide oxygen, reduce pollution, and help maintain ecological balance.

11. Trees provide?
    Answer: Oxygen

12. Trees reduce?
    Answer: Pollution

13. Trees help maintain?
    Answer: Ecological balance

14. Passage discusses?
    Answer: Importance of trees

15. Trees are essential for?
    Answer: Life

## Passage 4

Education helps people gain knowledge and skills. It improves confidence and creates better career opportunities.

16. Education provides?
    Answer: Knowledge and skills

17. Education improves?
    Answer: Confidence

18. Education creates?
    Answer: Career opportunities

19. Passage is about?
    Answer: Importance of education

20. Education helps people?
    Answer: Gain knowledge

## Passage 5

Water is a precious resource. People should avoid wasting water and use it carefully.

21. Water is a?
    Answer: Precious resource

22. People should avoid?
    Answer: Wasting water

23. Water should be used?
    Answer: Carefully

24. Passage focuses on?
    Answer: Water conservation

25. Water is important because?
    Answer: It is precious

## Passage 6

Books are good sources of knowledge. Reading books improves vocabulary and communication skills.

26. Books provide?
    Answer: Knowledge

27. Reading improves?
    Answer: Vocabulary

28. Reading also improves?
    Answer: Communication skills

29. Passage is about?
    Answer: Benefits of reading books

30. Books are considered?
    Answer: Sources of knowledge

## Passage 7

Teamwork is important in organizations. It helps employees work together efficiently.

31. Teamwork is important in?
    Answer: Organizations

32. Teamwork helps employees?
    Answer: Work together efficiently

33. Passage discusses?
    Answer: Teamwork

34. Teamwork improves?
    Answer: Efficiency

35. Employees should?
    Answer: Work together

## Passage 8

Healthy food keeps the body strong. Junk food may lead to health problems.

36. Healthy food keeps body?
    Answer: Strong

37. Junk food may cause?
    Answer: Health problems

38. Passage is about?
    Answer: Healthy eating

39. Good health needs?
    Answer: Healthy food

40. Junk food is?
    Answer: Harmful

## Passage 9

Computers are widely used in education and business. They help save time and improve productivity.

41. Computers are used in?
    Answer: Education and business

42. Computers save?
    Answer: Time

43. Computers improve?
    Answer: Productivity

44. Passage discusses?
    Answer: Uses of computers

45. Computers are?
    Answer: Widely used

## Passage 10

Discipline is necessary for success. It helps people stay focused and organized.

46. Discipline is necessary for?
    Answer: Success

47. Discipline helps people stay?
    Answer: Focused

48. Discipline also helps people stay?
    Answer: Organized

49. Passage is about?
    Answer: Discipline

50. Success requires?
    Answer: Discipline

# 2. Synonyms & Antonyms (50 Questions)

1. Synonym of Happy
   Answer: Joyful

2. Antonym of Happy
   Answer: Sad

3. Synonym of Fast
   Answer: Quick

4. Antonym of Fast
   Answer: Slow

5. Synonym of Begin
   Answer: Start

6. Antonym of Begin
   Answer: End

7. Synonym of Brave
   Answer: Courageous

8. Antonym of Brave
   Answer: Cowardly

9. Synonym of Large
   Answer: Huge

10. Antonym of Large
    Answer: Small

11. Synonym of Smart
    Answer: Intelligent

12. Antonym of Smart
    Answer: Dull

13. Synonym of Rich
    Answer: Wealthy

14. Antonym of Rich
    Answer: Poor

15. Synonym of Honest
    Answer: Truthful

16. Antonym of Honest
    Answer: Dishonest

17. Synonym of Strong
    Answer: Powerful

18. Antonym of Strong
    Answer: Weak

19. Synonym of Beautiful
    Answer: Attractive

20. Antonym of Beautiful
    Answer: Ugly

21. Synonym of Silent
    Answer: Quiet

22. Antonym of Silent
    Answer: Noisy

23. Synonym of Angry
    Answer: Furious

24. Antonym of Angry
    Answer: Calm

25. Synonym of Difficult
    Answer: Hard

26. Antonym of Difficult
    Answer: Easy

27. Synonym of Ancient
    Answer: Old

28. Antonym of Ancient
    Answer: Modern

29. Synonym of Clever
    Answer: Bright

30. Antonym of Clever
    Answer: Foolish

31. Synonym of Help
    Answer: Assist

32. Antonym of Help
    Answer: Hinder

33. Synonym of Create
    Answer: Build

34. Antonym of Create
    Answer: Destroy

35. Synonym of Victory
    Answer: Triumph

36. Antonym of Victory
    Answer: Defeat

37. Synonym of Friend
    Answer: Companion

38. Antonym of Friend
    Answer: Enemy

39. Synonym of Increase
    Answer: Grow

40. Antonym of Increase
    Answer: Decrease

41. Synonym of Active
    Answer: Energetic

42. Antonym of Active
    Answer: Lazy

43. Synonym of Famous
    Answer: Popular

44. Antonym of Famous
    Answer: Unknown

45. Synonym of Freedom
    Answer: Liberty

46. Antonym of Freedom
    Answer: Slavery

47. Synonym of Strongly
    Answer: Firmly

48. Antonym of Strongly
    Answer: Weakly

49. Synonym of Calm
    Answer: Peaceful

50. Antonym of Calm
    Answer: Disturbed

# 3. Sentence Correction (50 Questions)

1. She go to school daily.
   Answer: She goes to school daily.

2. He have a car.
   Answer: He has a car.

3. I am knowing the answer.
   Answer: I know the answer.

4. They was playing.
   Answer: They were playing.

5. She do not like tea.
   Answer: She does not like tea.

6. We is ready.
   Answer: We are ready.

7. He eat food.
   Answer: He eats food.

8. I has a pen.
   Answer: I have a pen.

9. She were happy.
   Answer: She was happy.

10. They enjoys cricket.
    Answer: They enjoy cricket.

11. He don't study.
    Answer: He doesn't study.

12. I goes to market.
    Answer: I go to market.

13. She have completed work.
    Answer: She has completed work.

14. We was late.
    Answer: We were late.

15. He do his homework.
    Answer: He does his homework.

16. They is dancing.
    Answer: They are dancing.

17. I were absent.
    Answer: I was absent.

18. She sing well.
    Answer: She sings well.

19. We has finished.
    Answer: We have finished.

20. He are my friend.
    Answer: He is my friend.

21. The boys is playing.
    Answer: The boys are playing.

22. She don't understand.
    Answer: She doesn't understand.

23. I has done it.
    Answer: I have done it.

24. They was happy.
    Answer: They were happy.

25. He write a letter.
    Answer: He writes a letter.

26. We is going.
    Answer: We are going.

27. She have a dog.
    Answer: She has a dog.

28. They goes there.
    Answer: They go there.

29. I am agree.
    Answer: I agree.

30. He were tired.
    Answer: He was tired.

31. She do her work.
    Answer: She does her work.

32. We has a house.
    Answer: We have a house.

33. They is late.
    Answer: They are late.

34. He go every day.
    Answer: He goes every day.

35. I were hungry.
    Answer: I was hungry.

36. She have many books.
    Answer: She has many books.

37. We was watching TV.
    Answer: We were watching TV.

38. He don't know.
    Answer: He doesn't know.

39. They enjoys music.
    Answer: They enjoy music.

40. She are absent.
    Answer: She is absent.

41. I has two brothers.
    Answer: I have two brothers.

42. We is friends.
    Answer: We are friends.

43. He do exercise.
    Answer: He does exercise.

44. They was sleeping.
    Answer: They were sleeping.

45. She don't sing.
    Answer: She doesn't sing.

46. I goes daily.
    Answer: I go daily.

47. He have a laptop.
    Answer: He has a laptop.

48. We was busy.
    Answer: We were busy.

49. They is coming.
    Answer: They are coming.

50. She write neatly.
    Answer: She writes neatly.

# 4. Error Detection (50 Questions)

1. He go to school.
   Answer: go -> goes

2. She do not sing.
   Answer: do -> does

3. They was late.
   Answer: was -> were

4. I has a pen.
   Answer: has -> have

5. We is friends.
   Answer: is -> are

6. He don't play.
   Answer: don't -> doesn't

7. She were happy.
   Answer: were -> was

8. They enjoys cricket.
   Answer: enjoys -> enjoy

9. I goes there.
   Answer: goes -> go

10. We was working.
    Answer: was -> were

11. She have books.
    Answer: have -> has

12. He are tall.
    Answer: are -> is

13. They is dancing.
    Answer: is -> are

14. I were absent.
    Answer: were -> was

15. She sing songs.
    Answer: sing -> sings

16. We has completed.
    Answer: has -> have

17. He do homework.
    Answer: do -> does

18. They was sleeping.
    Answer: was -> were

19. She don't know.
    Answer: don't -> doesn't

20. I has done work.
    Answer: has -> have

21. He write letters.
    Answer: write -> writes

22. We is going.
    Answer: is -> are

23. They goes home.
    Answer: goes -> go

24. She are my friend.
    Answer: are -> is

25. I were tired.
    Answer: were -> was

26. He have a bike.
    Answer: have -> has

27. We was ready.
    Answer: was -> were

28. They is late.
    Answer: is -> are

29. She do homework.
    Answer: do -> does

30. I goes daily.
    Answer: goes -> go

31. He don't study.
    Answer: don't -> doesn't

32. We has food.
    Answer: has -> have

33. They was happy.
    Answer: was -> were

34. She sing well.
    Answer: sing -> sings

35. I are ready.
    Answer: are -> am

36. He go every day.
    Answer: go -> goes

37. We is busy.
    Answer: is -> are

38. They enjoys music.
    Answer: enjoys -> enjoy

39. She have completed.
    Answer: have -> has

40. I were hungry.
    Answer: were -> was

41. He do not understand.
    Answer: do -> does

42. We was late.
    Answer: was -> were

43. They is absent.
    Answer: is -> are

44. She write neatly.
    Answer: write -> writes

45. I has many friends.
    Answer: has -> have

46. He were angry.
    Answer: were -> was

47. We goes together.
    Answer: goes -> go

48. They has books.
    Answer: has -> have

49. She don't dance.
    Answer: don't -> doesn't

50. I is correct.
    Answer: is -> am

# 5. Para Jumbles (50 Questions)

1. Arrange: (a) I woke up (b) I brushed teeth (c) I had breakfast
   Answer: a-b-c

2. (a) He studied (b) He passed (c) He got a job
   Answer: a-b-c

3. (a) Rain started (b) We opened umbrellas (c) We stayed dry
   Answer: a-b-c

4. (a) She cooked food (b) Family ate dinner (c) Everyone was happy
   Answer: a-b-c

5. (a) Train arrived (b) Passengers boarded (c) Train departed
   Answer: a-b-c

6. (a) Teacher entered (b) Students stood up (c) Class started
   Answer: a-b-c

7. (a) Alarm rang (b) He woke up (c) He got ready
   Answer: a-b-c

8. (a) Match began (b) Team played well (c) Team won
   Answer: a-b-c

9. (a) Child cried (b) Mother comforted (c) Child slept
   Answer: a-b-c

10. (a) Sun rose (b) Birds chirped (c) Morning began
    Answer: a-b-c

11. (a) He applied job (b) He attended interview (c) He got selected
    Answer: a-b-c

12. (a) Exam started (b) Students wrote answers (c) Exam ended
    Answer: a-b-c

13. (a) We bought tickets (b) We entered theatre (c) Movie started
    Answer: a-b-c

14. (a) Farmer sowed seeds (b) Plants grew (c) Crops harvested
    Answer: a-b-c

15. (a) Doctor checked patient (b) Medicine given (c) Patient recovered
    Answer: a-b-c

16. (a) He practiced daily (b) Skills improved (c) He succeeded
    Answer: a-b-c

17. (a) Cake baked (b) Guests arrived (c) Party started
    Answer: a-b-c

18. (a) Bell rang (b) Students left class (c) School closed
    Answer: a-b-c

19. (a) Phone rang (b) He answered call (c) Conversation started
    Answer: a-b-c

20. (a) Car stopped (b) Mechanic repaired (c) Car moved again
    Answer: a-b-c

# 6. Fill in the Blanks (50 Questions)

1. She ___ to school daily.
   Answer: goes

2. They ___ cricket every evening.
   Answer: play

3. He ___ a new car.
   Answer: has

4. I ___ my homework yesterday.
   Answer: completed

5. We ___ happy today.
   Answer: are

6. She ___ singing songs.
   Answer: likes

7. He ___ hard for exams.
   Answer: studies

8. They ___ watching TV.
   Answer: are

9. I ___ coffee every morning.
   Answer: drink

10. We ___ friends.
    Answer: are

11. She ___ English well.
    Answer: speaks

12. He ___ to market yesterday.
    Answer: went

13. They ___ football now.
    Answer: are playing

14. I ___ a letter yesterday.
    Answer: wrote

15. We ___ dinner together.
    Answer: had

16. She ___ very intelligent.
    Answer: is

17. He ___ the answer.
    Answer: knows

18. They ___ completed work.
    Answer: have

19. I ___ reading books.
    Answer: enjoy

20. We ___ the project successfully.
    Answer: finished

21. She ___ tea every morning.
    Answer: drinks

22. He ___ absent yesterday.
    Answer: was

23. They ___ to music.
    Answer: listen

24. I ___ my keys.
    Answer: lost

25. We ___ watching a movie.
    Answer: were

26. She ___ beautifully.
    Answer: dances

27. He ___ breakfast at 8 AM.
    Answer: eats

28. They ___ honest.
    Answer: are

29. I ___ tired yesterday.
    Answer: was

30. We ___ a good time.
    Answer: had

31. She ___ mathematics.
    Answer: teaches

32. He ___ swimming every Sunday.
    Answer: goes

33. They ___ preparing for exams.
    Answer: are

34. I ___ this book before.
    Answer: read

35. We ___ the answer.
    Answer: know

36. She ___ very fast.
    Answer: runs

37. He ___ his work carefully.
    Answer: does

38. They ___ lunch together.
    Answer: ate

39. I ___ the truth.
    Answer: know

40. We ___ football yesterday.
    Answer: played

41. She ___ happy with results.
    Answer: was

42. He ___ the window.
    Answer: opened

43. They ___ dancing now.
    Answer: are

44. I ___ milk daily.
    Answer: drink

45. We ___ to temple yesterday.
    Answer: went

46. She ___ a doctor.
    Answer: is

47. He ___ many books.
    Answer: has

48. They ___ for the bus.
    Answer: waited

49. I ___ learning English.
    Answer: am

50. We ___ proud of success.
    Answer: are
"""

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

topics = raw_text.strip().split('\n# ')

for topic_block in topics:
    if not topic_block.strip(): continue
    lines = topic_block.strip().split('\n')
    
    topic_header = lines[0].strip()
    if 'Reading Comprehension' in topic_header: key = 'ReadingComprehension'
    elif 'Synonyms & Antonyms' in topic_header: key = 'SynonymsAntonyms'
    elif 'Sentence Correction' in topic_header: key = 'SentenceCorrection'
    elif 'Error Detection' in topic_header: key = 'ErrorDetection'
    elif 'Para Jumbles' in topic_header: key = 'ParaJumbles'
    elif 'Fill in the Blanks' in topic_header: key = 'FillBlanks'
    else: continue
    
    parsed = []
    
    if key == 'ReadingComprehension':
        current_passage = ""
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line.startswith('## Passage'):
                # Extract paragraph
                current_passage = lines[i+1].strip()
                if not current_passage: current_passage = lines[i+2].strip()
            elif re.match(r'^\d+\.', line) and 'Answer:' in '\n'.join(lines[i:i+3]):
                q_text = re.sub(r'^\d+\.\s*', '', line)
                ans_line = [l for l in lines[i:i+3] if 'Answer:' in l][0]
                ans_text = ans_line.replace('Answer:', '').strip()
                
                # generate options
                opts = [ans_text]
                opts.extend(["Communication and growth", "Benefits of nature", "Other factors"])
                opts = list(set(opts))
                while len(opts) < 4:
                    opts.append(opts[0] + " variant")
                opts = opts[:4]
                random.shuffle(opts)
                
                parsed.append({
                    "q": f"<b>Passage:</b> {current_passage}<br><br><b>Question:</b> {q_text}",
                    "options": opts,
                    "ans": opts.index(ans_text),
                    "exp": "Found in the passage."
                })
    else:
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if re.match(r'^\d+\.', line):
                if '21-50' in line: continue # skip that weird para jumbles line
                q_text = re.sub(r'^\d+\.\s*', '', line)
                ans_text = ""
                # look for answer
                for j in range(i+1, min(i+4, len(lines))):
                    if lines[j].strip().startswith('Answer:'):
                        ans_text = lines[j].replace('Answer:', '').strip()
                        break
                        
                if ans_text:
                    opts = [ans_text]
                    if key == 'SynonymsAntonyms':
                        opts.extend(["Neutral", "Different", "Unrelated"])
                    elif key == 'SentenceCorrection':
                        opts.extend(["No correction needed", "Is incorrect grammatically", "Alternative phrasing"])
                    elif key == 'ErrorDetection':
                        opts.extend(["No error", "Subject verb mismatch", "Tense error"])
                    elif key == 'ParaJumbles':
                        opts.extend(["b-a-c", "c-b-a", "a-c-b"])
                    elif key == 'FillBlanks':
                        opts.extend(["is", "are", "was"])
                        
                    opts = list(set(opts))
                    while len(opts) < 4:
                        opts.append(opts[0] + " variant")
                    opts = opts[:4]
                    random.shuffle(opts)
                    
                    parsed.append({
                        "q": q_text,
                        "options": opts,
                        "ans": opts.index(ans_text),
                        "exp": "Correct English grammar/vocabulary."
                    })
    
    quizzes[key] = parsed
    print(f"Loaded {len(parsed)} questions into {key}")

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")
