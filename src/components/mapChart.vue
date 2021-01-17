<template>
  <div id="map">
    <div>
      <Echart
        :options="options"
        id="centerUp"
        height="6rem"
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
export default {
  props: {
    week: Number,
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
      twitterPerPoint: 300, // 每个点对应的推文数量
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

      let visualMapSet = this.getVisualMap("infected");
      let valueSeries = this.getValueSeries("infected", week);

      const seriesSet = [
        {
          name: "twitter",
          type: "scatter",
          coordinateSystem: "geo",
          data: this.pointsData,
          symbolSize: 15,
          colorAlpha: 1,
          symbol:
            "image://data:image/png;base64,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",
          label: {
            normal: {
              show: false,
            },
            emphasis: {
              show: false,
            },
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
          zoom: 1.2, // 初始缩放大小
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
            color: "rgba(0,0,0,0.4)",
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
          max: 500,
          left: "left",
          top: "bottom",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#e0ffff", "#006edd"],
          },
          calculable: true,
        };
      } else if (order == "death") {
        return {
          min: 0,
          max: 500,
          left: "left",
          top: "bottom",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#e0ffff", "#006edd"],
          },
          calculable: true,
        };
      } else if (order == "cured") {
        return {
          min: 0,
          max: 500,
          left: "left",
          top: "bottom",
          text: ["High", "Low"],
          seriesIndex: [1],
          inRange: {
            color: ["#e0ffff", "#006edd"],
          },
          calculable: true,
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



