<template>
  <div id="leftUp">
    <div class="week-string d-flex jc-center">
      {{ weekString }}
    </div>
    <div class="before-time-string d-flex jc-center">
      {{ beforeTimeString + "  ~  " }}
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
      beforeYear: "2020",
      beforeMonth: "10",
      beforeDay: "20",
      afterYear: "2020",
      afterMonth: "11",
      afterDay: "20",
      beforeTimeString: null,
      afterTimeString: null,
      weekString: null,
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
      this.afterDay = week;
      //字符串
      this.beforeTimeString = this.beforeYear + "年" + this.beforeMonth + "月" + this.beforeDay + "日";
      this.afterTimeString = this.afterYear + "年" + this.afterMonth + "月" + this.afterDay + "日";
      this.weekString = "第" + week + "周";
    },
  },
};
</script>

<style lang="scss">
#leftUp {
  padding-top: 0.3rem;
  .before-time-string {
    color: #B4B4B4;
    font-size: 16px;
    margin-left: 20px;
    margin-top: 24px;
    float: left;
  }
  .after-time-string {
    color: #B4B4B4;
    font-size: 16px;
    margin-right: 20px;
    margin-top: 24px;
    float: right;
  }
  .week-string {
    color: #FFFFFF;
    font-size: 24px;
    margin-top: 8px;
  }
}
</style>