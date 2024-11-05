from pydantic import BaseModel, Field
from autogen import register_function
import os
from autogen import ConversableAgent
from typing import Annotated, Literal

Operator = Literal["+", "-", "*", "/"]


class CalculatorInput(BaseModel):
    a: Annotated[int, Field(description="The first number.")]
    b: Annotated[int, Field(description="The second number.")]
    operator: Annotated[Operator, Field(description="The operator.")]


def calculator(input: Annotated[CalculatorInput, "Input to the calculator."]) -> int:
    if input.operator == "+":
        return input.a + input.b
    elif input.operator == "-":
        return input.a - input.b
    elif input.operator == "*":
        return input.a * input.b
    elif input.operator == "/":
        return int(input.a / input.b)
    else:
        raise ValueError("Invalid operator")


# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get(
        "content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# # Register the tool signature with the assistant agent.
# assistant.register_for_llm(
#     name="calculator", description="A simple calculator")(calculator)

# # Register the tool function with the user proxy agent.
# user_proxy.register_for_execution(name="calculator")(calculator)


# Register the calculator function to the two agents.
register_function(
    calculator,
    # The assistant agent can suggest calls to the calculator.
    caller=assistant,
    # The user proxy agent can execute the calculator calls.
    executor=user_proxy,
    # By default, the function name is used as the tool name.
    name="calculator",
    # A description of the tool.
    description="A calculator tool that accepts nested expression as input",
)

chat_result = user_proxy.initiate_chat(
    assistant, message="What is (1423 - 123) / 3 + (32 + 23) * 5?")
