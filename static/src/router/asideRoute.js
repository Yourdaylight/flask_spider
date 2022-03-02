import Positive from '../views/positive/positive.vue'
import Negative from '../views/negative/negative.vue'
import WordCloud from "../views/wordCloud/wordCloud.vue"
import Netease from "../views/netease/netease.vue"
import CommentsType from "../views/commentsType/commentsType.vue"

const asideRoute = [
    {
        path: '/positive',
        name: 'Top积极词汇统计',
        meta: {
            title: 'positive',
            // icon: 'fa fa-paper-plane'
        },
        component: Positive,
    },{
        path: '/negative',
        name: 'Top消极词汇统计',
        component: Negative,
        meta: {
            title: 'negative',
            // icon: 'fa fa-paper-plane'
        },
    },{
        path: '/wordCloud',
        name: '词云图分析',
        component: WordCloud,
        meta: {
            title: 'wordCloud',
            // icon: 'fa fa-paper-plane'
        },
    },{
        path: '/commentsType',
        name: '评论类型占比',
        component: CommentsType,
        meta: {
            title: 'commentsType',
            // icon: 'fa fa-paper-plane'
        },
    },{
        path: '/netease',
        name: '网易严选',
        component: Netease,
        meta: {
            title: 'netease',
            // icon: 'fa fa-paper-plane'
        },
    }
]

export default asideRoute