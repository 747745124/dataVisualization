<template>
  <div id="centreRight1">
    <div class="d-flex pt-2 pl-2">
      <span style="color: #5cd9e8">
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
      config: {
        // "讨论人数"
        header: ["话题", "讨论频次"],
        topic1: "",
        topic2: "",
        topic3: "",
        data: [],
        rowNum: 3, //表格行数
        headerHeight: 35,
        headerBGC: "#0f1325", //表头
        oddRowBGC: "#0f1325", //奇数行
        evenRowBGC: "#171c33", //偶数行
        index: true,
        columnWidth: [50],
        align: ["center"],
      },
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
      this.data[0][0] = Data.data[week - 1].twitter.topic[0];
      this.data[1][0] = Data.data[week - 1].twitter.topic[1];
      this.data[2][0] = Data.data[week - 1].twitter.topic[2];
      let pair1 = [this.topic1, "<span  class='colorGrass'>↑75%</span>"];
      let pair2 = [this.topic2, "<span  class='colorRed'>↓33%</span>"];
      let pair3 = [this.topic3, "<span  class='colorGrass'>↑100%</span>"];
      this.data.push(pair1, pair2, pair3);
    },
  },
};
</script>

<style lang="scss">
#centreRight1 {
  padding: 0.2rem;
  height: 5.125rem;
  min-width: 3.75rem;
  border-radius: 0.0625rem;
  .bg-color-black {
    height: 4.3125rem;
    border-radius: 0.125rem;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 0.125rem;
    overflow: hidden;
  }
}
</style>