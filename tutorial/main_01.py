import os
from dotenv import load_dotenv
# import autogen
from autogen import ConversableAgent

load_dotenv()

# llm_config = {
#     "model": "gpt-4o",
#     "api_key": os.environ["OPENAI_API_KEY"]
# }

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "temperature": 0.7, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "good bye" in msg["content"].lower(),
)

result = joe.initiate_chat(
    cathy, message="Cathy, tell me a joke and then say the words GOOD BYE.")
