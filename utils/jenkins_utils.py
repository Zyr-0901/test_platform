from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:
    # Jenkins 服务
    BASE_URL = "http://43.138.100.186:8080/"
    # Jenkins 服务对应的用户名
    USERNAME = "admin"
    # Jenkins 服务对应的token
    PASSWORD = "1115d6ae3b2368dd0361f411054e1ff29e"
    JOB = "test_platfrom"

    @classmethod
    def invoke(cls, invoke_params):
        """
        执行构建任务
        :return:
        """
        jenkins_obj = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取Jenkins 的job 对象
        job = jenkins_obj.get_job(cls.JOB)
        # 构建hogwarts job， 传入的值必须是字典， key 对应 jenkins 设置的参数名
        # job.invoke(build_params={"methods": "CalculatorProject/test/cases/test_div.py"})
        job.invoke(build_params={"methods": invoke_params})
        # 获取job 最后一次完成构建的编号
        # http://43.138.100.186:8080/ck24/20/allure/
        last_build_number = job.get_last_buildnumber() + 1
        # pytest 用例名称 指定报告生成地址
        # pytest $task --alluredir=path
        report_url = f"{cls.BASE_URL}job/{cls.JOB}/{last_build_number}/allure/"
        return report_url
