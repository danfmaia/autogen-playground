import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"]
}

with autogen.coding.DockerCommandLineCodeExecutor(work_dir="coding_02") as code_executor:
    assistant = AssistantAgent("assistant", llm_config=llm_config)
    user_proxy = UserProxyAgent(
        "user_proxy", code_execution_config={"executor": code_executor}
    )

    # Start the chat
    user_proxy.initiate_chat(
        assistant,
        message="Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png",
    )
