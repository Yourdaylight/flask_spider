<template>
  <div class="negative">
    <span>评论类型占比:</span>
    <div id="pieChart" class="chart-size"></div>
  </div>
</template>
<script>

export default {
  name: "commentsType",
  data() {
    return {
      data: {
        pieChart: null,
        pieChartData: [],
      },
    };
  },
  created() {
    this.pieChartData = JSON.parse(localStorage.getItem('pieChartData'));
  },
  mounted() {
    this.pieChart = this.$echarts.init(document.getElementById("pieChart"));
    //窗口大小变化时，实现自适应
    window.addEventListener("resize", () => {
      this.pieChart.resize();
    });
    this.drawChart()
  },
  methods: {
   drawChart(){
      let pieOption = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          right: '0%'
        },
        series: [
          {
            name: '评论类型占比',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            emphasis: {
              label: {
                show: true,
                fontSize: '20',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: true
            },
            data: this.pieChartData
          }
        ]
      };
      this.pieChart.setOption(pieOption);
   }
  },
};
</script>
<style scoped>
.negative{
  width: 100%;
  height: 100%;
  padding: 20px;
}
.negative>span:first-child{
  margin: 20px 0 0 20px;
  font-size: 24px;
  display: block;
}
.chart-size{
  height: 90%;
  width: 90%;
}
</style>