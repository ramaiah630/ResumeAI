import reflex as rx


class ResumeState(rx.State):
    full_name: str = "Dhasaradha Ramaiah"
    email: str = "ramaiah@example.com"
    phone: str = "7207805637"
    summary: str = "Passionate software engineer..."
    education: str = "B.Tech in Computer Science"
    skills: str = "Python, React, SQL, Git"
    company: str = "OpenAI"
    job_title: str = "AI Developer"
    duration: str = "Jan 2026 - Present"
    experience_description: str = "Built AI-powered applications using Python, Reflex, and modern web technologies."


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