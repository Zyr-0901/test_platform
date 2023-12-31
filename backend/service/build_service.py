from dao.build_dao import BuildDao
from dao.plan_dao import PlanDao
from do.build_do import BuildDo
from utils.jenkins_utils import JenkinsUtils

build_dao = BuildDao()
plan_dao = PlanDao()


class BuildService:
    def get(self, build_id) -> BuildDo:
        return build_dao.get(build_id)

    def get_by_name(self, name) -> BuildDo:
        return build_dao.get_by_name(name)

    def list(self):
        return build_dao.all()

    def create(self, plan_id):
        # 获取要执行的用例
        plan = plan_dao.get(plan_id)
        if plan:
            testcases = [testcase.method for testcase in plan.testcases]
            methods = " ".join(testcases)
            report_url = JenkinsUtils.invoke(methods)
            build_do = BuildDo(plan_id=plan_id, report_url=report_url)
            return build_dao.create(build_do)
        else:
            return False

    def delete(self, build_id):
        info = self.get(build_id)
        if info:
            build_dao.delete(build_id)
            return True
        else:
            return False
