"""
noun generator module will take the string and return the nouns list in string.
"""
import os
import openai
from dotenv import load_dotenv, find_dotenv
from audio_thread import voice_class
from video_thread import video_class
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
def chat_completion(messages):
    """
    code_debug method take topic type link tone length as input and return the output
    according to the prompt.

    Parameters
    ----------
    text: str
        user message or text.
    Return
    ------
        return generated response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages,
            temperature = 1,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
            stream = True,
        )
        collected_messages = []
        for chunk in response:
            delta = chunk['choices'][0]['delta']
            if 'content' in delta.keys():
                collected_messages.append(delta['content'])
        return collected_messages
    except Exception as error:
        print("OPenAI reponse (streaming) error" + str(error))
        return 503
    
def set_user_response(user_message, chat_history):
    """
    doc
    """
    chat_history +=  [[user_message, None]]
    return "", chat_history
def generated_message(messages):
    """
    doc
    """
    formatted_messages = [
        {
            'role' : 'system',
            'content' : 'you are a helpful assistant'
        }
    ]
    for message in messages:
        formatted_messages.append({
            'role' : 'user',
            'content' : message[0]
        })
        if message[1] is not None:
            formatted_messages.append({
                'role' : 'assistant',
                'content' : message[1]
            })
    return formatted_messages
def generate_response(chat_history):
    """
    doc
    """
    messages = generated_message(chat_history)
    bot_message = chat_completion(messages)
    audio_text = ' '.join([str(chunk) for chunk in bot_message])
    voice_class(audio_text).start()
    video_class("female.wav", "demo/img/image1.jpg").start()
    chat_history[-1][1] = ""
    for message in bot_message:
        chat_history[-1][1] += message
        yield chat_history
