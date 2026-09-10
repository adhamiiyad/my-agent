import argparse
import json
import os
import sys
from typing import Any
from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def generate_content(client: OpenAI, messages: list[dict[str, Any]]) -> Any:
    return client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not found. Check your .env file.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    max_iterations = 20

    for iteration in range(max_iterations):
        response = generate_content(client, messages)

        if response.usage is None:
            raise RuntimeError("API request failed: response usage data is missing.")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                print(f" - Calling function: {tool_call.function.name}")

                result_str = call_function(tool_call, working_directory="calculator")

                tool_message = {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result_str,
                }
                messages.append(tool_message)
        else:
            if message.content:
                print(message.content)
            return

    print("Error: Reached maximum agent loop iterations without a final response.")
    sys.exit(1)


if __name__ == "__main__":
    main()