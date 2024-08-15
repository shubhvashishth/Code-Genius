'''
author : Shubham
Project : Code-Genius

'''

import os

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.theme import Theme
from emoji import emojize

# from src.code_completion.code_completion import CodeCompletion
# from src.bug_detection.bug_detection import BugDetection
# from src.code_documentation.code_documentation import CodeDocumentation
from src.code_summary.code_summary import summarize_code

custom_theme = Theme({
    "welcome": "bold cyan",
    "command": "bold green",
    "info": "bold yellow",
    "error": "bold red",
    "success": "bold blue",
})

# Initialize the rich console with custom theme
console = Console(theme=custom_theme)

# Initialize the rich console with custom theme
console = Console(theme=custom_theme)

def print_welcome_message():
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="command")
    table.add_column("Description", style="command")
    table.add_row(emojize(":mag_right: detect <file_path>"), "Perform bug detection on the file")
    table.add_row(emojize(":book: document <file_path>"), "Generate documentation for the file")
    table.add_row(emojize(":page_facing_up: summary <file_path>"), "Get a summary of the code in the file")
    table.add_row(emojize(":pencil: complete <code_context>"), "Get code completion suggestion")
    
    commands_panel = Panel(
        Align.center(table),
        title=emojize(":rocket: CodeGenius :rocket:"),
        title_align="center",
        expand=False,
        border_style="bold magenta"
    )
    console.print(commands_panel)

def handle_command(command):
    try:
        command = command.strip().split(maxsplit=1)
        
        if len(command) < 2:
            if command[0] == "quit" or command[0] == "abort":
                console.print(emojize(":wave: Exiting CodeGenius Goodbye! :wave:"))
                return False
            console.print("[error]Invalid command. Please provide the necessary arguments or type 'quit' to exit.[/error]")
            return True

        action, argument = command

        if action == "detect":
            # perform_bug_detection(argument)
            pass
        elif action == "document":
            # generate_documentation(argument)
            pass
        elif action == "complete":
            # get_code_completion(argument)
            pass
        elif action == "summary":
            summary = summarize_code(argument)
            
            summary_panel = Panel(
                Text.from_markup(f"\n\n{summary}"),
                title=emojize(":scroll: Summary"),
                title_align="center",
                expand=False,
                border_style="bold yellow", 
                style="white"               
            )
            console.print(summary_panel)
        else:
            console.print("[error]Unknown command. Please use one of the available commands or type 'quit' to exit.[/error]")
        
    except Exception as e:
        console.print(f"[error]An error occurred: {e}[/error]")
    
    return True


def main():

    print_welcome_message()

    while True:
        command = Prompt.ask(
            "\n[bold green]What would you like to do?[/bold green] [italic cyan](Type 'quit' or 'abort' to exit)[/italic cyan]"
        )
        if not handle_command(command):
            break

if __name__ == "__main__":
    main()
    