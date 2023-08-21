from typing import List
from do.plan_do import PlanDo
from server import db_session


class PlanDao:
    def get(self, plan_id) -> PlanDo:
        return db_session.query(PlanDo).filter_by(id=plan_id).frist()

    def all(self) -> List[PlanDo]:
        return db_session.query(PlanDo).all()

    def create(self, plan_do: PlanDo) -> PlanDo:
        db_session.add(plan_do)
        db_session.commit()
        return plan_do

    def delete(self, plan_id):
        db_session.query(PlanDo).filter_by(id=plan_id).delete()
        db_session.commit()

    def get_by_name(self, name):
        return db_session.query(PlanDo).filter_by(name=name).first()
