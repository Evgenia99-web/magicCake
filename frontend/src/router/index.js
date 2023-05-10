import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Registration from "@/views/Registration.vue";
import Auth from "@/views/Auth.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
        {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/auth',
        name: 'Auth',
        component: Auth
    },
     {
        path: '/registration',
        name: 'Registration',
        component: Registration
    },

]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;