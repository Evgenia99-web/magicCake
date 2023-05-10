<template>
  <swiper
      :modules="modules"
      :slides-per-view="2"
      :space-between="25"
      :loop="true"
      navigation
      :autoplay="{
        delay:7000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true
      }">
    <swiper-slide v-for="text in swiperTextFeedback" :key="text.author">
      <div class="slide_feed">
        <div class="slide_person">
          <img :src=text.avatar class="avatar" alt="">
          <p class="person_name">{{text.author}}</p>
        </div>
        <p class="feed_info">{{text.type}} / Кондитер: {{text.cooker}}</p>
        <p class="feed_text">{{text.text}}</p>
        <p class="feed_date">{{text.date}}</p>
      </div>
    </swiper-slide>
  </swiper>
</template>

<script>
import {Swiper, SwiperSlide} from "swiper/vue";
import SwiperCore, {Autoplay, Navigation} from "swiper";
import 'swiper/swiper-bundle.css'
import 'swiper/swiper.css'
import {ref} from "vue";

SwiperCore.use([Navigation]);
export default {
  name: "FeedbackSlider",
  components: { Swiper, SwiperSlide},
  setup(){
    const swiperTextFeedback = ref([
        {
        author: 'Саева Кристина',
        type: 'Торт',
        avatar: 'src/assets/author1.jpg',
        cooker: 'Талых Ольга',
        date: '01.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Красилова Анна',
        type: 'Торт',
        avatar: 'src/assets/author2.jpg',
        cooker: 'Иванова Елизаветта',
        date: '30.04.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Кузьминых Ольга',
        type: 'Капкейки',
        avatar: 'src/assets/author3.jpg',
        cooker: 'Ушакова Татьяна',
        date: '01.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Лавреньтева Инна',
        type: 'Торт',
        avatar: 'src/assets/author4.jpg',
        cooker: 'Талых Ольга',
        date: '28.04.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Алехина Вероника',
        type: 'Чизкейк',
        avatar: 'src/assets/author5.jpg',
        cooker: 'Уразова Ильсияр',
        date: '02.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
    ]);
    return {modules: [Autoplay, Navigation], swiperTextFeedback}
  }
}
</script>

<style scoped>
.slide_feed{
  background: rgba(234, 234, 234, 0.72);
  border-radius: 25px;
  padding: 30px;
}
.slide_person{display: flex; align-items: center; margin-bottom: 30px;}
.avatar{width: 76px; border: 3px solid #69BEB8; border-radius: 50%;margin-right: 18px;}
.person_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 24px;
  color: #69BEB8;
}
.feed_info{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  color: #808080;
  margin-bottom: 20px;
}
.feed_text, .feed_date{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 12px;
  line-height: 27px;
  color: #808080;
  margin-bottom: 20px;
}
.feed_date{font-weight: 400; margin-bottom: 0;}
</style>