<template>
  <div class="login">
    <div class="hed" style="text-align:center">
      <el-image style="height:120px;width:405px" :src="'http://r.photo.store.qq.com/psc?/V143D3j445iBwL/45NBuzDIW489QBoVep5mcVXyL*BsvZygoyXkXSowchA7gJ2NMBMBsOjMwY5piqegdZCDtFL6KmYG89tApO1qbCXbnAYUG9HzopHGRYUR1HI!/r'"></el-image>
      <h1 style="color:#f96332" >找回密码</h1>
    </div>
    <div class="bc">
          <el-form :model="ruleForm2" :rules="rules2" status-icon ref="ruleForm2">
            <el-form-item label-width="40px" style="width:310px">
                <el-input style="width:60%;float:left" type="email" auto-complete="off" placeholder="邮箱"></el-input>
                <el-button style="background-color:#f96332;color:white;width:40%;float:left" >发送验证码</el-button>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px">
                <el-input type="text" auto-complete="off" placeholder="验证码"></el-input>
            </el-form-item>
            <el-form-item label-width="40px" style="width:310px">
                <el-input type="password" auto-complete="off" placeholder="新密码"></el-input>
            </el-form-item > 
            <el-form-item label-width="40px" style="width:310px">
                <el-input type="password2"  auto-complete="off" placeholder="重复密码"></el-input>
            </el-form-item > 
            <el-form-item label-width="20px" style="width:400px">
              <el-button style="background-color:#f96332;color:white;">确认更改</el-button>
              <el-button style="background-color:#f96332;color:white;" @click="Return" >返回</el-button>
              <el-button style="background-color:#f96332;color:white;" @click="Login" >直接登录</el-button>
            </el-form-item>
          </el-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
        logining: false,
        checked: true
      };
    },
    methods: {
      Return(){
        this.$router.push('/')
      },
      Login(){
        this.$router.push('/Login')
      }
      
    }
  }
</script>

<style scoped>
.el-checkbox__input is checked{
  fill:#f96332;
  border-color:#f96332;
  color:#f96332;
}
.login
{
    width:100%;
    height:100%;
    z-index:-1;
    position:fixed;
	  background-color:#f7f7f7;
    position: fixed;
    background-size: 100% 100%;
    overflow-y: auto;
}
.mid
{
	height:100%;
}
.bc
{
 background-color: rgba(255, 255, 255, 0.7);
    border-radius:50px;
	padding-top:2%;
	padding-bottom:1%;
	padding-left:3.5%;
    margin: 3% auto;
    width: 500px;
}
</style>