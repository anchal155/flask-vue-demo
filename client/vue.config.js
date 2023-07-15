module.exports = {
    devServer: {
      contentBase: 'src/assets',
      proxy:'http://localhost:5001'
    },
    chainWebpack: config => {
      config.module
        .rule('Vue')
        .rule('vue')
        .test(/\.vue$/)
        .use('vue-loader')
        .loader('vue-loader')
        .end();
    }
};