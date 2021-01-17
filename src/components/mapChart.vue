<template>
  <div id="map">
    <div>
      <Echart
        :options="options"
        id="centerUp"
        height="6.8rem"
        width="100%"
      ></Echart>
    </div>
  </div>
</template>

<script>
import echarts from "echarts";
import dataJson from "@/static/data.json";
import mapJson from "@/static/map.json";
import Echart from "@/common/echart";
import * as Icons from "@/static/icon.js";
export default {
  props: {
    week: Number,
    order: String,
  },
  data() {
    return {
      options: {},
      boroughsName: [
        "Bronx",
        "Manhattan",
        "Queens",
        "Brooklyn",
        "Staten Island",
      ],
      twitterPerPoint: 100, // 每个点对应的推文数量
      maxTwitterNum: 0, // 每周最大推文数
      maxPointsData: [], // 最大可显示点集合
      maxPointsNum: 0, // 总共最多点数量
      pointsData: [],
      minMoodIndex: Infinity,
      maxMoodIndex: -Infinity,
    };
  },
  mounted() {
    this.initMap();
  },
  watch: {
    week: {
      handler(newWeek) {
        // 当周数发生变动时，重设数据
        this.setWeekData(newWeek);
      },
    },
    order:{
      handler() {
        // 当周数发生变动时，重设数据
        this.setWeekData(this.week);
      },
    }
  },
  components: {
    Echart,
  },
  methods: {
    setWeekData(week) {
      let weekNum = week - 1;
      let pointNum =
        dataJson.data[weekNum].twitter.total / this.twitterPerPoint;

      // 随机从maxPointData中挑选出几个点
      let shuffled = this.maxPointsData.slice(0),
        i = this.maxPointsData.length,
        min = i - pointNum,
        temp,
        index;
      while (i-- > min) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
      }
      this.pointsData = shuffled.slice(min);
      this.pointsData.sort(function (a, b) {
        return a[0] - b[0];
      });
      this.pointsData.sort(function (a, b) {
        return a[1] - b[1];
      });

      let visualMapSet = this.getVisualMap(this.order);
      let valueSeries = this.getValueSeries(this.order, week);
      // 获取心情百分比，越接近1越消极
      let moodPercent =
        (dataJson.data[weekNum].twitter.moodIndex - this.minMoodIndex) /
        (this.maxMoodIndex - this.minMoodIndex);

      const seriesSet = [
        {
          name: "twitter",
          type: "scatter",
          encode: {
            tooltip: [0, 1],
          },
          coordinateSystem: "geo",
          data: this.pointsData,
          symbolSize: 15,
          colorAlpha: 1,
          symbol: function () {
            if (Math.random() > moodPercent) return Icons.positiveIcon;
            else return Icons.negativeIcon;
          },
        },
        valueSeries,
      ];

      this.options = {
        visualMap: visualMapSet,
        roam: true,
        tooltip: {},
        geo: {
          map: "New York",
          zoom: 1.1, // 初始缩放大小
          scaleLimit: {
            // 最大允许缩放
            min: 0.5,
            max: 2.0,
          },
          itemStyle: {
            borderColor: "rgba(0, 0, 0, 0.2)",
          },
          label: {
            show: true,
            color: "rgba(255,255,255,1)",
          },
          emphasis: {
            itemStyle: {
              areaColor: null,
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              shadowBlur: 20,
              borderWidth: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
        series: seriesSet,
      };
    },
    initMap() {
      echarts.registerMap("New York", mapJson, {});

      for (let i = 0; i < dataJson.data.length; i++) {
        // 获得所有周中推文最大数
        if (this.maxTwitterNum < dataJson.data[i].twitter.total) {
          this.maxTwitterNum = dataJson.data[i].twitter.total;
        }

        // 获取心情指数的上边界和下边界
        let moodIndex = dataJson.data[i].twitter.moodIndex;
        if (this.minMoodIndex > moodIndex) {
          this.minMoodIndex = moodIndex;
        }
        if (this.maxMoodIndex < moodIndex) {
          this.maxMoodIndex = moodIndex;
        }
      }

      this.maxPointsNum = this.maxTwitterNum / this.twitterPerPoint;
      // 设置地图上的随机点
      for (let i = 0; i < this.boroughsName.length; i++) {
        this.generateRandomPoint(this.boroughsName[i], this.maxPointsNum / 5);
      }

      this.setWeekData(1);
    },

    // 检查指定点是否在多边形内部
    checkPointInPoly(point, poly) {
      for (var flag = false, i = -1, l = poly.length, j = l - 1; ++i < l; j = i)
        ((poly[i].y <= point.y && point.y < poly[j].y) ||
          (poly[j].y <= point.y && point.y < poly[i].y)) &&
          point.x <
            ((poly[j].x - poly[i].x) * (point.y - poly[i].y)) /
              (poly[j].y - poly[i].y) +
              poly[i].x &&
          (flag = !flag);
      return flag;
    },

    // 生成随机点
    generateRandomPoint(boroughName, pointNum) {
      let polygonArr = Array(); //不规则区域数组
      let maxX = -Infinity,
        maxY = -Infinity,
        minX = Infinity,
        minY = Infinity;
      //然后开始执行
      let geoJsonObj = mapJson;
      let featuresArr = geoJsonObj.features;
      let areaArr = Array(); //区域的array的保存
      for (let key in featuresArr) {
        let model = featuresArr[key];
        if (model.properties.name.indexOf(boroughName) > -1) {
          let arr = model.geometry.coordinates; //经纬度的数组
          for (let key2 in arr) {
            let arr2 = arr[key2];
            for (let key3 in arr2) {
              let arr3 = arr2[key3];
              for (let key4 in arr3) {
                let arr4 = arr3[key4];
                //生成不规则点数组
                let pt = { x: arr4[0], y: arr4[1] };
                polygonArr.push(pt);
                areaArr.push(arr3[key4]);
                //获取最高维度， 获取最低维度  获取最东经度  获取最东短经度
                if (arr4[0] > maxX) {
                  maxX = arr4[0];
                }
                if (arr4[0] < minX) {
                  minX = arr4[0];
                }
                if (arr4[1] > maxY) {
                  maxY = arr4[1];
                }
                if (arr4[1] < minY) {
                  minY = arr4[1];
                }
              }
            }
          }
          let generateNum = 0;
          for (;;) {
            //无限循环直到生成所有点
            let indexX = (Math.random() * (maxX - minX) + minX).toFixed(6); //四舍五入取后六位
            let indexy = (Math.random() * (maxY - minY) + minY).toFixed(6);
            let pt = { x: indexX, y: indexy };
            //判断生成的点是否在区域内
            let flag = this.checkPointInPoly(pt, polygonArr);
            if (flag) {
              this.maxPointsData.push([indexX, indexy]);
              generateNum++;
            }
            if (generateNum > pointNum) {
              break;
            }
          }
        }
      }
    },

    // 获取用于显示颜色的集合
    getVisualMap(order) {
      if (order == "infected") {
        return {
          min: 0,
          max: 70000,
          left: "7%",
          top: "10%",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#06cd43", "#b0aa0a", "#920404"],
          },
          calculable: true,
          textStyle: {
            color: "white",
          },
        };
      } else if (order == "death") {
        return {
          min: 0,
          max: 6000,
          left: "7%",
          top: "10%",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#00a4f9", "#956fd4", "#653fa5"],
          },
          calculable: true,
          textStyle: {
            color: "white",
          },
        };
      } else if (order == "cured") {
        return {
          min: 0,
          max: 17000,
          left: "7%",
          top: "10%",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#aee3ff", "#3EACE5", "#0168f4"],
          },
          calculable: true,
          textStyle: {
            color: "white",
          },
        };
      }
    },
    // 获取人数数据
    getValueSeries(order, week) {
      if (order == "infected") {
        let set = [];
        for (let i = 0; i < this.boroughsName.length; i++) {
          set.push({
            name: this.boroughsName[i],
            value: dataJson.data[week - 1].virusdata[i].infected,
          });
        }
        return {
          name: "感染数",
          type: "map",
          geoIndex: 0,
          data: set,
        };
      } else if (order == "death") {
        let set = [];
        for (let i = 0; i < this.boroughsName.length; i++) {
          set.push({
            name: this.boroughsName[i],
            value: dataJson.data[week - 1].virusdata[i].death,
          });
        }
        return {
          name: "死亡数",
          type: "map",
          geoIndex: 0,
          data: set,
        };
      } else if (order == "cured") {
        let set = [];    
        for (let i = 0; i < this.boroughsName.length; i++) {
          set.push({
            name: this.boroughsName[i],
            value: dataJson.data[week - 1].virusdata[i].cured,
          });
        }
        return {
          name: "治愈数",
          type: "map",
          geoIndex: 0,
          data: set,
        };
      }
    },
  },
};
</script>



