from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv

#load_dotenv(override=True)
#root_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = Path(__file__).parent.parent.parent
dotenv_path = os.path.join(root_dir, '.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY is missing")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

# Initialize the OpenAI client
client = OpenAI(api_key=openai_api_key)

def openAI_chat(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI API call failed:", e)


if __name__ == "__main__":
    print("Hello")
    question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
    messages = [{"role": "user", "content": question}]
    print(openAI_chat(messages))


