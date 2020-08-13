<template>
    <div>
        <Guider id="navBar" :class="{isFixed:istabBar}"/>
        <main id="mainPart" role="main" class="container">
            <div class="showplaintext_new">
                <h4 v-text="doc_name">文档名:{{doc_name}}</h4>
                <h4 v-text="doc_creater">作者:{{doc_creater}}</h4>
                <h4 v-text="doc_intro">文档信息:{{doc_intro}}</h4>
                <span v-html="htmlData">
                    {{htmlData}}
                </span>
            </div>
        </main>
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
            istabBar: false,
            doc_name: '',
            doc_creater: '',
            doc_intro: '',
            htmlData: ''
        }
    },
    methods: {
        
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
    background-color: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(30px);
}
#mainPart {
    width: 100%;
}
</style>