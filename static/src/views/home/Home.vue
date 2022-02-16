<template>
  <div class="homePage">
    <div class="header">
      <div class="header-title">
        <img class="header-icon" src="../../assets/images/pull.png" />
        <span class="title">爬虫数据可视化系统</span>
      </div>
      <div class="user-info">
        <img class="header-icon" src="../../assets/images/userIcon.png" />
        <span>{{ username }}</span>
      </div>
    </div>
    <div class="content">
      <div class="search">
        <el-form :inline="true" :model="formData" class="demo-form-inline">
          <el-form-item>
            <el-input
              v-model="formData.url"
              placeholder="请输入URL..."
              style="width: 500px"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              type="primary"
              @click="onSubmit"
              icon="el-icon-search"
            ></el-button>
            <el-button
              @click="resetSearch"
              icon="el-icon-refresh-right"
            ></el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="charts">
        <el-card class="box-card">
          <span>Top10积极词汇评分</span>
          <div id="positiveChart" style="width: 700px; height: 400px"></div>
        </el-card>
        <el-card class="box-card">
          <div id="pieChart" style="width: 700px; height: 400px"></div>
        </el-card>
        <el-card class="box-card">
          <span>Top10消极词汇评分</span>
          <div id="negativeChart" style="width: 700px; height: 400px"></div>
        </el-card>
        <el-card class="box-card">
          <div id="frequencyChart" style="width: 700px; height: 400px"></div>
        </el-card>
      </div>
    </div>
  </div>
</template>
<script>
import * as info from "../../api/info";
export default {
  data() {
    return {
      activeIndex: 1,
      formData: {
        url: "",
      },
      username: "",
      chartsData: [],
      positiveChart: null,
      negativeChart: null,
      pieChart: null,
      frequencyChart: null,
      positiveChartData: {xData:[],yData:[]},
      negativeChartData: {xData:[],yData:[]},
      pieChartData: [],
      frequencyChartData: [],
    };
  },
  mounted() {
    let _this = this;
    this.positiveChart = this.$echarts.init(
      document.getElementById("positiveChart")
    );
    this.negativeChart = this.$echarts.init(
      document.getElementById("negativeChart")
    );
    this.pieChart = this.$echarts.init(document.getElementById("pieChart"));
    this.frequencyChart = this.$echarts.init(
      document.getElementById("frequencyChart")
    );
    //窗口大小变化时，实现自适应
    window.addEventListener("resize", () => {
      _this.positiveChart.resize();
      _this.negativeChart.resize();
      _this.pieChart.resize();
      _this.frequencyChart.resize();
    });
    this.username = localStorage.getItem("username");
  },
  methods: {
    onSubmit() {
      let params = {
        username: this.username,
        url: this.formData.url,
      };
      info
        .display(params)
        .then((res) => {
          if (res.data.code == 200) {
            console.log(res);
            this.chartsData = res.data.data;
            let positiveChartData = res.data.data.positive;
            let negativeChartData = res.data.data.negative;
            let pieChartData = res.data.data.tags;
            let frequencyChartData = res.data.data.frequency;

            this.positiveChartData['xData'] = Object.keys(positiveChartData);
            this.positiveChartData.xData.forEach((el) => {
              this.positiveChartData['yData'].push(Number(positiveChartData[el].toFixed(2)));
            });
            this.negativeChartData.xData = Object.keys(negativeChartData);
            this.negativeChartData.xData.forEach((el) => {
              this.negativeChartData.yData.push(Number(negativeChartData[el].toFixed(2)));
            });
            let frequencyKeys = Object.keys(frequencyChartData);
            frequencyKeys.forEach((el) => {
              this.frequencyChartData.push({name:el,value:frequencyChartData[el]})
            });
            let keys = Object.keys(pieChartData);
            keys.splice(0, 1);
            keys.forEach((el) => {
              this.pieChartData.push({name:el,value:pieChartData[el]})
            });
            
            console.log(keys,this.pieChartData)
            this.drawChart();
          } else {
            this.$message.error("拉取错误！");
          }
        })
        // .catch((err) => {
        //   // this.$Message.error(err + "!");
        // });
    },
    resetSearch() {
      this.formData.url = "";
    },
    drawChart() {

      let positiveOption = {
        xAxis: {
          type: "category",
          data: this.positiveChartData.xData,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: this.positiveChartData.yData,
            type: "bar",
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      };
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
            name: 'Access From',
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
      let frequencyOption = {
        series: [{
            type: 'wordCloud',
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 8,
            shape: 'pentagon',
            width: '100%',
            height: '100%',
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                }
            },
            data: this.frequencyChartData
        }]
      };
      this.positiveChart.setOption(positiveOption);
      this.negativeChart.setOption(negativeOption);
      this.pieChart.setOption(pieOption);
      this.frequencyChart.setOption(frequencyOption);
    },
  },
};
</script>
<style scoped>
::v-deep .el-form-item {
  margin-bottom: 0px;
}
::v-deep .el-menu.el-menu--horizontal {
  border: none;
}
.homePage {
  margin: 0;
  padding: 0;
  height: 100%;
}
.header {
  width: 100%;
  height: 60px;
  line-height: 60px;
  background: #0f1423;
  position: fixed;
  z-index: 999;
}
.content {
  padding-top: 60px;
  background: #eeeff4;
  width: 100%;
  display: table;
}
.content::after {
  content: '';
  display: block;
  clear: both;
}
.search {
  width: 100%;
  background-color: #202741;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.header-title{
  margin-left:50px;
  float: left;
}
.title{
  color: #fff;
  margin-left: 40px;
  font-size: 20px;
}
.user-info {
  float: right;
  margin-right: 50px;
  color: #fff;
}
.user-info >span:last-child{
  margin-left: 40px;
}
.header-icon{
  position: absolute; 
  top: 12px;
}
.charts {
  padding: 20px;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
.box-card {
  width: 48%;
  height: 420px;
  float: left;
  margin: 10px;
}
</style>