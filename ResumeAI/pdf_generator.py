from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def generate_resume_pdf(data: dict, filename: str = "resume.pdf"):
    """Generate a resume PDF from resume data."""

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Header
    elements.append(Paragraph(data.get("full_name", ""), styles["Title"]))
    elements.append(Paragraph(data.get("email", ""), styles["BodyText"]))
    elements.append(Paragraph(data.get("phone", ""), styles["BodyText"]))

    # Summary
    elements.append(Paragraph("<b>Professional Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(data.get("summary", ""), styles["BodyText"]))

    # Education
    elements.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    elements.append(Paragraph(data.get("education", ""), styles["BodyText"]))

    doc.build(elements)

    return filename