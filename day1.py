# Import the OpenAI library (works with Groq too — same API style)
from openai import OpenAI

# os lets us read environment variables (like our secret API key)
import os

# python-dotenv loads our .env file so the key isn't hardcoded
from dotenv import load_dotenv

# Actually load the .env file into memory
load_dotenv()

# ── Create the client ───────────────────────────────────────────
# We point to Groq's API (it's free!). The OpenAI client works
# because Groq uses the same API format as OpenAI.
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),   # read key from .env file
    base_url="https://api.groq.com/openai/v1"  # point to Groq, not OpenAI
)

# ── Define your prompt ──────────────────────────────────────────
# This is the text you SEND to the AI (the "input")
my_prompt = "55/600 divide it and give it step by step process"

# ── Make the API call ───────────────────────────────────────────
# chat.completions.create() sends your message to the AI
response = client.chat.completions.create(
    # ✅ NEW — this works right now (free on Groq)
model="llama-3.3-70b-versatile",       # which AI model to use (free on Groq)
    temperature=0.7,              # creativity: 0=predictable, 1=creative
    max_tokens=300,               # limit the response length
    messages=[
        # The "system" message gives the AI a role / personality
        {"role": "system", "content": "You are a helpful AI teacher for beginners ."},

        # The "user" message is your actual question or request
        {"role": "user",   "content": my_prompt},
    ]
)

# ── Extract and print the answer ────────────────────────────────
# The response has a nested structure — we drill into it
answer = response.choices[0].message.content

# Print the AI's reply to your terminal
print("🤖 AI says:\n")
print(answer)

# ── Print token usage ───────────────────────────────────────────
# This tells you how many tokens your prompt and response used
print(f"\n📊 Tokens used: {response.usage.total_tokens}")
print(f"   Prompt tokens:     {response.usage.prompt_tokens}")
print(f"   Completion tokens: {response.usage.completion_tokens}")