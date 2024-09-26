from openai import ChatCompletion, Completion
import os
from dotenv import load_dotenv
import argparse

load_dotenv()


def call_chatgpt_api(msgs=[], model="gpt-4-1106-preview"):
    "This function sends a list of messages to ChatGPT and returns the response"
    if not msgs:
        print("No messages to send to ChatGPT")

    try:
        return ChatCompletion.create(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model,
            messages=msgs,
            max_tokens=250,
            temperature=0.83,
            organization=os.getenv("OPENAI_ORGANIZATION"),
        )
    except openai.error.RateLimitError as e:
        retry_after = int(e.headers.get("retry-after", 60))
        print(f"Rate limit exceeded, waiting for {retry_after} seconds...")
        time.sleep(retry_after)
        return call_api(params, model=model)


if __name__ == "__main__":

    print(call_chatgpt_api(msgs=["Hello, how are you?"]))
