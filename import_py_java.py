import json
import re

python_raw = """
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

java_raw = """
1. What is Java?

Answer:
Java is a high-level, object-oriented programming language.

2. Who developed Java?

Answer:
James Gosling developed Java.

3. What are the features of Java?

Answer:
Platform independent, object-oriented, secure, robust, and portable.

4. What is JVM?

Answer:
JVM (Java Virtual Machine) runs Java programs.

5. What is JDK?

Answer:
JDK (Java Development Kit) provides tools to develop Java applications.

6. What is JRE?

Answer:
JRE (Java Runtime Environment) provides libraries and JVM to run Java programs.

7. Difference between JDK, JRE, and JVM?

Answer:
JDK → Development tools
JRE → Runtime environment
JVM → Executes Java bytecode

8. What is a class in Java?

Answer:
A class is a blueprint for creating objects.

class Student {
}
9. What is an object?

Answer:
An object is an instance of a class.

10. What is OOP?

Answer:
OOP stands for Object-Oriented Programming.

11. What are the pillars of OOP?

Answer:
Encapsulation, inheritance, polymorphism, and abstraction.

12. What is inheritance?

Answer:
Inheritance allows one class to acquire properties of another class.

13. What is polymorphism?

Answer:
Polymorphism allows methods to perform different actions.

14. What is encapsulation?

Answer:
Encapsulation binds data and methods together.

15. What is abstraction?

Answer:
Abstraction hides implementation details.

16. What is a constructor?

Answer:
A constructor initializes objects.

Student() {
}
17. What is method overloading?

Answer:
Using same method name with different parameters.

18. What is method overriding?

Answer:
Redefining a parent class method in child class.

19. What is static keyword?

Answer:
static belongs to the class, not objects.

20. What is final keyword?

Answer:
final prevents modification.

21. What is this keyword?

Answer:
this refers to the current object.

22. What is super keyword?

Answer:
super refers to the parent class object.

23. What is an interface?

Answer:
An interface contains abstract methods.

24. What is an abstract class?

Answer:
An abstract class cannot be instantiated.

25. Difference between abstract class and interface?

Answer:
Abstract class can have normal methods; interface mainly contains abstract methods.

26. What is exception handling?

Answer:
Handling runtime errors using try-catch blocks.

try {
}
catch(Exception e) {
}
27. What is try-catch?

Answer:
Used to handle exceptions.

28. What is finally block?

Answer:
finally executes whether exception occurs or not.

29. What is multithreading?

Answer:
Executing multiple threads simultaneously.

30. What is thread?

Answer:
A thread is a lightweight process.

31. What is synchronization?

Answer:
Synchronization prevents data inconsistency.

32. What is array in Java?

Answer:
Array stores multiple values of same type.

int a[] = {1,2,3};
33. What is String in Java?

Answer:
String is a sequence of characters.

34. Difference between == and equals()?

Answer:
== compares references; equals() compares values.

35. What is package in Java?

Answer:
A package is a collection of classes.

36. What is access modifier?

Answer:
Controls visibility of variables and methods.

37. Types of access modifiers?

Answer:
public, private, protected, default.

38. What is collection framework?

Answer:
Collection framework provides classes for storing data.

39. What is ArrayList?

Answer:
ArrayList is a dynamic array.

40. What is HashMap?

Answer:
HashMap stores key-value pairs.

41. What is LinkedList?

Answer:
LinkedList stores elements using linked nodes.

42. What is loop in Java?

Answer:
Loops repeat code execution.

43. Types of loops in Java?

Answer:
for loop, while loop, do-while loop.

44. What is break statement?

Answer:
break exits the loop.

45. What is continue statement?

Answer:
continue skips current iteration.

46. What is garbage collection?

Answer:
Garbage collection removes unused objects from memory.

47. Why is Java platform independent?

Answer:
Because Java uses bytecode executed by JVM.

48. What is bytecode?

Answer:
Intermediate code generated after compilation.

49. What is Java used for?

Answer:
Web applications, Android apps, enterprise software, and backend systems.

50. Why do you want to learn Java?

Answer:
“Java is powerful, secure, and widely used in software development.”
"""

def parse_blocks(raw_text):
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
    return parsed

python_data = parse_blocks(python_raw)
java_data = parse_blocks(java_raw)

print(f"Loaded {len(python_data)} Python questions.")
print(f"Loaded {len(java_data)} Java questions.")

with open('static/interviewData.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace using index and string slicing to avoid any regex grouping issues with literal escapes
import json

python_json = json.dumps(python_data, indent=4)
java_json = json.dumps(java_data, indent=4)

# Replace python block
# Find python: [ ... ], java:
m1 = re.search(r'(python:\s*)\[.*?\](,\s*java:)', content, flags=re.DOTALL)
if m1:
    content = content[:m1.start(1)] + m1.group(1) + python_json + m1.group(2) + content[m1.end(2):]

# Replace java block
# Find java: [ ... ], react:
m2 = re.search(r'(java:\s*)\[.*?\](,\s*react:)', content, flags=re.DOTALL)
if m2:
    content = content[:m2.start(1)] + m2.group(1) + java_json + m2.group(2) + content[m2.end(2):]

with open('static/interviewData.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved to interviewData.js successfully!")
