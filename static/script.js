class JobRecommendationSystem {
    constructor() {
        this.selectedFile = null;
        this.initEventListeners();
    }

    initEventListeners() {
        const uploadArea = document.getElementById('uploadArea');
        const resumeInput = document.getElementById('resumeInput');

        // Drag & drop visual feedback
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.style.borderColor = '#58a6ff';
            uploadArea.style.boxShadow = '0 10px 30px rgba(7, 89, 133, 0.12)';
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.style.borderColor = '';
            uploadArea.style.boxShadow = '';
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.style.borderColor = '';
            uploadArea.style.boxShadow = '';
            const files = e.dataTransfer.files;
            if (files.length && files[0].type === 'application/pdf') {
                this.handleFileSelect(files[0]);
            } else {
                this.showError('Please upload a PDF file.');
            }
        });

        resumeInput.addEventListener('change', (e) => {
            if (e.target.files.length) this.handleFileSelect(e.target.files[0]);
        });
    }

    handleFileSelect(file) {
        if (file.type !== 'application/pdf') {
            return this.showError('Please upload a PDF file.');
        }

        this.selectedFile = file;
        document.getElementById('fileName').textContent = file.name;
        document.getElementById('fileInfo').style.display = 'flex';
        document.getElementById('uploadArea').style.display = 'none';
        this.hideError();
    }

    async analyzeResume() {
        if (!this.selectedFile) {
            return this.showError('Please select a resume file first.');
        }

        this.showLoading();

        try {
            const formData = new FormData();
            formData.append('resume', this.selectedFile);

            const response = await fetch('/analyze', { method: 'POST', body: formData });
            const contentType = response.headers.get('content-type') || '';

            if (!response.ok) {
                if (contentType.indexOf('application/json') !== -1) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || errorData.message || 'Resume analysis failed.');
                } else {
                    throw new Error('Resume analysis failed.');
                }
            }

            const data = await response.json();
            this.displayResults(data);
        } catch (err) {
            console.error('Error:', err);
            this.showError(err.message || 'Failed to analyze resume.');
        }
    }

    displayResults(data) {
        this.hideLoading();

        // --- Score & Level ---
        document.getElementById('resumeScore').textContent = '0';
        document.getElementById('resumeLevel').textContent = data.level || 'Novice';
        
        // Animate score circle
        const score = data.score || 0;
        let currentScore = 0;
        const scoreCircle = document.querySelector('.score-circle');
        
        const scoreInterval = setInterval(() => {
            if (currentScore >= score) {
                clearInterval(scoreInterval);
            } else {
                currentScore += 2;
                if (currentScore > score) currentScore = score;
                document.getElementById('resumeScore').textContent = currentScore;
                
                // Color change based on score
                let color = '#ef4444'; // Red for low
                if (currentScore > 40) color = '#eab308'; // Yellow for medium
                if (currentScore > 70) color = '#22c55e'; // Green for good
                if (currentScore >= 90) color = '#38bdf8'; // Blue for excellent
                
                scoreCircle.style.background = `conic-gradient(${color} ${currentScore}%, rgba(255,255,255,0.05) ${currentScore}%)`;
                scoreCircle.style.boxShadow = `0 0 20px ${color}40`;
            }
        }, 30);

        // --- Skills ---
        const skillsContainer = document.getElementById('skillsContainer');
        skillsContainer.innerHTML = '';
        if (data.skills && data.skills.length > 0) {
            data.skills.forEach(skill => {
                const skillEl = document.createElement('div');
                skillEl.className = 'skill-item';
                skillEl.textContent = skill;
                skillsContainer.appendChild(skillEl);
            });
        } else {
            skillsContainer.innerHTML = '<div class="no-skills">No technical skills detected in your resume. No jobs found.</div>';
        }

        // --- Jobs ---
        const jobsContainer = document.getElementById('jobsContainer');
        jobsContainer.innerHTML = '';
        if (data.jobs && data.jobs.length > 0) {
            data.jobs.forEach(job => {
                const jobEl = document.createElement('div');
                jobEl.className = 'job-item';
                jobEl.innerHTML = `
                    <h3>${escapeHtml(job.title)}</h3>
                    <div class="job-buttons">
                        <a href="${job.linkedin}" target="_blank" class="linkedin-btn"><i class="fab fa-linkedin"></i> LinkedIn</a>
                        <a href="${job.naukri}" target="_blank" class="naukri-btn"><i class="fas fa-briefcase"></i> Naukri</a>
                        <a href="${job.indeed}" target="_blank" class="indeed-btn"><i class="fas fa-search"></i> Indeed</a>
                    </div>
                `;
                jobsContainer.appendChild(jobEl);
            });
        } else {
            jobsContainer.innerHTML = '<div class="no-jobs">Here are some beginner courses recommended for you to get started:</div>';
        }

        // --- Courses ---
        const coursesContainer = document.getElementById('coursesContainer');
        coursesContainer.innerHTML = ''; // clear previous content

        let coursesToShow = [];

        // If backend returns courses, use them
        if (data.courses && data.courses.length > 0) {
            coursesToShow = data.courses;
        } 
        // If no jobs or skills, show beginner courses
        else if ((!data.skills || data.skills.length === 0) || (!data.jobs || data.jobs.length === 0)) {
            coursesToShow = get_course_suggestions();
        }

        coursesToShow.forEach(course => {
            const courseEl = document.createElement('div');
            courseEl.className = 'course-item';

            if (course.description || course.provider) {
                // Backend course format
                courseEl.innerHTML = `
                    <h4>${escapeHtml(course.name || course.title || '')}</h4>
                    <div class="provider" style="color: #a78bfa; font-size: 0.9rem; margin-bottom: 5px;">${escapeHtml(course.provider || '')}</div>
                    <p style="margin-bottom: 15px; font-size: 0.95rem; color: #cbd5e1;">${escapeHtml(course.description || '')}</p>
                    <a href="${course.link}" target="_blank" class="course-link"><i class="fas fa-graduation-cap"></i> Enroll Now</a>
                `;
            } else {
                // Static beginner course format
                courseEl.innerHTML = `
                    <h4>${escapeHtml(course.name)}</h4>
                    <a href="${course.link}" target="_blank" class="course-link"><i class="fas fa-graduation-cap"></i> Enroll Now</a>
                `;
            }

            coursesContainer.appendChild(courseEl);
        });

        // --- Generate Cover Letter ---
        const coverLetterBox = document.getElementById('coverLetterText');
        if (coverLetterBox) {
            let skillsStr = data.skills && data.skills.length > 0 ? data.skills.join(', ') : 'my diverse technical skill set';
            let dateStr = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            
            const template = `[Your Name]
[Your Address] | [Your Email] | [Your Phone]
[LinkedIn Profile / GitHub]

${dateStr}

Hiring Manager
[Company Name]
[Company Address]

Dear Hiring Manager,

I am writing to express my enthusiastic interest in the Software Engineering / IT role at [Company Name]. With a solid foundation in ${skillsStr}, I am confident in my ability to make an immediate impact on your team.

Throughout my academic and professional journey, I have developed a deep passion for building scalable, efficient, and user-centric applications. My experience working with these technologies has equipped me with strong problem-solving abilities and a continuous learning mindset. I am particularly drawn to [Company Name] because of your commitment to innovation and excellence.

I would welcome the opportunity to discuss how my technical skills, paired with my dedication, align with the goals of your team. Thank you for your time and consideration.

Sincerely,

[Your Name]`;
            
            coverLetterBox.value = template;
        }

        // Show results
        document.getElementById('resultsSection').style.display = 'grid';
        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });

        // Trigger confetti!
        if (typeof confetti === 'function') {
            confetti({
                particleCount: 150,
                spread: 80,
                origin: { y: 0.5 },
                colors: ['#a78bfa', '#38bdf8', '#8b5cf6', '#ffffff']
            });
        }
    }

    showLoading() {
        document.getElementById('uploadSection').style.display = 'none';
        document.getElementById('fileInfo').style.display = 'none';
        document.getElementById('loadingSection').style.display = 'block';
        document.getElementById('resultsSection').style.display = 'none';
        document.getElementById('errorSection').style.display = 'none';
    }

    hideLoading() {
        document.getElementById('loadingSection').style.display = 'none';
    }

    showError(message) {
        document.getElementById('errorText').textContent = message;
        document.getElementById('errorSection').style.display = 'block';
        document.getElementById('uploadSection').style.display = 'none';
        document.getElementById('fileInfo').style.display = 'none';
        document.getElementById('loadingSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
    }

    hideError() {
        document.getElementById('errorSection').style.display = 'none';
    }

    resetApp() {
        document.getElementById('uploadSection').style.display = 'flex';
        document.getElementById('fileInfo').style.display = 'none';
        document.getElementById('uploadArea').style.display = 'block';
        document.getElementById('resumeInput').value = '';
        document.getElementById('loadingSection').style.display = 'none';
        document.getElementById('resultsSection').style.display = 'none';
        document.getElementById('errorSection').style.display = 'none';
        this.selectedFile = null;
    }
}

// --- Helper ---
function escapeHtml(str) {
    if (!str) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// --- Initialize ---
document.addEventListener('DOMContentLoaded', function() {
    window.jobSystem = new JobRecommendationSystem();
});

function analyzeResume() { window.jobSystem.analyzeResume(); }
function resetApp() { window.jobSystem.resetApp(); }

function get_course_suggestions() {
    return [
        { name: "Python for Everybody", link: "https://www.coursera.org/specializations/python" },
        { name: "Web Development for Beginners", link: "https://www.coursera.org/learn/web-development" },
        { name: "Data Science Foundations", link: "https://www.coursera.org/specializations/data-science-foundations" }
    ];
}

// ==========================================
// NEW FEATURES: TABS, INTERVIEW, AND QUIZ
// ==========================================

function switchTab(tabId) {
    // Hide all tabs
    document.querySelectorAll('.tab-pane').forEach(el => el.style.display = 'none');
    // Remove active class from buttons
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabId).style.display = 'block';
    // Set active class on clicked button
    event.currentTarget.classList.add('active');

    if(tabId === 'interview') {
        loadInterviewQA();
    }
}

// --- Interview QA Logic ---
// interviewData is now loaded externally from static/interviewData.js

function loadInterviewQA() {
    const topic = document.getElementById('interviewTopic').value;
    const container = document.getElementById('qaContainer');
    container.innerHTML = '';

    const questions = interviewData[topic] || [];
    questions.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'qa-item';
        div.innerHTML = `
            <div class="qa-question" onclick="toggleAnswer('ans-${index}')">
                <span>Q: ${item.q}</span>
                <i class="fas fa-chevron-down"></i>
            </div>
            <div class="qa-answer" id="ans-${index}">
                <strong><i class="fas fa-robot"></i> AI Suggestion:</strong> ${item.a}
            </div>
        `;
        container.appendChild(div);
    });
}

function toggleAnswer(id) {
    const el = document.getElementById(id);
    el.style.display = el.style.display === 'block' ? 'none' : 'block';
}

// --- Quiz Logic ---
// quizzes loaded from massiveQuizData.js

const topicsList = [
    { cat: "Quantitative Aptitude", color: "#38bdf8", items: [
        { id: "NumberSystem", name: "Number System", yt: "Number System aptitude" },
        { id: "Simplification", name: "Simplification & Approx", yt: "Simplification aptitude" },
        { id: "Percentage", name: "Percentage", yt: "Percentage aptitude tricks" },
        { id: "ProfitAndLoss", name: "Profit & Loss", yt: "Profit and Loss aptitude tricks" },
        { id: "Ratio", name: "Ratio & Proportion", yt: "Ratio and Proportion aptitude" },
        { id: "Average", name: "Average", yt: "Average aptitude tricks" },
        { id: "TimeWork", name: "Time and Work", yt: "Time and Work aptitude" },
        { id: "TimeSpeed", name: "Time, Speed, Distance", yt: "Time Speed Distance aptitude" },
        { id: "Interest", name: "Simple & Compound Interest", yt: "Simple Compound Interest aptitude" },
        { id: "Mixtures", name: "Mixtures & Alligations", yt: "Mixtures and Alligations" },
        { id: "Permutation", name: "Permutation & Combination", yt: "Permutation and Combination" },
        { id: "Probability", name: "Probability", yt: "Probability aptitude" },
        { id: "Mensuration", name: "Mensuration", yt: "Mensuration aptitude" },
        { id: "DataInterpretation", name: "Data Interpretation", yt: "Data Interpretation" }
    ]},
    { cat: "Logical Reasoning", color: "#a78bfa", items: [
        { id: "Series", name: "Series (Number, Alphabet)", yt: "Number Series Reasoning" },
        { id: "CodingDecoding", name: "Coding-Decoding", yt: "Coding Decoding Reasoning" },
        { id: "BloodRelations", name: "Blood Relations", yt: "Blood Relations Reasoning" },
        { id: "DirectionSense", name: "Direction Sense Test", yt: "Direction Sense Reasoning" },
        { id: "Syllogism", name: "Syllogism", yt: "Syllogism Reasoning" },
        { id: "Seating", name: "Seating Arrangement", yt: "Seating Arrangement Reasoning" },
        { id: "Puzzles", name: "Puzzles", yt: "Puzzles Reasoning" },
        { id: "VennDiagrams", name: "Venn Diagrams", yt: "Venn Diagrams Reasoning" },
        { id: "StatementConclusion", name: "Statement & Conclusion", yt: "Statement Conclusion Reasoning" },
        { id: "CauseEffect", name: "Cause and Effect", yt: "Cause and Effect Reasoning" }
    ]},
    { cat: "Verbal Ability", color: "#fbbf24", items: [
        { id: "ReadingComprehension", name: "Reading Comprehension", yt: "Reading Comprehension tricks" },
        { id: "SynonymsAntonyms", name: "Synonyms & Antonyms", yt: "Synonyms Antonyms vocabulary" },
        { id: "SentenceCorrection", name: "Sentence Correction", yt: "Sentence Correction English" },
        { id: "ErrorDetection", name: "Error Detection", yt: "Error Detection English grammar" },
        { id: "ParaJumbles", name: "Para Jumbles", yt: "Para Jumbles tricks" },
        { id: "FillBlanks", name: "Fill in the Blanks", yt: "Fill in the blanks English grammar" }
    ]},
    { cat: "Non-Verbal Reasoning", color: "#f87171", items: [
        { id: "MirrorImages", name: "Mirror Images", yt: "Mirror Images reasoning" },
        { id: "PaperFolding", name: "Paper Folding & Cutting", yt: "Paper Folding and Cutting" },
        { id: "FigureSeries", name: "Figure Series", yt: "Figure Series reasoning" },
        { id: "EmbeddedFigures", name: "Embedded Figures", yt: "Embedded Figures reasoning" },
        { id: "CubeDice", name: "Cube and Dice", yt: "Cube and Dice reasoning tricks" }
    ]}
];

function renderTopicGrids() {
    const container = document.getElementById('quizSetup');
    if (!container) return;
    container.innerHTML = '';
    
    topicsList.forEach(category => {
        const catTitle = document.createElement('h3');
        catTitle.style.color = category.color;
        catTitle.style.marginTop = '25px';
        catTitle.style.borderBottom = `1px solid ${category.color}40`;
        catTitle.style.paddingBottom = '10px';
        catTitle.style.marginBottom = '15px';
        catTitle.textContent = category.cat;
        container.appendChild(catTitle);
        
        const grid = document.createElement('div');
        grid.className = 'topic-grid';
        
        category.items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'topic-card';
            card.innerHTML = `
                <h4>${item.name}</h4>
                <div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px;">
                    <a href="https://www.youtube.com/results?search_query=${encodeURIComponent(item.yt)}" target="_blank" class="btn btn-secondary yt-link" style="text-align:center;"><i class="fab fa-youtube" style="color: #ef4444;"></i> Watch Tutorial</a>
                    <button class="btn btn-primary" onclick="startQuiz('${item.id}')" style="font-size: 0.9rem; padding: 8px;">Start Quiz (${typeof massiveQuizData !== 'undefined' && massiveQuizData[item.id] ? massiveQuizData[item.id].length : 100} Qs)</button>
                </div>
            `;
            grid.appendChild(card);
        });
        container.appendChild(grid);
    });
}

// Call render on load
document.addEventListener('DOMContentLoaded', () => {
    renderTopicGrids();
});

let currentQuiz = [];
let currentQuestionIndex = 0;
let score = 0;
let userAnswers = [];

function startQuiz(type) {
    if (typeof massiveQuizData !== 'undefined' && massiveQuizData[type]) {
        currentQuiz = massiveQuizData[type];
    } else {
        alert("Quiz data for " + type + " not found!");
        return;
    }
    currentQuestionIndex = 0;
    score = 0;
    userAnswers = new Array(currentQuiz.length).fill(null);
    
    document.getElementById('quizSetup').style.display = 'none';
    document.getElementById('quizResult').style.display = 'none';
    document.getElementById('quizContainer').style.display = 'block';
    
    renderNavGrid();
    showQuestion();
}

function renderNavGrid() {
    const grid = document.getElementById('questionNavGrid');
    if (!grid) return;
    grid.innerHTML = '';
    for(let i=0; i<currentQuiz.length; i++) {
        const box = document.createElement('div');
        box.className = 'nav-box';
        box.textContent = i + 1;
        box.id = 'nav-box-' + i;
        box.onclick = () => jumpToQuestion(i);
        grid.appendChild(box);
    }
}

function jumpToQuestion(index) {
    currentQuestionIndex = index;
    showQuestion();
}

function showQuestion() {
    const qData = currentQuiz[currentQuestionIndex];
    
    // Calculate Difficulty
    let diffText = "";
    let color = "";
    if (currentQuestionIndex < 33) {
        diffText = "Difficulty: Basic";
        color = "#22c55e"; // Green
    } else if (currentQuestionIndex < 66) {
        diffText = "Difficulty: Intermediate";
        color = "#eab308"; // Yellow
    } else {
        diffText = "Difficulty: Hard";
        color = "#ef4444"; // Red
    }
    
    document.getElementById('quizProgress').innerHTML = `Question ${currentQuestionIndex + 1}/${currentQuiz.length} <span style="margin-left: 20px; color: ${color}; font-size: 0.85em; font-weight: 600; padding: 3px 10px; border: 1px solid ${color}; border-radius: 12px;">${diffText}</span>`;
    
    document.querySelectorAll('.nav-box').forEach(b => b.classList.remove('current'));
    const currBox = document.getElementById('nav-box-' + currentQuestionIndex);
    if(currBox) currBox.classList.add('current');
    
    document.getElementById('questionText').textContent = qData.q;
    
    const optsContainer = document.getElementById('optionsContainer');
    optsContainer.innerHTML = '';
    
    const alreadyAnswered = userAnswers[currentQuestionIndex] !== null;
    
    qData.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-option';
        btn.textContent = opt;
        
        if (alreadyAnswered) {
            btn.disabled = true;
            if (idx === qData.ans) {
                btn.classList.add('correct');
            }
        } else {
            btn.onclick = () => checkAnswer(idx, btn);
        }
        optsContainer.appendChild(btn);
    });
    
    // Manage Prev / Next buttons
    const prevBtn = document.getElementById('prevQuestionBtn');
    const nextBtn = document.getElementById('nextQuestionBtn');
    
    prevBtn.disabled = currentQuestionIndex === 0;
    prevBtn.style.opacity = currentQuestionIndex === 0 ? '0.5' : '1';
    
    if (currentQuestionIndex === currentQuiz.length - 1) {
        nextBtn.innerHTML = 'Finish <i class="fas fa-flag-checkered"></i>';
        nextBtn.onclick = () => {
            const answeredCount = userAnswers.filter(a => a !== null).length;
            if (answeredCount === currentQuiz.length) {
                endQuiz();
            } else if (confirm("You have unanswered questions! Are you sure you want to finish?")) {
                endQuiz();
            }
        };
    } else {
        nextBtn.innerHTML = 'Next <i class="fas fa-arrow-right"></i>';
        nextBtn.onclick = nextQuestion;
    }
    
    const expBox = document.getElementById('explanationBox');
    if (alreadyAnswered) {
        const correctAnsText = qData.options[qData.ans];
        expBox.innerHTML = `<strong>Correct Answer:</strong> <span style="color:#22c55e;">${correctAnsText}</span><br><br><strong>Explanation:</strong> ${qData.exp}`;
        expBox.style.display = 'block';
    } else {
        expBox.style.display = 'none';
    }
}

function checkAnswer(selectedIndex, btnElement) {
    const options = document.querySelectorAll('.quiz-option');
    options.forEach(opt => opt.disabled = true);
    
    const qData = currentQuiz[currentQuestionIndex];
    const isCorrect = (selectedIndex === qData.ans);
    
    userAnswers[currentQuestionIndex] = isCorrect;
    const currBox = document.getElementById('nav-box-' + currentQuestionIndex);
    
    if (isCorrect) {
        btnElement.classList.add('correct');
        score++;
        document.getElementById('quizScoreTrack').textContent = `Score: ${score}`;
        if(currBox) currBox.classList.add('answered-correct');
        
        if (typeof confetti === 'function') {
            confetti({ particleCount: 30, spread: 50, origin: { y: 0.8 }, colors: ['#22c55e'] });
        }
    } else {
        btnElement.classList.add('wrong');
        options[qData.ans].classList.add('correct');
        if(currBox) currBox.classList.add('answered-wrong');
    }
    
    const expBox = document.getElementById('explanationBox');
    const correctAnsText = qData.options[qData.ans];
    expBox.innerHTML = `<strong>Correct Answer:</strong> <span style="color:#22c55e;">${correctAnsText}</span><br><br><strong>Explanation:</strong> ${qData.exp}`;
    expBox.style.display = 'block';
    
    // Automatically transition if on last question and done
    const answeredCount = userAnswers.filter(a => a !== null).length;
    if (answeredCount === currentQuiz.length && currentQuestionIndex === currentQuiz.length - 1) {
        document.getElementById('nextQuestionBtn').innerHTML = 'Finish <i class="fas fa-flag-checkered"></i>';
    }
}

function prevQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showQuestion();
    }
}

function nextQuestion() {
    let nextIdx = currentQuestionIndex + 1;
    if (nextIdx < currentQuiz.length) {
        currentQuestionIndex = nextIdx;
        showQuestion();
    }
}

function endQuiz() {
    document.getElementById('quizContainer').style.display = 'none';
    document.getElementById('quizResult').style.display = 'block';
    document.getElementById('quizScoreDisplay').textContent = `${score} / ${currentQuiz.length}`;
    
    const percentage = (score / currentQuiz.length) * 100;
    const feedback = document.getElementById('quizFeedback');
    if (percentage === 100) feedback.textContent = "Outstanding! You are totally ready.";
    else if (percentage >= 60) feedback.textContent = "Good job! A little more practice and you'll be perfect.";
    else feedback.textContent = "Keep practicing! Review the materials tab to improve.";
    
    if (percentage >= 60 && typeof confetti === 'function') {
        confetti({ particleCount: 150, spread: 80, origin: { y: 0.5 } });
    }
}

function resetQuiz() {
    document.getElementById('quizResult').style.display = 'none';
    document.getElementById('quizSetup').style.display = 'block';
}

// ==========================================
// JOB TRACKER (KANBAN BOARD)
// ==========================================

let jobsData = JSON.parse(localStorage.getItem('jobTrackerData')) || {
    'wishlist-col': [],
    'applied-col': [],
    'interview-col': [],
    'offer-col': [],
    'rejected-col': []
};

function saveTracker() {
    localStorage.setItem('jobTrackerData', JSON.stringify(jobsData));
}

function renderTracker() {
    Object.keys(jobsData).forEach(colId => {
        const colContainer = document.querySelector(`#${colId} .kanban-cards`);
        if (!colContainer) return;
        colContainer.innerHTML = '';
        jobsData[colId].forEach(job => {
            const card = document.createElement('div');
            card.className = 'k-card';
            card.draggable = true;
            card.id = job.id;
            card.ondragstart = drag;
            card.innerHTML = `
                <div class="k-card-title">${escapeHtml(job.company)}</div>
                <div class="k-card-role">${escapeHtml(job.role)}</div>
                <button class="k-card-delete-btn" title="Delete Job" onmousedown="event.stopPropagation()" onclick="event.stopPropagation(); deleteJob('${job.id}', '${colId}')" style="position: absolute; top: 8px; right: 8px; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); color: #ef4444; cursor: pointer; border-radius: 4px; transition: all 0.2s; padding: 3px 8px; font-size: 0.8rem; font-weight: bold; display: flex; align-items: center; gap: 5px;">
                    <i class="fas fa-trash"></i> Delete
                </button>
            `;
            colContainer.appendChild(card);
        });
    });
}

function addJobToTracker() {
    const compInput = document.getElementById('newJobCompany');
    const roleInput = document.getElementById('newJobRole');
    const company = compInput.value.trim();
    const role = roleInput.value.trim();
    
    if (!company || !role) {
        alert("Please enter both Company and Role.");
        return;
    }
    
    const jobId = 'job-' + Date.now();
    jobsData['wishlist-col'].push({ id: jobId, company, role });
    saveTracker();
    renderTracker();
    
    compInput.value = '';
    roleInput.value = '';
}

function deleteJob(jobId, colId) {
    if(confirm("Are you sure you want to remove this job?")) {
        jobsData[colId] = jobsData[colId].filter(j => j.id !== jobId);
        saveTracker();
        renderTracker();
    }
}

function clearAllJobs() {
    if(confirm("Are you sure you want to clear ALL jobs from the tracker? This cannot be undone.")) {
        jobsData = {
            'wishlist-col': [],
            'applied-col': [],
            'interview-col': [],
            'offer-col': [],
            'rejected-col': []
        };
        saveTracker();
        renderTracker();
    }
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    ev.dataTransfer.setData("sourceCol", ev.target.closest('.kanban-column').id);
}

function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData("text");
    const sourceCol = ev.dataTransfer.getData("sourceCol");
    
    // Find closest kanban-column we dropped on
    const targetColEl = ev.target.closest('.kanban-column');
    if (!targetColEl) return;
    
    const targetCol = targetColEl.id;
    
    if (sourceCol === targetCol) return; // Didn't move between columns
    
    // Find job data
    const jobIndex = jobsData[sourceCol].findIndex(j => j.id === data);
    if (jobIndex > -1) {
        const job = jobsData[sourceCol].splice(jobIndex, 1)[0];
        jobsData[targetCol].push(job);
        saveTracker();
        renderTracker();
    }
}

// Call render on load
document.addEventListener('DOMContentLoaded', () => {
    renderTracker();
});

function copyCoverLetter() {
    const textData = document.getElementById('coverLetterText');
    textData.select();
    textData.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(textData.value).then(() => {
        alert("Cover letter copied to clipboard!");
    }).catch(err => {
        console.error("Could not copy text: ", err);
    });
}
