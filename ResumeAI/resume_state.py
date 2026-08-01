import reflex as rx
from ResumeAI.utils.pdf_generator import generate_resume_pdf
from ResumeAI.utils.docx_generator import generate_resume_docx
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
        self.summary = (
            f"Motivated {self.education} graduate with skills in "
            f"{self.skills}. Passionate about learning new technologies "
            "and contributing effectively to a dynamic organization."
        )

        return rx.toast.success("Professional summary generated!")


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
        self.cover_letter = f"""
    Dear Hiring Manager,

    My name is {self.full_name}, and I am applying for this opportunity.

    With experience in {self.professional_title}, along with my skills in {self.skills}, I believe I can contribute effectively to your team.

    Thank you for your time and consideration.

    Sincerely,

    {self.full_name}
    """

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