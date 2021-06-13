from flask import Flask,render_template

# create App

app=Flask(__name__)

# create a function to interact with browser
# decorator as router
@app.route('/')
def show():
    # read data and override the template
    return render_template("index.html")

if __name__=="__main__":
    app.run()