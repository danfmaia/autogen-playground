import tempfile
import os

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

# Instead of temp_dir = tempfile.TemporaryDirectory()
work_dir = "output"  # or any other directory name

# Create the directory if it doesn't exist
os.makedirs(work_dir, exist_ok=True)

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    # Use the permanent directory to store the code files.
    work_dir=work_dir,
)

# Create an agent with code executor configuration.
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    # Use the local command line code executor.
    code_execution_config={"executor": executor},
    # Always take human input for this agent for safety.
    human_input_mode="ALWAYS",
)

message_with_code_block = """This is a message with code block.
The code block is below:
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)
plt.scatter(x, y)
plt.savefig('scatter.png')
print('Scatter plot saved to scatter.png')
```
This is the end of the message.
"""

# Generate a reply for the given code.
reply = code_executor_agent.generate_reply(
    messages=[{"role": "user", "content": message_with_code_block}])
print(reply)
