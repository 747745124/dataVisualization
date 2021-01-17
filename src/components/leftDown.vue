<template>
  <div id="leftDown">
    <div class="d-flex pt-1 pl-3">
      <span style="color:rgba(0, 183, 255, 0.55)">
        <icon name="chart-line"></icon>
      </span>
    </div>
    <div>
      <Echart
        :options="options"
        id="leftDownChart"
        height="5.5rem"
        width="7rem"
      ></Echart>
    </div>
  </div>
</template>

<script>
import Data from "@/static/data.json";
import Echart from "@/common/echart";
export default {
  data() {
    return {
      options: {},
      cdata: {
        city: [],
        infected: [],
        death: [],
        cured: [],
      },
    };
  },
  components: {
    Echart,
  },
  props: {
    week: Number,
  },
  watch: {
    week: {
      handler(newWeek) {
        // 当周数发生变动时，重设数据
        this.setData(newWeek);
      },
    },
    cdata: {
      handler(newData) {
        this.options = {
          title: {
            text: "",
          },
          tooltip: {
            trigger: "axis",
            backgroundColor: "rgba(30,30,30,0.4)",
            axisPointer: {
              type: "shadow",
              label: {
                show: true,
                backgroundColor: "#7B7DDC",
              },
            },
          },
          legend: {
            data: ["感染数", "死亡数", "治愈数"],
            textStyle: {
              color: "#B4B4B4",
            },
            left: "20%",
            top: "0%",
          },
          grid: {
            x: "15%",
            width: "75%",
            y: "12%",
          },
          xAxis: {
            data: newData.city,
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              },
            },
            axisTick: {
              show: false,
            },
          },
          yAxis: [
            {
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: "#B4B4B4",
                },
              },
              axisLabel: {
                formatter: "{value} ",
              },
            },
            {
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: "#B4B4B4",
                },
              },
              axisLabel: {
                formatter: "{value} ",
              },
            },
          ],
          series: [
            {
              name: "感染数",
              type: "line",
              smooth: true,
              showAllSymbol: true,
              symbol: "emptyCircle",
              symbolSize: 8,
              yAxisIndex: 0,
              itemStyle: {
                normal: {
                  color: "#F02FC2",
                },
              },
              data: newData.infected,
            },
            {
              name: "死亡数",
              type: "line",
              smooth: true,
              showAllSymbol: true,
              symbol: "emptyCircle",
              symbolSize: 8,
              yAxisIndex: 1,
              itemStyle: {
                normal: {
                  color: "#956FD4",
                },
              },
              data: newData.death,
            },
            {
              name: "治愈数",
              type: "line",
              smooth: true,
              showAllSymbol: true,
              symbol: "emptyCircle",
              symbolSize: 8,
              yAxisIndex: 0,
              itemStyle: {
                normal: {
                  color: "#3EACE5",
                },
              },
              data: newData.cured,
            },
          ],
        };
      },
      immediate: true,
      deep: true,
    },
  },
  mounted() {
    this.setData(1);
  },
  methods: {
    // 显示当周数据
    setData(week) {
      let newData = {
        city: [],
        infected: [],
        death: [],
        cured: [],
      };
      let weekNum = week - 1;
      let weekData = Data.data[weekNum].virusdata;
      for (let i = 0; i < weekData.length; i++) {
        newData.city.push(weekData[i].name);
        newData.infected.push(weekData[i].infected);
        newData.death.push(weekData[i].death);
        newData.cured.push(weekData[i].cured);
      }
      this.cdata = newData;
    },
  },
};
</script>

<style lang="scss">
#leftDown {
  padding: 0.3rem 0.2rem;
  height: 6.5rem;
  min-width: 3.75rem;
  border-radius: 0.0625rem;
  .bg-color-black {
    height: 6.0625rem;
    border-radius: 0.125rem;
  }
  .text {
    color: #c3cbde;
  }
  .chart-box {
    margin-top: 0.2rem;
    width: 2.125rem;
    height: 2.125rem;
    .active-ring-name {
      padding-top: 0.125rem;
    }
  }
}
</style>