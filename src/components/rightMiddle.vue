<template>
  <div id="center">
    <div class="up">
      <div
        class="bg-color-black item"
        v-for="item in titleItem"
        :key="item.title"
      >
        <p class="ml-3 colorBlue fw-b">{{ item.title }}</p>
        <div>
          <dv-digital-flop
            :config="item.number"
            style="width: 1.25rem; height: 0.625rem"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Data from "@/static/data.json";
export default {
  data() {
    return {
      titleItem: [
        {
          title: "本周Twitter",
          number: {
            number: ["1.2k"],
            toFixed: 1,
            content: "{nt}",
          },
        },
        {
          title: "本周心情指数",
          number: {
            number: [18],
            toFixed: 1,
            content: "{nt}",
          },
        },
      ],
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
      this.titleItem[0].number.number[0] = Data.data[week - 1].twitter.total;
      this.titleItem[1].number.number[0] =
        Data.data[week - 1].twitter.moodIndex;
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
}
</style>