<template>
  <div class="auth_page">
    <HomeHeader/>
    <div class="regist_block container">
      <img src="src/assets/girl_donat.png" class="welcome_img" alt="">
      <div class="regist_block_form">
        <h2 class="regist_title">Авторизация</h2>
        <div class="regist_form_block">
          <form @submit="login">
            <div class="form_block_item">
              <label for="username">Логин</label>
              <input v-model="username" type="text" id="username" placeholder="Введите логин"/>
            </div>
            <div class="form_block_item">
              <label for="password">Пароль</label>
              <input v-model="password" type="password" id="password" placeholder="Введите пароль"/>
            </div>
            <button type="submit" class="auth_btn">Войти</button>
          </form>
          <span class="not_yet">У вас еще нет аккаунта? <router-link to="Registration">Зарегистрироваться</router-link></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomeHeader from "@/components/HomeHeader.vue";
import axios from "axios";

export default {

  name: "Auth",
  components: {HomeHeader},
  data() {
    return{
      username: "",
      password: ""
    };
  },
  methods: {
    login(event) {
      event.preventDefault();
      // auth logic
      axios.post(`http://127.0.0.1:8000/api/token/`,
          {
            headers : { 'Content-type': 'application/json'},
            'username' : this.username, 'password': this.password
          })
          .then(response => {
            this.setLogined(response.data.access)
          })
          .catch(err => {console.error(err)})
    },
    setLogined(token) {
      // save token
     console.log(token);
      localStorage.setItem('token', token);
    }
  }
}
</script>

<style scoped>
header{  margin-top: 0; margin-bottom: 20px;}
.auth_page{
  background: url("src/assets/bg_auth.png") no-repeat center;
  background-size: cover;
  height: 100vh;
  padding-top: 35px;
}
.regist_block{display: flex; justify-content: space-around; align-items: center;}
.welcome_img{ width: 550px;}
.regist_title{
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 59px;
  color: #FFFFFF;
  text-align: center;
  margin-bottom: 30px;
}
.regist_form_block{  width: 400px; text-align: center;}
.form_block_item label{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: #B16FBC;
  margin-bottom: 6px;
  margin-left: 30px;
}
.form_block_item input{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 16px;
  line-height: 20px;
  color: #D5A3DD;
  background: rgba(255, 255, 255, 0.46);
  border: 2px solid #D5A3DD;
  border-radius: 25px;
  width: 100%;
  padding: 17px 27px;
}
.form_block_item{ margin-bottom: 10px;   text-align: left;}
.auth_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  color: #FFFFFF;
  padding: 12px 90px;
  margin-top: 10px;
  margin-bottom: 30px;
  background: #B16FBC;
  border-radius: 25px;
  border: none;
}
.not_yet{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 20px;
  color: #B16FBC;
}
</style>