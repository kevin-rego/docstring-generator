from langchain.prompts import PromptTemplate, ChatPromptTemplate


def doc_string_generator(language):
    prompt_text = f"""
    You are an expert in docstring creation for code blocks.    
    Create comprehensive docstrings for the provided code block, ensuring that it explains the function/method/class/module correctly. 

    {f'Language of the code block is {language}' if f'{language}' != "" else 'Please identify the programming language of the code block' }

    Follow widely accepted formatting guidelines specific to the programming language in question.

    Use clear, concise, and formal language throughout the docstring.

    Clearly state the purpose of the code block, its parameters, return values, and provide usage examples if possible.

    Provide the docstring as the answer, without any additional information.

    The aim is to enhance code readability and provide developers with a clear understanding of the code's purpose and usage.

    Note: Remember to adapt the format and content of the docstring based on the programming language of the code block.

    =====================

    Here's an example of an answer for Python language:

    Example answer: 

        '''Sums two numbers and returns the result.

        Args:
            a (int): The first number to add.
            b (int): The second number to add.

        Returns:
            int: The sum of `a` and `b`.

        Examples:
            >>> add(1, 2)
            3
            >>> add(-1, 1)
            0
        '''

    Here's an example of an answer for Javascript language:

    Example answer:

       /*
        * Adds one to the supplied number
        *
        * @param {{{{number}}}} number - Number to add one to
        * @returns incremented number
        */

    ======================

    CODE: ``` {{code}} ```    

    ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(template=prompt_text)

    return prompt
