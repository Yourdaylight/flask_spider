<template>
  <div class="about">
    <el-container>
      <el-aside width="230px">
        <Aside />
      </el-aside>
      <el-container>
        <el-header>
          <BreadCrumb @search="search" :url.sync="newUrl"/>
        </el-header>
        <el-main class="main">
          <AppMain/>
        </el-main>
        <!-- <el-footer>Footer</el-footer> -->
      </el-container>
    </el-container>
  </div>
</template>
<script>
import Aside from "./components/aside.vue";
import BreadCrumb from "./components/breadcrumb.vue";
import AppMain from "./components/appmain.vue";
import * as info from "../../api/info";
export default {
  name: "about",
  components: { Aside, BreadCrumb, AppMain },
  props:{
    newUrl:{
      type:String,
      default:''
    }
  },
  data() {
    return {
      username: "",
      url: this.newUrl,
      chartsData: [],
      positiveChartData: { xData: [], yData: [] },
      negativeChartData: { xData: [], yData: [] },
      pieChartData: [],
      frequencyChartData: [],
    };
  },
  mounted() {
    this.username = localStorage.getItem("username");
    this.search();
  },
  methods: {
    search(value) {
      // let url = value == undefined ? this.url: value.url;
      this.url = value;
      let params = {
        username: this.username,
        url: this.url,
      };
      info.display(params).then((res) => {
        if (res.data.code == 200) {
          localStorage.setItem("positiveChartData", JSON.stringify( { xData: [], yData: [] }));
          localStorage.setItem("negativeChartData", JSON.stringify( { xData: [], yData: [] }));
          localStorage.setItem("frequencyChartData", JSON.stringify([]));
          localStorage.setItem("pieChartData", JSON.stringify([]));
          this.chartsData = res.data.data;
          let positiveChartData = res.data.data.positive;
          let negativeChartData = res.data.data.negative;
          let pieChartData = res.data.data.tags;
          let frequencyChartData = res.data.data.frequency;

          this.positiveChartData["xData"] = Object.keys(positiveChartData);
          this.positiveChartData.xData.forEach((el) => {
            this.positiveChartData["yData"].push(
              Number(positiveChartData[el].toFixed(2))
            );
          });
          this.negativeChartData.xData = Object.keys(negativeChartData);
          this.negativeChartData.xData.forEach((el) => {
            this.negativeChartData.yData.push(
              -Number(negativeChartData[el].toFixed(2))
            );
          });
          let frequencyKeys = Object.keys(frequencyChartData);
          frequencyKeys.forEach((el) => {
            this.frequencyChartData.push({
              name: el,
              value: frequencyChartData[el],
            });
          });
          let keys = Object.keys(pieChartData);
          keys.splice(0, 1);
          this.pieChartData=[]
          keys.forEach((el) => {
            this.pieChartData.push({ name: el, value: pieChartData[el] });
          });

          localStorage.setItem("positiveChartData", JSON.stringify(this.positiveChartData));
          localStorage.setItem("negativeChartData", JSON.stringify(this.negativeChartData));
          localStorage.setItem("frequencyChartData", JSON.stringify(this.frequencyChartData));
          localStorage.setItem("pieChartData", JSON.stringify(this.pieChartData));
          localStorage.setItem("url", this.url);
          this.$message.success("数据获取成功！请点击相关页签查看更新数据")
        } else {
          this.$message.error("拉取错误！");
        }
      });
      // .catch((err) => {
      //   // this.$Message.error(err + "!");
      // });
    },
  },
};
</script>
<style scoped>
::v-deep .el-container {
  height: 100%;
}
.about {
  height: 100%;
}
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  /* line-height: 80px; */
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  /* line-height: 200px; */
  height: 100%;
  position: fixed;
}

.el-header {
  position: fixed;
  left: 229px;
  width: 100%;
  padding: 0;
  z-index: 999;
}

.el-footer {
  position: fixed;
  left: 230px;
  width: 100%;
  bottom: 0;
}

.el-main {
  background-color: #f0f2f5;
  color: #333;
  /* text-align: center;
  line-height: 160px; */
  padding: 90px 10px 10px 240px;
  min-height: calc(100% - 100px);
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>