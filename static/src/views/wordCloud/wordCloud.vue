<template>
  <div class="wordCloud">
    <div id="frequencyChart" class="chart-size"></div>
  </div>
</template>
<script>
export default {
  name: "wordCloud",
  data() {
    return {
      data: {
        frequencyChart: null,
        frequencyChartData: [],
      },
    };
  },
  created() {
    this.frequencyChartData = JSON.parse(
      localStorage.getItem("frequencyChartData")
    );
  },
  mounted() {
    this.frequencyChart = this.$echarts.init(
      document.getElementById("frequencyChart")
    );
    //窗口大小变化时，实现自适应
    window.addEventListener("resize", () => {
      this.frequencyChart.resize();
    });
    this.drawChart();
  },
  methods: {
    drawChart() {
      // let frequencyOption = {
      //   series: [{
      //       type: 'wordCloud',
      //       sizeRange: [15, 80],
      //       rotationRange: [0, 0],
      //       rotationStep: 45,
      //       gridSize: 8,
      //       // shape: 'pentagon',
      //       width: '100%',
      //       height: '100%',
      //       textStyle: {
      //         color: function () {
      //           return 'rgb(' + [
      //               Math.round(Math.random() * 160),
      //               Math.round(Math.random() * 160),
      //               Math.round(Math.random() * 160)
      //             ].join(',') + ')';
      //         }
      //       },
      //       data: this.frequencyChartData
      //   }]
      // };
      let frequencyOption = {
        backgroundColor: "#F7F7F7",
        tooltip: {
          show: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {
              iconStyle: {
                normal: {
                  color: "#FFFFFF",
                },
              },
            },
          },
        },
        series: [
          {
            name: "热点分析",
            type: "wordCloud",
            //size: ['9%', '99%'],
            // sizeRange: [6, 66],
            //textRotation: [0, 45, 90, -45],
            rotationRange: [-45, 90],
            sizeRange: [15, 80],
            // rotationRange: [0, 0],
            //shape: 'circle',
            textPadding: 0,
            autoSize: {
              enable: true,
              minSize: 6,
            },
            textStyle: {
              color: function () {
                return (
                  "rgb(" +
                  [
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                  ].join(",") +
                  ")"
                );
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333",
              },
            },
            data: this.frequencyChartData,
          },
        ],
      };
      this.frequencyChart.setOption(frequencyOption);
    },
  },
};
</script>
<style scoped>
.wordCloud {
  width: 100%;
  height: 100%;
  padding: 20px;
}
.chart-size {
  height: 100%;
  width: 100%;
}
</style>