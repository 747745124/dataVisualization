<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue'
import FakeData from '@/static/data.json'
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
  mounted () {
    this.setData();
  },
  methods: {
    // 根据自己的业务情况修改
    setData () {     
      for (let i = 0; i < FakeData.data[0].virusData.length; i++) {
        this.cdata.city.push(FakeData.data[0].virusData[i].name);
        this.cdata.infected.push(FakeData.data[0].virusData[i].infected);
        this.cdata.death.push(FakeData.data[0].virusData[i].death);
        this.cdata.cured.push(FakeData.data[0].virusData[i].cured);
      }
    },
  }
};
</script>

<style lang="scss" scoped>
</style>