import { createRouter, createWebHistory } from 'vue-router'
import DisplayVideo from '../components/DisplayVideo.vue';
import Home from '../views/Home.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path:'/display',
      name:'DisplayVideo',
      component:DisplayVideo,
    }
    
  ]
})

export default router
