"""
   APlicación de escritorio que pregunta el nommbre
   de una persona.
"""
from guizero import App, Text, PushButton, TextBox

app= App(title="ICI App")

message= Text(app, text="¡Cómo te llamas?")
name= TextBox(app)

app.display()