<!-- {{dateYear}} {{dateWeek}} {{dateDay}} -->
<template>
  <div id="index">
    <dv-full-screen-container class="bg">
      <dv-loading style="height: 85%" v-if="loading">Loading...</dv-loading>
      <div v-else class="host-body">
        <!-- 第一行 标题 -->
        <div class="d-flex jc-between px-2">
          <div class="d-flex" style="width: 45%">
            <div
              class="react-right bg-color-blue ml-3"
              style="width: 24rem; text-align: left"
            >
              <span class="react-before bg-color-blue"></span>
              <span class="text">{{ title }}</span>
            </div>
          </div>
          <div class="d-flex" style="width: 45%">
            <div
              class="react-left mr-3"
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
              <dv-border-box-7 class="border-shadow"> </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7 class="border-shadow">
                <leftDown :week="curWeek"></leftDown>
              </dv-border-box-7>
            </div>
          </div>

          <!-- 中间 -->
          <div class="center-box ml-3">
            <div class="mb-2">
              <dv-border-box-7 class="border-shadow">
                <mapChart :week="curWeek"></mapChart>
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7 class="border-shadow">
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
              <dv-border-box-7 class="border-shadow">
                <rightUp :week="curWeek"></rightUp>
              </dv-border-box-7>
            </div>
            <div class="mb-2">
              <dv-border-box-7 class="border-shadow">
                <moodChart :week="curWeek"></moodChart>
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7 class="border-shadow">
                <rightDown :week="curWeek"></rightDown>
              </dv-border-box-7>
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
import moodChart from "@/components/moodChart";
import rightUp from "@/components/rightUp";
import rightDown from "@/components/rightDown";
export default {
  data() {
    return {
      loading: true,
      dateDay: null,
      dateYear: null,
      dateWeek: null,
      weekday: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
      //字符串
      title: "当疫情发生的时候我们在想什么",
      groupMember: "李绍康 朱晴川 席昊",
      startWeek: 1,
      curWeek: 1, // 当前周
      order: "0", // 当前选择显示的部分，0：感染数，1：死亡数，2：治愈数
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
    rightDown,
    mapChart,
    rightUp,
    moodChart
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
    },
  },
};
</script>

<style lang="scss">
@import "../assets/scss/index.scss";
.border-shadow {
  box-shadow: #ffffff44 0px 0px 20px inset;
  border: 1px solid #ffffff54;
  background-color: #22222222;
}
</style>