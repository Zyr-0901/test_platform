from do.plan_do import PlanDo
from service.plan_service import PlanService


class TestPlanService:

    def setup_class(self):
        self.plan = PlanService()

    def test_get(self):
        self.plan.get(1)

    def test_all(self):
        self.plan.list()

    def test_create(self):
        plan_do = PlanDo(name="计划4")
        create_result = self.plan.create([1,2], plan_do)
        assert create_result

    def test_delete(self):
        result = self.plan.delete(2)
        assert result



