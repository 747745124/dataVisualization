<template>
  <div id="centreRight1">
    <div class="d-flex pt-2 pl-2">
      <span style="color: rgba(0, 183, 255, 0.55)">
        <icon name="chart-line"></icon>
      </span>
      <div class="d-flex">
        <span class="fs-xl text mx-2">话题热度排行榜</span>
      </div>
    </div>
    <div class="d-flex jc-center body-box">
      <dv-scroll-board
        :config="config"
        style="width: 5.375rem; height: 1.8rem"
      />
    </div>
  </div>
</template>

<script>
import Data from "@/static/data.json";
export default {
  data() {
    return {
      config: {},
    };
  },
  props: { week: Number },
  components: {},
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
    setWeek(week) {
      this.config = {
        // "讨论人数"
        header: ["话题", "频次"],
        topic1: "",
        topic2: "",
        topic3: "",
        data: [
          [
            Data.data[week - 1].twitter.topic[0],
            "<span  style='color: #dc3530'>↑75%</span>",
          ],
          [
            Data.data[week - 1].twitter.topic[1],
            "<span  style='color: #4aa0eb'>↓33%</span>",
          ],
          [
            Data.data[week - 1].twitter.topic[2],
            "<span  style='color: #dc3530'>↑66%</span>",
          ],
        ],
        rowNum: 2, //表格行数
        headerHeight: 35,
        headerBGC: "#0f1325", //表头
        oddRowBGC: "#0f1325", //奇数行
        evenRowBGC: "#171c33", //偶数行
        index: true,
        columnWidth: [50],
        align: ["center"],
      };
    },
  },
};
</script>

<style lang="scss">
// #leftUp {
//   padding-top: 0.3rem;
//   .before-time-string {
//     color: #b4b4b4;
//     font-size: 20px;
//     margin-left: 20px;
//     margin-top: 24px;
//     float: left;
//   }
//   #tilde {
//     font-size: 32px !important;
//     margin-left: 3px !important;
//     margin-right: 3px !important;
//   }
//   .after-time-string {
//     color: #b4b4b4;
//     font-size: 20px;
//     margin-right: 20px;
//     margin-top: 24px;
//     float: right;
//   }
//   .week-string {
//     color: #ffffff;
//     font-size: 24px;
//     margin-top: 8px;
//   }
// }
</style>