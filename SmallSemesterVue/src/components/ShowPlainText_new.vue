<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
       <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-1" class="el-menu-vertical-demo" :default-openeds="opend"
            @open="handleOpen" @close="handleClose" background-color="#fff"
            text-color="#000000" active-text-color="#f96332" >
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>工作台</span>
                </template>
                    <el-menu-item index="1-1" @click="Mywork" :loading="logining"><i class="el-icon-notebook-2" style="color:black"></i>我的文档</el-menu-item>
                    <el-menu-item index="1-2" @click="Myteam" :loading="logining"><i class="el-icon-set-up" style="color:black"></i>我的团队</el-menu-item>
                    <el-menu-item index="1-3" @click="MyFavorite" :loading="logining"><i class="el-icon-star-off" style="color:black"></i>我的收藏</el-menu-item>
                    <el-menu-item index="1-4" @click="Trash" :loading="logining"><i class="el-icon-delete" style="color:black"></i>回收站</el-menu-item>
                    <el-menu-item index="1-5" @click="Message" :loading="logining"><i class="el-icon-chat-dot-round" style="color:black"></i>收件箱</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-s-home"></i>
                    <span>个人信息</span>
                </template>
                    <el-menu-item index="2-1" @click="Person" :loading="logining"><i class="el-icon-user" style="color:black"></i>个人资料</el-menu-item>
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
                        <el-button @click="dialogFormVisible = true" style="background-color:#f96332;color:white;float: right;" size="medium" round>写评论</el-button>
                        <el-dialog title="创建评论" :visible.sync="dialogFormVisible">
                        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                            <el-form-item label="评论内容" :label-width="formLabelWidth" prop="content" required>
                            <el-input v-model="ruleForm.content"></el-input>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button style="width:70px;background-color:#f96332;color:white" @click="addCommentFunc(),dialogFormVisible = false">确 定</el-button>
                        </div>
                        </el-dialog>
                    </div>
                    <span v-html="htmlData">
                        {{htmlData}}
                    </span>
                </el-card>

            

                <!-- 正文的回复点赞-->
                <div style="height:50px;width:100%;margin-top:20px">
                    
                    
                    <el-button @click="thumb" style="float:right;margin-left:10px;"><i class="el-icon-thumb" style="width:30px;"></i></el-button>
                    <el-button @click="showInput" style="float:right"><i class="el-icon-chat-round" style="width:30px;"></i></el-button>
                </div>
                <div v-bind:class="{'div1':isTrue}"><el-input v-model="input" placeholder="请输入内容"></el-input></div>


            </div>
                <div style="font-size:30px;margin-top:100px"><b>评论区</b></div>
                <div style="width:100%;background-color:transparent" v-for="item in commentData" :key="item.com_id">
                  
                    <el-card class="box-card" style="width:100%;margin-top:20px;">
                        <div slot="header" class="clearfix">
                            <div style="float:left;height:50px;width:50px;">
                                <img src="../assets/logo.png" style="height:50px;width:50px;">
                            </div>
                            <div style="float:left;height:50px;width:500px`;">
                                <div style="height:25px;width:500px;"></div>
                                <div style="height:25px;width:500px;"><b v-text="item.com_author">{{item.com_author}}</b></div>
                            </div>
                        </div>
                    <el-button @click="dialogDelComVisible = true" style="background-color:#f96332;color:white;float: right;" size="medium" round>删除评论</el-button>
                    <el-dialog title="删除评论" :visible.sync="dialogDelComVisible">
                        确定删除评论吗？
                        <div slot="footer" class="dialog-footer">
                            <el-button style="width:70px;background-color:#f96332;color:white" @click="delCommentFunc(item.com_id),dialogDelComVisible = false">确 定</el-button>
                        </div>
                    </el-dialog>
                    <div v-text="item.com_content">{{item.com_content}}</div>
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
            input: '',
            isTrue:true,
            opend:['1','2','3'],
            uniqueOpened:false,
            istabBar: false,
            dialogFormVisible:false,
            dialogDelComVisible:false,
            doc_name: '',
            doc_creater: '',
            doc_intro: '',
            htmlData: '',
            commentData: [],
            ruleForm:{
                content:''
            },
            rules:{
                content: [
                    { required: true, message: '请输入评论内容', trigger: 'blur' },
                    { min: 1, max: 300, message: '长度在 1 到 300 个字符', trigger: 'blur' }
                ]
            },
        }
    },
    methods: {
        showInput(){
            this.isTrue = !this.isTrue
        },
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
        },
        addCommentFunc(){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/add_comment/',
                data: {'doc_id': this.$route.query.doc_id, 'username': localStorage.getItem('username'), 'content': this.ruleForm.content}
            })
            .then(response => {
                if(response.data.code === 200){
                    alert('添加评论成功')
                    this.$router.go(0)
                }
                else if(response.data.code === 400){
                    alert('有错误')
                }
                else{
                    alert('错误')
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')            
            });
        },
        delCommentFunc(cid){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/del_comment/',
                data: {'com_id': cid}
            })
            .then(response => {
                if(response.data.code === 200){
                    alert('删除评论成功')
                    this.$router.go(0)
                }
                else if(response.data.code === 400){
                    alert('删除错误')
                }
                else{
                    alert('删除错误')
                }
            })
            .catch(error => {
                console.log(error)
                alert('出现错误')            
            });
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
        });
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/show_comment/',
            data: {'doc_id': this.$route.query.doc_id}
        })
        .then(response => {
            if(response.data.code === 200){
                this.commentData = response.data.commentlist
            }
            else if(response.data.code === 401){

            }
            else if(response.data.code === 400){
                alert('有错误')
            }
            else{
                alert('错误')
            }
        })
        .catch(error => {
            console.log(error)
            alert('出现错误')            
        });
    },
    mounted:function() {
        window.addEventListener('scroll', this.handleScroll); // Dom树加载完毕
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll) // 销毁页面时清除
    }
}
</script>

<style scoped>
.div1{
    display: none;
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