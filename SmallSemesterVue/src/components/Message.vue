<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="2-5" class="el-menu-vertical-demo" :default-openeds="opend"
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
                    <el-menu-item index="2-2" @click="Myteam" :loading="logining"><i class="el-icon-set-up" style="color:black"></i>我的团队</el-menu-item>
                    <el-menu-item index="2-3" @click="MyFavorite" :loading="logining"><i class="el-icon-sunny" style="color:black"></i>我的收藏</el-menu-item>
                    <el-menu-item index="2-4" @click="Trash" :loading="logining"><i class="el-icon-delete" style="color:black"></i>回收站</el-menu-item>
                    <el-menu-item index="2-5" @click="Message" :loading="logining"><i class="el-icon-chat-dot-round" style="color:black"></i>收件箱</el-menu-item>
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
        <main id="mainPart" role="main" class="container" color="black">

    <!-- 页面内部的内容写在main中间即可 -->
    <br>
    <el-tabs type="card">
        <el-tab-pane label="系统通知">
            <el-card class="box-card" v-for="(item) in MessageData" :key="item">
            <div slot="header" class="clearfix">
                <span class="title" >{{item.MessageTitle}}</span>
                <span class="time">{{item.date}}</span>
            </div>
            <div class="text item" >
                {{ item.MessageContent }}
            </div>
        </el-card>
        </el-tab-pane>
        <el-tab-pane label="团队通知">配置管理</el-tab-pane>
        <el-tab-pane label="文档通知">角色管理</el-tab-pane>
        </el-tabs>

        

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
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            MessageData:[
                {
                    id:'1',
                    MessageTitle:'特朗普决定变更国籍为中国',
                    MessageContent:'北京时间8月26日，特朗普来到中国，在天安门面前大喊:\'Make Chine Great Again！\'，然后宣誓入籍中国。',
                    date:'2000-8-13 19:19:68'
                },
                {
                    id:'2',
                    MessageTitle:'奥巴马决定变更国籍为中国',
                    MessageContent:'北京时间8月26日，特朗普来到中国，在天安门面前大喊:\'Make Chine Great Again！\'，然后宣誓入籍中国。',
                    date:'2000-8-13 19:19:68'
                },
                {
                    id:'3',
                    MessageTitle:'希拉里决定变更国籍为中国',
                    MessageContent:'北京时间8月26日，特朗普来到中国，在天安门面前大喊:\'Make Chine Great Again！\'，然后宣誓入籍中国。',
                    date:'2000-8-13 19:19:68'
                },{
                    id:'4',
                    MessageTitle:'比利海灵顿决定变更国籍为中国',
                    MessageContent:'北京时间8月26日，特朗普来到中国，在天安门面前大喊:\'Make Chine Great Again！\'，然后宣誓入籍中国。',
                    date:'2000-8-13 19:19:68'
                }
            ]
        }
    },
    methods: {
        //侧边栏的跳转
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
        MyFavorite(){
            this.$router.push('/MyFavoriteDoc');
        },
        TeamM(){
            this.$router.push('/TeamManagement');
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

<style scoped>
.time{
    font-size: 13px;
    margin: 20px;
    color:rgb(153, 153 ,153)
}
.title{
    font-size:15px;
    font-weight:bold;
    color: rgb(51,51,51);
}
.text {
    font-size: 15px;
    color: rgb(102,102,102);
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 100%;
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