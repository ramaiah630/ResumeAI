import reflex as rx
from ResumeAI.utils.pdf_generator import generate_resume_pdf
from ResumeAI.utils.docx_generator import generate_resume_docx
from ResumeAI.utils.ai_service import (
    improve_experience,
    generate_summary,
    generate_cover_letter,
    analyze_resume,
)
import os
import json

class ResumeState(rx.State):
    # ==========================
    # Personal Information
    # ==========================
    full_name: str = ""
    professional_title: str = ""
    email: str = ""
    phone: str = ""

    # ==========================
    # Professional Summary
    # ==========================
    summary: str = ""

    improved_experience: str = ""

    # ==========================
    # Education
    # ==========================
    education: str = ""

    # ==========================
    # Skills
    # ==========================
    skills: str = ""


    # ==========================
    # Experience
    # ==========================
    company: str = ""
    job_title: str = ""
    duration: str = ""
    experience_description: str = ""
    experiences: list[dict] = [
        {
            "company": "",
            "job_title": "",
            "duration": "",
            "description": "",
        }
    ]

    # ==========================
    # Projects
    # ==========================

    project_title: str = ""
    project_technologies: str = ""
    project_github: str = ""
    project_description: str = ""

    # ==========================
    # certifications
    # ==========================

    certification_name: str = ""
    certification_organization: str = ""
    certification_issue_date: str = ""
    certification_credential_id: str = ""

    # ==========================
    # Languages
    # ==========================

    languages: str = ""

    # ==========================
    # Resume Template
    # ==========================

    selected_template: str = "classic"

    selected_theme: str = "Blue"
    theme_color: str = "#2563eb"

    # ==========================
    # Job_description & cover letter
    # ==========================

    job_description: str = ""
    cover_letter: str = ""


    # ==========================
    # Job Description Matcher
    # ==========================

    job_match_score: int = 0

    matched_skills: list[str] = []
    missing_skills: list[str] = []
    extra_skills: list[str] = []

    job_match_feedback: str = ""

    known_skills: list[str] = [
        "python",
        "java",
        "javascript",
        "typescript",
        "react",
        "angular",
        "vue",
        "html",
        "css",
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "gcp",
        "git",
        "github",
        "linux",
        "fastapi",
        "flask",
        "django",
        "rest api",
        "node.js",
        "power bi",
        "tableau",
        "excel",
        "figma",
    ]

    # ==========================
    # AI Loading States
    # ==========================

    is_generating_summary: bool = False
    summary_status: str = ""

    is_generating_experience: bool = False
    experience_status: str = ""

    is_generating_cover_letter: bool = False
    cover_letter_status: str = ""

    is_generating_review: bool = False
    review_status: str = ""
     
    # ==========================
    # Resume Review & Score
    # ==========================

    resume_review: str = ""
    resume_score: str = ""

    resume_score_value: int = 0


    overall_summary: str = ""

    strengths: list[str] = []

    improvements: list[str] = []

    missing_keywords: list[str] = []

    ai_ats_suggestions: list[str] = []

    recruiter_advice: str = ""


    # ==========================
    # Computed Variables
    # ==========================
    @rx.var
    def skills_list(self) -> list[str]:
        """Convert comma-separated skills into a list."""
        return [
            skill.strip()
            for skill in self.skills.split(",")
            if skill.strip()
        ]

    @rx.var
    def completed_sections(self) -> int:
        count = 0

        if self.full_name.strip():
            count += 1

        if self.email.strip():
            count += 1

        if self.phone.strip():
            count += 1

        if self.summary.strip():
            count += 1

        if self.education.strip():
            count += 1

        if self.skills.strip():
            count += 1

        if self.company.strip():
            count += 1

        if self.project_title.strip():
            count += 1

        if self.certification_name.strip():
            count += 1

        if self.languages.strip():
            count += 1   

        return count


    @rx.var
    def completion_percentage(self) -> int:
     total_sections = 10
     return int((self.completed_sections / total_sections) * 100)


    @rx.var
    def languages_list(self) -> list[str]:
     return [
        language.strip()
        for language in self.languages.split(",")
        if language.strip()
    ]
    

    @rx.var
    def ats_score(self) -> int:
        score = 0

        if self.full_name.strip():
            score += 10

        if self.email.strip():
            score += 10

        if self.phone.strip():
            score += 10

        if self.summary.strip():
            score += 15

        if self.education.strip():
            score += 10

        if self.skills.strip():
            score += 15

        if self.company.strip():
            score += 10

        if self.project_title.strip():
            score += 10

        if self.certification_name.strip():
            score += 5

        if self.languages.strip():
            score += 5

        return score

    @rx.var
    def ats_suggestions(self) -> list[str]:
        suggestions = []

        if not self.summary.strip():
           suggestions.append("Add a professional summary.")

        if len(self.skills_list) < 5:
           suggestions.append("Include at least 5 relevant skills.")

        if not self.company.strip():
           suggestions.append("Add work experience.")

        if not self.project_title.strip():
           suggestions.append("Add at least one project.")

        if not self.certification_name.strip():
           suggestions.append("Add certifications to strengthen your resume.")

        if not self.languages.strip():
           suggestions.append("Include the languages you know.")

        return suggestions

    @rx.var
    def resume_score_color(self) -> str:
        try:
            score = int(self.resume_score.split("/")[0])

            if score >= 80:
                return "green"

            if score >= 60:
                return "orange"

            return "red"

        except:
            return "gray"

    
    # ==========================
    # Setter Methods
    # ==========================
    def set_full_name(self, value: str):
        self.full_name = value

    def set_professional_title(self, value: str):
        self.professional_title = value

    def set_email(self, value: str):
        self.email = value

    def set_phone(self, value: str):
        self.phone = value

    def set_summary(self, value: str):
        self.summary = value

    def set_education(self, value: str):
        self.education = value

    def set_skills(self, value: str):
        self.skills = value

    def set_company(self, value: str):
        self.company = value

    def set_job_title(self, value: str):
        self.job_title = value

    def set_duration(self, value: str):
        self.duration = value

    def set_experience_description(self, value: str):
        self.experience_description = value

    def set_project_title(self, value: str):
        self.project_title = value

    def set_project_technologies(self, value: str):
        self.project_technologies = value

    def set_project_github(self, value: str):
        self.project_github = value

    def set_project_description(self, value: str):
        self.project_description = value

    def set_certification_name(self, value: str):
        self.certification_name = value

    def set_certification_organization(self, value: str):
        self.certification_organization = value

    def set_certification_issue_date(self, value: str):
        self.certification_issue_date = value

    def set_certification_credential_id(self, value: str):
        self.certification_credential_id = value

    def set_languages(self, value: str):
        self.languages = value

    def set_selected_template(self, value: str):
        self.selected_template = value

    def add_experience(self):
        self.experiences.append(
            {
                "company": "",
                "job_title": "",
                "duration": "",
                "description": "",
            }
        )
    def remove_experience(self, index: int):
        if len(self.experiences) > 1:
            self.experiences.pop(index)



    def export_pdf(self):
        """Generate a PDF from the current resume data."""

        resume_data = {
        "full_name": self.full_name,
        "email": self.email,
        "phone": self.phone,
        "summary": self.summary,
        "education": self.education,
        "skills": self.skills,
        "company": self.company,
        "job_title": self.job_title,
        "duration": self.duration,
        "experience_description": self.experience_description,
        "project_title": self.project_title,
        "project_technologies": self.project_technologies,
        "project_description": self.project_description,
        "project_github": self.project_github,
        "certification_name": self.certification_name,
        "certification_organization": self.certification_organization,
        "certification_issue_date": self.certification_issue_date,
        "certification_credential_id": self.certification_credential_id,
        "languages": self.languages,
        }

        generate_resume_pdf(resume_data)

        return rx.toast.success("PDF generated successfully!")


    def export_docx(self):
        """Generate a DOCX from the current resume data."""

        resume_data = {
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "summary": self.summary,
            "education": self.education,
            "skills": self.skills,
            "company": self.company,
            "job_title": self.job_title,
            "duration": self.duration,
            "experience_description": self.experience_description,
            "project_title": self.project_title,
            "project_technologies": self.project_technologies,
            "project_description": self.project_description,
            "project_github": self.project_github,
            "certification_name": self.certification_name,
            "certification_organization": self.certification_organization,
            "certification_issue_date": self.certification_issue_date,
            "certification_credential_id": self.certification_credential_id,
            "languages": self.languages,
        }

        generate_resume_docx(resume_data)

        return rx.toast.success("DOCX generated successfully!")



    def generate_ai_summary(self):

        if not self.education.strip():
            return rx.toast.warning(
                "Please enter your education."
            )

        if not self.skills.strip():
            return rx.toast.warning(
                "Please enter your skills."
            )
        self.is_generating_summary = True
        self.summary_status = "🤖 Gemini is generating your professional summary..."

        try:

            self.summary = generate_summary(
                education=self.education,
                skills=self.skills,
                job_title=self.professional_title,
            )

            return rx.toast.success(
                "Professional summary generated!"
            )
        finally:

            self.is_generating_summary = False
            self.ai_status = ""


    def save_resume(self):
        resume_data = {
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "summary": self.summary,
            "education": self.education,
            "skills": self.skills,
            "company": self.company,
            "job_title": self.job_title,
            "duration": self.duration,
            "experience_description": self.experience_description,
            "project_title": self.project_title,
            "project_technologies": self.project_technologies,
            "project_github": self.project_github,
            "project_description": self.project_description,
            "certification_name": self.certification_name,
            "certification_organization": self.certification_organization,
            "certification_issue_date": self.certification_issue_date,
            "certification_credential_id": self.certification_credential_id,
            "languages": self.languages,
            "selected_template": self.selected_template,
        }

        os.makedirs("ResumeAI/saved_resumes", exist_ok=True)

        filename = os.path.join(
            "ResumeAI",
            "saved_resumes",
            "resume_data.json",
        )

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(resume_data, file, indent=4)

        return rx.toast.success("Resume saved successfully!")


    def load_resume(self):
        filename = os.path.join(
            "ResumeAI",
            "saved_resumes",
            "resume_data.json",
        )

        if not os.path.exists(filename):
            print("No saved resume found.")
            return

        with open(filename, "r", encoding="utf-8") as file:
            resume_data = json.load(file)

        self.full_name = resume_data.get("full_name", "")
        self.email = resume_data.get("email", "")
        self.phone = resume_data.get("phone", "")
        self.summary = resume_data.get("summary", "")
        self.education = resume_data.get("education", "")
        self.skills = resume_data.get("skills", "")
        self.company = resume_data.get("company", "")
        self.job_title = resume_data.get("job_title", "")
        self.duration = resume_data.get("duration", "")
        self.experience_description = resume_data.get("experience_description", "")
        self.project_title = resume_data.get("project_title", "")
        self.project_technologies = resume_data.get("project_technologies", "")
        self.project_github = resume_data.get("project_github", "")
        self.project_description = resume_data.get("project_description", "")
        self.certification_name = resume_data.get("certification_name", "")
        self.certification_organization = resume_data.get("certification_organization", "")
        self.certification_issue_date = resume_data.get("certification_issue_date", "")
        self.certification_credential_id = resume_data.get("certification_credential_id", "")
        self.languages = resume_data.get("languages", "")
        self.selected_template = resume_data.get("selected_template", "classic")

        return rx.toast.success("Resume loaded successfully!")


    def reset_resume(self):
        # Personal Information
        self.full_name = ""
        self.email = ""
        self.phone = ""

        # Summary
        self.summary = ""

        # Education
        self.education = ""

        # Skills
        self.skills = ""

        # Experience
        self.company = ""
        self.job_title = ""
        self.duration = ""
        self.experience_description = ""

        # Projects
        self.project_title = ""
        self.project_technologies = ""
        self.project_github = ""
        self.project_description = ""

        # Certifications
        self.certification_name = ""
        self.certification_organization = ""
        self.certification_issue_date = ""
        self.certification_credential_id = ""

        # Languages
        self.languages = ""

        # Template
        self.selected_template = "classic"

        return rx.toast.info("Started a new resume.")

    
    def choose_template(self, template: str):
        self.selected_template = template

    def set_job_description(self, value: str):
        self.job_description = value


    def generate_cover_letter(self):

        self.is_generating_cover_letter = True
        self.cover_letter_status = (
            "🤖 Gemini is writing your cover letter..."
        )

        try:

            self.cover_letter = generate_cover_letter(
                ...
            )

            return rx.toast.success(
                "Cover letter generated!"
            )

        finally:

            self.is_generating_cover_letter = False
            self.cover_letter_status = ""


    def change_theme(self, value: str):
        self.selected_theme = value

        colors = {
            "Blue": "#2563eb",
            "Green": "#16a34a",
            "Purple": "#9333ea",
            "Red": "#dc2626",
            "Black": "#000000",
        }

        self.theme_color = colors[value]


    def analyze_job_description(self):

        # Resume skills entered by user
        resume_skills = [
            skill.strip().lower()
            for skill in self.skills.split(",")
            if skill.strip()
        ]

        # Entire job description
        job_text = self.job_description.lower()

        # Detect skills mentioned in the job description
        job_skills = []

        for skill in self.known_skills:
            if skill in job_text:
                job_skills.append(skill)

        # Compare
        matched = [
            skill
            for skill in job_skills
            if skill in resume_skills
        ]

        missing = [
            skill
            for skill in job_skills
            if skill not in resume_skills
        ]

        extra = [
            skill
            for skill in resume_skills
            if skill not in job_skills
        ]

        self.matched_skills = matched
        self.missing_skills = missing
        self.extra_skills = extra

        # ATS Score
        if len(job_skills) == 0:
            score = 0
        else:
            score = int(
                len(matched) / len(job_skills) * 100
            )

        self.job_match_score = score

        # Suggestions
        suggestions = []

        if missing:
            suggestions.append(
                "Consider adding these skills if you have experience:"
            )

            for skill in missing:
                suggestions.append(f"• {skill.title()}")

        if not suggestions:
            suggestions.append(
                "Excellent! Your resume matches the required skills."
            )

        self.job_match_feedback = "\n".join(suggestions)

    def improve_experience(self):

        if not self.experience_description.strip():
            return rx.toast.warning(
                "Please enter your experience first."
            )

        self.is_generating = True
        self.ai_status = "🤖 Gemini is improving your work experience..."

        try:

            self.improved_experience = improve_experience(
                experience=self.experience_description,
                job_title=self.job_title,
                company=self.company,
                skills=self.skills,
            )

            return rx.toast.success(
                "Experience improved successfully!"
            )

        finally:

            self.is_generating = False
            self.ai_status = ""


    def accept_improved_experience(self):
        self.experience_description = self.improved_experience
        self.improved_experience = ""

        return rx.toast.success(
            "Experience updated!"
    )

    def analyze_resume(self):

        self.is_generating_review = True
        self.review_status = "🤖 Gemini is analyzing your resume..."

        try:

            self.resume_review = analyze_resume(
                full_name=self.full_name,
                professional_title=self.professional_title,
                summary=self.summary,
                education=self.education,
                skills=self.skills,
                experience=self.experience_description,
                projects=self.project_description,
            )

            import json

            try:
                data = json.loads(self.resume_review)

                self.resume_score_value = data.get("resume_score", 0)
                self.resume_score = f"{self.resume_score_value}/100"

                self.overall_summary = data.get(
                    "overall_summary",
                    "",
                )

                self.strengths = data.get(
                    "strengths",
                    [],
                )

                self.improvements = data.get(
                    "improvements",
                    [],
                )

                self.missing_keywords = data.get(
                    "missing_keywords",
                    [],
                )

                self.ai_ats_suggestions = data.get(
                    "ats_suggestions",
                    [],
                )

                self.recruiter_advice = data.get(
                    "recruiter_advice",
                    "",
                )

            except Exception:

                self.resume_score = "N/A"
                self.resume_score_value = 0

            return rx.toast.success(
                "Resume analysis completed!"
            )

        finally:

            self.is_generating_review = False
            self.review_status = ""