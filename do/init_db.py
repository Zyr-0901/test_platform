from server import db
from do.build_do import BuildDo
from do.testcase_do import TestcaseDo
from do.plan_do import PlanDo
from do.case_plan_rel import case_plan_rel

if __name__ == '__main__':
    db.create_all()
