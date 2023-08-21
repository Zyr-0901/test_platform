from dao.plan_dao import PlanDao
from do.plan_do import PlanDo
from service.testcase_service import TestcaseService

plan_dao = PlanDao()
testcase_service = TestcaseService()


class PlanService:
    def get(self, plan_id) -> PlanDo:
        return plan_dao.get(plan_id)

    def get_by_name(self, name) -> PlanDo:
        return plan_dao.get_by_name(name)

    def list(self):
        return plan_dao.all()

    def create(self, testcase_id_list, plan_do: PlanDo):
        info = self.get_by_name(plan_do.name)
        if info:
            return False
        else:
            testcase = [testcase_service.get(testcase_id) for testcase_id in testcase_id_list]
            plan_do.testcases = testcase
            return plan_dao.create(plan_do)

    def delete(self, plan_id):
        info = self.get(plan_id)
        if info:
            plan_dao.delete(plan_id)
            return True
        else:
            return False
