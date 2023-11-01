"""
app main module
"""
import gradio as gr
import pyttsx3
def create_avator_audio(text):
    """
    doc
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # engine.say(text)
    engine.save_to_file(text, 'male.wav')
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file(text, 'female.wav')
def get_video(gender):
    """
    doc
    """
    if gender == "male":
        return "male.wav"
    return "female.wav"
with gr.Blocks(theme = gr.themes.Monochrome()) as app:
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
                msg = gr.Textbox(label="USER", placeholder = "Enter user message here")
                submit_button = gr.Button("Submit")
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
if __name__=="__main__":
    app.queue(concurrency_count = 1)
    app.launch(debug = True, enable_queue = True, share = True)
