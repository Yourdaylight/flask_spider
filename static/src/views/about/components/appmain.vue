<template>
    <div class="appmain">
        <router-view/>
    </div>
</template>
<script>
export default {
    // props:{
    //     url:{
    //         type:String,
    //         default:''
    //     }
    // },
    // data(){
    //     return{
    //         theUrl:this.url
    //     }
    // },
//     created(){
//         console.log(this.theUrl ,this.url);
//         this.theUrl = this.url;
//     }
}
</script>
<style>
.appmain{
    /* margin: 20px; */
    background-color: #fff;
    height: 100%;
    border-radius: 4px
}
</style>