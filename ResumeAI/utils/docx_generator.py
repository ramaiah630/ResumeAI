from docx import Document


def generate_resume_docx(resume_data):
    document = Document()

    # Header
    document.add_heading(resume_data["full_name"], level=1)
    document.add_paragraph(
        f'{resume_data["email"]} | {resume_data["phone"]}'
    )

    # Professional Summary
    document.add_heading("Professional Summary", level=2)
    document.add_paragraph(resume_data["summary"])

    # Education
    document.add_heading("Education", level=2)
    document.add_paragraph(resume_data["education"])

    # Skills
    document.add_heading("Skills", level=2)
    document.add_paragraph(resume_data["skills"])

    # Experience
    document.add_heading("Experience", level=2)
    document.add_paragraph(
        f'{resume_data["job_title"]} - {resume_data["company"]}'
    )
    document.add_paragraph(resume_data["experience_description"])

    # Projects
    document.add_heading("Projects", level=2)
    document.add_paragraph(resume_data["project_title"])
    document.add_paragraph(resume_data["project_description"])

    # Certifications
    document.add_heading("Certifications", level=2)
    document.add_paragraph(resume_data["certification_name"])

    # Languages
    document.add_heading("Languages", level=2)
    document.add_paragraph(resume_data["languages"])

    output_path = "ResumeAI/generated_resume.docx"
    document.save(output_path)

    return output_path