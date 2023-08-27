
import instance from "./http"

const plan = {
     //获取计划信息
    getPlan(params) {
        return instance({
            method: 'GET',
            url: '/plan',
            params: params
        })
    },
     //创建计划
    addPlan(data) {
        return instance({
            method: 'POST',
            url: '/plan',
            data: data
        })
    },
     //删除计划信息
    deletePlan(params) {
        return instance({
            method: 'DELETE',
            url: '/plan',
            params: params
        })
    },


}

export default plan