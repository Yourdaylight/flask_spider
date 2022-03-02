<template>
  <div class="login">
    <div class="login-container">
      <div class="contenter">
        <!-- 登录 -->
        <transition name="slide-fade">
          <el-form
            v-if="isLogin"
            :model="formData"
            status-icon
            :rules="rules"
            ref="formData"
            label-width="100px"
            class="ruleForm"
            label-position="top"
            :hide-required-asterisk="true"
          >
            <div class="title">爬虫数据可视化系统</div>
            <el-form-item prop="user" label="用户名">
              <el-input
                type="text"
                v-model="formData.user"
                id="username"
                autocomplete="off"
                placeholder="请输入登录用户名"
              ></el-input>
            </el-form-item>
            <el-form-item prop="pass" label="密码">
              <el-input
                class="password"
                type="password"
                v-model="formData.pass"
                autocomplete="off"
                placeholder="请输入登录密码"
              ></el-input>
            </el-form-item>
            <el-form-item style="margin-top: 35px">
              <el-button
                class="sign-in"
                style="width: 100%"
                type="primary"
                @click="submitForm('formData')"
                >登 录</el-button
              >
              <span class="sign-up-tag"
                >还没有账户？<el-button type="text" @click="toRegist()"
                  >立即创建</el-button
                ></span
              >
            </el-form-item>
          </el-form>
        </transition>
        <!-- 注册 -->
        <transition name="slide-fade">
          <el-form
          style="position:absolute"
            v-if="!isLogin && isRegist"
            label-position="top"
            :model="ruleForm"
            status-icon
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="ruleForm"
            :hide-required-asterisk="true"
          >
            <el-form-item >
              <div class="title-little">注册</div>
            </el-form-item>
            <el-form-item label="用户名" prop="userNew">
              <el-input v-model="ruleForm.userNew"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="passNew">
              <el-input
                type="password"
                v-model="ruleForm.passNew"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
              <el-input
                type="password"
                v-model="ruleForm.checkPass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item style="margin-top:30px">
              <el-button type="primary" @click="saveForm('ruleForm')"
                >提交</el-button
              >
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </transition>
        
        <!-- 注册成功 -->
        <transition name="slide-fade">
          <div class="regist-success ruleForm" style="position:absolute" v-if="registSuccess && !isLogin">
            <div class="title-little">注册</div>
            <img class="success-icon" src="../../assets/images/success (2).png" />
            <div>账号注册成功！</div>
            <el-button
              class="sign-in"
              style="width: 100%"
              type="primary"
              @click="returnLogin()"
              >返回登录页面</el-button
            >
          </div>
        </transition>
      </div>
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import * as info from "../../api/info";
export default {
  name: "Login",
  components: {},
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.passNew) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      index: 11111111,
      formData: {
        user: "",
        pass: "",
      },
      rules: {
        user: [
          { required: true, message: "请输入登录用户名", trigger: "blur" },
                    {
            pattern: /^.{1,20}$/,
            message: "输入的用户名不得超过20位",
            trigger: "blur",
          },
        ],
        pass: [{ required: true, message: "请输入登录密码", trigger: "blur" },{
            pattern: /^.{1,8}$/,
            message: "输入密码不得超过8位",
            trigger: "blur",
          }],
        passNew: [{ validator: validatePass, trigger: "blur" },{
            pattern: /^.{1,8}$/,
            message: "输入密码不得超过8位",
            trigger: "blur",
          }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
        userNew: [{ required: true, message: "请输入用户名", trigger: "blur" },
          {
            pattern: /^.{1,20}$/,
            message: "输入的用户名不得超过20位",
            trigger: "blur",
          },
        ],
      },
      ruleForm: {
        passNew: "",
        checkPass: "",
        userNew: "",
      },
      rules2: {},
      isLogin: true,
      isRegist:false,
      registSuccess: false
    };
  },
  mounted() {
  },
  methods: {
    submitForm(formName) {
      // this.$router.push({ path: "/positive" });
      // console.log(formName);
      this.$refs[formName].validate((valid) => {
        let params = {
          username: this.formData.user,
          password: this.formData.pass,
        };
        if (valid) {
          info
            .login(params)
            .then((res) => {
              if (res.data.code == 200) {
                this.data = res.data.data;
                localStorage.setItem('username',this.formData.user)
                this.$router.push({ path: "/positive" });
              } else {
                this.$message.error("用户名或密码错误！");
              }
            })
            .catch((err) => {
              this.$Message.error(err + "!");
            });
        } else {
          return false;
        }
      });
    },
    toRegist(){
      this.isLogin = false; 
      setTimeout(()=>{
        this.isRegist = true
      },500)
      
    },
    saveForm(formName) {
      this.$refs[formName].validate((valid) => {
        let params = {
          username: this.ruleForm.userNew,
          password: this.ruleForm.passNew,
        };
        if (valid) {
          info
            .regist(params)
            .then((res) => {
              if (res.data.code == 200 && res.data.msg == 'success') {
                this.data = res.data.data;
                this.isRegist = false;
                setTimeout(()=>{
                  this.registSuccess = true;
                },500);
              } else {
                this.$message.error(res.data.msg + "！");
              }
            })
            .catch((err) => {
              this.$Message.error(err + "!");
            });
        } else {
          return false;
        }
      });
    },
    returnLogin(){
      this.registSuccess = false;
      setTimeout(()=>{
        this.isLogin = true;
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>
<style scoped>
/* 可以设置不同的进入和离开动画 */
/* 设置持续时间和动画函数 */
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .5s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
::v-deep .el-form--label-top .el-form-item__label {
  padding: 0;
}
::v-deep .el-form-item {
  margin-bottom: 10px;
}
::v-deep .el-form-item__content {
    line-height: 0px;
}
/* ::v-deep .el-button--warning.is-plain:focus,
::v-deep .el-button--warning.is-plain:hover {
  border-color: #fdb851;
  background: #f9deb5;
} */
.login {
  height: 100%;
  background: url("../../assets/images/bg1.jpg") no-repeat left 20%;
  background-size: cover;
}
.login-title {
  height: 100px;
}
.login-container { 
  padding-top: calc(50% - 200px);
}
.login-bottom {
  height: 60px;
  position: absolute;
  left: 0;
  bottom: 0;
}
.content {
  width: 360px;
  position: relative;
  left: calc(50% - 180px);
  z-index: 9;
  background-color: rgba(251, 252, 241, 0.8);
  /* opacity: 0.9; */
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.contenter {
  width: 400px;
  height: 420px;
  position: absolute;
  top: calc(50% - 200px);
  right: 250px;
  z-index: 999;
  background-color: rgba(255, 255, 255);
  border-radius: 10px;
  padding: 20px 30px 20px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.title {
  font-size: 26px;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 40px;
  text-align: center;
  letter-spacing: 16px；;
}
.ruleForm {
    position: absolute;
    width: calc(100% - 60px);
}
.con-title {
  text-align: left;
}
.img-logo {
  position: relative;
  z-index: 9999;
  /* top: 100px; */
  left: calc(50% - 90px);
}

/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
.sign-in {
  width: 100%;
}
.sign-up {
  width: 100%;
  margin-top: 15px;
  margin-left: 0px !important;
}
.sign-up-tag {
  text-align: center;
  display: block;
  width: 100%;
  margin-top: 15px;
  margin-left: 0px !important;
}
.title-little {
  font-size: 22px;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 10px;
}
.success-icon{
  margin: 70px auto 10px;
  display: block;
  width: 100px;
  height: 100px;
}
.regist-success{
  padding-bottom: 30px;
}
.regist-success>div:nth-child(3){
  text-align: center;
  margin-bottom: 80px;
}
</style>

