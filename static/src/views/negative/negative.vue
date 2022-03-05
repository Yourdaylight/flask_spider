<template>
  <div class="negative">
    <span>Top{{ topSelected }}消极词汇评分:</span>
    <div id="negativeChart" class="chart-size"></div>
    <div class="select-top">
      <el-select v-model="topSelected" placeholder="请选择" @change="onChange">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </div>
  </div>
</template>
<script>
import * as info from "../../api/info";
export default {
  name: "negative",
  data() {
    return {
      data: {
        negativeChart: null,
        negativeChartData: [],
      },
      options: [
        {
          value: 5,
          label: "Top5",
        },
        {
          value: 10,
          label: "Top10",
        },
        {
          value: 20,
          label: "Top20",
        },
        {
          value: 50,
          label: "Top50",
        },
      ],
      topSelected: "10",
    };
  },
  created() {
    this.negativeChartData = JSON.parse(
      localStorage.getItem("negativeChartData")
    );
  },
  mounted() {
    this.negativeChart = this.$echarts.init(
      document.getElementById("negativeChart")
    );
    //窗口大小变化时，实现自适应
    window.addEventListener("resize", () => {
      this.negativeChart.resize();
    });
    this.drawChart();
  },
  methods: {
    onChange(val) {
      let params = {
        username: localStorage.getItem("username"),
        url: localStorage.getItem("url"),
        top: val,
      };
      info.display(params).then((res) => {
        if (res.data.code == 200) {
          this.negativeChartData["yData"] = [];
          let negativeChartData = res.data.data.negative;
          this.negativeChartData.xData = Object.keys(negativeChartData);
          this.negativeChartData.xData.forEach((el) => {
            this.negativeChartData.yData.push(
              -Number(negativeChartData[el].toFixed(2))
            );
          });
          localStorage.setItem(
            "negativeChartData",
            JSON.stringify(this.negativeChartData)
          );

          this.drawChart();
          if (negativeChartData){
            this.$message.warning("该链接评论数据为空")
          }
          this.negativeChart.resize();
        }
      });
    },
    drawChart() {
      let negativeOption = {
        xAxis: {
          type: "category",
          data: this.negativeChartData.xData,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: this.negativeChartData.yData,
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      };
      this.negativeChart.setOption(negativeOption);
    },
  },
};
</script>
<style scoped>
.negative {
  width: 100%;
  height: 100%;
  padding: 20px;
  text-align: left;
  line-height: 100%;
}
.negative > span:first-child {
  margin: 20px 0 0 20px;
  font-size: 24px;
  display: block;
}
.chart-size {
  height: 90%;
  width: 90%;
  float: left;
  margin-top: 40px;
}
.select-top {
  width: 10%;
  position: absolute;
  line-height: 100%;
  right: 50px;
}
</style>