import tempfile
import os
from autogen import ConversableAgent, GroupChat, GroupChatManager

temp_dir = tempfile.gettempdir()

# The Number Agent always returns the same numbers.
number_agent = ConversableAgent(
    name="Number_Agent",
    system_message="You return me the numbers I give you, one number each line.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 0.0}]},
    human_input_mode="NEVER",
)

# The Adder Agent adds 1 to each number it receives.
adder_agent = ConversableAgent(
    name="Adder_Agent",
    system_message="You add 1 to each number I give you and return me the new numbers, one number each line.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 0.0}]},
    human_input_mode="NEVER",  # main.py

    from agents import UserProxyAgent, RequirementsAgent, CodingAgent, TestingAgent, ReviewAgent, DeploymentAgent

    def main():
    # Initialize agents
    user_proxy_agent=UserProxyAgent()
    requirements_agent=RequirementsAgent()
    coding_agent=CodingAgent()
    testing_agent=TestingAgent()
    review_agent=ReviewAgent()
    deployment_agent=DeploymentAgent()

    # Example workflow execution
    # Step 1: Requirement Capture & Refinement
    user_input=user_proxy_agent.collect_user_input()
    requirements=requirements_agent.decompose_requests(user_input)
    refined_requirements=requirements_agent.refine_with_feedback(requirements)

    # Step 2: TDD Implementation
    tests=coding_agent.write_tests(refined_requirements)
    code=coding_agent.implement_code(tests)
    coding_agent.refactor_code(code)

    # Step 3: Testing and Validation
    test_results=testing_agent.execute_tests(code)
    testing_agent.generate_reports(test_results)

    # Step 4: Code Review
    review_feedback=review_agent.conduct_review(code)
    review_agent.suggest_enhancements(review_feedback)

    # Step 5: Deployment and Monitoring
    deployment_agent.automate_deployment(code)
    deployment_agent.monitor_performance()

    # Step 6: Feedback Loop
    user_proxy_agent.route_feedback()

    if __name__ == "__main__":
    main()2 and return me the new numbers, one number each line.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 0.0}]},
    human_input_mode="NEVER",
)

# The Subtracter Agent subtracts 1 from each number it receives.
subtracter_agent = ConversableAgent(
    name="Subtracter_Agent",
    system_message="You subtract 1 from each number I give you and return me the new numbers, one number each line.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 0.0}]},
    human_input_mode="NEVER",
)

# The Divider Agent divides each number it receives by 2.
divider_agent = ConversableAgent(
    name="Divider_Agent",
    system_message="You divide each number I give you by 2 and return me the new numbers, one number each line.",
    llm_config={"config_list": [
        {"model": "gpt-4o",
         "api_key": os.environ["OPENAI_API_KEY"],
         "temperature": 0.0}]},
    human_input_mode="NEVER",
)

arithmetic_agent = ConversableAgent(
    name="Arithmetic_Agent",
    llm_config=False,
    human_input_mode="ALWAYS",
    # This agent will always require human input to make sure the code is
    # safe to execute.
    code_execution_config={"use_docker": False, "work_dir": temp_dir},
)

code_writer_agent = ConversableAgent(
    name="Code_Writer_Agent",
    system_message="You are a code writer. You write Python script in Markdown code blocks.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
    human_input_mode="NEVER",
)

poetry_agent = ConversableAgent(
    name="Poetry_Agent",
    system_message="You are an AI poet.",
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
    human_input_mode="NEVER",
)

group_chat_with_introductions = GroupChat(
    agents=[adder_agent, multiplier_agent,
            subtracter_agent, divider_agent, number_agent],
    messages=[],
    max_round=6,
    send_introductions=True,
)

group_chat_manager_with_intros = GroupChatManager(
    groupchat=group_chat_with_introductions,
    llm_config={"config_list": [
        {"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

nested_chats = [
    {
        "recipient": group_chat_manager_with_intros,
        "summary_method": "reflection_with_llm",
        "summary_prompt": "Summarize the sequence of operations used to turn " "the source number into target number.",
    },
    {
        "recipient": code_writer_agent,
        "message": "Write a Python script to verify the arithmetic operations is correct.",
        "summary_method": "reflection_with_llm",
    },
    {
        "recipient": poetry_agent,
        "message": "Write a poem about it.",
        "max_turns": 1,
        "summary_method": "last_msg",
    },
]

arithmetic_agent.register_nested_chats(
    nested_chats,
    # The trigger function is used to determine if the agent should start the nested chat
    # given the sender agent.
    # In this case, the arithmetic agent will not start the nested chats if the sender is
    # from the nested chats' recipient to avoid recursive calls.
    trigger=lambda sender: sender not in [
        group_chat_manager_with_intros, code_writer_agent, poetry_agent],
)

# Instead of using `initiate_chat` method to start another conversation,
# we can use the `generate_reply` method to get single reply to a message directly.
reply = arithmetic_agent.generate_reply(
    messages=[
        {"role": "user", "content": "I have a number 3 and I want to turn it into 7."}]
)
