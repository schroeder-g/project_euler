import json, time, os, argparse
from num_tokens import num_tokens_from_messages
from classes.Chat import Open_AI_Chat
from classes.Message import OAIMessage
from utils.optional_set import opt_set
from utils.converse import converse


def add(*args):
    """
    Adds an arbitrary number of numbers together.
    """
    return sum(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converse with a zero-shot classifier."
    )
    params = {
        "--model": {"help": "The model to use for the completion."},
        "--temperature": {"help": "The temperature to use for the completion."},
        "--num_tokens": {"help": "The number of tokens to use for the completion."},
        "--system": {"help": "The system prompt to use for the completion."},
        "--tools": {"help": "The functions to use for the completion."},
        "--i": {"help": "Enter interactive mode."},
    }
    parser.add_argument("prompt", help="The prompt to use for the completion.")
    for param, p_dict in params.items():
        parser.add_argument(f"{param}", help=p_dict["help"])

    args = parser.parse_args()
    # Unpack args
    prompt, model, temperature, num_tokens, system, tools = (
        args.prompt,
        args.model,
        args.temperature,
        args.num_tokens,
        args.system,
        args.tools,
    )
    chat = Open_AI_Chat(
        model=opt_set(model, "gpt-4-1106-preview"),
        system=OAIMessage(
            role="system",
            content=opt_set(
                system,
                "You are an intelligent assistant that enjoys Australian Aphorisms. Use python for any required computations.",
            ),
        ),
        max_tokens=opt_set(num_tokens, 100),
        temperature=opt_set(temperature, 0.83),
    )

    if args.i:
        converse(chat)
    else:
        chat.completion(prompt)
        print("lastly", chat.history.last())
