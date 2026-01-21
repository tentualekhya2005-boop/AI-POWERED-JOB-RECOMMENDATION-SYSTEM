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
            skillsContainer.innerHTML = '<div class="no-skills">No technical skills detected in your resume.No job is found</div>';
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
                        <a href="${job.linkedin}" target="_blank" class="linkedin-btn">View on LinkedIn</a>
                        <a href="${job.naukri}" target="_blank" class="naukri-btn">View on Naukri</a>
                        <a href="${job.indeed}" target="_blank" class="indeed-btn">View on Indeed</a>
                    </div>
                `;
                jobsContainer.appendChild(jobEl);
            });
        } else {
            jobsContainer.innerHTML = '<div class="no-jobs">Tese Are The Some Of courses Recommended To You From Coursera</div>';
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

            if (course.title || course.provider) {
                // Backend course format
                courseEl.innerHTML = `
                    <h4>${escapeHtml(course.title || '')}</h4>
                    <div class="provider">${escapeHtml(course.provider || '')}</div>
                    <div class="skills">Skills: ${(course.skills || []).map(s => escapeHtml(s)).join(', ')}</div>
                    <p>${escapeHtml(course.description || '')}</p>
                `;
            } else {
                // Static beginner course format
                courseEl.innerHTML = `
                    <h4>${escapeHtml(course.name)}</h4>
                    <a href="${course.link}" target="_blank" class="course-link">Enroll Now</a>
                `;
            }

            coursesContainer.appendChild(courseEl);
        });

        // Show results
        document.getElementById('resultsSection').style.display = 'grid';
        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
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
