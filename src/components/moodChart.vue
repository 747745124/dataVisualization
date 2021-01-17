<template>
  <div id="map">
    <div>
      <div class="d-flex pt-2 pl-2">
        <span style="color: rgba(0, 183, 255, 0.55)">
          <icon name="chart-pie"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">心情指数</span>
        </div>
      </div>
      <Echart
        :options="options"
        id="rightUp"
        height="2.5rem"
        width="100%"
      ></Echart>
    </div>
  </div>
</template>

<script>
import dataJson from "@/static/data.json";
import Echart from "@/common/echart";
export default {
  props: {
    week: Number,
  },
  data() {
    return {
      options: {},
    };
  },
  mounted() {
    this.initChart();
  },
  watch: {
    week: {
      handler(newWeek) {
        // 当周数发生变动时，重设数据
        this.setWeekData(newWeek);
      },
    },
  },
  components: {
    Echart,
  },
  methods: {
    setWeekData(week) {
      let weekIndex = week - 1;
      let twitterTotal = dataJson.data[weekIndex].twitter.total;
      // 消极和积极的推文数量
      let negative = parseInt(
        twitterTotal * dataJson.data[weekIndex].twitter.moodIndex
      );
      let positive = twitterTotal - negative;
      this.options = {
        tooltip: {
          trigger: "item",
          formatter: "{b} : {c} ({d}%)",
        },
        series: [
          {
            name: "推文态度",
            type: "pie",
            radius: "80%",
            center: ["50%", "50%"],
            data: [
              { value: positive, name: "积极" },
              { value: negative, name: "消极" },
            ],
            roseType: "radius",
            label: {
              color: "rgba(255, 255, 255, 1)",
              fontSize: "12",
              formatter: "{b}\n{c} ({d}%)",
            },
            labelLine: {
              lineStyle: {
                color: "rgba(255, 255, 255, 0.3)",
              },
              smooth: 0.2,
              length: 10,
              length2: 20,
            },
            itemStyle: {
              color: function (param) {
                if (param.name == "积极") return "#1DA1F2";
                if (param.name == "消极") return "#EF1622";
              },
            },
            animationType: "scale",
            animationEasing: "elasticOut",
            animationDelay: function () {
              return Math.random() * 200;
            },
          },
        ],
      };
    },
    initChart() {
      this.setWeekData(1);
    },
  },
};
</script>