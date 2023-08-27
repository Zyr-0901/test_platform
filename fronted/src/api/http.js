// 完成http请求的基本配置
import axios from "axios";

// 创建实例
var instance = axios.create({
    headers: {
        'Content-Type': 'application/json'
    },
    timeout: 2500,
    baseURL: 'http://127.0.0.1:5001/'
})

//设置请求拦截器
instance.interceptors.request.use(
    config => {
        const token = localStorage.getItem("token")
        if(!token){
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config
    },
    error => {
        return Promise.reject(error)
    }
);

export default instance