<template>
  <footer>
    <div class="container">
      <div class="footer_logo_block">
        <div class="left_side">
          <div class="left_side_name">
            <p class="main_name left_name">MAGIC</p>
          </div>
        </div>
        <div class="logo_center">
          <router-link :to="{name: 'Home'}">
            <img src="src/assets/logo_white.png" class="logo white" alt="логотип Magoc Cake">
          </router-link>
        </div>
        <div class="right_side">
          <div class="right_side_name">
            <p class="main_name right_name">CAKE</p>
          </div>
        </div>
      </div>
      <div class="footer_nav_block">
        <div class="footer_nav">
          <div class="footer_nav_left">
            <router-link :to="{name: 'Home'}" class="nav_item">Главная</router-link>
            <router-link :to="{name: 'About'}" class="nav_item">О портале</router-link>
            <router-link :to="{name: 'Home'}" class="nav_item">Кондитеры</router-link>
          </div>
          <div class="footer_nav_right">
            <router-link :to="{name: 'Home'}" class="nav_item">Рецепты</router-link>
            <router-link :to="{name: 'Home'}" class="nav_item">Публикации</router-link>
          </div>
        </div>
        <div class="footer_poster">
          <img src="src/assets/footer_img.png" class="footer_img" alt="Картинка торта">
        </div>
        <div class="footer_info">
          <p class="footer_info_item">Для сотрудничества обращаться на почту <a href="mailto:proximastar@yandex.ru">proximastar@yandex.ru</a></p>
          <p class="footer_info_item">&copy Все права защищены 2023 </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>
.footer_logo_block, .left_side, .right_side, .footer_nav_block{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
footer{
  background: linear-gradient(154.86deg, #9CE3DE 12.83%, #0FAA9F 115.97%);
  height: 520px;
  padding-top: 30px;
  margin-top: 50px;
}
.left_side, .right_side{
  width: 550px;
  border-bottom: 1px solid #ffffff;
  padding-bottom: 18px;
}
.logo_center{  margin: 0 23px;}
.main_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 44px;
  color: #ffffff;
}
.left_side{justify-content: end;}
.footer_nav, .footer_nav_block{align-items: flex-start; display: flex;}
.footer_nav_right, .footer_nav_left{  display: grid;  max-width: 140px;}
.footer_nav_left{margin-right: 25px;}
.nav_item{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 35px;
  color: #FFFFFF;
}
.footer_img{  width: 100%;}
.footer_info_item{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 35px;
  text-align: center;
  color: #FFFFFF;
  max-width: 286px;
  margin-bottom: 30px;
}
</style>