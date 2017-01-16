# Vue版本迁移教程学习
* Author: RaySun
* Date: 2016/12/03
* 教程地址：https://cn.vuejs.org/v2/guide/migration.html

# 从Vue1.X迁移
* 片段实例移除：每个组件有且仅有一个根节点，不再支持片段实例
* 生命周期钩子：beforeCompile移除，用created钩子替换；compiled钩子用mounted钩子替换；
attached钩子移除（依赖其他钩子使用自定义的dom内部方法），改变为使用mounted钩子里面this.$nextTick；
detached钩子移除，改变为使用destroyed钩子里面this.$nextTick；init钩子用新的beforeCreate钩子代替；
ready钩子用新的mouted钩子代替（注意：使用mounted钩子并不能保证实例已经插入文档，还应该在钩子函数中包含Vue.nextTick/vm.$nextTick）
* v-for数组参数的顺序：参数顺序由(index, value)变为(value, index)，与js新数组方法forEach、map保持一致
* vfor对象参数的顺序：同上，(key, value) 改为(value, key)
* $index and %key：隐式申明的$index和$key两个变量在新版中已经弃用了，取代的是在v-for中显式的申明
* track-by替换：track-by被key取代？
* v-for排序值：`v-for="number in 10"`将使得number从0到9迭代，现在变成从1到10
* prop的参数ceorce：组件中需要检查prop的值，创建一个内部的computed的值，而不再在props内部去定义
* prop的参数twoWay移除：props现在只能单项传递，要对父组件产生反向影响，子组件需要显式地传递一个事件而不是依赖隐式的双向绑定
* v-bind的.once和.sync修饰符移除：props现在只能单项传递
* 修改props弃用：组件内修改prop是反模式（不推荐的）
* 根实例的props替换：对于一个根实例（如new Vue({...})），只能用propsData而不是props
