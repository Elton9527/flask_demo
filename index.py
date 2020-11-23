from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "elton"

# 路由默认只支持GET，如果需要增加，需要自行指定
@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello World Elton"
    return  render_template("index.html")


@app.route("/saytemplate")
def sayTemplate():
    #模板传参
    url_str="www.mamamiya.com"
    return  render_template("say.html", url_str=url_str)


# 路由传参
@app.route("/sayhi/<name>")
def sayHi(name):
    return "My name is %s" % name

# 对路由参数类型进行限制参数类型
@app.route("/sayage/<int:age>")
def sayAge(age):
    return "My age is %d" % age

# The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
# 需要secret_key 做秘钥混淆

@app.route("/testform", methods=['GET', 'POST'])
def indexForm():
    # 引入request
    # request.form.get() 获取表单
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            #print("参数不完整")
            # 引入flash ，将信息打印到页面
            flash("参数不完整")


        if password != password2:
            #print("密码不一致")
            flash("密码不一致")
    return render_template("demo_form.html")


if __name__ == '__main__':
    app.run()