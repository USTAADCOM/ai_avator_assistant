"""
app main module
"""
import gradio as gr
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
                    submit_button = gr.Button("Woman")
                    submit_button = gr.Button("Man")
    ######################  back-end #########################
if __name__=="__main__":
    app.queue(concurrency_count = 1)
    app.launch(debug = True, enable_queue = True, share = True)
