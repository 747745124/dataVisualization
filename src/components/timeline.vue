<template>
  <div class="Echarts">
    <div id="timeline" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  props: {
    min: Number,
    max: Number,
  },
  data() {
    return {
      chart: null,
    };
  },
  mounted() {
    this.chart = this.$echarts.init(document.getElementById("timeline"));

    let _this = this;
    this.chart.on("timelinechanged", function (timelineIndex) {
      _this.$emit("onSlide", timelineIndex.currentIndex + _this.min);
    });

    let weeks = [];
    for (let i = this.min; i <= this.max; i++) {
      weeks.push({ value: i, tooltip: { formatter: "{b}" } });
    }

    console.log(weeks);
    this.chart.setOption({
      baseOption: {
        timeline: {
          axisType: "category",
          realtime: false,
          data: weeks,
          playInterval: 2000,
          label: {
            formatter: function (s) {
              return s;
            },
            color: "#B4B4B4",
          },
          tooltip: {},
          controlStyle: {
            color: "#B4B4B4",
            borderColor: "#B4B4B4",
          },
          lineStyle: {
          },
          autoPlay: false,
          loop: true,
          left: "5%",
          right: "5%",
          top: "30%",
        },
      },
      options: [[1], [2], [3]],
    });
  },
};
</script>

<style>
.Echarts {
  height: 100%;
  width: 100%;
}
</style>
