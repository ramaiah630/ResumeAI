import reflex as rx


class ResumeState(rx.State):
    # ==========================
    # Personal Information
    # ==========================
    full_name: str = "Dhasaradha Ramaiah"
    email: str = "ramaiah@example.com"
    phone: str = "7207805637"

    # ==========================
    # Professional Summary
    # ==========================
    summary: str = "Passionate software engineer..."

    # ==========================
    # Education
    # ==========================
    education: str = "B.Tech in Computer Science"

    # ==========================
    # Skills
    # ==========================
    skills: str = "Python, React, SQL, Git"


    # ==========================
    # Experience
    # ==========================
    company: str = "OpenAI"
    job_title: str = "AI Developer"
    duration: str = "Jan 2026 - Present"
    experience_description: str = (
        "Built AI-powered applications using Python, Reflex, "
        "and modern web technologies."
    )

    # ==========================
    # Projects
    # ==========================

    project_title: str = "ResumeAI"
    project_technologies: str = "Python, Reflex, Gemini AI"
    project_github: str = "https://github.com/yourusername/resumeai"
    project_description: str = "An AI-powered resume builder with live preview, ATS score, and PDF export."

    # ==========================
    # certifications
    # ==========================

    certification_name: str = ""
    certification_organization: str = ""
    certification_issue_date: str = ""
    certification_credential_id: str = ""
  

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
            
        return count


    @rx.var
    def completion_percentage(self) -> int:
     total_sections = 9
     return int((self.completed_sections / total_sections) * 100)
    
   
    # ==========================
    # Setter Methods
    # ==========================
    def set_full_name(self, value: str):
        self.full_name = value

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