import os
from autogen import ConversableAgent

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="You are playing a game of guess-my-number. You have the "
    "number random number between 1 and 100 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. "
    "When I guess the number, say 'correct'. That will terminate the game.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 1.5}]},
    # terminate if the number is guessed by the other agent
    is_termination_msg=lambda msg: "correct" in msg["content"],
    human_input_mode="NEVER",  # never ask for human input
)

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

# Start a chat with the agent with number with an initial guess.
result = human_proxy.initiate_chat(
    agent_with_number,  # this is the same agent with the number as before
    message="50",
)
