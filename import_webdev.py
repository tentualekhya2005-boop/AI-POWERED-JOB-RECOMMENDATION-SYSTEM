import json
import re

raw_text = """
1. What is web development?

Answer:
Web development is the process of creating websites and web applications.

2. What are the types of web development?

Answer:
Frontend, Backend, and Full Stack development.

3. What is HTML?

Answer:
HTML is a markup language used to create web pages.

4. What is CSS?

Answer:
CSS is used to style web pages.

5. What is JavaScript?

Answer:
JavaScript is used to make web pages interactive.

6. What is a webpage?

Answer:
A webpage is a document displayed in a web browser.

7. What is a website?

Answer:
A website is a collection of related web pages.

8. What is a browser?

Answer:
A browser is software used to access websites.

Examples: Google Chrome
, Mozilla Firefox

9. What is the difference between frontend and backend?

Answer:
Frontend is what users see; backend handles server and database operations.

10. What is responsive web design?

Answer:
Responsive design makes websites work on all screen sizes.

11. What is an HTML tag?

Answer:
HTML tags define webpage elements.

<h1>Hello</h1>
12. What is the use of <!DOCTYPE html>?

Answer:
It tells the browser the document type is HTML5.

13. What is a hyperlink?

Answer:
A hyperlink connects one webpage to another.

14. What is CSS used for?

Answer:
CSS controls colors, fonts, spacing, and layout.

15. What is inline CSS?

Answer:
CSS written inside an HTML tag.

16. What is internal CSS?

Answer:
CSS written inside the <style> tag.

17. What is external CSS?

Answer:
CSS written in a separate .css file.

18. What is an ID in CSS?

Answer:
An ID uniquely identifies an element.

19. What is a class in CSS?

Answer:
A class styles multiple elements.

20. What is JavaScript used for?

Answer:
JavaScript adds dynamic behavior to websites.

21. What is a variable in JavaScript?

Answer:
A variable stores data.

let x = 10;
22. What is a function in JavaScript?

Answer:
A function is a reusable block of code.

23. What is DOM?

Answer:
DOM (Document Object Model) represents webpage structure.

24. What is an event in JavaScript?

Answer:
An event is an action like click or keypress.

25. What is a form in HTML?

Answer:
A form collects user input.

26. What is GET method?

Answer:
GET sends data through URL.

27. What is POST method?

Answer:
POST sends data securely to the server.

28. What is Bootstrap?

Answer:
Bootstrap
 is a CSS framework used for responsive design.

29. What is React?

Answer:
React
 is a JavaScript library for building user interfaces.

30. What is Angular?

Answer:
Angular
 is a frontend framework for web applications.

31. What is Node.js?

Answer:
Node.js
 allows JavaScript to run on the server side.

32. What is Express.js?

Answer:
Express.js
 is a backend framework for Node.js.

33. What is a database?

Answer:
A database stores website data.

34. What is SQL?

Answer:
SQL is used to manage databases.

35. What is MySQL?

Answer:
MySQL
 is a relational database management system.

36. What is API?

Answer:
API allows communication between applications.

37. What is JSON?

Answer:
JSON is a lightweight data format.

{
  "name":"John"
}
38. What is Git?

Answer:
Git
 is a version control system.

39. What is GitHub?

Answer:
GitHub
 is a platform to store and manage code repositories.

40. What is hosting?

Answer:
Hosting makes websites available on the internet.

41. What is a domain name?

Answer:
A domain name is the website address.

Example: google.com

42. What is HTTP?

Answer:
HTTP is a protocol for transferring web data.

43. What is HTTPS?

Answer:
HTTPS is secure HTTP with encryption.

44. What is SEO?

Answer:
SEO improves website visibility in search engines.

45. What is debugging?

Answer:
Debugging means finding and fixing errors.

46. What is localhost?

Answer:
localhost refers to the local computer server.

47. What is deployment?

Answer:
Deployment means publishing a website online.

48. What is full stack development?

Answer:
Full stack development includes frontend and backend development.

49. What are frameworks?

Answer:
Frameworks provide pre-written code structure for development.

50. Why do you want to learn web development?

Answer:
“Web development helps create websites and applications used by people worldwide”
"""

blocks = re.split(r'\n(?=\d+\.\s)', '\n' + raw_text.strip())
blocks = [b.strip() for b in blocks if b.strip()]
parsed = []
for block in blocks:
    if 'Answer:' not in block: continue
    parts = block.split('Answer:')
    q_text = parts[0].strip()
    a_text = parts[1].strip()
    
    q_text = re.sub(r'^\d+\.\s*', '', q_text)
    if '\n' in a_text:
        a_text = a_text.replace('\n', '<br>')
        
    parsed.append({
        "q": q_text,
        "a": a_text
    })

print(f"Loaded {len(parsed)} Web Dev questions.")

with open('static/interviewData.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = json.dumps(parsed, indent=4)

m = re.search(r'(react:\s*)\[.*?\](,\s*sql:)', content, flags=re.DOTALL)
if m:
    content = content[:m.start(1)] + 'webdev: ' + json_str + m.group(2) + content[m.end(2):]

with open('static/interviewData.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved successfully!")
