print("Starting test_pdf.py")

from ResumeAI.pdf_generator import generate_resume_pdf

resume_data = {
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "+91 9876543210",
    "summary": "Software Engineer with experience in Python and AI.",
    "education": "B.Tech in Computer Science",
}

print("Calling PDF generator...")
filename = generate_resume_pdf(resume_data)

print(f"PDF saved as: {filename}")
print("Done!")