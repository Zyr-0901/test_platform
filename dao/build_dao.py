from typing import List
from do.build_do import BuildDo
from server import db_session


class BuildDao:
    def get(self, build_id) -> BuildDo:
        return db_session.query(BuildDo).filter_by(id=build_id).frist()

    def all(self) -> List[BuildDo]:
        return db_session.query(BuildDo).all()

    def create(self, build_do: BuildDo) -> BuildDo:
        db_session.add(build_do)
        db_session.commit()
        return build_do

    def delete(self, build_id):
        db_session.query(BuildDo).filter_by(id=build_id).delete()
        db_session.commit()

    def get_by_name(self, name):
        return db_session.query(BuildDo).filter_by(name=name).first()
