// vue.config.js
module.exports = {
    chainWebpack: config => {
        config
        .plugin('html')
        .tap(args => {
            args[0].title= '爬虫数据可视化系统'
            return args
        })
    },
    devServer: {
        proxy: {
          '/': {
            target: 'http://101.35.53.113:5000',
            changeOrigin: true,
            // pathRewrite: {
            //   '^/server-eggs': ''
            // }
          }
        }
    }
}