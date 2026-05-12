import json

# Same parsed_python array from before
with open('import_python.py', 'r') as f:
    script = f.read()

exec(script.split('with open')[0]) # Execute everything up to reading interviewData.js

with open('static/interviewData.js', 'r') as f:
    content = f.read()

import re

# To avoid re.sub replacement errors, we can use a match object to slice the string.
match = re.search(r'(.*?python:\s*)\[.*?\](,\s*java:.*)', content, flags=re.DOTALL)
if match:
    new_python_json = json.dumps(parsed_python, indent=4)
    new_content = match.group(1) + new_python_json + match.group(2)
    with open('static/interviewData.js', 'w') as f:
        f.write(new_content)
    print("Success!")
else:
    print("Match failed")
