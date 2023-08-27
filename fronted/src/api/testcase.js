
import instance from "./http"

const testcase = {
     //获取用例信息
    getTestcase(params) {
        return instance({
            method: 'GET',
            url: '/testcase',
            params: params
        })
    },
     //创建用例
    addTestcase(data) {
        return instance({
            method: 'POST',
            url: '/testcase',
            data: data
        })
    },
     //更新用例信息
    editTestcase(data) {
        return instance({
            method: 'UPDATE',
            url: '/testcase',
            data: data
        })
    },
     //删除用例信息
    deleteTestcase(params) {
        return instance({
            method: 'DELETE',
            url: '/testcase',
            params: params
        })
    },


}

export default testcase