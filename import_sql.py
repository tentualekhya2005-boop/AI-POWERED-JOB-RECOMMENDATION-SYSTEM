import json
import re

raw_text = """
1. What is DBMS?

Answer:
DBMS (Database Management System) is software used to store, manage, and retrieve data.

2. What is a database?

Answer:
A database is an organized collection of data.

3. What are the advantages of DBMS?

Answer:
Data security, reduced redundancy, easy access, and backup support.

4. What is RDBMS?

Answer:
RDBMS (Relational DBMS) stores data in tables.

Examples: MySQL
, Oracle Database

5. Difference between DBMS and RDBMS?

Answer:
DBMS stores data generally, while RDBMS stores data in related tables.

6. What is a table?

Answer:
A table stores data in rows and columns.

7. What is a row?

Answer:
A row represents a single record in a table.

8. What is a column?

Answer:
A column represents an attribute of data.

9. What is a primary key?

Answer:
A primary key uniquely identifies each record.

10. What is a foreign key?

Answer:
A foreign key connects two tables.

11. What is SQL?

Answer:
SQL (Structured Query Language) is used to manage databases.

12. What are SQL commands?

Answer:
DDL, DML, DCL, and TCL commands.

13. What is DDL?

Answer:
DDL (Data Definition Language) defines database structure.

Examples: CREATE, ALTER, DROP.

14. What is DML?

Answer:
DML (Data Manipulation Language) manages data.

Examples: INSERT, UPDATE, DELETE.

15. What is DCL?

Answer:
DCL (Data Control Language) controls permissions.

Examples: GRANT, REVOKE.

16. What is TCL?

Answer:
TCL (Transaction Control Language) manages transactions.

Examples: COMMIT, ROLLBACK.

17. What is normalization?

Answer:
Normalization reduces data redundancy.

18. What is denormalization?

Answer:
Denormalization combines tables to improve performance.

19. What is 1NF?

Answer:
1NF removes repeating groups and ensures atomic values.

20. What is 2NF?

Answer:
2NF removes partial dependency.

21. What is 3NF?

Answer:
3NF removes transitive dependency.

22. What is BCNF?

Answer:
BCNF is an advanced form of normalization.

23. What is a candidate key?

Answer:
A candidate key can uniquely identify records.

24. What is a super key?

Answer:
A super key uniquely identifies rows.

25. What is an alternate key?

Answer:
Candidate keys not selected as primary key.

26. What is a composite key?

Answer:
A key made of multiple columns.

27. What is NULL value?

Answer:
NULL means no value or unknown value.

28. What is a constraint?

Answer:
Constraints apply rules to table columns.

29. Types of constraints?

Answer:
NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK.

30. What is a query?

Answer:
A query requests data from the database.

31. What is SELECT statement?

Answer:
SELECT retrieves data from tables.

SELECT * FROM student;
32. What is WHERE clause?

Answer:
WHERE filters records.

33. What is ORDER BY?

Answer:
ORDER BY sorts records.

34. What is GROUP BY?

Answer:
GROUP BY groups rows with same values.

35. What is JOIN?

Answer:
JOIN combines data from multiple tables.

36. Types of joins?

Answer:
INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN.

37. What is INNER JOIN?

Answer:
Returns matching records from both tables.

38. What is LEFT JOIN?

Answer:
Returns all left table records and matching right table records.

39. What is index?

Answer:
An index improves data retrieval speed.

40. What is view?

Answer:
A view is a virtual table.

41. What is stored procedure?

Answer:
A stored procedure is a saved SQL program.

42. What is trigger?

Answer:
A trigger automatically executes on database events.

43. What is transaction?

Answer:
A transaction is a sequence of database operations.

44. What are ACID properties?

Answer:
Atomicity, Consistency, Isolation, Durability.

45. What is commit?

Answer:
COMMIT permanently saves changes.

46. What is rollback?

Answer:
ROLLBACK undoes changes.

47. What is data redundancy?

Answer:
Duplicate data stored unnecessarily.

48. What is data integrity?

Answer:
Ensures data accuracy and consistency.

49. What is backup?

Answer:
Backup is a copy of database data.

50. Why is DBMS important?

Answer:
DBMS helps organize, secure, and manage large amounts of data efficiently.
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

print(f"Loaded {len(parsed)} DBMS questions.")

with open('static/interviewData.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = json.dumps(parsed, indent=4)

m = re.search(r'(sql:\s*)\[.*?\]', content, flags=re.DOTALL)
if m:
    content = content[:m.start(1)] + 'sql: ' + json_str + content[m.end():]

with open('static/interviewData.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved successfully!")
