from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from server import db


class BuildDo(db.Model):
    __tablename__ = "build"

    # 创建字段映射关系
    id = Column(Integer, primary_key=True, autoincrement=True)
    plan_id = Column(Integer, ForeignKey('plan.id', ondelete="CASCADE"))
    report_url = Column(String(255))
    create_time = Column(DateTime, nullable=True, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 提供对象转json
    def as_dict(self):
        return {
            "id": self.id,
            "plan_id": self.plan_id,
            "report_url": self.report_url,
            "create_time": str(self.create_time)
        }
