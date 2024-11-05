import os
from typing_extensions import Annotated, List, Tuple
from autogen import UserProxyAgent, AssistantAgent

default_path = os.path.abspath("./output") + "/"
docs_path = os.path.abspath("./output/docs") + "/"  # Path for documentation


def register_tools(user_proxy: UserProxyAgent, coding_agent: AssistantAgent, project_manager: AssistantAgent):
    # Tools for Coding Agent
    @user_proxy.register_for_execution()
    @coding_agent.register_for_llm(description="List files in chosen directory.")
    def list_dir(
        directory: Annotated[str, "Directory to check."]
    ) -> Annotated[Tuple[int, List[str]], "Status code and list of files"]:
        files = os.listdir(default_path + directory)
        return 0, files

    @user_proxy.register_for_execution()
    @coding_agent.register_for_llm(description="Check the contents of a chosen file.")
    def see_file(
        filename: Annotated[str, "Name and path of file to check."]
    ) -> Annotated[Tuple[int, str], "Status code and file contents."]:
        with open(default_path + filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
        file_contents = "".join(formatted_lines)

        return 0, file_contents

    @user_proxy.register_for_execution()
    @coding_agent.register_for_llm(description="Replaces all the code within a file with new one. Proper indentation is important.")
    def modify_code(
        filename: Annotated[str, "Name and path of file to change."],
        new_code: Annotated[str, "New piece of code to replace old code with. Remember about providing indents."],
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        with open(default_path + filename, "w", encoding="utf-8") as file:
            file.write(new_code)
        return 0, "Code was written successfully."

    @user_proxy.register_for_execution()
    @coding_agent.register_for_llm(description="Create a new file with code.")
    def create_file_with_code(
        filename: Annotated[str, "Name and path of file to create."],
        code: Annotated[str, "Code to write in the file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        with open(default_path + filename, "w", encoding="utf-8") as file:
            file.write(code)
        return 0, "File created successfully"

    @user_proxy.register_for_execution()
    @coding_agent.register_for_llm(description="Execute bash command.")
    def execute_command(
        command: Annotated[str, "Command to execute."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        os.system(f"CI=true cd {default_path} && {command}")
        return 0, "Command executed successfully"

    # Tools for Project Manager
    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Create a documentation file.")
    def create_doc_file(
        filename: Annotated[str, "Name and path of documentation file to create."],
        content: Annotated[str, "Content to write in the documentation file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        with open(docs_path + filename, "w", encoding="utf-8") as file:
            file.write(content)
        return 0, "Documentation file created successfully"

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="List documentation files in the docs directory.")
    def list_docs(
        directory: Annotated[str, "Directory to check."]
    ) -> Annotated[Tuple[int, List[str]], "Status code and list of documentation files"]:
        files = os.listdir(docs_path + directory)
        return 0, files

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Check the contents of a documentation file.")
    def see_doc_file(
        filename: Annotated[str,
                            "Name and path of documentation file to check."]
    ) -> Annotated[Tuple[int, str], "Status code and file contents."]:
        with open(docs_path + filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
        file_contents = "".join(formatted_lines)

        return 0, file_contents

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Modify the contents of a documentation file.")
    def modify_doc_file(
        filename: Annotated[str, "Name and path of documentation file to modify."],
        new_content: Annotated[str,
                               "New content to replace the old content in the documentation file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        with open(docs_path + filename, "w", encoding="utf-8") as file:
            file.write(new_content)
        return 0, "Documentation file modified successfully"