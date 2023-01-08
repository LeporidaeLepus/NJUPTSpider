from NS_Utils import initLog, initDb, stopDb, formatTable
from NS_SpiderCore import Spider
from flask import Flask, request, render_template
from flask_bootstrap3 import Bootstrap

# 引入flask-bootstrap框架
app = Flask(__name__)
bootstrap = Bootstrap(app)


# 通过methods实现交互
@app.route('/', methods=['GET', 'POST'])
def defaultHandler():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        logger = initLog()
        connector = initDb(logger)
        A = Spider(request.form["url"], logger, timeout=10.0)
        SpiderResult = A.takeAction(connector)
        stopDb(logger, connector)
        return formatTable(SpiderResult)

# python开始运行时打开flask-bootstrap框架下端口9999的网页
if __name__ == "__main__":
    app.run(port=9999, debug=True)
