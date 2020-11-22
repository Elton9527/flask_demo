from flask import Flask, render_template

app = Flask(__name__)


# 路由默认只支持GET，如果需要增加，需要自行指定
@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello World Elton"
    return  render_template("index.html")


# 路由传参
@app.route("/sayhi/<name>")
def sayHi(name):
    return "My name is %s" % name

# 对路由参数类型进行限制参数类型
@app.route("/sayage/<int:age>")
def sayAge(age):
    return "My age is %d" % age


if __name__ == '__main__':
    app.run()