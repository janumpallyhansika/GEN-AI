
# Step 1: Import required libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Load environment variables
load_dotenv()

# Step 3: Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Check your .env file.")

print("OpenAI API key loaded successfully.")

# Step 4: Initialize OpenAI client
client = OpenAI(api_key=api_key)

print("OpenAI client initialized successfully.")

# Step 5: Send prompt to OpenAI
response = client.responses.create(
    model="gpt-4.1-mini",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Step 6: Display AI response
print("\nLLM Response:")
print(response.output_text)
