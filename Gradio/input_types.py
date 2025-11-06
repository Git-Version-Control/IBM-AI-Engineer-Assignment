"""
Common Inputs
Gradio has a large number of input types. The more commonly encountered ones are listed below:

Checkbox: A checkbox that can be set to True or False.
CheckboxGroup: An input type that allows users to select multiple values from a predefined checkbox list.
Dropdown: An input type that provides a dropdown list where, by default, one value can be selected. If multiselect is set to True, then one or more values can be selected.
File: An input type that allows a user to upload a file.
Image: An input type that allows the user to select or upload an image.
Radio: An input type that forces the user to choose one value.
Slider: 
    An input type that provides a slider where a value must be selected between a minimum and a maximum range. 
    The value parameter defines the default value, and step provides the increment value. 
    Setting the minimum, maximum, and step values to integers will select integer values.
Textbox: An expandible text box that allows the user to type in text.
Common Outputs
Many of Gradio's input types can also function as outputs. 
The available output types depend on the output of the function provided to Interface. 
In practice, for most LLM applications, the output type is typically text. As such, a suitable choice is either gr.Textbox(), or just "text", which offers an expandable text box.

Another frequently encountered output type is Label. 
Label is typically used for classification tasks, and can output the predicted probabilities of each class. 
If you have a large number of classes, you can use the num_top_classes parameter to control the number of classes that are outputted. 
For instance, if you have 1000 classes, setting Label(num_top_classes=3) would output just the three classes with the highest predicted probabilities instead of the predicted probabilities for all classes.
"""

import gradio as gr

def sentence_builder(quantity, tech_worker_type, countries, place, activity_list, morning):
    return f"""The {quantity} {tech_worker_type}s from {" and ".join(countries)} went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""

demo = gr.Interface(
    fn=sentence_builder,
    inputs=[
        gr.Slider(3, 20, value=4, step=1, label="Count", info="Choose between 3 and 20"),
        gr.Dropdown(
            ["Data Scientist", "Software Developer", "Software Engineer"], 
            label="tech_worker_type", 
            info="Will add more tech worker types later!"
        ),
        gr.CheckboxGroup(["Canada", "Japan", "France"], label="Countries", info="Where are they from?"),
        gr.Radio(["office", "restaurant", "meeting room"], label="Location", info="Where did they go?"),
        gr.Dropdown(
            ["partied", "brainstormed", "coded", "fixed bugs"], 
            value=["brainstormed", "fixed bugs"], 
            multiselect=True, 
            label="Activities", 
            info="Which activities did they perform?"
        ),
        gr.Checkbox(label="Morning", info="Did they do it in the morning?"),
    ],
    outputs="text",
    examples=[
        [3, "Software Developer", ["Canada", "Japan"], "restaurant", ["coded", "fixed bugs"], True],
        [4, "Data Scientist", ["Japan"], "office", ["brainstormed", "partied"], False],
        [10, "Software Engineer", ["Canada", "France"], "meeting room", ["brainstormed"], False],
        [8, "Data Scientist", ["France"], "restaurant", ["coded"], True],
    ]
)

demo.launch(server_name="127.0.0.1", server_port= 7860)