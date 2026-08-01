from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

def generate_resume_pdf(data: dict, filename="resume.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    # ==========================
    # Header
    # ==========================
    story.append(Paragraph(f"<b><font size=18>{data.get('full_name','')}</font></b>", styles["Title"]))
    story.append(Paragraph(data.get("email",""), styles["BodyText"]))
    story.append(Paragraph(data.get("phone",""), styles["BodyText"]))
    story.append(Spacer(1, 12))

    # ==========================
    # Summary
    # ==========================
    if data.get("summary"):
        story.append(Paragraph("<b>Professional Summary</b>", styles["Heading2"]))
        story.append(Paragraph(data["summary"], styles["BodyText"]))
        story.append(Spacer(1, 10))

    # ==========================
    # Education
    # ==========================
    if data.get("education"):
        story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
        story.append(Paragraph(data["education"], styles["BodyText"]))
        story.append(Spacer(1, 10))

    # ==========================
    # Skills
    # ==========================
    if data.get("skills"):
        story.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
        story.append(Paragraph(data["skills"], styles["BodyText"]))
        story.append(Spacer(1, 10))

    # ==========================
    # Experience
    # ==========================
    if data.get("company"):
        story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
        story.append(
            Paragraph(
                f"<b>{data.get('job_title','')}</b> | {data.get('company','')}",
                styles["BodyText"],
            )
        )
        story.append(Paragraph(data.get("duration",""), styles["Italic"]))
        story.append(
            Paragraph(data.get("experience_description",""), styles["BodyText"])
        )
        story.append(Spacer(1, 10))

    # ==========================
    # Projects
    # ==========================
    if data.get("project_title"):
        story.append(Paragraph("<b>Projects</b>", styles["Heading2"]))
        story.append(
            Paragraph(
                f"<b>{data.get('project_title','')}</b>",
                styles["BodyText"],
            )
        )
        story.append(
            Paragraph(
                f"Technologies: {data.get('project_technologies','')}",
                styles["BodyText"],
            )
        )
        story.append(
            Paragraph(
                data.get("project_description",""),
                styles["BodyText"],
            )
        )

        if data.get("project_github"):
            story.append(
                Paragraph(
                    f"GitHub: {data.get('project_github')}",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 10))

    # ==========================
    # Certifications
    # ==========================
    if data.get("certification_name"):
        story.append(Paragraph("<b>Certifications</b>", styles["Heading2"]))
        story.append(
            Paragraph(
                f"{data.get('certification_name')} - {data.get('certification_organization')}",
                styles["BodyText"],
            )
        )
        story.append(
            Paragraph(
                f"Issue Date: {data.get('certification_issue_date')}",
                styles["BodyText"],
            )
        )
        story.append(Spacer(1, 10))

    # ==========================
    # Languages
    # ==========================
    if data.get("languages"):
        story.append(Paragraph("<b>Languages</b>", styles["Heading2"]))
        story.append(
            Paragraph(
                data.get("languages"),
                styles["BodyText"],
            )
        )

    doc.build(story)

    return filename