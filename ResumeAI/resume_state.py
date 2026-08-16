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

    # Structured education entries
    education_entries: list[dict[str, str]] = [
        {
            "institution": "",
            "location": "",
            "qualification": "",
            "course": "",
            "start_year": "",
            "end_year": "",
            "grade": "",
        }
    ]

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
    
    improving_experience_index: int = -1

    is_generating_cover_letter: bool = False
    cover_letter_status: str = ""

    is_generating_review: bool = False
    review_status: str = ""

    is_analyzing_job: bool = False
    job_match_status: str = ""
     
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

        education_complete = any(
            entry.get("institution", "").strip()
            and entry.get("qualification", "").strip()
            and (
                entry.get("course", "").strip()
                or entry.get("grade", "").strip()
            )
            for entry in self.education_entries
        )

        if education_complete:
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
            score += 15

        if self.email.strip():
            score += 10

        if self.phone.strip():
            score += 10

        if self.summary.strip():
            score += 15

        education_complete = any(
            entry.get("institution", "").strip()
            and entry.get("qualification", "").strip()
            and (
                entry.get("course", "").strip()
                or entry.get("grade", "").strip()
            )
            for entry in self.education_entries
        )

        if education_complete:
            score += 10


        if len(self.skills_list) >= 5:
            score += 15
        elif len(self.skills_list) > 0:
            score += 8

        if (
            self.company.strip()
            or self.job_title.strip()
            or self.experience_description.strip()
        ):
            score += 10

        if (
            self.project_title.strip()
            or self.project_description.strip()
        ):
            score += 15

        return score


    @rx.var
    def ats_suggestions(self) -> list[str]:
        suggestions = []

        if not self.full_name.strip():
            suggestions.append("Add your full name.")

        if not self.email.strip():
            suggestions.append("Add a professional email address.")

        if not self.phone.strip():
            suggestions.append("Add a phone number.")

        if not self.summary.strip():
            suggestions.append("Add a professional summary.")

        education_complete = any(
            entry.get("institution", "").strip()
            and entry.get("qualification", "").strip()
            and (
                entry.get("course", "").strip()
                or entry.get("grade", "").strip()
            )
            for entry in self.education_entries
        )

        if not education_complete:
            suggestions.append(
                "Complete your education details with your institution, qualification, and course or grade."
            )

        if len(self.skills_list) < 5:
            suggestions.append("Include at least 5 relevant skills.")

        if not (
            self.company.strip()
            or self.job_title.strip()
            or self.experience_description.strip() 
        ):
            suggestions.append("Add work experience or relevant experience.")

        if not (
            self.project_title.strip()
            or self.project_description.strip()
        ):
            suggestions.append("Add at least one relevant project.")

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

    def add_education(self):
        self.education_entries = self.education_entries + [
            {
                "institution": "",
                "location": "",
                "qualification": "",
                "course": "",
                "start_year": "",
                "end_year": "",
                "grade": "",
            }
        ]


    def remove_education(self, index: int):
        if len(self.education_entries) > 1:
            self.education_entries = [
                entry
                for i, entry in enumerate(self.education_entries)
                if i != index
            ]


    def set_education_field(
        self,
        index: int,
        field: str,
        value: str,
    ):
        entries = [
            dict(entry)
            for entry in self.education_entries
        ]

        if 0 <= index < len(entries):
            entries[index][field] = value
            self.education_entries = entries


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

    def set_experience_field(
        self,
        index: int,
        field: str,
        value: str,
    ):
        experiences = [
            dict(experience)
            for experience in self.experiences
        ]

        if 0 <= index < len(experiences):
            experiences[index][field] = value
            self.experiences = experiences



    def export_pdf(self):
        """Generate a PDF from the current resume data."""

        resume_data = {
        "full_name": self.full_name,
        "email": self.email,
        "phone": self.phone,
        "summary": self.summary,
        "education_entries": self.education_entries,
        "skills": self.skills,
        "company": self.company,
        "job_title": self.job_title,
        "duration": self.duration,
        "experience_description": self.experience_description,
        "experiences": self.experiences,
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
            "education_entries": self.education_entries,
            "skills": self.skills,
            "company": self.company,
            "job_title": self.job_title,
            "duration": self.duration,
            "experience_description": self.experience_description,
            "experiences": self.experiences,
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

        # ==========================
        # Validate Education
        # ==========================

        education_complete = any(
            entry.get("institution", "").strip()
            and entry.get("qualification", "").strip()
            and (
                entry.get("course", "").strip()
                or entry.get("grade", "").strip()
            )
            for entry in self.education_entries
        )

        if not education_complete:
            return rx.toast.warning(
                "Please complete your education details."
            )

        # ==========================
        # Validate Skills
        # ==========================

        if not self.skills.strip():
            return rx.toast.warning(
                "Please enter your skills."
            )

        # ==========================
        # Loading State
        # ==========================

        self.is_generating_summary = True

        self.summary_status = (
            "🤖 Gemini is generating your professional summary..."
        )

        yield

        try:

            # ==========================
            # Prepare Education
            # ==========================

            education_parts = []

            for entry in self.education_entries:

                institution = entry.get(
                    "institution",
                    "",
                ).strip()

                location = entry.get(
                    "location",
                    "",
                ).strip()

                qualification = entry.get(
                    "qualification",
                    "",
                ).strip()

                course = entry.get(
                    "course",
                    "",
                ).strip()

                start_year = entry.get(
                    "start_year",
                    "",
                ).strip()

                end_year = entry.get(
                    "end_year",
                    "",
                ).strip()

                grade = entry.get(
                    "grade",
                    "",
                ).strip()

                # Skip completely empty entries
                if not any([
                    institution,
                    location,
                    qualification,
                    course,
                    start_year,
                    end_year,
                    grade,
                ]):
                    continue

                education_text = ""

                if institution:
                    education_text += institution

                if location:
                    education_text += f", {location}"

                if qualification:
                    education_text += f" | {qualification}"

                if course:
                    education_text += f" - {course}"

                if start_year or end_year:

                    education_text += " | "

                    if start_year:
                        education_text += start_year

                    if start_year and end_year:
                        education_text += " - "

                    if end_year:
                        education_text += end_year

                if grade:
                    education_text += f" | {grade}"

                education_parts.append(
                    education_text
                )

            education_text = "\n".join(
                education_parts
            )

            # ==========================
            # Generate Summary
            # ==========================

            self.summary = generate_summary(
                education=education_text,
                skills=self.skills,
                job_title=self.professional_title,
            )

            yield rx.toast.success(
                "Professional summary generated!"
            )

        finally:

            self.is_generating_summary = False
            self.summary_status = ""

            yield


    def save_resume(self):
        resume_data = {
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "summary": self.summary,

            # Education
            "education_entries": self.education_entries,

            "skills": self.skills,

            # Experience
            "experiences": self.experiences,

            # Old Experience fields kept for compatibility
            "company": self.company,
            "job_title": self.job_title,
            "duration": self.duration,
            "experience_description": self.experience_description,

            # Projects
            "project_title": self.project_title,
            "project_technologies": self.project_technologies,
            "project_github": self.project_github,
            "project_description": self.project_description,

            # Certifications
            "certification_name": self.certification_name,
            "certification_organization": self.certification_organization,
            "certification_issue_date": self.certification_issue_date,
            "certification_credential_id": self.certification_credential_id,

            # Languages
            "languages": self.languages,

            # Template
            "selected_template": self.selected_template,
        }

        os.makedirs(
            "ResumeAI/saved_resumes",
            exist_ok=True,
        )

        filename = os.path.join(
            "ResumeAI",
            "saved_resumes",
            "resume_data.json",
        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                resume_data,
                file,
                indent=4,
            )

        return rx.toast.success(
            "Resume saved successfully!"
        )


    def load_resume(self):
        filename = os.path.join(
            "ResumeAI",
            "saved_resumes",
            "resume_data.json",
        )

        if not os.path.exists(filename):
            print("No saved resume found.")
            return

        with open(
            filename,
            "r",
            encoding="utf-8",
        ) as file:

            resume_data = json.load(file)

        self.full_name = resume_data.get(
            "full_name",
            "",
        )

        self.email = resume_data.get(
            "email",
            "",
        )

        self.phone = resume_data.get(
            "phone",
            "",
        )

        self.summary = resume_data.get(
            "summary",
            "",
        )

        # ==========================
        # Education
        # ==========================

        if "education_entries" in resume_data:

            self.education_entries = (
                resume_data.get(
                    "education_entries",
                    [],
                )
            )

        else:

            # Backward compatibility
            old_education = resume_data.get(
                "education",
                "",
            )

            if old_education:

                self.education_entries = [
                    {
                        "institution": "",
                        "location": "",
                        "qualification": old_education,
                        "course": "",
                        "start_year": "",
                        "end_year": "",
                        "grade": "",
                    }
                ]

            else:

                self.education_entries = [
                    {
                        "institution": "",
                        "location": "",
                        "qualification": "",
                        "course": "",
                        "start_year": "",
                        "end_year": "",
                        "grade": "",
                    }
                ]

        # Keep old education field
        # for backward compatibility
        self.education = resume_data.get(
            "education",
            "",
        )

        # ==========================
        # Skills
        # ==========================

        self.skills = resume_data.get(
            "skills",
            "",
        )

        # ==========================
        # Experience
        # ==========================

        if "experiences" in resume_data:

            self.experiences = (
                resume_data.get(
                    "experiences",
                    [],
                )
            )

        else:

            # Backward compatibility
            # for old single experience

            old_company = resume_data.get(
                "company",
                "",
            )

            old_job_title = resume_data.get(
                "job_title",
                "",
            )

            old_duration = resume_data.get(
                "duration",
                "",
            )

            old_description = resume_data.get(
                "experience_description",
                "",
            )

            self.experiences = [
                {
                    "company": old_company,
                    "job_title": old_job_title,
                    "duration": old_duration,
                    "description": old_description,
                }
            ]

        # Keep old Experience fields
        # for backward compatibility

        self.company = resume_data.get(
            "company",
            "",
        )

        self.job_title = resume_data.get(
            "job_title",
            "",
        )

        self.duration = resume_data.get(
            "duration",
            "",
        )

        self.experience_description = (
            resume_data.get(
                "experience_description",
                "",
            )
        )

        # ==========================
        # Projects
        # ==========================

        self.project_title = resume_data.get(
            "project_title",
            "",
        )

        self.project_technologies = (
            resume_data.get(
                "project_technologies",
                "",
            )
        )

        self.project_github = resume_data.get(
            "project_github",
            "",
        )

        self.project_description = (
            resume_data.get(
                "project_description",
                "",
            )
        )

        # ==========================
        # Certifications
        # ==========================

        self.certification_name = (
            resume_data.get(
                "certification_name",
                "",
            )
        )

        self.certification_organization = (
            resume_data.get(
                "certification_organization",
                "",
            )
        )

        self.certification_issue_date = (
            resume_data.get(
                "certification_issue_date",
                "",
            )
        )

        self.certification_credential_id = (
            resume_data.get(
                "certification_credential_id",
                "",
            )
        )

        # ==========================
        # Languages
        # ==========================

        self.languages = resume_data.get(
            "languages",
            "",
        )

        # ==========================
        # Template
        # ==========================

        self.selected_template = (
            resume_data.get(
                "selected_template",
                "classic",
            ) 
        )

        return rx.toast.success(
            "Resume loaded successfully!"
        )


    def reset_resume(self):
        # ==========================
        # Personal Information
        # ==========================

        self.full_name = ""
        self.email = ""
        self.phone = ""

        # ==========================
        # Summary
        # ==========================

        self.summary = ""

        # ==========================
        # Education
        # ==========================

        self.education = ""

        self.education_entries = [
            {
                "institution": "",
                "location": "",
                "qualification": "",
                "course": "",
                "start_year": "",
                "end_year": "",
                "grade": "",
            }
        ]

        # ==========================
        # Skills
        # ==========================

        self.skills = ""

        # ==========================
        # Experience
        # ==========================

        self.company = ""
        self.job_title = ""
        self.duration = ""
        self.experience_description = ""
        self.experiences = [
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

        self.project_title = ""
        self.project_technologies = ""
        self.project_github = ""
        self.project_description = ""

        # ==========================
        # Certifications
        # ==========================

        self.certification_name = ""
        self.certification_organization = ""
        self.certification_issue_date = ""
        self.certification_credential_id = ""

        # ==========================
        # Languages
        # ==========================

        self.languages = ""

        # ==========================
        # Template
        # ==========================

        self.selected_template = "classic"

        return rx.toast.info(
            "Started a new resume."
        )

    
    def choose_template(self, template: str):
        self.selected_template = template

    def set_job_description(self, value: str):
        self.job_description = value


    def generate_cover_letter(self):

        self.is_generating_cover_letter = True
        self.cover_letter_status = (
            "🤖 Gemini is writing your cover letter..."
        )

        yield

        try:

            self.cover_letter = generate_cover_letter(
                full_name=self.full_name,
                job_title=self.professional_title,
                education=self.education,
                skills=self.skills,
                experience=self.experience_description,
                job_description=self.job_description,
            )

            yield rx.toast.success(
                "Cover letter generated!"
            )

        finally:

            self.is_generating_cover_letter = False
            self.cover_letter_status = ""

            yield


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

        self.is_analyzing_job = True
        self.job_match_status = "🔎 Analyzing your resume against the job description..."

        yield

        try:


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

            yield rx.toast.success(
                "Job matching completed!"
            )

        finally:

            self.is_analyzing_job = False
            self.job_match_status = ""

            yield



    def improve_experience(self, index: int):

        # Make sure the index is valid
        if index < 0 or index >= len(self.experiences):
            return rx.toast.warning(
                "Invalid experience selected."
            )

        experience_entry = self.experiences[index]

        company = experience_entry.get(
            "company",
            "",
        ).strip()

        job_title = experience_entry.get(
            "job_title",
            "",
        ).strip()

        experience_description = experience_entry.get(
            "description",
            "",
        ).strip()

        if not experience_description:
            return rx.toast.warning(
                "Please enter your experience first."
            )

        # Remember which experience is being improved
        self.improving_experience_index = index

        self.is_generating_experience = True

        self.experience_status = (
            "🤖 Gemini is improving your work experience..."
        )

        # Allow loading card to render
        yield

        try:

            result = improve_experience(
                experience=experience_description,
                job_title=job_title,
                company=company,
                skills=self.skills,
            )

            # ==========================
            # Clean Gemini Markdown
            # ==========================

            import re

            cleaned_lines = []

            for line in result.splitlines():

                line = line.strip()

                if not line:
                    continue

                # Remove Markdown formatting
                line = line.replace("**", "")
                line = line.replace("__", "")
                line = line.replace("*", "")

                # Remove existing bullets
                line = re.sub(
                    r"^[-•]\s*",
                    "",
                    line,
                )

                # Add clean resume bullet
                line = f"• {line}"

                cleaned_lines.append(line)

            self.improved_experience = "\n".join(
                cleaned_lines
            )

            yield rx.toast.success(
                "Experience improved successfully!"
            )

        finally:

            self.is_generating_experience = False
            self.experience_status = ""

            yield


    def accept_improved_experience(self, index: int):

        if index < 0 or index >= len(self.experiences):
            return rx.toast.warning(
                "Invalid experience selected."
            )

        if not self.improved_experience.strip():
            return rx.toast.warning(
                "No improved experience available."
            )

        experiences = [
            dict(experience)
            for experience in self.experiences
        ]

        experiences[index]["description"] = (
            self.improved_experience
        )

        self.experiences = experiences

        self.improved_experience = ""
        self.improving_experience_index = -1

        return rx.toast.success(
            "Experience updated!"
        )
        

    def analyze_resume(self):

        self.is_generating_review = True
        self.review_status = "🤖 Gemini is analyzing your resume..."

        yield

        try:

            # ==========================
            # Prepare Education
            # ==========================

            education_parts = []

            for entry in self.education_entries:

                institution = entry.get(
                    "institution",
                    "",
                ).strip()

                location = entry.get(
                    "location",
                    "",
                ).strip()

                qualification = entry.get(
                    "qualification",
                    "",
                ).strip()

                course = entry.get(
                    "course",
                    "",
                ).strip()

                start_year = entry.get(
                    "start_year",
                    "",
                ).strip()

                end_year = entry.get(
                    "end_year",
                    "",
                ).strip()

                grade = entry.get(
                    "grade",
                    "",
                ).strip()

                # Skip completely empty entries
                if not any([
                    institution,
                    location,
                    qualification,
                    course,
                    start_year,
                    end_year,
                    grade,
                ]):
                    continue

                education_text = ""

                if institution:
                    education_text += institution

                if location:
                    education_text += f", {location}"

                if qualification:
                    education_text += f" | {qualification}"

                if course:
                    education_text += f" - {course}"

                if start_year or end_year:

                    education_text += " | "

                    if start_year:
                        education_text += start_year

                    if start_year and end_year:
                        education_text += " - "

                    if end_year:
                        education_text += end_year

                if grade:
                    education_text += f" | {grade}"

                education_parts.append(
                    education_text
                )

            education_text = "\n".join(
                education_parts
            )

            # ==========================
            # Analyze Resume
            # ==========================

            self.resume_review = analyze_resume(
                full_name=self.full_name,
                professional_title=self.professional_title,
                summary=self.summary,
                education=education_text,
                skills=self.skills,
                experience=self.experience_description,
                projects=self.project_description,
            )

            import json

            try:

                data = json.loads(
                    self.resume_review
                )

                self.resume_score_value = data.get(
                    "resume_score",
                    0,
                )

                self.resume_score = (
                    f"{self.resume_score_value}/100"
                )

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

            yield rx.toast.success(
                "Resume analysis completed!"
            )

        finally:

            self.is_generating_review = False
            self.review_status = ""

            yield