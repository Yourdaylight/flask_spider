<template>
    <div class="netease">
        <iframe src="http://you.163.com/item/detail?id=4028691" id="mobsf" scrolling="no" frameborder="0" style=""></iframe>
    </div>
</template>
<script>
export default {
    name:'netease',
    data(){
        return {
            
        }
    },
    mounted(){
    /**
      * iframe-宽高自适应显示   
      */
      function changeMobsfIframe(){
        const mobsf = document.getElementById('mobsf');
        const deviceWidth = document.body.clientWidth;
        const deviceHeight = document.body.clientHeight;
        mobsf.style.width = (Number(deviceWidth)-120) + 'px'; //数字是页面布局宽度差值
        mobsf.style.height = (Number(deviceHeight)-80) + 'px'; //数字是页面布局高度差
      }
 
      changeMobsfIframe()
 
      window.onresize = function(){
        changeMobsfIframe()
      }

    }
}
</script>
<style scoped>
.netease{
    width: 100%;
    height: 100%;
}
</style>