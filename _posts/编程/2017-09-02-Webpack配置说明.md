---
layout: post
title: Webpack配置说明
category: 编程
tag: Webpack，前端
exception: 前端Webpack打包项目，现在是最常见不过的了。网上的脚手架工具也很多，会自动加载webpack和相应的配置，但自己能看懂这些配置也是相当重要的。
readtime: 16
---

# 配置文件
````javascript
const HtmlWebpackPlugin = require('html-webpack-plugin'); 
const webpack = require('webpack');

module.exports = {
  // 构建目标，默认值是web，还可为node,webworker,electron等
  target: 'web',
  // 简单单一入口
  // entry: './path/to/my/entry/file.js',
  // 常用入口场景
  entry: {
    app: './src/app.js',
    vendors: './src/vendors.js'
  },
  // 编译文件输出，可以传入的值：[id],[name],[hash],[chunkhash]
  output: {
    filename: 'bundle.js',
    path: '/home/project/public/assets/'
  },
  // 加载器，将资源文件作为参数的来源，然后返回新的资源文件
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [resolve('src'), resolve('test')],
        options: { transpileOnly: false }
      }
     ]
   },
   // 插件的目的在于解决loader无法实现的事情
   // webpack 插件是一个具有 apply 属性的 JavaScript 对象。 apply 属性会被 webpack compiler 调用，并且 compiler 对象可在整个 compilation 生命周期访问
   plugins: [
     new webpack.optimize.UglifyJsPlugin(),
     new HtmlWebpackPlugin({template: './src/index.html'})
   ]
}
````

# 加载器
* `raw-loader`：加载文件原始内容(utf-8)
* `val-loader`： 将代码作为模块执行，并将 exports 转为 JS 代码
* `url-loader`： 像 file loader 一样工作，但如果文件小于限制，可以返回 data URL
* `file-loader`： 将文件发送到输出文件夹，并返回（相对）URL
* `json-loader`： 加载 JSON 文件（默认包含）
* `json5-loader`： 加载和转译 JSON 5 文件
* `cson-loader`： 加载和转译 CSON 文件
* `script-loader`： 在全局上下文中执行一次 JavaScript 文件（如在 script 标签），不需要解析
* `babel-loader`： 加载 ES2015+ 代码，然后使用 Babel 转译为 ES5
* `traceur-loader`： 加载 ES2015+ 代码，然后使用 Traceur 转译为 ES5
* `typescript-loader`： 像 JavaScript 一样加载 TypeScript
* `coffee-loader`： 像 JavaScript 一样加载 CoffeeScript
* `html-loader`： 导出 HTML 为字符串，需要引用静态资源
* `pug-loader`： 加载 Pug 模板并返回一个函数
* `jade-loader`： 加载 Jade 模板并返回一个函数
* `markdown-loader`： 将 Markdown 转译为 HTML
* `posthtml-loader`： 使用 PostHTML 加载并转换 HTML 文件
* `handlebars-loader`： 将 Handlebars 转移为 HTML
* `style-loader`： 将模块的导出作为样式添加到 DOM 中
* `css-loader`： 解析 CSS 文件后，使用 import 加载，并且返回 CSS 代码
* `less-loader`： 加载和转译 LESS 文件
* `sass-loader`： 加载和转译 SASS/SCSS 文件
* `stylus-loader`： 加载和转译 Stylus 文件
* `postcss-loader`： 使用 PostCSS 加载和转译 CSS/SSS 文件
* `mocha-loader`： 使用 mocha 测试（浏览器/NodeJS）
* `eslint-loader`： PreLoader，使用 ESLint 清理代码
* `jshint-loader`： PreLoader，使用 JSHint 清理代码
* `jscs-loader`： PreLoader，使用 JSCS 检查代码样式
* `coverjs-loader`： PreLoader，使用 CoverJS 确定测试覆盖率
* `vue-loader`： 加载和转译 Vue 组件
* `polymer-loader`： 使用选择预处理器(preprocessor)处理，并且 require() 类似一等模块(first-class)的 Web 组件
* `angular2-template-loader`： 加载和转译 Angular 组件

# 插件
* `BannerPlugin`：为每个chunk文件头部添加banner
* `CommonsChunkPlugin`：将公用的模块拆出来，建立单独的文件
* `ComponentWebpackPlugin`：使用组件
* `CompressionWebpackPlugin`：预压缩资源
* `DefinePlugin`：允许你创建一个在编译时可以配置的全局常量
* `EnvironmentPlugin`：是在process.env 键(key) 上使用DefinePlugin的简写方式
* `ExtractTextWebpackPlugin`：将所有的 入口chunk (entry chunks) 中的 require("style.css") 移动到分开的 css 文件
* `HtmlWebpackPlugin`：简化了HTML文件的创建，以便为您的 webpack bundle 提供服务
* `I18nWebpackPlugin`：添加i18n支持到打包
* `LoaderOptionsPlugin`：帮助人们从 webpack 1 迁移至 webpack 2
* `NormalModuleReplacementPlugin`：将与resourceRegExp匹配的资源替换为newResource
* `NpmInstallWebpackPlugin`：使用 Webpack 通过自动安装和保存依赖关系来提升开发速度
* `ProvidePlugin`：自动加载模块
* `SourceMapDevToolPlugin`：为资源添加SourceMaps
* `UglifyjsWebpackPlugin`：使用 UglifyJS 去压缩你的JavaScript代码

# 参考资料
* [webpack2.2中文文档](http://www.css88.com/doc/webpack2/)
* [webpack官方组织](https://webpack.js.org/)
* [webpack开源文档](http://webpack.github.io/docs/)
















