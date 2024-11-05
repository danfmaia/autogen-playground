import os
from autogen import ConversableAgent

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="You are playing a game of guess-my-number. "
    "number random number between 1 and 100 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. "
    "When I guess the number, say 'correct'. That will terminate the game.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
    # maximum number of consecutive auto-replies before asking for human input
    max_consecutive_auto_reply=1,
    # terminate if the number is guessed by the other agent
    is_termination_msg=lambda msg: "correct" in msg["content"],
    human_input_mode="TERMINATE",  # ask for human input until the game is terminated
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
    human_input_mode="NEVER",
)

result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)
