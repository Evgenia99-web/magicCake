<template>
  <swiper
      :modules="modules"
      :space-between="0"
      :loop="true"
      :pagination="{clickable: true}"
      :autoplay="{
        delay:7000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true
      }">
    <swiper-slide v-for="text in swiperTextBase" :key="text.title">
      <div class="slide" :class="text.class">
        <div class="slide_flex">
          <div class="slide_info">
            <h1 class="slide_title">{{text.title}}</h1>
            <router-link to="#" class="slide_btn">{{text.textbtn}}</router-link>
          </div>
          <div class="slide_poster">
            <img :src="text.img" class="slide_img" alt="Картинка слайда">
          </div>
        </div>
      </div>
    </swiper-slide>
  </swiper>
</template>

<script>
import {Swiper, SwiperSlide} from "swiper/vue";
import SwiperCore, {Autoplay, Pagination} from "swiper";
import 'swiper/swiper-bundle.css'
import 'swiper/swiper.css'
import {ref} from "vue";

SwiperCore.use([Pagination]);

export default {
  name: "Slider",
  components: { Swiper, SwiperSlide},
  setup(){
    const swiperTextBase = ref([
      {
        title: 'Кондитеры с радостью делятся с вами своими авторскими рецептами. С ними вы почувствуете себя кондитером',
        textbtn: 'Посмотреть все',
        img: 'src/assets/slide1.png',
        class: 'slide1'
      },
      {
        title: 'Магия рождает вкусные шедевры на кухне кондитера. Убедитесь сами, как они это делают в их постах',
        textbtn: 'Посмотреть все',
        img: 'src/assets/slide2.png',
        class: 'slide2'
      },
      {
        title: 'Здесь Вы сможете найти лучшего для себя кондитера в своем городе легко и просто. Все кондитеры в одном месте',
        textbtn: 'Посмотреть все',
        img: 'src/assets/slide3.png',
        class: 'slide3'
      },
  ]);
    return {modules: [Autoplay, Pagination], swiperTextBase}
  }
}
</script>

<style scoped>
.slide1{background: linear-gradient(286.97deg, #FCD7B8 22.51%, #F2B989 66.97%);}
.slide2{background: linear-gradient(286.08deg, #CBD5DF 19.79%, #8AABCE 81.56%);}
.slide3{background: linear-gradient(293.56deg, #E4C6E9 29.17%, #D5A3DD 74.25%);}
.swiper{margin-top: -220px;}
.slide_flex{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 120px;
  padding-top: 220px;
  padding-bottom: 120px;
}
.slide_title{
  font-family: 'Rubik Moonrocks',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 35px;
  line-height: 55px;
  color: #FFFFFF;
  max-width: 615px;
  margin-bottom: 63px;
}
.swiper-wrapper{height: 100vh !important;}
.slide_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  color: #FFFFFF;
  border: 2px solid #FFFFFF;
  border-radius: 25px;
  padding: 20px 42px;
}
.slide_img{max-width: 750px;}
.swiper-horizontal>.swiper-pagination-bullets, .swiper-pagination-bullets.swiper-pagination-horizontal{ margin-top: 680px !important;}
</style>