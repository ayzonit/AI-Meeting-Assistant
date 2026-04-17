import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.API_KEY)

def generate_summary(transcript: str):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Convert the following meeting transcript into structured output:

    Sections:
    - Summary
    - Decisions
    - Action Items (with owner if mentioned)

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)
    return response.text