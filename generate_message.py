"""
noun generator module will take the string and return the nouns list in string.
"""
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
def generate(text = " "):
    """
    code_debug method take topic type link tone length as input and return the output
    according to the prompt.

    Parameters
    ----------
    text: str
        user message or text.
    Return
    ------
        return generated blog or essay.
    """
    full_text =  ""
    messages=[
        {
        "role": "system",
        "content": "As an assistant assist the user in a soft tone"
        },
        {
        "role": "user",
        "content": text
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature = 1,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
        # stream = True,
        stop = None
    )
    return response['choices'][0]['text']
    # try:
    #     for chunk in response:
    #         chunk_message = chunk['choices'][0]['delta'].get("content")
    #         full_text = full_text + chunk_message
    #         yield full_text
    # except Exception as error:
    #     print("OPenAI reponse (streaming) error" + str(error))
    #     return 503
