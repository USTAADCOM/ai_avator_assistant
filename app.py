"""
app main module
"""
import gradio as gr
from generate_message import generate_response, set_user_response
def get_video(gender):
    """
    doc
    """
    if gender == "male":
        return "male.wav"
    return "female.wav"
with gr.Blocks(theme = gr.themes.Soft()) as app:
    gr.Markdown(
        '''
        <div style="text-align:center;">
            <span style="font-size:3em; font-weight:bold;">AI AVATOR ASSISTANT</span>
        </div>
        '''
    )
    with gr.Row():
        with gr.Row():
            with gr.Column(scale = 2):
                chatbot = gr.Chatbot()
                message = gr.Textbox(label="USER", placeholder = "Enter user message here")
                state = gr.State()
        with gr.Row():
            with gr.Column(scale = 2):
                output_video = gr.Video(label = "Avator Video").style(height="300px")
                with gr.Row():
                    male_button = gr.Button("Male")
                    female_button = gr.Button("Female")
                    male = gr.Textbox(value = "male", visible = False)
                    female = gr.Textbox(value = "female", visible = False)
    ######################  back-end #########################
            male_button.click(
                fn = get_video,
                inputs = male,
                    outputs = [output_video]
                )
            female_button.click(
                fn = get_video,
                inputs = female,
                    outputs = [output_video]
                )
            message.submit(set_user_response, [message, chatbot],
                           [message, chatbot],
                           queue=False).then(generate_response, chatbot, chatbot)
if __name__=="__main__":
    app.queue(concurrency_count = 1)
    app.launch(debug = True, enable_queue = True, share = True)
