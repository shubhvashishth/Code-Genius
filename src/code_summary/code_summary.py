'''
author : Shubham
Project : Code-Genius

'''

import os

from meta_ai_api import MetaAI

meta = MetaAI()

from meta_ai_api import MetaAI

def summarize_code(file_path):
    if not os.path.exists(file_path):
        return "[error]File does not exist.[/error]"
    
    with open(file_path, 'r') as file:
        code_content = file.read()

    response = meta.prompt(message=f"Please understand the following code and give the summary in a clear concise manner:\n\n{code_content}")

    # Return the summary
    return response['message']