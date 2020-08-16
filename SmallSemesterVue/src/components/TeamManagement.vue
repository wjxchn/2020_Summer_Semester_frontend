<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
      <el-container>
            <el-aside class="leftside" width="210px">

            <!--     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓  这个default-active是指当前激活的页面，把页面对应的index写进去，例如：当前页面是我的文档，则写进去2-1 -->
            <el-menu class="el-menu-vertical-demo" :default-openeds="opend"
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

    
        <h5 style="padding:20px">{{this.$route.query.group_name}}团队 的团队主页</h5>
        <el-tabs v-model="activeName" type="card">
            <el-tab-pane label="团队文档" name="first">
                <el-button style="width:70px;background-color:#f96332;color:white;float:right;margin-left:15px" @click="NewGroupdoc" >新建</el-button>
                <el-button  style="width:70px;background-color:#f96332;color:white;float:right" @click="dialogFormVisible = true;getPersonalDoc()">添加</el-button>
                 <el-dialog title="选择文件" :visible.sync="dialogFormVisible">
                    <el-table
                        ref="multipleTable"
                        :data="PersonalDocData"
                        tooltip-effect="dark"
                        style="width: 100%"
                        @selection-change="handleSelectionChange">
                       <el-table-column
                            type="selection"
                            width="55">
                        </el-table-column>
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
                    </el-table>
                    <div style="margin-top: 20px">
                        <el-button @click="dialogFormVisible=false" style="float:right;margin-left:10px;margin-right:10px" type="danger">取消</el-button>
                        <el-button @click="submitSelectedDoc();dialogFormVisible=false" style="float:right" type="primary">确定</el-button>
                        
                        <el-button @click="toggleSelection()">取消选择</el-button>
                    </div>                   
                    </el-dialog>
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
                        <el-button style="width:70px;background-color:#f96332;color:white" size=mini @click="handleEdit(scope.row)">编辑</el-button>
                        <el-button size=mini type="danger"  @click="handleDelete(scope.row)">删除</el-button>
                    
                    </template>
                    
                    </el-table-column>
                 </el-table>
            </el-tab-pane>
            <el-tab-pane label="团队管理" name="second">
                <el-button style="width:100px;background-color:#f96332;color:white;float:right" type="danger" @click="dismiss">解散团队</el-button>
                <el-button style="width:100px;background-color:#f96332;color:white;float:right">邀请成员</el-button>
                <el-table
                    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                    style="width: 100%;"
                    max-height="450"
                    >
                    <el-table-column
                    label="姓名"
                    prop="name" width="150px">
                    </el-table-column>
                    <el-table-column
                    label="权限"
                    prop="authority" width="300px">
                        <div style="width:100%;height:50px">
                            <el-slider  v-model="value" :show-tooltip="false" :max=2 :marks="marks" :step="1" show-stops @change="change"></el-slider>
                        </div>
                        

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
                        @click="prioritymanagement(scope.row)">权限管理</el-button>
                        <el-button
                        size="mini"
                        type="danger"
                       @click="handleDeletePerson(scope.row)">删除</el-button>
                    </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="分享" name="third">分享</el-tab-pane>
            <el-tab-pane label="历史记录" name="fourth">历史记录</el-tab-pane>
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
import axios from 'axios'
export default {
    name: 'PageDemo',
    components: {
        Guider,
        BottomGuider
    },
    data () {
        return {
            value: [0,2],
            marks:{
                0:'低',
                1:'中',
                2:'高'
            },
            authoritylevel:0,
            opend:['1','2','3'],
            uniqueOpened:false,
            activeName: 'first',
            istabBar: false,
            tableData: ['1','2'],     //团队成员管理数据
            search: '',              
            DocData:[],            //显示团队文件数据
            dialogFormVisible: false,
            formLabelWidth: '120px',
            PersonalDocData:[],
            multipleSelection: []
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
                if(response.data.code === 200){
                    this.$set(this, 'DocData', response.data.list)
                }
                else if(response.data.code === 400){
                    alert('加载团队文档错误')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
        axios({
                method: 'post',
                url: 'http://localhost:8000/api/showgroupmemberlist/',
                data: {'group_id':this.$route.query.group_id}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    this.$set(this,'tableData',response.data.memberlist)
                }
                else if(response.data.code===400){
                    alert('返回失败')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
    },
    
    methods: {
        change(e){
            this.authoritylevel=e
        },
        //侧边栏的跳转
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClick(row){
            console.log(row.docid)//此时就能拿到整行的信息
            this.$router.push({path: '/showplaintext_new', query: {doc_id: row.docid}})     
        },
        handleEdit(row){
            console.log(row.docid)//此时就能拿到整行的信息
            this.$router.push({path: '/editgroupdoc', query: {doc_id: row.docid, group_id: this.$route.query.group_id, group_name:
                                this.$route.query.group_name}})
        },
        handleDelete(row){
            console.log(row.docid)
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/deletegroupdoc/',
                data: {'docid': row.docid, 'groupid': this.$route.query.group_id}
            })
            .then(response =>{
                console.log(response)
                if(response.data.code === 200){
                    alert('删除团队文档成功')
                    this.$router.go(0)
                }
                else if(response.data.code === 400){
                    alert('删除团队文档失败')
                    this.$router.go(0)
                }
                else{
                    alert("错误")
                    this.$router.go(0)
                }
            })
            .catch(error =>{
                console.log(error)
                alert('出现错误')
                this.$router.go(0)
            })

        },
        handleDeletePerson(row){
            console.log(row.name)
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/deletegroupmember/',
                data: {'groupid': this.$route.query.group_id,
                       'usernameA':localStorage.getItem('username'),
                       'usernameB':row.name}
            })
            .then(response =>{
                console.log(response)
                if(response.data.code === 200){
                    alert('删除团队成员成功')
                    this.$router.go(0)
                }
                else if(response.data.code === 400){
                    alert('非团队管理员无权限删除团队成员')
                }
                else if(response.data.code === 401){
                    alert('无法删除团队创建者')
                }
                else{
                    alert("错误")
                    this.$router.go(0)
                }
            })
            .catch(error =>{
                console.log(error)
                alert('出现错误')
                this.$router.go(0)
            })

        },
        NewGroupdoc(){
            this.$router.push({path: '/newgroupdoc', query: {group_id: this.$route.query.group_id, group_name: this.$route.query.group_name}})
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
        dismiss(){
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/dismissgroup/',
                data: {'group_id':this.$route.query.group_id,
                       'username':localStorage.getItem('username')}
            })
            .then(response => {
                console.log(response)
                if(response.data.code===200){
                    alert('解散成功')
                    this.$router.push('/Team');
                }
                else if(response.data.code===400){
                    alert('团队创建者才可以解散团队')
                    this.$router.go(0)
                }
                else{
                    alert('错误')
                    this.$router.go(0)
                }
            })
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
        getPersonalDoc(){
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/showpersonaldoclist/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code===200){
                this.$set(this,'PersonalDocData',response.data.list)
            }
            else if(response.data.code===400){
                alert('文件不存在')
                this.$router.go(0)
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
        });
        },
        toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
        }
        },
        handleSelectionChange(val) {
        this.multipleSelection = val;
        },
        submitSelectedDoc(){  
            for(var i=0;i<this.multipleSelection.length;i++)
            {
                this.submitADoc(this.multipleSelection[i]);
            }
            this.$router.go(0)
        },
        submitADoc(item){
            console.log(item);
            axios({
            method: 'post',
            url: 'http://localhost:8000/api/addgroupdoc/',
            data: {'groupid': this.$route.query.group_id,
                   'item':item
            },
        })
        .then(response => {
            console.log(response)
        });
        },
        getTeamDoc(){
            axios({
            method: 'post',
            url: 'http://localhost:8000/api/show_group_doclist/',
            data: {'username': localStorage.getItem('username')}
        })
        .then(response => {
            console.log(response)
            if(response.data.code===200){
                this.$set(this,'DocData',response.data.list)
            }
            else if(response.data.code===400){
                alert('文件不存在')
                this.$router.go(0)
            }
            else{
                alert('错误')
                this.$router.go(0)
            }
        });
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