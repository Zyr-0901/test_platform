from typing import List

from do.testcase_do import TestcaseDo
from server import db_session


class TestcaseDao:
    def get(self, testcase_id) -> TestcaseDo:
        return db_session.query(TestcaseDo).filter_by(id=testcase_id).first()

    def all(self) -> List[TestcaseDo]:
        return db_session.query(TestcaseDo).all()

    def create(self, testcase_do: TestcaseDo) -> TestcaseDo:
        db_session.add(testcase_do)
        db_session.commit()
        return testcase_do

    def update(self, testcase_do: TestcaseDo) -> TestcaseDo:
        db_session.query(TestcaseDo).filter_by(id=testcase_do.id).update(testcase_do.as_dict())
        db_session.commit()
        return testcase_do

    def delete(self, testcase_id):
        db_session.query(TestcaseDo).filter_by(id=testcase_id).delete()
        db_session.commit()

    def get_by_name(self, name):
        return db_session.query(TestcaseDo).filter_by(name=name).first()


