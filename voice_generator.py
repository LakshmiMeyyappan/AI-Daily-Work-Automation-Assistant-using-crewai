import pyttsx3
from crewai.llm import LLM
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def morning_briefing(report_content):
    prompt = f"""
    You are a professional assistant. Below is a list of tasks for today.
    Please provide:
    1. A short, warm 'Good morning'.
    2. A quick summary of these specific tasks.
    3. One short motivational quote.
    
    Tasks to summarize: {report_content}
    
    Keep it under 55 words. Do not mention technical logs or JSON.
    """
    
    # We store the AI's spoken version in 'response'
    response = llm.call(prompt)
    
    # 2. CLEAN THE AI RESPONSE (Not the raw report)
    # We use 'response' here so she says the warm greeting, not the code!
    clean_voice_text = response.replace("_", " ")
    clean_voice_text = clean_voice_text.replace(".py", " Python file")
    clean_voice_text = clean_voice_text.replace("*", "")

    # 3. Initialize Engine
    engine = pyttsx3.init()

    # --- VOICE SELECTION (Female) ---
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # --- VOICE SETTINGS (Soft & Slow) ---
    engine.setProperty('rate', 127)    
    engine.setProperty('volume', 0.8) # 80% is the "sweet spot" for clarity

    # 4. Speak the CLEANED AI response
    print(f"AI Briefing: {clean_voice_text}") # So you can read along
    engine.say(clean_voice_text)
    engine.runAndWait()