from flask import Flask,render_template

# create App

app=Flask(__name__)

# create a function to interact with browser
# decorator as router
@app.route('/')
def show():
    # read data and override the template
    # data=
    return render_template("index.html")
# 可乐鸡翅         257
# 西红柿炒鸡蛋       256
# 糖醋排骨         254
# 红烧茄子         252
# 酸辣土豆丝        250
if __name__=="__main__":
    app.run()