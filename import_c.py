import json
import re

raw_text = """
1. What is C language?
Answer:
C is a procedural programming language used for system and application development.

2. Who developed C language?
Answer:
Dennis Ritchie developed C language.

3. What are the features of C?
Answer:
Simple, fast, portable, structured, and efficient.

4. What is a variable in C?
Answer:
A variable stores data values.
int x = 10;

5. What are data types in C?
Answer:
int, float, char, double, etc.

6. What is a keyword in C?
Answer:
Keywords are reserved words with special meanings.
Example: int, return, if.

7. What is a constant?
Answer:
A constant is a fixed value that cannot change.

8. What is printf()?
Answer:
printf() displays output on the screen.
printf("Hello");

9. What is scanf()?
Answer:
scanf() takes input from the user.

10. What is a function?
Answer:
A function is a reusable block of code.

11. What is main() function?
Answer:
main() is the starting point of a C program.

12. What is an operator?
Answer:
Operators perform operations on variables.

13. Types of operators in C?
Answer:
Arithmetic, relational, logical, assignment, etc.

14. What is an if statement?
Answer:
if statement is used for decision-making.

15. What is a loop?
Answer:
A loop repeats a block of code.

16. Types of loops in C?
Answer:
for loop, while loop, do-while loop.

17. What is a for loop?
Answer:
for(int i=0;i<5;i++){    printf("%d",i);}

18. What is a while loop?
Answer:
A while loop repeats while condition is true.

19. What is a do-while loop?
Answer:
Executes at least once before checking condition.

20. What is break statement?
Answer:
break exits the loop.

21. What is continue statement?
Answer:
continue skips current iteration.

22. What is an array?
Answer:
An array stores multiple values of same type.
int a[3]={1,2,3};

23. What is a string?
Answer:
A string is a collection of characters.

24. What is a pointer?
Answer:
A pointer stores the address of another variable.

25. What is NULL pointer?
Answer:
A pointer that points to nothing.

26. What is a structure?
Answer:
A structure groups different data types.

27. What is union in C?
Answer:
Union stores different data types in same memory location.

28. Difference between structure and union?
Answer:
Structure allocates separate memory; union shares memory.

29. What is recursion?
Answer:
A function calling itself is recursion.

30. What is a header file?
Answer:
Header files contain declarations and functions.
Example: stdio.h

31. What is #include?
Answer:
Used to include header files.

32. What is #define?
Answer:
Used to define constants or macros.

33. What is dynamic memory allocation?
Answer:
Allocating memory during runtime.

34. What are malloc() and calloc()?
Answer:
Functions used for dynamic memory allocation.

35. What is free()?
Answer:
free() releases allocated memory.

36. What is file handling?
Answer:
Used to read and write files.

37. What is fopen()?
Answer:
fopen() opens a file.

38. What is fclose()?
Answer:
fclose() closes a file.

39. What is EOF?
Answer:
EOF means End Of File.

40. What is a compiler?
Answer:
A compiler converts C code into machine code.

41. What is syntax error?
Answer:
An error caused by incorrect code syntax.

42. What is runtime error?
Answer:
An error occurring during execution.

43. What is logical error?
Answer:
An error causing incorrect output.

44. What is type casting?
Answer:
Converting one data type to another.
float x = (float)5/2;

45. What is call by value?
Answer:
Copies actual values into function parameters.

46. What is call by reference?
Answer:
Passes variable addresses to functions.

47. What is an infinite loop?
Answer:
A loop that never ends.

48. What is nested loop?
Answer:
A loop inside another loop.

49. Why is C language important?
Answer:
C is fast and forms the base for many programming languages.

50. Why do you want to learn C?
Answer:
“C helps understand programming fundamentals and system-level programming.”
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

print(f"Loaded {len(parsed)} C questions.")

with open('static/interviewData.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = json.dumps(parsed, indent=4)

# Insert c block after java
m = re.search(r'(java:\s*\[.*?\](,\s*))', content, flags=re.DOTALL)
if m:
    content = content[:m.end()] + 'c: ' + json_str + ',\n    ' + content[m.end():]

with open('static/interviewData.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved successfully!")
