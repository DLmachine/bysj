<template>
    <div class="login-container">
        <el-form :model="ruleForm2" :rules="rules2"
         status-icon
         ref="ruleForm2"
         label-position="left"
         label-width="0px"
         class="demo-ruleForm login-page">
            <h3 class="title">系统登录</h3>
            <el-form-item prop="username">
                <el-input type="text"
                    v-model="ruleForm2.username"
                    auto-complete="off"
                    placeholder="用户名"
                ></el-input>
            </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password"
                        v-model="ruleForm2.password"
                        auto-complete="off"
                        placeholder="密码"
                    ></el-input>
                </el-form-item>
            <el-checkbox
                v-model="checked"
                class="rememberme"
            >记住密码</el-checkbox>
            <el-form-item style="width:100%;">
                <el-button type="primary" style="width:100%;" @click="login" :loading="logining">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data(){
        return {
            logining: false,                      //设置登录按钮状态
            ruleForm2: {
                username: '',
                password: ''
            },
            rules2: {
                username: [{required: true, message: '请输入用户名', trigger: 'blur'}],   //登录时验证用户名密码是否为空
                password: [{required: true, message: '请输入密码', trigger: 'blur'}]
            },
            checked: false                        //设置是否记住密码初始状态
        }
    },
    methods: {
        myLogin (params) {
          return axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/index/login/',
            data: params    //post用data,get用params
          })
        },
        login(event) {
            this.$refs.ruleForm2.validate((valid) => {
                if(valid){
                    this.myLogin({username : this.ruleForm2.username, password : this.ruleForm2.password})
                        .then((data) => {
                          console.log(data.data)
                            if (data.data.state == 1) {
                                this.$message({
                                    type: 'success',
                                    message: data.data.data
                                })
                                this.$router.push({path: '/'});
                            }
                            else {
                                this.$message({
                                    type: 'error',
                                    message: data.data.data
                                })
                           // this.$router.go(0);
                        }
                    })
                }
            });
        }
    }
};
</script>

<style scoped>
.login-container {
    width: 100%;
    height: 100%;
}
.login-page {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}
label.el-checkbox.rememberme {
    margin: 0px 0px 15px;
    text-align: left;
}
</style>
