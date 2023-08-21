from flask import request
from flask_restx import Resource, Namespace, fields
from do.build_do import BuildDo
from server import api
from service.build_service import BuildService
from utils.log_util import logger

build_service = BuildService()
build_ns = Namespace("build", description="构建记录管理")


@build_ns.route("")
class TestcaseController(Resource):
    build_get_parser = api.parser()
    build_get_parser.add_argument("id", type=int, location="args")

    @build_ns.expect(build_get_parser)
    def get(self):
        """
        构建记录获取
        :return:
        """
        build_id = request.args.get("id")
        if build_id:
            result = build_service.get(build_id)
            if result:
                data = [result.as_dict()]
                return {"code": 0, "msg": "success", "data": data}
            else:
                return {"code": 400, "msg": "data is not exists"}
        else:
            result = build_service.list()
            data = [c.as_dict() for c in result]
        return {"code": 0, "msg": "success", "data": data}

    build_post_model = build_ns.model("build_post_model", {
        "plan_id": fields.Integer
    })

    @build_ns.expect(build_post_model)
    def post(self):
        """
        构建记录新建
        :return:
        """
        data = request.json
        result = build_service.create(data.get("plan_id"))
        if result:
            return {"code": 0, "msg": f"{result.as_dict()['plan_id']} add success"}
        else:
            return {"code": 400, "msg": "build add fail"}

    build_delete_parser = api.parser()
    build_delete_parser.add_argument("id", type=int, location="args")

    @build_ns.expect(build_delete_parser)
    def delete(self):
        """
        构建记录删除
        :return:
        """
        build_id = request.args.get("id")
        if build_id:
            build_service.delete(build_id)
            return {"code": 400, "msg": f"{build_id} delete success"}
        else:
            return {"code": 400, "msg": "delete fail"}
