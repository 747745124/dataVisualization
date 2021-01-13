<template>
    <div class="testChart" id="testChart" ></div>
</template>

<script>
export default {
    name: 'TestEchart',
    data () {
        // 可能用于传递数据
    },
    mounted(){
        this.drawLine();
    },
    methods: {
        drawLine(){
            //部分引入
            var echarts = require('echarts/lib/echarts');
            // 引入柱状图
            require('echarts/lib/chart/bar');
            // 引入提示框和标题组件
            require('echarts/lib/component/tooltip');
            require('echarts/lib/component/title');

            // 基于准备好的dom，初始化echarts实例
            let myChart = echarts.init(document.getElementById('testChart'))
            // 绘制图表
            myChart.setOption({
                title: { text: '在Vue中使用echarts' },
                tooltip: {},
                xAxis: {
                    data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                },
                yAxis: {},
                series: [{
                    name: '好耶',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20]
                }]
            });
        }
    }
}

</script>
<style scoped>
    .testChart {
        display: inline-block;
        min-width: 200px;
        height: 400px;
        width: 50%;
    }
</style>