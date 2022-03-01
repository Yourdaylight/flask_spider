import axios from 'axios';

export function regist(params){
    return axios({
        url:'/regist',
        method:'post',
        data:params
    })
}
export function login(params){
    return axios({
        url:'/login',
        method:'post',
        data:params
    })
}
export function display(params){
    return axios({
        url:'/display',
        method:'post',
        data:params
    })
}