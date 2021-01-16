<template>
    <div class="map-chart" id="map">
</template>

<script>
import echarts from 'echarts'
import mapJson from '@/static/map.json'
export default {
    mounted () {
        this.initMap()
    },

    methods: {
        initMap () {
            var myChart = echarts.init(document.getElementById('map'));
            echarts.registerMap('New York', mapJson, {});
            var option = {
                series: [{
                    type: 'map',
                    mapType: 'New York'
                }]
            };
            myChart.setOption(option)
        }
    }
}
</script>



