import tempfile
from autogen import ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    # Execute code using the given docker image name.
    image="python:3.12-slim",
    timeout=10,  # Timeout for each code execution in seconds.
    # Use the temporary directory to store the code files.
    work_dir=temp_dir.name,
)

# Create an agent with code executor configuration that uses docker.
code_executor_agent_using_docker = ConversableAgent(
    "code_executor_agent_docker",
    llm_config=False,  # Turn off LLM for this agent.
    # Use the docker command line code executor.
    code_execution_config={"executor": executor},
    # Always take human input for this agent for safety.
    human_input_mode="ALWAYS",
)

# When the code executor is no longer used, stop it to release the resources.
# executor.stop()
