<template>
  <div id="map">
    <div>
      <Echart
        :options="options"
        id="centerUp"
        height="7rem"
        width="100%"
      ></Echart>
    </div>
  </div>
</template>

<script>
import echarts from "echarts";
import mapJson from "@/static/map.json";
import Echart from "@/common/echart";
export default {
  data() {
    return {
      options: {},
    };
  },
  mounted() {
    this.initMap();
  },
  components: {
    Echart,
  },
  methods: {
    // https://blog.csdn.net/wscwj8/article/details/90903710 先放个代码链接，明天再做
    initMap() {
      echarts.registerMap("New York", mapJson, {});
      this.options = {
        tooltip: {
          trigger: "item",
          formatter: "{b}",
        },
        series: [
          {
            type: 'map',
            mapType: "New York",
            label: {
              show: true,
            },
            data: [
              { name: "Bronx", value: 1 },
              { name: "Manhattan", value: 2 },
              { name: "Queens", value: 3 },
              { name: "Brooklyn", value: 4 },
              { name: "Staten Island", value: 5 },
            ],
          },
        ],
      };
    },
  },
};
</script>



