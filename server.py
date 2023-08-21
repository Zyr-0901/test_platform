from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

# 实例化接口实例
app = Flask(__name__)
api = Api(app)

# 解决浏览器的跨域问题
CORS(app, supports_credentials=True)

# 用例的命名空间
username = "root"
password = 'root'
server = "127.0.0.1:3306"
database = "test_platform"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"
# JWTManager 绑定 app
jwt = JWTManager(app)
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)
# 为了有类型提示所做的声明
db_session: Session = db.session


def register_router():
    # 如果出现循环导入，把导包语句放在方法内执行。并且调用此函数
    from controller.testcase_controller import case_ns
    from controller.plan_controller import plan_ns
    from controller.build_controller import build_ns
    # from controller.user_controller import user_ns
    api.add_namespace(case_ns, "/testcase")
    api.add_namespace(plan_ns, "/plan")
    api.add_namespace(build_ns, "/build")
    # api.add_namespace(user_ns, "/user")


if __name__ == '__main__':
    register_router()
    app.run(debug=True, port=5001)
