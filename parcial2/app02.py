from guizero import App, Text, PushButton

app= App(title="ICI App")

message= Text(app, text="Welcome to ICI App!")
button= PushButton(app, text="click me")

app.display()