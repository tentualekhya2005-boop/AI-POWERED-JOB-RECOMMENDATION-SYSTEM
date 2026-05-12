import json
import re

raw_text = """
1. Tell me about yourself.

Answer:
“I am a hardworking and motivated person who is eager to learn new things and improve my skills.”

2. What are your strengths?

Answer:
“My strengths are teamwork, quick learning, and positive thinking.”

3. What is your weakness?

Answer:
“I sometimes overthink my work, but I am learning to manage time better.”

4. Why should we hire you?

Answer:
“I am dedicated, willing to learn, and ready to give my best to the company.”

5. Where do you see yourself in 5 years?

Answer:
“I see myself in a good position with more knowledge and responsibilities.”

6. Why do you want this job?

Answer:
“I want this job to improve my skills and build my career.”

7. What motivates you?

Answer:
“Success and learning new things motivate me.”

8. Are you a team player?

Answer:
“Yes, I enjoy working with teams and sharing ideas.”

9. How do you handle pressure?

Answer:
“I stay calm and focus on completing the work step by step.”

10. What are your hobbies?

Answer:
“My hobbies are going to the gym, listening to music, and learning new skills.”

11. Describe yourself in one word.

Answer:
“Dedicated.”

12. What is your biggest achievement?

Answer:
“My biggest achievement is completing important tasks successfully with consistency.”

13. Are you willing to relocate?

Answer:
“Yes, I am open to relocation.”

14. Can you work under pressure?

Answer:
“Yes, I can manage pressure and complete work on time.”

15. How do you manage your time?

Answer:
“I plan my tasks based on priority and deadlines.”

16. What makes you unique?

Answer:
“My positive attitude and willingness to learn make me unique.”

17. How do you handle failure?

Answer:
“I learn from my mistakes and try to improve.”

18. What is your short-term goal?

Answer:
“My short-term goal is to gain experience and improve my skills.”

19. What is your long-term goal?

Answer:
“My long-term goal is to achieve a good position in my career.”

20. What do you know about our company?

Answer:
“I know your company is well known for its growth and work culture.”

21. Why do you want to join our company?

Answer:
“I want to grow professionally and learn from your organization.”

22. Can you work in shifts?

Answer:
“Yes, I am comfortable working in shifts.”

23. Are you comfortable with teamwork?

Answer:
“Yes, teamwork helps in better learning and productivity.”

24. What are your salary expectations?

Answer:
“I expect salary according to company standards.”

25. What do you do in your free time?

Answer:
“I spend my free time learning new things and relaxing with hobbies.”

26. How do you deal with criticism?

Answer:
“I take criticism positively and use it to improve myself.”

27. What is your dream job?

Answer:
“My dream job is one where I can learn and grow continuously.”

28. What kind of work environment do you prefer?

Answer:
“I prefer a positive and supportive work environment.”

29. What are your communication skills like?

Answer:
“I communicate clearly and respectfully with others.”

30. Are you comfortable learning new technologies?

Answer:
“Yes, I enjoy learning new technologies and skills.”

31. What is your leadership style?

Answer:
“I believe in supporting and motivating team members.”

32. How do you solve problems?

Answer:
“I analyze the situation carefully and find practical solutions.”

33. Do you prefer working alone or in a team?

Answer:
“I can work both independently and in a team.”

34. How quickly do you learn new things?

Answer:
“I am a quick learner and adapt easily.”

35. What are your expectations from this company?

Answer:
“I expect learning opportunities and career growth.”

36. What is your greatest challenge?

Answer:
“Managing multiple tasks at the same time was challenging, but I improved through planning.”

37. How do you stay motivated?

Answer:
“I stay motivated by setting goals and achieving them.”

38. What is your proudest moment?

Answer:
“My proudest moment is completing difficult tasks successfully.”

39. How do you handle disagreements?

Answer:
“I listen carefully and try to solve issues professionally.”

40. What are your future plans?

Answer:
“My future plans are to build a successful and stable career.”

41. What does success mean to you?

Answer:
“Success means achieving goals through hard work and consistency.”

42. How do you improve yourself?

Answer:
“I improve myself by learning from mistakes and practicing regularly.”

43. What inspires you?

Answer:
“Successful people and continuous learning inspire me.”

44. Are you confident?

Answer:
“Yes, I am confident in my ability to learn and work hard.”

45. What are your values?

Answer:
“My values are honesty, discipline, and respect.”

46. How do you react to challenges?

Answer:
“I see challenges as opportunities to learn.”

47. What is your biggest strength in teamwork?

Answer:
“My cooperation and communication skills help the team work smoothly.”

48. What do you expect from your manager?

Answer:
“I expect guidance, support, and opportunities to learn.”

49. How would your friends describe you?

Answer:
“My friends describe me as helpful and responsible.”

50. Do you have any questions for us?

Answer:
“Yes, what learning opportunities are available for freshers?”
"""

blocks = re.split(r'\n\d+\.\s', '\n' + raw_text.strip())
blocks = [b.strip() for b in blocks if b.strip()]

parsed_hr = []
for block in blocks:
    if 'Answer:' not in block: continue
    parts = block.split('Answer:')
    q_text = parts[0].strip()
    a_text = parts[1].strip().strip('“').strip('”').strip('"').strip()
    
    parsed_hr.append({
        "q": q_text,
        "a": a_text
    })

print(f"Loaded {len(parsed_hr)} HR questions.")

with open('static/interviewData.js', 'r') as f:
    content = f.read()

# Replace hr array
new_hr_json = json.dumps(parsed_hr, indent=4)
new_content = re.sub(r'hr:\s*\[.*?\](,\s*python:)', f'hr: {new_hr_json}\\1', content, flags=re.DOTALL)

with open('static/interviewData.js', 'w') as f:
    f.write(new_content)
