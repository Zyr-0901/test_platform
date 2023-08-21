from dao.testcase_dao import TestcaseDao
from do.testcase_do import TestcaseDo

testcase_dao = TestcaseDao()


class TestcaseService:
    def get(self, testcase_id) -> TestcaseDo:
        return testcase_dao.get(testcase_id)

    def get_by_name(self, name) -> TestcaseDo:
        return testcase_dao.get_by_name(name)

    def list(self):
        return testcase_dao.all()

    def create(self, testcase_do: TestcaseDo):
        info = self.get_by_name(testcase_do.name)
        if info:
            return False
        else:
            return testcase_dao.create(testcase_do)

    def update(self, testcase_do: TestcaseDo):
        info = self.get(testcase_do.id)
        if info:
            return testcase_dao.update(testcase_do)
        else:
            return False

    def delete(self, testcase_id):
        info = self.get(testcase_id)
        if info:
            testcase_dao.delete(testcase_id)
            return True
        else:
            return False
