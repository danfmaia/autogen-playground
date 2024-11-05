import os
from autogen import GroupChat, GroupChatManager
from agents import user_proxy, project_manager, coding_agent, testing_agent
from tools import register_tools

# Register tools for execution
register_tools(user_proxy, project_manager, coding_agent, testing_agent)

##################
# Set up the chat #
##################
groupchat = GroupChat(
    agents=[user_proxy, project_manager, coding_agent, testing_agent],
    messages=[],
    max_round=100,
    send_introductions=True,
    enable_clear_history=True,
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={
        "model": "gpt-4o",
        "api_key": os.environ["OPENAI_API_KEY"],
        "temperature": 0,
    },
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

##################
# Start the chat #
##################
chat_result = user_proxy.initiate_chat(
    manager,
    message="""
Create a React app that is a simple todo list.
""",
)
