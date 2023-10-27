from guizero import App, Text, PushButton

def say_hello():
    message2.value = "ICI Rocks"  # con .value le damos la Propiedad del widget

app= App(title="ICI App")

message= Text(app, text="Welcome to ICI App!")
message2= Text(app)
button= PushButton(app, text="click me", command=say_hello)

app.display()