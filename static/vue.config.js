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
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            // pathRewrite: {
            //   '^/server-eggs': ''
            // }
          }
        }
    }
}