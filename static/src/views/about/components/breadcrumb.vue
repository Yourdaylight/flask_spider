<template>
  <!-- <div class="breadcrumb"> -->
  <div class="header">
    <el-form :inline="true" :model="formData" class="demo-form-inline">
      <el-form-item>
        <el-input
          v-model="formData.url"
          placeholder="请输入URL..."
          style="width: 500px"
        >
          <el-button
            slot="append"
            icon="el-icon-search"
            @click="onSubmit"
          ></el-button
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          @click="resetSearch"
          icon="el-icon-refresh-right"
        ></el-button>
      </el-form-item>
    </el-form>
    <div class="user-info">
      <img class="header-icon" src="../../../assets/images/userIcon.png" />
      <div>
        <el-dropdown @command="handleCommand" placement="bottom">
          <span class="el-dropdown-link">
            {{ username }}<i class="el-icon-arrow-down el-icon--right" style="position:absolute;margin-right:20px"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="a">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <!-- {{ username }}admin -->
        </div>
    </div>
  </div>
  <!-- </div> -->
</template>
<script>
export default {
  name: "breadcrumb",
  data() {
    return {
      formData: {
        url: "http://you.163.com/item/detail?id=4028691",
      },
      username:""
    };
  },
  mounted() {
    this.username = localStorage.getItem("username")
  },
  methods: {
    onSubmit() {
      this.$emit("search", this.formData.url);
      this.$emit("update:url", this.formData.url);
    },
    resetSearch() {
      this.formData.url = "";
    },
    handleCommand() {
      this.$router.push({ path: "/" });
    }
  },
};
</script>
<style scoped>
::v-deep .el-form-item {
  margin-bottom: 0px;
}
::v-deep .el-dropdown{
  color:#fff
}
.header {
  width: 100%;
  height: 80px;
  /* line-height: 80px; */
  background: #0f1423;
  background-color: #202741;
  position: fixed;
  padding-top: 20px;
}
.header-title {
  margin-left: 50px;
  float: left;
}
.title {
  color: #fff;
  margin-left: 40px;
  font-size: 20px;
}
.user-info {
  color: #fff;
  position: absolute;
  left: calc(100% - 350px);
  z-index:1999;
  top: 9px;
}
.user-info > div:last-child {
  margin-left: 40px;
  margin-top: 23px;
  position: absolute;
  color: #fff;
}
.header-icon {
  position: absolute;
  top: 15px;
}
</style>