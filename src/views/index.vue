<!-- {{dateYear}} {{dateWeek}} {{dateDay}} -->
<template>
  <div id="index">
    <dv-full-screen-container class="bg">
      <dv-loading v-if="loading">Loading...</dv-loading>
      <div v-else class="host-body">
        <!-- 第一行 标题 -->
        <div class="d-flex jc-between px-2">
          <div class="d-flex" style="width: 45%">
            <div
              class="react-right bg-color-blue ml-4"
              style="width: 24rem; text-align: left"
            >
              <span class="react-before bg-color-blue"></span>
              <span class="text">{{ title }}</span>
            </div>
          </div>
          <div class="d-flex" style="width: 45%">
            <div
              class="react-left mr-4"
              style="width: 16rem; background-color: #0f1325; text-align: right"
            >
              <span class="react-after"></span>
              <span class="text">{{ groupMember }}</span>
            </div>
          </div>
        </div>

        <div class="body-box">
          <!-- 左侧 -->
          <div class="left-box">
            <div class="mb-2">
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                "
              >
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                ">
                <leftDown :week="curWeek"></leftDown>
              </dv-border-box-7>
            </div>
          </div>

          <!-- 中间 -->
          <div class="center-box ml-3">
            <div class="mb-2">
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                ">
                <mapChart :week="curWeek"></mapChart>
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                ">
                <!-- 时间滚动条 -->
                <slider-bar
                  :min="1"
                  :max="21"
                  v-model="startWeek"
                  @onSlide="updateWeek"
                ></slider-bar>
              </dv-border-box-7>
            </div>
          </div>

          <!-- 右侧 -->
          <div class="right-box ml-3">
            <div class="mb-2">
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                ">
                <rightUp :week="curWeek"></rightUp>
              </dv-border-box-7>
            </div>
            <div class="mb-2">
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                "> </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7
                style="
                  box-shadow: rgba(0, 0, 0, 0.3) 0px 0px 20px inset;
                  border: 1px solid rgba(0, 0, 0, 0.3);
                  background-color: #33333333;
                "> </dv-border-box-7>
            </div>
          </div>
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import sliderBar from "./sliderBar";
import { formatTime } from "../utils/index.js";
// import centerLeft1 from "./centerLeft1";
// import centerRight1 from "./centerRight1";
// import centerRight2 from "./centerRight2";
// import center from "./center";
// import bottomLeft from "./bottomLeft";
// import bottomRight from "./bottomRight";
import leftDown from "@/components/leftDown";
import mapChart from "@/components/mapChart";
import rightUp from "@/components/rightUp";
export default {
  data() {
    return {
      loading: true,
      dateDay: null,
      dateYear: null,
      dateWeek: null,
      weekday: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
      // 字符串
      title: "当我们在做数据可视化的时候我们是在生产什么垃圾",
      groupMember: "李绍康 朱晴川 席昊",
      startWeek: 1,
      curWeek: 1, // 当前周
      order: '0', // 当前选择显示的部分，0：感染数，1：死亡数，2：治愈数
    };
  },
  components: {
    sliderBar,
    // centerLeft1,
    // centerRight1,
    // centerRight2,
    // center,
    // bottomLeft,
    // bottomRight
    leftDown,
    mapChart,
    rightUp,
  },
  mounted() {
    this.timeFn();
    this.cancelLoading();
  },
  methods: {
    timeFn() {
      setInterval(() => {
        this.dateDay = formatTime(new Date(), "HH: mm: ss");
        this.dateYear = formatTime(new Date(), "yyyy-MM-dd");
        this.dateWeek = this.weekday[new Date().getDay()];
      }, 1000);
    },
    cancelLoading() {
      setTimeout(() => {
        this.loading = false;
      }, 500);
    },
    updateWeek(week) {
      //滑块改变时间时调用
      this.curWeek = week;
    },
    updateOptions() {
        console.log(this.order);
    }
  }
};
</script>

<style lang="scss">
@import "../assets/scss/index.scss";
</style>