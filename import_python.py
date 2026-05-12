import json
import re

raw_text = """
1. What is Python?

Answer:
Python is a high-level, interpreted programming language known for its simplicity and readability.

2. Who developed Python?

Answer:
Guido van Rossum developed Python.

3. What are the features of Python?

Answer:
Easy syntax, interpreted language, object-oriented, portable, and open-source.

4. Is Python compiled or interpreted?

Answer:
Python is an interpreted language.

5. What is a variable in Python?

Answer:
A variable is used to store data values.

x = 10
6. What are data types in Python?

Answer:
int, float, string, list, tuple, set, and dictionary.

7. What is a list?

Answer:
A list is an ordered and mutable collection.

a = [1, 2, 3]
8. What is a tuple?

Answer:
A tuple is an ordered and immutable collection.

t = (1, 2, 3)
9. What is a dictionary?

Answer:
A dictionary stores data in key-value pairs.

d = {"name":"Ram"}
10. What is a set?

Answer:
A set is an unordered collection of unique elements.

11. Difference between list and tuple?

Answer:
Lists are mutable; tuples are immutable.

12. What is indentation in Python?

Answer:
Indentation defines blocks of code in Python.

13. What is a function?

Answer:
A function is a reusable block of code.

def add():
    print("Hello")
14. What is a loop?

Answer:
A loop repeats a block of code.

15. What is a for loop?

Answer:

for i in range(5):
    print(i)
16. What is a while loop?

Answer:

while True:
    break
17. What is a conditional statement?

Answer:
Used for decision-making using if, else, and elif.

18. What is OOP in Python?

Answer:
Object-Oriented Programming is based on classes and objects.

19. What is a class?

Answer:
A class is a blueprint for creating objects.

20. What is an object?

Answer:
An object is an instance of a class.

21. What is inheritance?

Answer:
Inheritance allows one class to use properties of another class.

22. What is polymorphism?

Answer:
Polymorphism allows methods to behave differently.

23. What is encapsulation?

Answer:
Encapsulation hides data inside a class.

24. What is abstraction?

Answer:
Abstraction hides implementation details.

25. What is a module?

Answer:
A module is a file containing Python code.

26. What is a package?

Answer:
A package is a collection of modules.

27. What is pip?

Answer:
pip is a package manager for Python.

28. What is NumPy?

Answer:
NumPy
 is a library for numerical operations.

29. What is Pandas?

Answer:
Pandas
 is a library for data analysis.

30. What is Matplotlib?

Answer:
Matplotlib
 is used for data visualization.

31. What is an exception?

Answer:
An exception is an error that occurs during execution.

32. What is try-except?

Answer:
Used for exception handling.

try:
    x = 1/0
except:
    print("Error")
33. What is recursion?

Answer:
A function calling itself is called recursion.

34. What is lambda function?

Answer:
A small anonymous function.

x = lambda a:a+1
35. What is slicing?

Answer:
Slicing extracts parts of sequences.

a = [1,2,3]
print(a[0:2])
36. What is type conversion?

Answer:
Changing one data type to another.

x = int("5")
37. What is file handling?

Answer:
Reading and writing files in Python.

38. What is open() function?

Answer:
Used to open files.

f = open("a.txt","r")
39. What is append()?

Answer:
Adds an element to a list.

40. What is len()?

Answer:
Returns the length of an object.

41. What is range()?

Answer:
Generates a sequence of numbers.

42. What is init()?

Answer:
A constructor method in Python classes.

43. What is self in Python?

Answer:
self refers to the current object.

44. Difference between == and is?

Answer:
== compares values; is compares memory locations.

45. What is pass statement?

Answer:
pass is a null statement.

46. What is break statement?

Answer:
break exits the loop.

47. What is continue statement?

Answer:
continue skips the current iteration.

48. What is Python used for?

Answer:
Web development, AI, data science, automation, and software development.

49. Why is Python popular?

Answer:
Because it is easy to learn and has many libraries.

50. Why do you want to learn Python?

Answer:
“Python is powerful, simple, and useful for many technologies like data science and AI.”
"""

blocks = re.split(r'\n(?=\d+\.\s)', '\n' + raw_text.strip())
blocks = [b.strip() for b in blocks if b.strip()]

parsed_python = []
for block in blocks:
    if 'Answer:' not in block: continue
    parts = block.split('Answer:')
    q_text = parts[0].strip()
    a_text = parts[1].strip()
    
    q_text = re.sub(r'^\d+\.\s*', '', q_text)
    
    # Format code blocks nicely
    if '\n' in a_text:
        # Wrap the whole answer in standard formatting but preserve newlines
        a_text = a_text.replace('\n', '<br>')
        
    parsed_python.append({
        "q": q_text,
        "a": a_text
    })

print(f"Loaded {len(parsed_python)} Python questions.")

with open('static/interviewData.js', 'r') as f:
    content = f.read()

new_python_json = json.dumps(parsed_python, indent=4)
new_content = re.sub(r'python:\s*\[.*?\](,\s*java:)', f'python: {new_python_json}\\1', content, flags=re.DOTALL)

with open('static/interviewData.js', 'w') as f:
    f.write(new_content)
