from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import PyPDF2
import re
from db_users import init_db, get_user_by_email, add_user

# Config
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "replace_this_with_a_strong_secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize DB
init_db()

# Skills Database
SKILLS_DATABASE = [
    "python","java","javascript","c","c++","c#","php","swift","kotlin","go","ruby",
    "html","css","react","angular","vue","django","flask","node","express","spring","bootstrap",
    "android","flutter","sql","mysql","mongodb","postgresql","oracle","aws","git","linux",
    "machine learning","deep learning","pandas","numpy","scikit-learn","tensorflow"
]

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

        user = get_user_by_email(email)
        if not user:
            flash("Email not registered!", "error")
            return redirect(url_for('forgot'))

        # later you can send email reset link
        flash("Password reset link sent to your email", "success")
        return redirect(url_for('forgot'))

    return render_template('forgot.html')


# ---------- Dashboard ----------

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template("index.html", username=session.get('username'))

# ---------- Resume Processing ----------

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
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
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
        # ✅ No skills found → suggest courses
        courses = get_course_suggestions()
        return jsonify({
            "skills": [],
            "jobs": [],
            "courses": courses
        })

    jobs = [get_job_links(skill) for skill in skills[:5]]

    return jsonify({
        "skills": skills,
        "jobs": jobs,
        "courses": []   # no courses needed if skills are found
    })


if __name__ == "__main__":
    app.run(debug=True)