from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from xml.sax.saxutils import escape


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
    story.append(
        Paragraph(
            f"<b><font size=18>{escape(data.get('full_name', ''))}</font></b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            escape(data.get("email", "")),
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            escape(data.get("phone", "")),
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 12))

    # ==========================
    # Summary
    # ==========================
    if data.get("summary"):
        story.append(
            Paragraph(
                "<b>Professional Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                escape(data["summary"]).replace("\n", "<br/>"),
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 10))

    # ==========================
    # Education
    # ==========================

    education_entries = data.get("education_entries", [])

    if education_entries:
        story.append(
            Paragraph(
                "<b>Education</b>",
                styles["Heading2"],
            )
        )

        for entry in education_entries:

            institution = escape(
                entry.get("institution", "")
            )

            location = escape(
                entry.get("location", "")
            )

            qualification = escape(
                entry.get("qualification", "")
            )

            course = escape(
                entry.get("course", "")
            )

            start_year = escape(
                entry.get("start_year", "")
            )

            end_year = escape(
                entry.get("end_year", "")
            )

            grade = escape(
                entry.get("grade", "")
            )

            # --------------------------------
            # Institution + Location
            # --------------------------------

            institution_line = institution

            if institution and location:
                institution_line += f", {location}"

            elif location:
                institution_line = location

            if institution_line:
                story.append(
                    Paragraph(
                        f"<b>{institution_line}</b>",
                        styles["BodyText"],
                    )
                )

            # --------------------------------
            # Education Details
            # --------------------------------

            details = ""

            # Years
            if start_year:
                details += start_year

            if end_year:
                if details:
                    details += f" – {end_year}"
                else:
                    details += end_year

            # Qualification + Course
            if qualification or course:

                if details:
                    details += " | "

                if qualification:
                    details += qualification

                if qualification and course:
                    details += " – "

                if course:
                    details += course

            # Grade
            if grade:

                if details:
                    details += " | "

                details += grade

            if details:
                story.append(
                    Paragraph(
                        details,
                        styles["BodyText"],
                    )
                )

            # Space between education entries
            story.append(
                Spacer(1, 10)
            )

        story.append(
            Spacer(1, 10)
        )

    # ==========================
    # Skills
    # ==========================
    if data.get("skills"):
        story.append(
            Paragraph(
                "<b>Skills</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                escape(data["skills"]),
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 10))

    # ==========================
    # Experience
    # ==========================

    experiences = data.get("experiences", [])

    if experiences:
        story.append(
            Paragraph(
                "<b>Experience</b>",
                styles["Heading2"],
            )
        )

        for experience_entry in experiences:

            company = escape(
                experience_entry.get(
                    "company",
                    "",
                )
            )

            job_title = escape(
                experience_entry.get(
                    "job_title",
                    "",
                )
            )

            duration = escape(
                experience_entry.get(
                    "duration",
                    "",
                )
            )

            description = (
                experience_entry.get(
                    "description",
                    "",
                )
            )

            # --------------------------
            # Company
            # --------------------------

            if company:
                story.append(
                    Paragraph(
                        f"<b>{company}</b>",
                        styles["BodyText"],
                    )
                )

            # --------------------------
            # Job Title
            # --------------------------

            if job_title:
                story.append(
                    Paragraph(
                        job_title,
                        styles["BodyText"],
                    )
                )

            # --------------------------
            # Duration
            # --------------------------

            if duration:
                story.append(
                    Paragraph(
                        duration,
                        styles["Italic"],
                    )
                )

            # --------------------------
            # Description / Bullets
            # --------------------------

            if description:

                for line in description.splitlines():

                    line = line.strip()

                    if not line:
                        continue

                    # Remove existing bullet characters
                    if line.startswith("•"):
                        line = line[1:].strip()

                    elif line.startswith("-"):
                        line = line[1:].strip()

                    # Remove Markdown formatting
                    line = line.replace("**", "")
                    line = line.replace("__", "")

                    story.append(
                        Paragraph(
                            f"• {escape(line)}",
                            styles["BodyText"],
                        )
                    )

                    story.append(
                        Spacer(1, 3)
                    )

            # Space between experiences
            story.append(
                Spacer(1, 10)
            )

        story.append(
            Spacer(1, 10)
        )

    # ==========================
    # Projects
    # ==========================
    if data.get("project_title"):
        story.append(
            Paragraph(
                "<b>Projects</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                f"<b>{escape(data.get('project_title', ''))}</b>",
                styles["BodyText"],
            )
        )

        if data.get("project_technologies"):
            story.append(
                Paragraph(
                    f"Technologies: "
                    f"{escape(data.get('project_technologies', ''))}",
                    styles["BodyText"],
                )
            )

        if data.get("project_description"):
            story.append(
                Paragraph(
                    escape(data.get("project_description", ""))
                    .replace("\n", "<br/>"),
                    styles["BodyText"],
                )
            )

        if data.get("project_github"):
            story.append(
                Paragraph(
                    f"GitHub: {escape(data.get('project_github', ''))}",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 10))

    # ==========================
    # Certifications
    # ==========================
    if data.get("certification_name"):
        story.append(
            Paragraph(
                "<b>Certifications</b>",
                styles["Heading2"],
            )
        )

        certification_text = (
            f"{escape(data.get('certification_name', ''))}"
            f" - "
            f"{escape(data.get('certification_organization', ''))}"
        )

        story.append(
            Paragraph(
                certification_text,
                styles["BodyText"],
            )
        )

        if data.get("certification_issue_date"):
            story.append(
                Paragraph(
                    f"Issue Date: "
                    f"{escape(data.get('certification_issue_date', ''))}",
                    styles["BodyText"],
                )
            )

        if data.get("certification_credential_id"):
            story.append(
                Paragraph(
                    f"Credential ID: "
                    f"{escape(data.get('certification_credential_id', ''))}",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 10))

    # ==========================
    # Languages
    # ==========================
    if data.get("languages"):
        story.append(
            Paragraph(
                "<b>Languages</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                escape(data.get("languages", "")),
                styles["BodyText"],
            )
        )

    # ==========================
    # Build PDF
    # ==========================
    doc.build(story)

    return filename