from flask import Flask

#Here Flask keyword is a class imported from flask module
#In the below 
app=Flask(__name__)

@app.route('/')
def Home():
    return 'Hello World'

app.run(port=5000)