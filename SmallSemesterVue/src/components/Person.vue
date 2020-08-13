<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-2" class="el-menu-vertical-demo"
            @open="handleOpen" @close="handleClose" background-color="#fff"
            text-color="#000000" active-text-color="#f96332" >
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-s-home"></i>
                    <span>主页</span>
                </template>
                    <el-menu-item index="1-1" @click="Home" :loading="logining" ><i class="el-icon-house" style="color:black"></i>首页</el-menu-item>
                    <el-menu-item index="1-2" @click="Person" :loading="logining"><i class="el-icon-user" style="color:black"></i>个人资料</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>工作台</span>
                </template>
                    <el-menu-item index="2-1" @click="Mywork" :loading="logining"><i class="el-icon-notebook-2" style="color:black"></i>我的文档</el-menu-item>
                    <el-menu-item   index="2-2" @click="Myteam" :loading="logining"><i class="el-icon-set-up" style="color:black"></i>我的团队</el-menu-item>
                    <el-menu-item index="2-3" @click="Trash" :loading="logining"><i class="el-icon-delete" style="color:black"></i>回收站</el-menu-item>
                    <el-menu-item index="2-4" @click="Message" :loading="logining"><i class="el-icon-chat-dot-round" style="color:black"></i>收件箱</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-s-opportunity"></i>
                    <span>其他</span>
                </template>
                    <el-menu-item index="3-1" @click="Help" :loading="logining"><i class="el-icon-view" style="color:black"></i>帮助</el-menu-item>
                    <el-menu-item index="3-2" @click="Aboutus" :loading="logining"><i class="el-icon-link" style="color:black"></i>开发者信息</el-menu-item>
            </el-submenu>
            </el-menu>
            </el-aside>
        <el-container>
        <main id="mainPart" role="main" class="container">
            <div class="div1">
                <div class="div2">
                    <div class="picture" style="width:100%;height:70%;background-color:transparent;">
                        <el-button class="but" size="small" plain ><i class="el-icon-camera" style="color:white" ></i>上传封面图片</el-button>
                    <div class="block1">
                    <el-row >
                            <el-col  span="4" >
                                <el-avatar shape="square":size="150" :src="circleUrl"></el-avatar>
                            </el-col> 
                            <el-col class="eman" span="6" > 
                                <h2 :value="showusername">{{showusername}}</h2>
                            </el-col>
                            <el-col class="edit" span="3" > 
                                
                                <el-button type="primary" round>编辑个人信息</el-button>
                            </el-col>
                        </el-row>
                    </div>
                    </div>
                </div>
                <div class="div3" >
                    <el-card class="box-card" style="width:100%;box-shadow:0px 0px  10px 5px #aaa;">
                        <div slot="header" >
                            <span>个人简介</span>
                         </div>   
                                <div style="height:10px;background-color:transparent"></div>

                                <el-input clearable v-model="input" placeholder="请输入内容"></el-input>
                        
                        
                    </el-card>
                </div>
                 <div class="div4">
                    <el-card class="box-card" style="width:100%;box-shadow:0px 0px  10px 5px #aaa;">
                        <div slot="header">
                            <span>个人信息</span>
                        </div>
                        <div style="width:50%;height:100%;float:left">
                            <el-table :data="tableData1" style="width: 100%">
                                <el-table-column prop="info" label=""></el-table-column>
                            </el-table>
                        </div>

                        <div style="width:50%;height:100%;float:right">
                            <el-table :data="tableData2" style="width: 100%">
                                <el-table-column prop="info" label=""></el-table-column>
                            </el-table>
                        </div>
                   
                    </el-card>
                </div>

            </div>
        </main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
export default {
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            input: '',
            
            tableData1: [{info:"姓名"},{info:"性别"},{info:"用户编号"}],
            tableData2: [{info:"xxx"},{info:"男"},{info:"12345678"}],
            circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
            showusername:"这里是用户昵称",
            istabBar: false
        }
        
    },
    methods: {
        //侧边栏的跳转
        click(){
            this.caninput = !this.caninput;
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        Home(){
            this.$router.push('/');
        },
        Person(){
            this.$router.push('/Person');
        },
        Mywork(){
            this.$router.push('/Personaldoc');
        },
        Myteam(){
            this.$router.push('/Team');
        },
        Trash(){
            this.$router.push('/Trash');
        },
        Message(){
            this.$router.push('/Message');
        },
        Help(){
            this.$router.push('/Help');
        },
        Aboutus(){
            this.$router.push('/Aboutus');
        },
        // 添加一个方法 兼容
        handleScroll () {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
                    
                // 固定导航栏
                let navBar = document.querySelector("#navBar");
                let mainPart = document.querySelector("#mainPart");
                if (scrollTop > 0){
                    this.istabBar = true
                    mainPart.style.paddingTop = navBar.offsetHeight + "px";
                } else {
                    this.istabBar = false
                    mainPart.style.paddingTop = "0px";
                }
        }
    },
    mounted () {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
}
</script>

<style>
.block1{
    padding-top: 100px;
    padding-left:20px;
}
.eman{
    padding-top:105px;
}
.edit{
    padding-top:105px;
    float:right;
}
.but{
    float:right;
    margin-top:10px;
    margin-right:10px;
    background-color:unset;
}
*{
    margin:0;
}
.div1{
    border:20px solid transparent;
    width:100%;
    height:1000px;
    background-color: transparent;
}
.div2{
    margin-top: 10px;
    width:100%;
    height:280px;
    background-color: transparent;
}
.div3{
    float:left;
    margin-top: 10px;
    width:70%;
    height:720px;
    background-color:transparent;
}
.div4{
    float:right;
    margin-top: 10px;
    width:25%;
    height:720px;
    background-color: transparent;
}

.picture{

    background-image: url("../assets/timg.jpg");
    background-size: 100% 100%;

}
.isFixed {
    position: fixed;
    top: 0;
    z-index: 10;
}
#navBar {
    width: 100%;
    background-color: #f96332;
    backdrop-filter: blur(30px);
}
#mainPart {
    width: 100%;
}

</style>