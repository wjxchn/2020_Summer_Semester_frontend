<template>
    <div>
        <div class="before-bottom-guider-style">   
        </div>
        <div class="bottom-guider-border-style border-top">
            <div class="container">
                <p class="bottom-guider-text">@2020 Fubao Document<br/>This is used only for learning. Commertial use is not allowed.<br/><br/></p>
                <a style="color:#f96332" href="/help" class="bottom-guider-link">User guide</a>
                <a style="color:#f96332" href="/aboutus" class="bottom-guider-link">About us</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BottomGuider'
}
</script>

<style scoped>
.before-bottom-guider-style{
    width: 100%;
    height: 50px;
    background-color: white;    
}
.bottom-guider-border-style{
    width: 100%;
    height: 150px;
    background-color: rgb(245, 245, 245);
    padding: 30px;
}
.bottom-guider-text{
    font-size: 15px;
    color: black;
}
.bottom-guider-link{
    margin-right: 20px;
}
</style>