from flask import request
from flask_restx import Resource, Namespace, fields
from do.testcase_do import TestcaseDo
from server import api
from service.testcase_service import TestcaseService

testcase_service = TestcaseService()
case_ns = Namespace("testcase", description="用例管理")


@case_ns.route("")
class TestcaseController(Resource):
    get_parser = api.parser()
    get_parser.add_argument("id", type=int, location="args")

    @case_ns.expect(get_parser)
    def get(self):
        """
        测试用例获取
        :return: 用例列表
        """
        testcase_id = request.args.get("id")
        if testcase_id:
            result = testcase_service.get(testcase_id)
            if result:
                data = [result.as_dict()]
                return {"code": 0, "msg": "success", "data": data}
            else:
                return {"code": 400, "msg": "data is not exists"}
        else:
            result = testcase_service.list()
            data = [c.as_dict() for c in result]
        return {"code": 0, "msg": "success", "data": data}

    post_model = case_ns.model("post_model", {
        "name": fields.String,
        "step": fields.String,
        "method": fields.String,
        "remark": fields.String
    })

    @case_ns.expect(post_model)
    def post(self):
        """
        测试用例新建
        :return:
        """
        data = request.json
        testcase_do = TestcaseDo(**data)
        result = testcase_service.create(testcase_do)
        if result:
            return {"code": 0, "msg": f"{result.name} add success"}
        else:
            return {"code": 400, "msg": f"{result.name} add fail"}

    update_model = case_ns.model("update_model", {
        "id": fields.Integer,
        "name": fields.String,
        "step": fields.String,
        "method": fields.String,
        "remark": fields.String
    })

    @case_ns.expect(update_model)
    def put(self):
        """
        测试用例更新
        :return:
        """
        data = request.json
        testcase_do = TestcaseDo(**data)
        result = testcase_service.update(testcase_do)
        if result:
            return {"code": 0, "msg": f"{result.name} update success"}
        else:
            return {"code": 400, "msg": f"{result.name} update fail"}

    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, location="args")

    @case_ns.expect(delete_parser)
    def delete(self):
        """
        测试用例删除
        :return:
        """
        testcase_id = request.args.get("id")
        if testcase_id:
            testcase_service.delete(testcase_id)
            return {"code": 400, "msg": f"{testcase_id} delete success"}
        else:
            return {"code": 400, "msg": "delete fail"}
