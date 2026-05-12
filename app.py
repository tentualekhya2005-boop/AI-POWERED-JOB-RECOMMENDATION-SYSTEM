from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import PyPDF2
import re
from db_users import init_db, get_user_by_email, add_user, update_password

# Config
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "replace_this_with_a_strong_secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize DB
init_db()

# Skills Database
SKILLS_DATABASE = [
    "python","java","javascript","c","c++","c#","php","swift","kotlin","go","ruby","rust","typescript",
    "html","css","react","angular","vue","django","flask","node","express","spring","bootstrap","tailwind",
    "android","flutter","react native","ios",
    "sql","mysql","mongodb","postgresql","oracle","redis","elasticsearch","cassandra",
    "aws","gcp","azure","docker","kubernetes","jenkins","terraform","ansible","git","linux",
    "machine learning","deep learning","pandas","numpy","scikit-learn","tensorflow","pytorch","nlp","computer vision",
    "data science","data analysis","business intelligence","tableau","power bi",
    "agile","scrum","jira","project management","communication","leadership","problem solving"
]

COURSE_MAPPING = {
    "python": {"name": "Python for Everybody Specialization", "provider": "Coursera", "description": "Master Python programming and data analysis.", "link": "https://www.coursera.org/specializations/python"},
    "machine learning": {"name": "Machine Learning Specialization", "provider": "Coursera", "description": "Learn foundational machine learning algorithms.", "link": "https://www.coursera.org/specializations/machine-learning-introduction"},
    "deep learning": {"name": "Deep Learning Specialization", "provider": "Coursera", "description": "Build and train deep neural networks.", "link": "https://www.coursera.org/specializations/deep-learning"},
    "data science": {"name": "IBM Data Science Professional Certificate", "provider": "Coursera", "description": "Kickstart your career in Data Science & ML.", "link": "https://www.coursera.org/professional-certificates/ibm-data-science"},
    "react": {"name": "Advanced React", "provider": "Coursera", "description": "Deep dive into React, Hooks, and state management.", "link": "https://www.coursera.org/learn/advanced-react"},
    "javascript": {"name": "JavaScript for Beginners", "provider": "Coursera", "description": "Build interactive web pages with JavaScript.", "link": "https://www.coursera.org/learn/javascript-basics"},
    "java": {"name": "Object Oriented Programming in Java", "provider": "Coursera", "description": "Learn OOP concepts and Java fundamentals.", "link": "https://www.coursera.org/specializations/object-oriented-programming"},
    "aws": {"name": "AWS Fundamentals", "provider": "Coursera", "description": "Learn core AWS services and infrastructure.", "link": "https://www.coursera.org/specializations/aws-fundamentals"},
    "sql": {"name": "Learn SQL Basics for Data Science", "provider": "Coursera", "description": "Analyze data and build queries with SQL.", "link": "https://www.coursera.org/specializations/learn-sql-basics-data-science"},
    "project management": {"name": "Google Project Management Certificate", "provider": "Coursera", "description": "Start a career in project management.", "link": "https://www.coursera.org/professional-certificates/google-project-management"},
}

def get_tailored_courses(skills):
    suggested = []
    seen_names = set()
    for skill in skills:
        course = COURSE_MAPPING.get(skill.lower())
        if course and course["name"] not in seen_names:
            suggested.append(course)
            seen_names.add(course["name"])
    
    if len(suggested) < 3:
        general = [
            {"name": "Google Data Analytics Professional Certificate", "provider": "Coursera", "description": "Get professional training designed by Google.", "link": "https://www.coursera.org/professional-certificates/google-data-analytics"},
            {"name": "Full-Stack Web Development with React", "provider": "Coursera", "description": "Comprehensive guide to full-stack development.", "link": "https://www.coursera.org/specializations/full-stack-react"},
            {"name": "Cloud Computing Specialization", "provider": "Coursera", "description": "Learn cloud infrastructure and applications.", "link": "https://www.coursera.org/specializations/cloud-computing"}
        ]
        for c in general:
            if len(suggested) >= 4:
                break
            if c["name"] not in seen_names:
                suggested.append(c)
                seen_names.add(c["name"])
    return suggested[:4]

# ---------- Auth Routes ----------

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password']

        if get_user_by_email(email):
            flash("Email already registered!", "error")
            return redirect(url_for('signup'))

        add_user(name, email, generate_password_hash(password))
        flash("Account created successfully! Please login.", "success")
        return redirect(url_for('home'))

    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email'].strip().lower()
    password = request.form['password']

    user = get_user_by_email(email)

    if user and check_password_hash(user[3], password):
        session['user'] = user[2]
        session['username'] = user[1]
        return redirect(url_for('dashboard'))

    flash("Invalid login credentials", "error")
    return redirect(url_for('home'))
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        new_password = request.form['new_password']

        user = get_user_by_email(email)
        if not user:
            flash("Email not registered!", "error")
            return redirect(url_for('forgot'))

        update_password(email, generate_password_hash(new_password))
        flash("Password reset successfully! Please login.", "success")
        return redirect(url_for('home'))

    return render_template('forgot.html')


# ---------- Dashboard ----------

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template("index.html", username=session.get('username'))

# ---------- Resume Processing ----------

def calculate_score_and_level(skills):
    # Calculate a resume strength score based on number of skills
    score = min(100, 30 + (len(skills) * 6))
    if len(skills) == 0:
        score = 0
        level = "Novice"
    elif len(skills) < 5:
        level = "Beginner"
    elif len(skills) < 10:
        level = "Intermediate"
    else:
        level = "Advanced"
    return score, level

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(path):
    text = ""
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text().lower() + " "
    return text

def extract_skills(text):
    found = set()
    for skill in SKILLS_DATABASE:
        # Use lookarounds to match boundaries including special characters like c++ and c#
        pattern = r"(?i)(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, text):
            # Special case for acronyms
            if skill.lower() in ['sql', 'aws', 'gcp', 'html', 'css', 'php', 'api', 'ios']:
                found.add(skill.upper())
            else:
                found.add(skill.title())
    return sorted(found)

def get_job_links(skill):
    skill_q = skill.replace(" ", "+")
    return {
        "title": skill + " Jobs",
        "linkedin": f"https://www.linkedin.com/jobs/search/?keywords={skill_q}",
        "naukri": f"https://www.naukri.com/{skill_q}-jobs",
        "indeed": f"https://www.indeed.com/jobs?q={skill_q}"
    }
def get_course_suggestions():
    return [
        {"name": "Introduction to Programming", "link": "https://www.coursera.org/learn/python"},
        {"name": "Web Development for Beginners", "link": "https://www.coursera.org/specializations/web-design"},
        {"name": "Machine Learning Basics", "link": "https://www.coursera.org/learn/machine-learning"},
        {"name": "Database Management Essentials", "link": "https://www.coursera.org/learn/database-management"},
        {"name": "Cloud Computing Fundamentals", "link": "https://www.coursera.org/learn/cloud-computing"}
    ]

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'user' not in session:
        return jsonify({"error": "Login required"}), 401

    if 'resume' not in request.files:
        return jsonify({"error": "Upload your resume!"}), 400

    file = request.files['resume']

    if not allowed_file(file.filename):
        return jsonify({"error": "Only PDF allowed!"}), 400

    path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(path)

    text = extract_text_from_pdf(path)
    os.remove(path)

    skills = extract_skills(text)

    if not skills:
        courses = get_course_suggestions()
        score, level = calculate_score_and_level([])
        return jsonify({
            "skills": [],
            "jobs": [],
            "courses": courses,
            "score": score,
            "level": level
        })

    jobs = [get_job_links(skill) for skill in skills[:5]]
    courses = get_tailored_courses(skills)
    score, level = calculate_score_and_level(skills)

    return jsonify({
        "skills": skills,
        "jobs": jobs,
        "courses": courses,
        "score": score,
        "level": level
    })


if __name__ == "__main__":
    app.run(debug=True)