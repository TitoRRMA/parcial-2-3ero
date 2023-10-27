"""
   APlicación de escritorio que pregunta el nommbre
   de una persona.
"""
from guizero import App, Text, PushButton, TextBox

def suma():
    app.info("suma", text= f"la suma es {int(num1.value)+int(num2.value)}")

app= App(title="ICI App")

message= Text(app, text="ingresa el primer numero")
num1= TextBox(app, multiline=True, height=2, width=40)
message= Text(app, text="ingresa el segundo numero")
num2= TextBox(app, multiline=True, height=2, width=40)
button=PushButton(app, text="Click", command=suma )
app.display()