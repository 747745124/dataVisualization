<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue'
import FakeData from '@/static/fakeData.vue'
export default {
  data () {
    return {
      cdata: {
        city: [],
        infected: [],
        virusData: 
        [
          {name:'Bronx',infected: 73371,death: 123,cured: 23313
          },
          {name:'Manhattan',infected: 24427,death: 109,cured: 12241
          },
          {name:'Queens',infected: 3512,death: 22,cured: 1234
          },
          {name:'Brooklyn',infected: 23441,death: 121,cured: 6632
          },
          {name:'Staten Island',infected: 11223,death: 231,cured: 5532
          }
        ],
        week: 1,
        twitter: 
        {
          topTwitter:'Make America Great Again!',
          total: 3220,
          moodIndex: 0.38,
          topic: ['virus','election','lockdown']
        }
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
      console.log(FakeData[0]);
      /*
      for (let i = 0; i < FakeData.data[0].virusData.length; i++) {
        this.cdata.city.push(FakeData.data[0].virusData[i].name);
        this.cdata.infected.push(FakeData.data[0].virusData[i].infected);
      }
      */
    },
  }
};
</script>

<style lang="scss" scoped>
</style>