import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_text(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return (
            "Gemini is currently unavailable or busy. "
            "Please try again in a few moments."
        )


def improve_experience(
    experience: str,
    job_title: str,
    company: str,
    skills: str,
) -> str:
    
    prompt = f"""
You are an expert resume writer.

Rewrite the following work experience for a professional resume.

Candidate Information

Job Title:
{job_title}

Company:
{company}

Skills:
{skills}

Current Experience:
{experience}

Instructions:

- Rewrite only what the candidate has provided.
- Do NOT invent technologies.
- Do NOT invent responsibilities.
- Do NOT invent achievements.
- Preserve the original meaning.
- Improve grammar and readability.
- Use strong action verbs.
- Make it ATS-friendly.
- Keep it concise.
- Return 2–4 professional bullet points.
- Return only the rewritten experience.
"""

    return generate_text(prompt)

def generate_summary(
    education: str,
    skills: str,
    job_title: str,
) -> str:

    prompt = f"""
You are an expert resume writer.

Write a professional resume summary.

Education:
{education}

Target Job Title:
{job_title}

Skills:
{skills}

Rules:
- Maximum 4 sentences.
- ATS-friendly.
- Professional.
- Do NOT invent experience.
- Focus on strengths and career goals.
- Return only the summary.
"""

    return generate_text(prompt)

def generate_cover_letter(
    full_name: str,
    job_title: str,
    education: str,
    skills: str,
    experience: str,
    job_description: str,
) -> str:

    prompt = f"""
You are an expert career coach and resume writer.

Write a professional cover letter.

Candidate Name:
{full_name}

Target Job:
{job_title}

Education:
{education}

Skills:
{skills}

Experience:
{experience}

Job Description:
{job_description}

Rules:
- Keep it professional.
- Keep it under 400 words.
- Tailor it to the job description.
- Do NOT invent experience.
- Return only the cover letter.
"""

    return generate_text(prompt)

def analyze_resume(
    full_name: str,
    professional_title: str,
    summary: str,
    education: str,
    skills: str,
    experience: str,
    projects: str,
) -> str:

    prompt = f"""
You are an expert ATS recruiter.

Analyze this resume.

Name:
{full_name}

Professional Title:
{professional_title}

Summary:
{summary}

Education:
{education}

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Provide:

1. Resume Score (0-100)

2. Strengths

3. Weaknesses

4. ATS Suggestions

5. Recruiter Advice

Do not invent information.

Return only the analysis.
"""

    return generate_text(prompt)