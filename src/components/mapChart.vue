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
      boroughsData: [
        { name: "Bronx", value: 1 },
        { name: "Manhattan", value: 2 },
        { name: "Queens", value: 3 },
        { name: "Brooklyn", value: 4 },
        { name: "Staten Island", value: 5 },
      ],
      maxPointsData: [], // 最大可显示点数量
      pointsData: [],
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
      let twitterNum = dataJson.data[weekNum].twitter.total / 5000 * 250;
      if(twitterNum > 250) twitterNum = 250;
      
      // 随机从maxPointData中挑选出几个点
      let shuffled = this.maxPointsData.slice(0), i = this.maxPointsData.length, min = i - twitterNum, temp, index;
      while (i-- > min) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
      }
      this.pointsData = shuffled.slice(min);

      // 设置地图
      this.options = {
        tooltip: {
          trigger: "item",
          formatter: "{b}",
        },
        geo: {
          map: "New York"
        },
        series: [
          {
            name: 'twitter',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: this.convertData(this.pointsData),
            symbolSize: function (val) {
                return val[2] / 5;
            },
            encode: {
                value: 2
            },
            itemStyle: {
                color: 'purple'
            },
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
          },
        ],
      };
    },
    initMap() {
      // 设置地图上的随机点
      for(let i = 0; i < this.boroughsData.length; i++){
        this.generateRandomPoint(this.boroughsData[i].name, 50);
      } 

      this.setWeekData(1);
      echarts.registerMap("New York", mapJson, {});
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
          //相同的区域   如果区域相同时生成全部的
          let arr = model.geometry.coordinates; //经纬度的数组
          for (let key2 in arr) {
            let arr2 = arr[key2];
            for (let key3 in arr2) {
              let arr3 = arr2[key3];
              for (let key4 in arr3) {
                let arr4 = arr3[key4];
                //生成 不规则点数组
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
            //无限循环
            let indexX = (Math.random() * (maxX - minX) + minX).toFixed(6); //四舍五入取后六位
            let indexy = (Math.random() * (maxY - minY) + minY).toFixed(6);
            let pt = { x: indexX, y: indexy };
            //判断生成的点是否在区域内
            let flag = this.checkPointInPoly(pt, polygonArr);
            if (flag) {
              this.maxPointsData.push([indexX, indexy]);
              generateNum++;
            }
            if (generateNum == pointNum) {
              //如果等于生成的点 则结束
              break;
            }
          }
        }
      }
    },

    // 将原始数据(纯坐标)转换为
    convertData(originData) {
      var res = [];
      for (var i = 0; i < originData.length; i++) {
        res.push({
          name: "Queens",
          value: originData[i].concat(10),
        });
      }
      return res;
    },
  },
};
</script>



