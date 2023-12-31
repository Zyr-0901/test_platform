from typing import List
from sqlalchemy.orm import relationship
from server import db
from do.testcase_do import TestcaseDo
from do.case_plan_rel import case_plan_rel
from sqlalchemy import Column, Integer, String


# 测试用例对象与数据库映射
class PlanDo(db.Model):
    __tablename__ = 'plan'

    # 设置表字段映射
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    testcases: List[TestcaseDo] = relationship("TestcaseDo", secondary=case_plan_rel, backref="plans")

    # 提供对象转json
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "testcases": [c.as_dict() for c in self.testcases]
        }
