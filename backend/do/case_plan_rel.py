from sqlalchemy import Column, Integer, ForeignKey

from server import db

case_plan_rel = db.Table(
    'case_plan_rel',
    Column("testcase_id", Integer, ForeignKey("testcase.id", ondelete="CASCADE"), primary_key=True),
    Column("plan_id", Integer, ForeignKey("plan.id", ondelete="CASCADE"), primary_key=True)
)