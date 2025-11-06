import gradio as gr

def add_numbers(num1, num2):
    return num1 + num2

iface = gr.Interface(fn=add_numbers, 
                     inputs=[gr.Number(), gr.Number()], # Create two numerical input fields where users can enter numbers
                     outputs=gr.Number()) # Create numerical output fields)

iface.launch() # Launch the Gradio interface