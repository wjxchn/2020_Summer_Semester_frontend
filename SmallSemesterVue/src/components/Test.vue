<template>
    <div :class="{'div':isTrue}"></div>

</template>
<style scoped>
.div{
width:100px;
height:100px;
background-color:blue
}

</style>
<script>

export default {
    
    data(){
        return{
            isTrue:true,
            hasError:false
        }
}}
</script>