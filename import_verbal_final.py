import json
import re
import random

raw_text = """
Para Jumbles – 50 Practice Questions
1.

Arrange the sentences:

A. He finally reached the station.
B. Ravi woke up late in the morning.
C. He missed the first bus.
D. Therefore, he had to take an auto.

Options:
a) B-C-D-A
b) B-C-A-D
c) C-B-D-A
d) B-D-C-A

Answer: a) B-C-D-A

2.

A. The rain stopped suddenly.
B. Children came out to play.
C. Dark clouds covered the sky.
D. Everyone rushed indoors.

Options:
a) C-D-A-B
b) A-B-C-D
c) C-A-D-B
d) D-C-B-A

Answer: a) C-D-A-B

3.

A. She prepared well for the exam.
B. She scored the highest marks.
C. Her teachers appreciated her effort.
D. She studied every day.

Options:
a) D-A-B-C
b) A-D-B-C
c) D-B-A-C
d) B-C-D-A

Answer: a) D-A-B-C

4.

A. The baby started crying loudly.
B. The mother picked him up.
C. He became silent immediately.
D. The room was very noisy.

Options:
a) D-A-B-C
b) A-B-C-D
c) D-B-A-C
d) A-D-B-C

Answer: a) D-A-B-C

5.

A. The teacher entered the classroom.
B. Students stood up respectfully.
C. The lesson began immediately.
D. Everyone was talking loudly.

Options:
a) D-A-B-C
b) A-D-B-C
c) B-A-D-C
d) D-B-A-C

Answer: a) D-A-B-C

6.

A. The electricity went off.
B. We lit some candles.
C. The entire street became dark.
D. After an hour, power returned.

Answer: A-C-B-D

7.

A. Priya planted a sapling.
B. She watered it daily.
C. It grew into a healthy tree.
D. Birds started sitting on it.

Answer: A-B-C-D

8.

A. The dog barked continuously.
B. A stranger was standing near the gate.
C. The owner came outside.
D. The stranger walked away.

Answer: B-A-C-D

9.

A. The shopkeeper opened the store early.
B. Customers started arriving soon.
C. Business was excellent that day.
D. He was very happy in the evening.

Answer: A-B-C-D

10.

A. The train arrived late.
B. Passengers became impatient.
C. Announcements were made repeatedly.
D. Finally, the journey started.

Answer: A-C-B-D

11.

A. The match was very exciting.
B. Our team won in the last over.
C. Fans cheered loudly.
D. Players celebrated together.

Answer: A-B-C-D

12.

A. Tina bought new books.
B. She covered them neatly.
C. Then she arranged them on the shelf.
D. Her room looked organized.

Answer: A-B-C-D

13.

A. The old bridge was damaged.
B. Heavy rains caused flooding.
C. Vehicles could not cross the river.
D. Authorities planned repairs.

Answer: B-A-C-D

14.

A. Mohan practiced football daily.
B. His skills improved greatly.
C. He was selected for the school team.
D. His parents felt proud.

Answer: A-B-C-D

15.

A. The librarian issued the book.
B. Rani searched every shelf carefully.
C. She finally found the novel.
D. She thanked the librarian.

Answer: B-C-A-D

16.

A. The farmer sowed seeds.
B. Rainfall was sufficient that year.
C. Crops grew very well.
D. The harvest was excellent.

Answer: A-B-C-D

17.

A. A loud noise was heard outside.
B. Everyone looked out of the window.
C. A tree had fallen on the road.
D. Traffic stopped for some time.

Answer: A-B-C-D

18.

A. The chef prepared delicious food.
B. Guests enjoyed the dinner party.
C. Everyone praised the dishes.
D. The host felt satisfied.

Answer: A-B-C-D

19.

A. Neha forgot her umbrella.
B. It started raining heavily.
C. She got completely wet.
D. Her friend offered help.

Answer: A-B-C-D

20.

A. The museum was crowded.
B. Visitors admired the paintings.
C. Guides explained the history.
D. Children asked many questions.

Answer: A-B-C-D

21.

A. The athlete trained hard every morning.
B. He participated in the marathon.
C. He finished the race successfully.
D. Everyone applauded his effort.

Answer: A-B-C-D

22.

A. The internet connection stopped working.
B. Students could not attend online classes.
C. The technician repaired the issue.
D. Classes resumed normally.

Answer: A-B-C-D

23.

A. A new mall opened in town.
B. Many people visited it on the first day.
C. Shops offered huge discounts.
D. Customers bought many products.

Answer: A-B-C-D

24.

A. The child learned cycling slowly.
B. He fell several times.
C. His father encouraged him.
D. Soon he rode confidently.

Answer: A-B-C-D

25.

A. The classroom was untidy.
B. Students cleaned it together.
C. Desks were arranged properly.
D. The teacher appreciated them.

Answer: A-B-C-D

26.

A. The sun was setting beautifully.
B. Birds returned to their nests.
C. Cool winds started blowing.
D. The evening looked peaceful.

Answer: A-B-C-D

27.

A. The doctor examined the patient carefully.
B. Medicines were prescribed.
C. The patient followed the instructions.
D. He recovered quickly.

Answer: A-B-C-D

28.

A. The car suddenly stopped on the highway.
B. The driver checked the engine.
C. A mechanic arrived after some time.
D. The problem was fixed.

Answer: A-B-C-D

29.

A. The principal announced a holiday.
B. Students shouted with joy.
C. Teachers smiled at their excitement.
D. Everyone left happily.

Answer: A-B-C-D

30.

A. The scientist conducted an experiment.
B. Data was recorded carefully.
C. The results were analyzed.
D. A report was published later.

Answer: A-B-C-D

31.

A. The cinema hall was full.
B. The movie started on time.
C. People enjoyed the action scenes.
D. They clapped at the end.

Answer: A-B-C-D

32.

A. The gardener removed weeds.
B. He planted colorful flowers.
C. The garden looked beautiful.
D. Visitors took photographs.

Answer: A-B-C-D

33.

A. A seminar was organized in college.
B. Experts delivered lectures.
C. Students asked interesting questions.
D. Everyone gained knowledge.

Answer: A-B-C-D

34.

A. The boy saved money regularly.
B. He bought a bicycle after a few months.
C. He rode it happily every evening.
D. His friends admired it.

Answer: A-B-C-D

35.

A. The police received a complaint.
B. An investigation was started immediately.
C. Evidence was collected carefully.
D. The case was solved.

Answer: A-B-C-D

36.

A. The teacher explained the concept clearly.
B. Students listened attentively.
C. They solved the problems easily.
D. Everyone understood the lesson.

Answer: A-B-C-D

37.

A. The river water rose dangerously.
B. Villagers moved to safer places.
C. Rescue teams arrived quickly.
D. Many lives were saved.

Answer: A-B-C-D

38.

A. The company launched a new product.
B. Advertisements appeared everywhere.
C. Customers showed great interest.
D. Sales increased rapidly.

Answer: A-B-C-D

39.

A. The student forgot his admit card.
B. He became nervous before the exam.
C. His friend helped him find it.
D. He entered the hall on time.

Answer: A-B-C-D

40.

A. The mountain path was difficult.
B. Climbers continued their journey carefully.
C. They finally reached the top.
D. The view was breathtaking.

Answer: A-B-C-D

41.

A. The school organized a cultural program.
B. Students performed dances and songs.
C. Parents enjoyed the performances.
D. The event ended successfully.

Answer: A-B-C-D

42.

A. The waiter served hot coffee.
B. Friends chatted happily in the café.
C. Soft music played in the background.
D. They spent a pleasant evening.

Answer: A-C-B-D

43.

A. The laptop battery was low.
B. Rahul searched for a charger.
C. He plugged it in quickly.
D. He continued his work.

Answer: A-B-C-D

44.

A. The passengers boarded the airplane.
B. Safety instructions were announced.
C. The flight took off smoothly.
D. Everyone relaxed during the journey.

Answer: A-B-C-D

45.

A. The baker prepared a chocolate cake.
B. Delicious smell filled the bakery.
C. Customers entered eagerly.
D. Cakes were sold quickly.

Answer: A-B-C-D

46.

A. The students visited a science exhibition.
B. They observed many innovative projects.
C. Teachers explained the working models.
D. Students felt inspired.

Answer: A-B-C-D

47.

A. The singer entered the stage.
B. The audience applauded loudly.
C. She performed beautifully.
D. Everyone enjoyed the concert.

Answer: A-B-C-D

48.

A. The worker repaired the machine.
B. Factory operations resumed.
C. Production increased again.
D. The manager appreciated the effort.

Answer: A-B-C-D

49.

A. The children decorated the classroom.
B. Balloons and lights were arranged.
C. The birthday celebration began.
D. Everyone had fun.

Answer: A-B-C-D

50.

A. The team discussed the project plan.
B. Tasks were divided among members.
C. Everyone completed the work on time.
D. The project became successful.

Answer: A-B-C-D

Fill in the Blanks – 50 Questions
1.
She ______ to school every day.
a) go
b) goes
c) going
d) gone
Answer: b) goes

2.
The sun ______ in the east.
a) rise
b) rises
c) rising
d) rose
Answer: b) rises

3.
They ______ football yesterday.
a) play
b) played
c) playing
d) plays
Answer: b) played

4.
I have ______ my homework.
a) complete
b) completed
c) completing
d) completes
Answer: b) completed

5.
He is fond ______ music.
a) in
b) on
c) of
d) for
Answer: c) of

6.
Ravi and Raju ______ best friends.
a) is
b) are
c) was
d) be
Answer: b) are

7.
She was absent ______ class yesterday.
a) from
b) in
c) at
d) on
Answer: a) from

8.
The train arrived ______ time.
a) in
b) on
c) at
d) by
Answer: b) on

9.
I prefer tea ______ coffee.
a) than
b) over
c) to
d) from
Answer: c) to

10.
He worked hard ______ he could succeed.
a) because
b) so that
c) although
d) unless
Answer: b) so that

11.
The baby is sleeping ______.
a) peaceful
b) peacefully
c) peace
d) peacefulness
Answer: b) peacefully

12.
Neither the teacher nor the students ______ present.
a) was
b) were
c) is
d) be
Answer: b) were

13.
She speaks English ______ than her brother.
a) good
b) best
c) better
d) well
Answer: c) better

14.
I ______ him two years ago.
a) meet
b) met
c) meeting
d) meets
Answer: b) met

15.
The book is ______ the table.
a) in
b) on
c) under
d) beside
Answer: b) on

16.
We should always speak the ______.
a) true
b) truth
c) truly
d) truthful
Answer: b) truth

17.
The weather is very hot ______ summer.
a) at
b) on
c) in
d) by
Answer: c) in

18.
My father ______ a doctor.
a) are
b) is
c) were
d) have
Answer: b) is

19.
He did not ______ the answer.
a) knew
b) know
c) known
d) knowing
Answer: b) know

20.
The students listened to the lecture ______.
a) attentive
b) attentively
c) attention
d) attend
Answer: b) attentively

21.
She is one of the ______ students in the class.
a) intelligent
b) more intelligent
c) most intelligent
d) intelligence
Answer: c) most intelligent

22.
The cat jumped ______ the wall.
a) over
b) under
c) between
d) beside
Answer: a) over

23.
He has been working here ______ 2020.
a) for
b) since
c) from
d) by
Answer: b) since

24.
I am interested ______ reading novels.
a) on
b) in
c) at
d) for
Answer: b) in

25.
They ______ already completed the project.
a) has
b) have
c) had
d) having
Answer: b) have

26.
The teacher asked the students to keep ______.
a) silent
b) silence
c) silently
d) silencing
Answer: a) silent

27.
If it rains, we ______ stay at home.
a) would
b) will
c) shall have
d) had
Answer: b) will

28.
He is taller ______ his brother.
a) then
b) than
c) from
d) to
Answer: b) than

29.
Please give me ______ water.
a) few
b) little
c) some
d) many
Answer: c) some

30.
The Earth ______ around the Sun.
a) revolve
b) revolves
c) revolved
d) revolving
Answer: b) revolves

31.
She was tired ______ she continued working.
a) but
b) because
c) if
d) unless
Answer: a) but

32.
I have never ______ such a beautiful place.
a) seen
b) saw
c) see
d) seeing
Answer: a) seen

33.
The boy ran ______ to catch the bus.
a) quick
b) quickly
c) quickest
d) quicker
Answer: b) quickly

34.
Would you like ______ cup of tea?
a) a
b) an
c) the
d) some
Answer: a) a

35.
The news ______ shocking.
a) were
b) are
c) was
d) have
Answer: c) was

36.
He succeeded because he worked very ______.
a) hard
b) hardly
c) harder
d) hardest
Answer: a) hard

37.
There are ______ apples in the basket.
a) much
b) little
c) many
d) less
Answer: c) many

38.
The meeting will start ______ 10 a.m.
a) on
b) in
c) at
d) by
Answer: c) at

39.
She ______ watching television now.
a) is
b) are
c) were
d) have
Answer: a) is

40.
We must protect nature ______ pollution.
a) from
b) with
c) by
d) into
Answer: a) from

41.
He is absent because he is suffering ______ fever.
a) with
b) from
c) by
d) at
Answer: b) from

42.
The teacher praised him ______ his honesty.
a) for
b) with
c) on
d) at
Answer: a) for

43.
Neither Ram nor Shyam ______ coming today.
a) are
b) were
c) is
d) have
Answer: c) is

44.
This road is ______ than that one.
a) narrow
b) narrower
c) narrowest
d) narrowly
Answer: b) narrower

45.
The children were playing ______ the garden.
a) in
b) on
c) at
d) by
Answer: a) in

46.
He apologized ______ being late.
a) of
b) with
c) for
d) at
Answer: c) for

47.
She has lived here ______ five years.
a) since
b) for
c) from
d) by
Answer: b) for

48.
The police ______ investigating the case.
a) is
b) are
c) was
d) has
Answer: b) are

49.
Everyone ______ the answer correctly.
a) know
b) knows
c) knowing
d) knew
Answer: b) knows

50.
The students were happy ______ the results.
a) with
b) at
c) for
d) by
Answer: a) with
"""

# Extract the two sections
para_match = re.search(r'Para Jumbles – 50 Practice Questions(.*?)Fill in the Blanks – 50 Questions', raw_text, re.DOTALL)
fill_match = re.search(r'Fill in the Blanks – 50 Questions(.*)', raw_text, re.DOTALL)

para_text = para_match.group(1) if para_match else ""
fill_text = fill_match.group(1) if fill_match else ""

def parse_para(text):
    blocks = re.split(r'\n\d+\.\n', '\n' + text.strip())
    blocks = [b.strip() for b in blocks if b.strip()]
    parsed = []
    
    for block in blocks:
        lines = block.split('\n')
        ans_line = [l for l in lines if l.startswith('Answer:')]
        if not ans_line: continue
        ans_text = ans_line[0].replace('Answer:', '').strip()
        
        actual_ans = ans_text
        if ') ' in ans_text:
            actual_ans = ans_text.split(') ')[1].strip()
            
        opt_lines = [l for l in lines if l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)')]
        
        q_text = "\n".join([l for l in lines if not l.startswith('Answer:') and not l.startswith('Options:') and not (l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)'))]).strip()
        q_text = q_text.replace('\n', '<br>')
        
        opts = []
        if opt_lines:
            for ol in opt_lines:
                opts.append(ol.split(')')[1].strip())
        else:
            opts = [actual_ans]
            opts.extend(['A-B-C-D', 'D-C-B-A', 'B-A-C-D', 'C-B-D-A', 'A-C-B-D'])
            opts = list(set(opts))
            if actual_ans in opts: opts.remove(actual_ans)
            opts = [actual_ans] + opts[:3]
            
        opts = list(set(opts))
        while len(opts) < 4:
            opts.append(opts[0] + " variant")
        opts = opts[:4]
        if actual_ans not in opts: opts[0] = actual_ans
        
        random.shuffle(opts)
        
        parsed.append({
            "q": q_text,
            "options": opts,
            "ans": opts.index(actual_ans),
            "exp": "Arranged in a logical sequence."
        })
    return parsed

def parse_fill(text):
    blocks = re.split(r'\n\d+\.\n', '\n' + text.strip())
    blocks = [b.strip() for b in blocks if b.strip()]
    parsed = []
    
    for block in blocks:
        lines = block.split('\n')
        ans_line = [l for l in lines if l.startswith('Answer:')]
        if not ans_line: continue
        ans_text = ans_line[0].replace('Answer:', '').strip()
        
        actual_ans = ans_text
        if ') ' in ans_text:
            actual_ans = ans_text.split(') ')[1].strip()
            
        q_text = "\n".join([l for l in lines if not l.startswith('Answer:') and not (l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)'))]).strip()
        q_text = q_text.replace('\n', '<br>')
        
        opt_lines = [l for l in lines if l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)')]
        opts = []
        if opt_lines:
            for ol in opt_lines:
                opts.append(ol.split(')')[1].strip())
        else:
            opts = [actual_ans, actual_ans+"ed", actual_ans+"s", actual_ans+"ing"]
            
        opts = list(set(opts))
        while len(opts) < 4:
            opts.append(opts[0] + " variant")
        opts = opts[:4]
        if actual_ans not in opts: opts[0] = actual_ans
        
        random.shuffle(opts)
        
        parsed.append({
            "q": q_text,
            "options": opts,
            "ans": opts.index(actual_ans),
            "exp": "Grammatically appropriate choice."
        })
    return parsed

with open('static/massiveQuizData.js', 'r') as f:
    content = f.read()

json_str = content.replace('const massiveQuizData = ', '').rstrip().rstrip(';')
quizzes = json.loads(json_str)

para_parsed = parse_para(para_text)
fill_parsed = parse_fill(fill_text)

quizzes['ParaJumbles'] = para_parsed
quizzes['FillBlanks'] = fill_parsed

with open('static/massiveQuizData.js', 'w') as f:
    f.write("const massiveQuizData = " + json.dumps(quizzes) + ";\n")

print(f"Loaded {len(para_parsed)} questions into ParaJumbles")
print(f"Loaded {len(fill_parsed)} questions into FillBlanks")
