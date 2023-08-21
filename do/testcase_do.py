from server import db
from sqlalchemy import *


# 测试用例对象与数据库映射
class TestcaseDo(db.Model):
    __tablename__ = 'testcase'

    # 设置表字段映射
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    step = Column(String(255))
    method = Column(String(255))
    remark = Column(String(255))

    # 提供对象转json
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "step": self.step,
            "method": self.method,
            "remark": self.remark
        }
