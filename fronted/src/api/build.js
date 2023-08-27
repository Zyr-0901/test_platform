
import instance from "./http"

const build = {
     //获取构建记录信息
    getBuild(params) {
        return instance({
            method: 'GET',
            url: '/build',
            params: params
        })
    },
     //创建构建记录
    addBuild(data) {
        return instance({
            method: 'POST',
            url: '/build',
            data: data
        })
    },
     //删除构建记录信息
    deleteBuild(params) {
        return instance({
            method: 'DELETE',
            url: '/build',
            params: params
        })
    },


}

export default build