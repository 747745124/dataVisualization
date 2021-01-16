<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue'
import Data from '@/static/data.json'
export default {
  data () {
    return {
      cdata: {
        city: [],
        infected: [],
        death: [],
        cured: []
      }
    };
  },
  components: {
    Chart,
  },
  props: {
    week: Number,
  },
  watch: {
    week: {
      handler(newWeek) {
        // 当周数发生变动时，重设数据
        this.setData(newWeek);
      }
    }
  },
  mounted () {
    this.setData(1);
  },
  methods: {
    // 显示当周数据
    setData (week) {     
      let newData = {
        city: [],
        infected: [],
        death: [],
        cured: []
      };
      let weekNum = week - 1;
      let weekData = Data.data[weekNum].virusdata;
      for (let i = 0; i < weekData.length; i++) {
        newData.city.push(weekData[i].name);
        newData.infected.push(weekData[i].infected);
        newData.death.push(weekData[i].death);
        newData.cured.push(weekData[i].cured);
      }
      this.cdata = newData;
    },
  }
};
</script>

<style lang="scss" scoped>
</style>