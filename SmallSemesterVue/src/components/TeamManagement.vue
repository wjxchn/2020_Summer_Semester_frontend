<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
       <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu default-active="1-2" class="el-menu-vertical-demo" :default-openeds="opend"
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
        <el-main id="TeamManagement" role="main" class="container">
            <h5>特朗普团队 的团队主页</h5>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="团队文档" name="first">
                <el-button style="width:70px;background-color:#f96332;color:white;float:right">新建</el-button>
                <el-button  style="width:70px;background-color:#f96332;color:white;float:right">添加</el-button>
                <el-table
                    :data="DocData.filter(data => !search || data.docname.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%"
                    :row-class-name="tableRowClassName">
                     <el-table-column type="index" label="序号"></el-table-column>
                    <el-table-column
                    prop="docname"
                    label="文档名"
                    >
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="creator"
                    label="创建者"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    fixed="right"
                    prop="createtime"
                    label="创建时间"
                    width="180">
                    </el-table-column>  
                     <el-table-column
                    fixed="right"
                    width="260">
                    <template slot="header" slot-scope="scope">
                        <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"/>
                    </template>
                    <template slot-scope="scope">
                    
                        <el-button style="width:70px;background-color:#f96332;color:white" size=mini @click="handleClick(scope.row)">查看</el-button>
                        <el-button style="width:70px;background-color:#f96332;color:white" size=mini >编辑</el-button>
                        <el-button size=mini type="danger"  @click="open">删除</el-button>
                    
                    </template>
                    
                    </el-table-column>
                 </el-table>
            </el-tab-pane>
            <el-tab-pane label="团队管理" name="second">
                <el-button style="width:100px;background-color:#f96332;color:white;float:right" type="danger">解散团队</el-button>
                <el-button style="width:100px;background-color:#f96332;color:white;float:right">邀请成员</el-button>
                <el-table
                    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%"
                    max-height="450"
                    >
                    <el-table-column
                    label="姓名"
                    prop="name">
                    </el-table-column>
                    <el-table-column
                    label="权限"
                    prop="authority">
                    </el-table-column>
                    <el-table-column
                    label="身份"
                    prop="identity">
                    </el-table-column>
                    <el-table-column
                    align="right">
                    <template slot="header" slot-scope="scope">
                        <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"/>
                    </template>
                    <template slot-scope="scope">
                        <el-button style="width:80px;background-color:#f96332;color:white"
                        size="mini"
                        @click="handleEdit(scope.$index, scope.row)">权限管理</el-button>
                        <el-button
                        size="mini"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="分享" name="third">分享</el-tab-pane>
            <el-tab-pane label="历史记录" name="fourth">历史记录</el-tab-pane>
        </el-tabs>

       

        </el-main>
        </el-container>
        </el-container>
        <BottomGuider/>
    </div>
</template>

<script>
import Guider from '../components/Guider'
import BottomGuider from '../components/BottomGuider'
import axios from 'axios'
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
            activeName: 'first',
            istabBar: false,
            tableData: [{
          authority: '查看 修改 删除 增加',
          name: '特朗普',
          identity:'创建者 管理员',
          address: '白宫'
        },{
          authority: '查看 修改 删除 增加',
          name: '特朗普的口罩',
          identity:'管理员',
          address: '白宫'
        }, {
          authority: '查看 修改 删除 增加',
          name: '特朗普的儿子',
          identity:'成员',
          address: '白宫'
        }, {
          authority: '查看 修改 删除 增加',
          name: '特朗普的儿子',
          identity:'成员',
          address: '白宫'
        },
        {
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        },{
          authority: '查看',
          name: '特朗普的金毛',
          identity:'成员',
          address: '白宫'
        }],
        search: '',
        DocData:[],
        }
    },
    created:function(){
        axios({
                method: 'post',
                url: 'http://localhost:8000/api/showgroupdoclist/',
                data: {'doc_groupid':this.$route.query.group_id}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    this.$set(this,'DocData',response.data.doclist)
                }
                else if(response.data.code===400){
                    alert('文件不存在')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
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
        },
        handleEdit(index, row) {
            console.log(index, row);
        },
        handleDelete(index, row) {
            console.log(index, row);
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

</style>