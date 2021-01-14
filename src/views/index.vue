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
              style="width: 24rem; text-align: left;"
            >
              <span class="react-before bg-color-blue"></span>
              <span class="text">{{ title }}</span>
            </div>
          </div>
          <div class="d-flex" style="width: 45%">
            <div
              class="react-left mr-4"
              style="width: 16rem; background-color: #0f1325; text-align: right;"
            >
              <span class="react-after"></span>
              <span class="text">{{ groupMember }}</span>
            </div>
          </div>
        </div>

        <div class="body-box">
          <!-- 第二行数据 -->
          <div class="content-box">
            <div>
              <dv-border-box-7>
                <centerLeft1 />
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7>
                <centerLeft2 />
              </dv-border-box-7>
            </div>
            <!-- 中间 -->
            <div>
              <center />
            </div>
            <!-- 中间 -->
            <div>
              <dv-border-box-7>
                <centerRight2 />
              </dv-border-box-7>
            </div>
            <div>
              <dv-border-box-7>
                <centerRight1 />
              </dv-border-box-7>
            </div>
          </div>

          <!-- 第三行数据 -->
          <div class="bototm-box">
            <dv-border-box-7>
              <bottomLeft />
            </dv-border-box-7>
            <dv-border-box-7>
              <bottomRight />
            </dv-border-box-7>
          </div>
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import { formatTime } from '../utils/index.js'
import centerLeft1 from "./centerLeft1";
import centerLeft2 from "./centerLeft2";
import centerRight1 from "./centerRight1";
import centerRight2 from "./centerRight2";
import center from "./center";
import bottomLeft from "./bottomLeft";
import bottomRight from "./bottomRight";
export default {
  data () {
    return {
      loading: true,
      dateDay: null,
      dateYear: null,
      dateWeek: null,
      weekday: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
      //字符串
      title: "当我们在做数据可视化的时候我们是在生产什么垃圾",
      groupMember: "李绍康 朱晴川 席昊"
    };
  },
  components: {
    centerLeft1,
    centerLeft2,
    centerRight1,
    centerRight2,
    center,
    bottomLeft,
    bottomRight
  },
  mounted () {
    this.timeFn();
    this.cancelLoading();
  },
  methods: {
    timeFn () {
      setInterval(() => {
        this.dateDay = formatTime(new Date(), 'HH: mm: ss');
        this.dateYear = formatTime(new Date(), 'yyyy-MM-dd');
        this.dateWeek = this.weekday[new Date().getDay()];
      }, 1000)
    },
    cancelLoading () {
      setTimeout(() => {
        this.loading = false;
      }, 500);
    }
  }
};
</script>

<style lang="scss">
@import '../assets/scss/index.scss';
</style>