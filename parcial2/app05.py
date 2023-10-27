"""
   APlicación de escritorio que pregunta el nommbre
   de una persona.
"""
from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("mensaje", "hola "+ name.value)
    #message2.value = "hola "+ name.value

app= App(title="ICI App")

message= Text(app, text="¿Cómo te llamas?")
name= TextBox(app, multiline=True, height=2, width=40)
message2=Text(app)
button=PushButton(app, text="Click", command=say_hello )
app.display()