from flask import request
from flask_restx import Resource, Namespace, fields
from do.plan_do import PlanDo
from server import api
from service.plan_service import PlanService
from utils.log_util import logger

plan_service = PlanService()
plan_ns = Namespace("plan", description="测试计划管理")


@plan_ns.route("")
class PlanController(Resource):
    plan_get_parser = api.parser()
    plan_get_parser.add_argument("id", type=int, location="args")

    @plan_ns.expect(plan_get_parser)
    def get(self):
        """
        测试计划获取
        :return: 计划列表
        """
        plan_id = request.args.get("id")
        if plan_id:
            result = plan_service.get(plan_id)
            if result:
                data = [result.as_dict()]
                return {"code": 0, "msg": "success", "data": data}
            else:
                return {"code": 400, "msg": "data is not exists"}
        else:
            result = plan_service.list()
            data = [c.as_dict() for c in result]
        return {"code": 0, "msg": "success", "data": data}

    plan_post_model = plan_ns.model("plan_post_model", {
        "name": fields.String,
        "testcase_ids": fields.List(fields.Integer)
    })

    @plan_ns.expect(plan_post_model)
    def post(self):
        """
        测试计划新建
        :return:
        """
        # data 格式： {name="计划1"， testcase_ids=[1,2,3]}
        data = request.json
        testcase_ids = data.pop("testcase_ids")
        plan_do = PlanDo(**data)
        result = plan_service.create(testcase_ids, plan_do)
        if result:
            return {"code": 0, "msg": f"{result.name} add success"}
        else:
            return {"code": 400, "msg": f"add fail"}

    plan_delete_parser = api.parser()
    plan_delete_parser.add_argument("id", type=int, location="args")

    @plan_ns.expect(plan_delete_parser)
    def delete(self):
        """
        测试计划删除
        :return:
        """
        plan_id = request.args.get("id")
        if plan_id:
            plan_service.delete(plan_id)
            return {"code": 400, "msg": f"{plan_id} delete success"}
        else:
            return {"code": 400, "msg": "delete fail"}
