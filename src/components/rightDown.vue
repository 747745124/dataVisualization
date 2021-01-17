<template>
  <div id="leftUp">
    <div class="week-string d-flex jc-center">
      {{ weekString }}
    </div>
    <div class="before-time-string d-flex jc-center">
      {{ beforeTimeString }}
      <!-- + "  ~  " -->
    </div>
    <div id="tilde" class="before-time-string d-flex jc-center">
      {{ " ~ " }}
    </div>
    <div class="after-time-string d-flex jc-center">
      {{ afterTimeString }}
    </div>
  </div>
</template>

<script>
// import Data from "@/static/data.json";
export default {
  data() {
    return {
      beforeYear: null,
      beforeMonth: null,
      beforeDay: null,
      afterYear: null,
      afterMonth: null,
      afterDay: null,
      beforeTimeString: null,
      afterTimeString: null,
      weekString: null,
      monthDay: [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    };
  },
  components: {},
  props: {
    week: Number,
  },
  watch: {
    week: {
      handler(newWeek) {
        // 当周数发生变动时，重设
        this.setWeek(newWeek);
      },
    },
  },
  mounted() {
    this.setWeek(1);
  },
  methods: {
    // 初始化为第一周
    setWeek(week) {
      //根据周数获得日期
      this.beforeYear = "2020";
      this.afterYear = "2020";

      let startDay = week * 7 - 1 - 5;
      for (let m = 1; m <= 12; m++) {
        this.beforeDay = startDay;
        startDay -= this.monthDay[m];
        if (startDay < 0) {
          this.beforeMonth = m;
          break;
        }
      }
      let endDay = week * 7 + 6 - 5;
      for (let m = 1; m <= 12; m++) {
        this.afterDay = endDay;
        endDay -= this.monthDay[m];
        if (endDay < 0) {
          this.afterMonth = m;
          break;
        }
      }
      //字符串
      this.beforeTimeString =
        this.beforeYear +
        "年" +
        this.beforeMonth +
        "月" +
        this.beforeDay +
        "日";
      this.afterTimeString =
        this.afterYear + "年" + this.afterMonth + "月" + this.afterDay + "日";
      this.weekString = "第" + week + "周";
    },
  },
};
</script>

<style lang="scss">
#leftUp {
  padding-top: 0.3rem;
  .before-time-string {
    color: #b4b4b4;
    font-size: 20px;
    margin-left: 20px;
    margin-top: 24px;
    float: left;
  }
  #tilde {
    font-size: 32px !important;
    margin-left: 3px !important;
    margin-right: 3px !important;
  }
  .after-time-string {
    color: #b4b4b4;
    font-size: 20px;
    margin-right: 20px;
    margin-top: 24px;
    float: right;
  }
  .week-string {
    color: #ffffff;
    font-size: 24px;
    margin-top: 8px;
  }
}
</style>