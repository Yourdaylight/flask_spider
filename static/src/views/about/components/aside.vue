<template>
  <div class="aside">
    <el-menu
      :default-active="$route.path"
      class="el-menu-vertical"
      @open="handleOpen"
      @close="handleClose"
      background-color="#202741"
      text-color="#e6e6e6"
      active-text-color="#ffd04b"
      :show-timeout="200"
      mode="vertical"
      router
    >
      <!-- <span class="aside-title">Fried Egg Managment </span> -->
      <div class="aside-title">
        <img class="aside-icon" src="../../../assets/images/pull.png" />
        <span class="title">爬虫数据可视化系统</span>
      </div>
      <template v-for="(item, index) in routes">
        <el-submenu v-if="item.children" :index="index + ''" :key="index + ''">
          <template slot="title">
            <!-- <i class="el-icon-location"></i> -->
            <span>{{ item.name }}</span>
          </template>
          <el-menu-item 
            v-for="child in item.children"
            :index="child.path"
            :key="child.path"
          >
            <!-- <i class="el-icon-location"></i> -->
            <span>{{ child.name }}</span>
          </el-menu-item>
        </el-submenu>
        <el-menu-item v-if="!item.children" :index="item.path" :key="item.path">
          <i :class="iconList[item.path]"></i>
          <span slot="title">{{ item.name }}</span>
        </el-menu-item>
      </template>
    </el-menu>
  </div>
</template>
<script>
import asideRoute from "../../../router/asideRoute";
export default {
  name: "asideConment",
  data() {
    return {
      routes: [],
      iconList:{
        '/positive':'el-icon-document-checked',
        '/negative':'el-icon-document-remove',
        '/wordCloud':'el-icon-cloudy',
        '/netease':'el-icon-connection',
        '/commentsType':'el-icon-edit-outline'
      }
    };
  },
  created() {
    this.routes = JSON.parse(JSON.stringify(asideRoute));
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style scoped>
.aside {
  height: 100%;
  width: 100%;
    overflow: hidden;
}
.el-menu-vertical {
  height: 100%;
  text-align: left;
}
.aside-title {
  height: 60px;
  line-height: 60px;
  width: 100%;
  font-weight: 600;
  color: #fff;
  margin-left: 5px;
}
.title{
  color: #fff;
  margin-left: 40px;
  font-size: 20px;
}
.aside-icon{
  position: absolute; 
  top: 12px;
}
</style>