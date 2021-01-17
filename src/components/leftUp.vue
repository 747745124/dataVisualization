<template>
  <div id="leftUp">
    <div class="week-string d-flex jc-center">
      {{ weekString }}
    </div>
    <div class="time-string d-flex jc-center">
      {{ beforeTimeString + "   ~   " + afterTimeString }}
    </div>
    <div class="infected-num d-flex jc-center">
      感染数：{{ infectedNum }} 新增：{{ infectedNumWeek }}
      <div>
        <div v-if="infectedChange == 1">
          <!-- 根据新增感染数是否增加判断箭头方向 -->
          <span class="ml-3" style="color: #ff0000aa">
            <icon name="arrow-up"></icon>
          </span>
        </div>
        <div v-else-if="infectedChange == 0">
          <span class="ml-3">
            <icon name="arrow-right" style="color: #00ff0099"></icon>
          </span>
        </div>
        <div v-else-if="infectedChange == -1">
          <span class="ml-3">
            <icon name="arrow-down" style="color: #0000ee"></icon>
          </span>
        </div>
      </div>
    </div>
    <div class="death-num d-flex jc-center">
      死亡数：{{ deathNum }} 新增：{{ deathNumWeek }}
      <div>
        <div v-if="deathChange == 1">
          <!-- 根据新增死亡数是否增加判断箭头方向 -->
          <span class="ml-3" style="color: #ff0000aa">
            <icon name="arrow-up"></icon>
          </span>
        </div>
        <div v-else-if="deathChange == 0">
          <span class="ml-3">
            <icon name="arrow-right" style="color: #00ff0099"></icon>
          </span>
        </div>
        <div v-else-if="deathChange == -1">
          <span class="ml-3">
            <icon name="arrow-down" style="color: #0000ee"></icon>
          </span>
        </div>
      </div>
    </div>
    <div class="cured-num d-flex jc-center">
      治愈数：{{ curedNum }} 新增：{{ curedNumWeek }}
      <div>
        <div v-if="curedChange == 1">
          <!-- 根据新增治愈数是否增加判断箭头方向 -->
          <span class="ml-3" style="color: #0000ee">
            <icon name="arrow-up"></icon>
          </span>
        </div>
        <div v-else-if="curedChange == 0">
          <span class="ml-3">
            <icon name="arrow-right" style="color: #00ff0099"></icon>
          </span>
        </div>
        <div v-else-if="curedChange == -1">
          <span class="ml-3">
            <icon name="arrow-down" style="color: #ff0000aa"></icon>
          </span>
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
      beforeYear: null,
      beforeMonth: null,
      beforeDay: null,
      afterYear: null,
      afterMonth: null,
      afterDay: null,
      beforeTimeString: null,
      afterTimeString: null,
      weekString: null,
      monthDay: [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
      infectedNum: null,
      deathNum: null,
      curedNum: null,
      infectedNumWeek: null,
      deathNumWeek: null,
      curedNumWeek: null,
      infectedChange: 0,
      deathChange: 0,
      curedChange: 0,
    };
  },
  components: {},
  props: {
    week: Number,
  },
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
    // 初始化为第一周
    setWeek(week) {
      //根据周数获得日期
      this.beforeYear = "2020";
      this.afterYear = "2020";

      let startDay = week * 7 - 1 - 5;
      for (let m = 1; m <= 12; m++) {
        this.beforeDay = startDay;
        startDay -= this.monthDay[m];
        if (startDay < 0) {
          this.beforeMonth = m;
          break;
        }
      }
      let endDay = week * 7 + 6 - 5;
      for (let m = 1; m <= 12; m++) {
        this.afterDay = endDay;
        endDay -= this.monthDay[m];
        if (endDay < 0) {
          this.afterMonth = m;
          break;
        }
      }
      //字符串
      this.beforeTimeString =
        this.beforeYear +
        "年" +
        this.beforeMonth +
        "月" +
        this.beforeDay +
        "日";
      this.afterTimeString =
        this.afterYear + "年" + this.afterMonth + "月" + this.afterDay + "日";
      this.weekString = "第" + week + "周";

      //死亡数等
      this.infectedNum = Data.data[week - 1].virusdata[5].infected;
      this.deathNum = Data.data[week - 1].virusdata[5].death;
      this.curedNum = Data.data[week - 1].virusdata[5].cured;
      //新增
      //第一周也是0
      if (week > 1) {
        this.infectedNumWeek =
          Data.data[week - 1].virusdata[5].infected -
          Data.data[week - 2].virusdata[5].infected;
        this.deathNumWeek =
          Data.data[week - 1].virusdata[5].death -
          Data.data[week - 2].virusdata[5].death;
        this.curedNumWeek =
          Data.data[week - 1].virusdata[5].cured -
          Data.data[week - 2].virusdata[5].cured;
      } else {
        this.infectedNumWeek = 0;
        this.deathNumWeek = 0;
        this.curedNumWeek = 0;
      }

      this.infectedChange = 0;
      this.deathChange = 0;
      this.curedChange = 0;
      //变化箭头
      if (week > 2) {
        if (
          this.infectedNum - Data.data[week - 2].virusdata[5].infected >
          Data.data[week - 2].virusdata[5].infected -
            Data.data[week - 3].virusdata[5].infected
        ) {
          this.infectedChange = 1;
        } else if (
          this.infectedNum - Data.data[week - 2].virusdata[5].infected <
          Data.data[week - 2].virusdata[5].infected -
            Data.data[week - 3].virusdata[5].infected
        ) {
          this.infectedChange = -1;
        }
        if (
          this.deathNum - Data.data[week - 2].virusdata[5].death >
          Data.data[week - 2].virusdata[5].death -
            Data.data[week - 3].virusdata[5].death
        ) {
          this.deathChange = 1;
        } else if (
          this.deathNum - Data.data[week - 2].virusdata[5].death <
          Data.data[week - 2].virusdata[5].death -
            Data.data[week - 3].virusdata[5].death
        ) {
          this.deathChange = -1;
        }
        if (
          this.curedNum - Data.data[week - 2].virusdata[5].cured >
          Data.data[week - 2].virusdata[5].cured -
            Data.data[week - 3].virusdata[5].cured
        ) {
          this.curedChange = 1;
        } else if (
          this.curedNum - Data.data[week - 2].virusdata[5].cured <
          Data.data[week - 2].virusdata[5].cured -
            Data.data[week - 3].virusdata[5].cured
        ) {
          this.curedChange = -1;
        }
      }
    },
  },
};
</script>

<style lang="scss">
#leftUp {
  padding-top: 0.3rem;
  .time-string {
    color: #b4b4b4;
    font-size: 16px;
    margin-top: 20px;
  }
  .week-string {
    color: #b4b4b4;
    font-size: 24px;
    margin-top: 4px;
  }
  .infected-num {
    color: #920404;
    font-size: 14px;
    font-weight: bold;
    margin-top: 14px;
    float: left;
    margin-left: 50px;
    width: 80%;
  }
  .death-num {
    color: #956fd4;
    font-size: 14px;
    font-weight: bold;
    margin-top: 6px;
    float: left;
    margin-left: 50px;
    width: 80%;
  }
  .cured-num {
    color: #3eace5;
    font-size: 14px;
    font-weight: bold;
    margin-top: 6px;
    float: left;
    margin-left: 50px;
    width: 80%;
  }
}
</style>