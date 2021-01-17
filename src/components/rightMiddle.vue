<template>
  <div id="center">
    <div class="d-flex pt-2 pl-2">
      <span style="color: rgba(0, 183, 255, 0.55)">
        <icon name="laptop"></icon>
      </span>
      <div class="d-flex">
        <span class="fs-xl text mx-2">本周最热门Twitter</span>
      </div>
    </div>
    <div class="up">
      <div class="item">
        <p class="ml-3 colorBlue fw-b">本周Twitter</p>
        <div>
          <dv-digital-flop
            :config="item1"
            style="width: 1.25rem; height: 0.625rem"
          />
        </div>
      </div>
      <div class="item">
        <p class="ml-3 colorBlue fw-b">本周心情指数</p>
        <div>
          <dv-digital-flop
            :config="item2"
            style="width: 1.25rem; height: 0.625rem"
          />
        </div>
      </div>
      <div class="twitter-text">
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