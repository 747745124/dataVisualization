<template>
  <div id="leftDown">
    <div class="d-flex pt-2 pl-2">
      <span style="color: rgba(0, 183, 255, 0.55)">
        <icon name="chart-line"></icon>
      </span>
      <div class="d-flex">
        <span class="fs-xl text mx-2">疫情累计变化图</span>
      </div>
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
        week: [],
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
            width: "70%",
            y: "12%",
          },
          xAxis: {
            data: newData.week,
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
                  color: "#920404",
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
    // 显示当周前后几周数据
    setData(week) {
      const deltaWeek = 3;
      const maxWeek = 21;
      let newData = {
        week: [],
        infected: [],
        death: [],
        cured: [],
      };
      let weekStart = 1;
      let weekEnd = maxWeek;
      if (week - deltaWeek > weekStart) {
        weekStart = week - deltaWeek;
      }
      if (week + deltaWeek < maxWeek) {
        weekEnd = week + deltaWeek;
      }
      for (let i = weekStart; i <= weekEnd; i++) {
        let weekData = Data.data[i - 1].virusdata[5];
        newData.week.push("第" + i + "周");
        newData.infected.push(weekData.infected);
        newData.death.push(weekData.death);
        newData.cured.push(weekData.cured);
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