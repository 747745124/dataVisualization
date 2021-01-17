<template>
  <div id="center">
    <div class="up">
      <div class="bg-color-black item">
        <p class="ml-3 colorBlue fw-b">本周Twitter</p>
        <div>
          <dv-digital-flop
            :config="item1"
            style="width: 1.25rem; height: 0.625rem"
          />
        </div>
      </div>
      <div class="bg-color-black item">
        <p class="ml-3 colorBlue fw-b">本周心情指数</p>
        <div>
          <dv-digital-flop
            :config="item2"
            style="width: 1.25rem; height: 0.625rem"
          />
        </div>
      </div>
      <div class="twitter-text fw-b">
        {{ twitterText }}
      </div>
    </div>
  </div>
</template>
<script>
import Data from "@/static/data.json";
export default {
  data() {
    return {
      item1: {},
      item2: {},
      twitterText: "twitterText",
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
      this.item1 = {
        number: [Data.data[week - 1].twitter.total.toString()],
        toFixed: 1,
        content: "{nt}",
      };
      this.item2 = {
        number: [
          Data.data[week - 1].twitter.moodIndex.toString().substring(0, 4),
        ],
        toFixed: 1,
        content: "{nt}",
      };
      this.twitterText = Data.data[week - 1].twitter.topTwitter;
    },
  },
};
</script>
<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;
  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    .item {
      border-radius: 0.0625rem;
      padding-top: 0.2rem;
      margin-top: 0.1rem;
      width: 32%;
      height: 0.875rem;
    }
  }
  .twitter-text {
    color: #e4e7ed;
    height: 1.5rem;
    width: 5rem;
    margin-top: 0.2rem;
    overflow: hidden;
  }
}
</style>