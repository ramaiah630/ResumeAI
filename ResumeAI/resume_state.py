import reflex as rx


class ResumeState(rx.State):
    full_name: str = "Dhasaradha Ramaiah"
    email: str = "ramaiah@example.com"
    phone: str = "7207805637"
    summary: str = "Passionate software engineer..."
    education: str = "B.Tech in Computer Science"
    skills: str = "Python, React, SQL, Git"


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