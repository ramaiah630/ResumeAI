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
        return f"Error: {str(e)}"


def improve_experience(
    experience: str,
    job_title: str,
    company: str,
    skills: str,
) -> str:

    prompt = f"""
You are an expert resume writer.

Improve the following work experience for a professional resume.

Job Title:
{job_title}

Company:
{company}

Skills:
{skills}

Current Experience:
{experience}

Requirements:
- Keep it professional.
- Use strong action verbs.
- Make it ATS-friendly.
- Keep it concise.
- Return only the improved experience.
"""

    return generate_text(prompt)