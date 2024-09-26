import openai
import argparse
from dotenv import load_dotenv

# Set up OpenAI API credentials
env = load_dotenv()
api_key = env.OPEN_AI

print(api_key)

# Define command line arguments
parser = argparse.ArgumentParser(description="Send a request to ChatGPT")
parser.add_argument("prompt", type=str, help="The prompt to send to ChatGPT")
parser.add_argument(
    "--model",
    type=str,
    default="text-davinci-002",
    help="The ID of the GPT model to use (default: text-davinci-002)",
)
parser.add_argument(
    "--temperature",
    type=float,
    default=0.5,
    help="The temperature to use for generating responses (default: 0.5)",
)
parser.add_argument(
    "--max_tokens",
    type=int,
    default=50,
    help="The maximum number of tokens to generate in the response (default: 50)",
)
parser.add_argument(
    "--stop_sequence",
    type=str,
    default="\n\n",
    help='The sequence of tokens to use to end the response (default: "\n\n")',
)

# Parse command line arguments
args = parser.parse_args()

# Send request to ChatGPT
response = openai.Completion.create(
    engine=args.model,
    prompt=args.prompt,
    temperature=args.temperature,
    max_tokens=args.max_tokens,
    stop=args.stop_sequence,
)

# Print response
try:
    print(response.choices[0])
except e:
    print(e)
