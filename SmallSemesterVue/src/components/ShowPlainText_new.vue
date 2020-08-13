<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
       <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="2-1" class="el-menu-vertical-demo" :default-openeds="opend"
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
            <div class="showplaintext_new">
            <div class="header">
                <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ path: '/Personaldoc' }">我的文档</el-breadcrumb-item>
                <el-breadcrumb-item>查看文档</el-breadcrumb-item>
            </el-breadcrumb>
            </div>
            <div class="hd3">
                <el-row :gutter="20">
                    <el-col :span="8"><div class="grid-content bg-purple">
                    <h4 style="text-align:center;display:block;color:white">文档名：</h4>
                    <h4 v-text="doc_name" style="text-align:center;color:white">{{doc_name}}</h4>
                    </div>
                    </el-col>
                    <el-col :span="8"><div class="grid-content bg-purple">
                    <h4 style="text-align:center;display:block;color:white">作者：</h4>
                    <h4 v-text="doc_name" style="text-align:center;color:white">{{doc_name}}</h4>
                    </div>
                    </el-col><el-col :span="8"><div class="grid-content bg-purple">
                    <h4 style="text-align:center;display:block;color:white">文档信息：</h4>
                    <h4 v-text="doc_name" style="text-align:center;color:white">{{doc_name}}</h4>
                    </div>
                    </el-col>
                </el-row>
            </div>

            <div class="zw">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <h4 style="text-align:center">文档内容</h4>
                        <el-button style="background-color:#f96332;color:white;float: right;" size="medium" round>修改</el-button>
                    </div>
                    <span v-html="htmlData">
                        {{htmlData}}
                    </span>
                </el-card>
                
            </div>
                <div style="font-size:30px;margin-top:100px"><b>评论区</b></div>
                <div style="width:100%;background-color:transparent" v-for="count in 10" :key="count">
                  
                    <el-card class="box-card" style="width:100%;margin-top:20px;">
                        <div slot="header" class="clearfix">
                            <div style="float:left;height:50px;width:50px;">
                                <img src="../assets/logo.png" style="height:50px;width:50px;">
                            </div>
                            <div style="float:left;height:50px;width:500px`;">
                                <div style="height:25px;width:500px;"></div>
                                <div style="height:25px;width:500px;"><b>这里是昵称</b></div>
                                
                            </div>
                        </div>

                    <div> 小车正穿行在落基山脉蜿蜒曲折的盘山公路上。克里斯朵夫·李维静静地望着窗外，发现每当车子即将行驶到无路的关头，
                        路边都会出现一块交通指示牌‘前方转弯’或‘注意！急转弯’。而拐过每一道弯之后，前方照例又是一片柳暗花明，豁然开朗。
                        山路弯弯，峰回路转，‘前方转弯’几个大字一次次地冲击着他的眼球，也渐渐叩醒了他的心扉：</div>


                        <el-card class="box-card" style="width:100%;margin-top:20px;">
                            <div slot="header" class="clearfix">
                                
                                <div style="float:left;height:50px;width:500px`;">
                                    <div style="height:25px;width:500px;"></div>
                                    <div style="height:25px;width:500px;"><b>评论区</b></div>
                                    
                                </div>
                            </div>
                            <div style="width:100%;background-color:transparent" v-for="count in 2" :key="count">
                                <div style="margin-top:10px"><b style="float:left">这里是昵称:</b>原来，不是路已到了尽头，而是该转弯了。路在脚下，
                        更在心中，心随路转，心路常宽。学会转弯也是人生的智慧，因为挫折往往是转折，危机同时是转机。
                                </div>
                            </div>

                        </el-card>

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
import axios from 'axios'
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
export default {
    name: 'ShowPlainText_new',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            doc_name: '',
            doc_creater: '',
            doc_intro: '',
            htmlData: ''
        }
    },
    methods: {
        Return(){
            this.$router.push('/Personaldoc');
        },
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
    created:function(){
        axios({
        method: 'post',
        url: 'http://localhost:8000/api/showpersonaldoc/',
        data: {'username': localStorage.getItem('username'), 'doc_id': this.$route.query.doc_id}
        })
        .then(response=>{
            if(response.data.code === 200){
                this.doc_name = response.data.doc_name
                this.doc_creater =response.data.doc_creater
                this.doc_intro = response.data.doc_intro
                this.htmlData = response.data.doc_content
            }
            else if(response.data.code === 400){
                alert('有错误')
            }
            else{
                alert('错误')
            }
        })
        .catch(error=>{
            console.log(error)
            alert('出现错误')
        })
    },
    mounted:function() {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
}
</script>

<style>
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
.header{
    margin-top:2%;
}
.hd3{
    margin-top:2%;
}
.el-row {
    margin-bottom: 20px;
    
}
.el-row:last-child{
    margin-bottom: 0;
}
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background:  #f96332;
  }
  .bg-purple {
    background:  #f96332;
  }
  .bg-purple-light {
    background:  #f96332;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color:  #f96332;
  }
</style>