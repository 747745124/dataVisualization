<template>
  <div id="bottomLeft">
    <div class="d-flex pt-2 pl-2">
      <!-- <span style="color:#5cd9e8">
        <icon name="chart-bar"></icon>
      </span> -->
      <!-- <div class="d-flex">
        <span class="fs-xl text mx-2">数据统计图</span>
      </div> -->
    </div>
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
import Data from '@/static/data.json';
import Echart from '@/common/echart';
export default {
    data() {
        return {
            options: {},
            cdata: {
                city: [],
                infected: [],
                death: [],
                cured: []
            }
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
            }
        },
        cdata: {
            handler (newData) {
                this.options = {
                title: {
                    text: "",
                },
                tooltip: {
                    trigger: "axis",
                    backgroundColor: "rgba(255,255,255,0.1)",
                    axisPointer: {
                    type: "shadow",
                    label: {
                        show: true,
                        backgroundColor: "#7B7DDC"
                    }
                    }
                },
                legend: {
                    data: ["感染数", "死亡数", "治愈数"],
                    textStyle: {
                    color: "#B4B4B4"
                    },
                    top: "0%"
                },
                grid: {
                    x: "8%",
                    width: "88%",
                    y: "4%"
                },
                xAxis: {
                    data: newData.city,
                    axisLine: {
                    lineStyle: {
                        color: "#B4B4B4"
                    }
                    },
                    axisTick: {
                    show: false
                    }
                },
                yAxis: [
                    {
                    splitLine: { show: false },
                    axisLine: {
                        lineStyle: {
                        color: "#B4B4B4"
                        }
                    },

                    axisLabel: {
                        formatter: "{value} "
                    }
                    },
                    {
                    splitLine: { show: false },
                    axisLine: {
                        lineStyle: {
                        color: "#B4B4B4"
                        }
                    },
                    axisLabel: {
                        formatter: "{value} "
                    }
                    }
                ],
                series: [
                    {
                    name: "感染数",
                    type: "line",
                    smooth: true,
                    showAllSymbol: true,
                    symbol: "emptyCircle",
                    symbolSize: 8,
                    yAxisIndex: 1,
                    itemStyle: {
                        normal: {
                        color: "#F02FC2"
                        }
                    },
                    data: newData.infected
                    },
                    {
                    name: "死亡数",
                    type: "bar",
                    barWidth: 10,
                    itemStyle: {
                        normal: {
                        barBorderRadius: 5,
                        color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: "#956FD4" },
                            { offset: 1, color: "#3EACE5" }
                        ])
                        }
                    },
                    data: newData.death
                    },
                    {
                    name: "治愈数",
                    type: "bar",
                    barGap: "-100%",
                    barWidth: 10,
                    itemStyle: {
                        normal: {
                        barBorderRadius: 5,
                        color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: "rgba(156,107,211,0.8)" },
                            { offset: 0.2, color: "rgba(156,107,211,0.5)" },
                            { offset: 1, color: "rgba(156,107,211,0.2)" }
                        ])
                        }
                    },
                    z: -12,
                    data: newData.cured
                    }
                ]
                }
            },
            immediate: true,
            deep: true
            },
    },
    mounted () {
        this.setData(1);
    },
    methods: {
        // 显示当周数据
        setData (week) {     
        let newData = {
            city: [],
            infected: [],
            death: [],
            cured: []
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
    }
}
</script>

<style lang="scss">
#bottomLeft {
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