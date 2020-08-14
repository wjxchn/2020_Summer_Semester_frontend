<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="" class="el-menu-vertical-demo" :default-openeds="opend"
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
        <div class="header" style="padding:20px">
            <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/Personaldoc' }">我的文档</el-breadcrumb-item>
            <el-breadcrumb-item>新建文档</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div >
        <el-row :gutter="20">
            <el-col :span="8" v-for="item in DocFormData" :key="item.index">
                <el-card :body-style="{ padding: '0px' }" style="width:90%;margin:10px" >
                <img v-bind:src="item.url" class="image">
                <div style="padding: 14px;">
                    <p style="text-align:center;font-size:18px">{{item.name}}</p>
                    <div class="bottom clearfix">
                        <el-button type="primary" class="button" style="float:right">创建</el-button>
                    </div>
                </div>
                </el-card>
            </el-col>
        </el-row>
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
    name: 'DocForm',
    components: {
        Guider,
        BottomGuider
    },
    data () {
       return {
            currentDate: new Date(),
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            DocFormData:[
                {
                    index:"1",
                    url:"http://m.qpic.cn/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/bqQfVz5yrrGYSXMvKr.cqal0AN6VQ0iw2YAmTiXSTlQWFKocisyr4FdC.N2I3kH32qPK41I1ovIrf4ToCYLDjrFbCS5JBcplEHLnwOX09M8!/b&bo=iwE1AgAAAAADB58!&rf=viewer_4",
                    name:"空白文档"
                },
                {
                    index:"2",
                    url:"http://m.qpic.cn/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/bqQfVz5yrrGYSXMvKr.cqVYbsi3361Tl8U.RzQolBhjzyp1f6JVmaATAaUfQFJGXvvHvv5Fv8.Bp8xcRutbzK0NDXIvMBqJ3ft7FfeAMtOs!/b&bo=gQKJAwAAAAADBys!&rf=viewer_4",
                    name:"2019年终总结通用模板"
                },
                {
                    index:"3",
                    url:"http://m.qpic.cn/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/TmEUgtj9EK6.7V8ajmQrEE3HyXMqX8rSCLTDyTAF8MW8NSvqDvHUtkAKqFy68jrJzqn9POwNla2oXQgooKgOmxlIbY4b15Jwxt80YXenGCo!/b&bo=fAKJAwAAAAADJ*Y!&rf=viewer_4",
                    name:"个人借款协议（无居间人）"
                },
                {
                    index:"4",
                    url:"http://m.qpic.cn/psc?/V50IFnJp4XxV2s3cUReP2J6k3C3FNeXZ/bqQfVz5yrrGYSXMvKr.cqSzkACjEy70*RAD5.Da9Vv0*.q5OOV.DmMQ2edWjzTtbnBk1J.1iI3duH9INwOep4me5QaDpo1dvSiR.LeXU.7s!/b&bo=fwKKAwAAAAADB9Y!&rf=viewer_4",
                    name:"外贸合同"
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
 .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .image {
    width: 100%;
    height: 450px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>