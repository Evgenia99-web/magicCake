<template>
  <HomeHeader/>
  <Slider/>
  <div class="interesting container">
    <h1 class="home_title">Интересное от кондитеров</h1>
    <div class="tabs_block">
      <div class="nav_tabs">
        <div class="nav_tabs_item" @click="setActive('tab-1')" :class="{ 'active active1' : isActive('tab-1') , 'pl' : isActive('tab-2')}">Рецепты</div>
        <div class="nav_tabs_item" @click="setActive('tab-2')" :class="{ 'active active2' : isActive('tab-2')}">Публикации</div>
      </div>
      <div class="tabs_content">
        <div class="tab tab1" v-show="isActive('tab-1')">
          <p>Тут будут рецепты</p>
          <router-link to="#" class="all_btn">Посмотреть все</router-link>
        </div>
        <div class="tab tab1" v-show="isActive('tab-2')">
          <p>Тут будут публикации</p>
          <router-link to="#" class="all_btn">Посмотреть все</router-link>
        </div>
      </div>
    </div>
  </div>
  <div class="banner">
    <img src="src/assets/donat_left.png" class="left_banner_img" alt="">
    <div class="banner_info">
      <p class="banner_info_text">Здесь Вы легко найдете легко найдете кондитера в своем городе</p>
      <router-link to="#" class="banner_info_btn">Найти кондитера</router-link>
    </div>
    <img src="src/assets/donat_right.png" class="right_banner_img" alt="">
  </div>
  <div class="feedback container">
    <h1 class="home_title">Отзывы заказчиков</h1>
    <FeedbackSlider/>
  </div>
  <Footer/>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Slider from "@/components/Slider.vue";
import HomeHeader from "@/components/HomeHeader.vue";
import FeedbackSlider from "@/components/FeedbackSlider.vue";

export default {
  name: "Home",
  components: {FeedbackSlider, HomeHeader, Slider, Footer},
  data: () => ({
    activeTab: 'tab-1'
  }),
  methods : {
    setActive(tab){
      this.activeTab = tab
    },
    isActive(tab){
      return this.activeTab === tab;
    }
  }
}
</script>

<style scoped>
.home_title{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 78px;
  color: #4C9691;
  margin-top: 100px;
  margin-bottom: 75px;
  text-align: center;
}
.interesting{margin-bottom: 100px;}
.tab{text-align: center;}
.tab p{margin: 30px 0}
.all_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 20px;
  color: #4C9691;
  border: 2px solid #4C9691;
  border-radius: 25px;
  padding: 12px 65px;
  margin-top: 100px;
}
.nav_tabs{
  display: flex;
  align-items: center;
  height: 55px;
  max-width: 600px;
  margin: 0 auto;
  border: 2px solid #0FAA9F;
  border-radius: 25px;
}
.nav_tabs_item{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  line-height: 39px;
  color: #69BEB8;
  cursor: pointer;
}
.active{
  color: #FFFFFF;
  background: #69BEB8;
  border-radius: 25px;
  padding: 7px 120px;
}
.active1{  margin-right: 37px;}
.active2{  margin-left: 40px;}
.pl{  margin-left: 48px;}
.banner{
  background: linear-gradient(167.24deg, #FCD1AC -1.55%, #F2B989 92.1%);
  height: 400px;
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 90px;
}
.banner img{ max-height: 450px;}
.banner_info{text-align: center;}
.banner_info_text{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 40px;
  line-height: 59px;
  color: #FFFFFF;
  margin-bottom: 80px;
}
.banner_info_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 26px;
  line-height: 39px;
  color: #D8A376;
  background: #FFFFFF;
  border-radius: 50px;
  padding: 15px 80px;
}
</style>