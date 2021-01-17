<template>
  <div :id="id" :class="className" :style="{ height: height, width: width }" />
</template>

<script>

export default {
  name: 'echart',
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '2.5rem'
    },
    options: {
      type: Object,
      default: ()=>({})
    },
    replace: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      chart: null
    }
  },
  watch: {
    options: {
      handler (options) {
        // 设置true清空echart缓存
        this.chart.setOption(options, this.replace);
      },
      deep: true
    }
  },
  mounted () {
    this.initChart();
  },
  methods: {
    initChart () {
      // 初始化echart
      this.chart = this.$echarts.init(this.$el, 'tdTheme');
      this.chart.setOption(this.options, true);
    }
  }
}
</script>

<style>
</style>
