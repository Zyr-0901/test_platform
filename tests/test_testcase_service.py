from do.testcase_do import TestcaseDo
from service.testcase_service import TestcaseService


class TestTestcaseService:

    def setup_class(self):
        self.testcase = TestcaseService

    def test_get(self):
        self.testcase.get(1)

    def test_all(self):
        self.testcase.list()

    def test_create(self):
        testcase_do = TestcaseDo(name="测试用例1", step="步骤一", method="tests/test_add_1.py", remark="测试")
        create_result = self.testcase.create(testcase_do)
        assert create_result

    def test_create(self):
        testcase_do = TestcaseDo(id=1, name="测试用例111", step="步骤一11", method="tests/test_add_1.py", remark="测试111")
        update_result = self.testcase.update(testcase_do)

        assert update_result and update_result.name == "测试用例111" and update_result.method == "tests/test_add_1.py"

    def test_delete(self):
        result = self.testcase.delete(1)
        assert result



