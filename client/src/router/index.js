import { createRouter, createWebHistory } from 'vue-router'
import DisplayVideo from '../components/DisplayVideo.vue';
import submitForm from '../components/submitForm.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Submitform',
      component: submitForm
    },
    {
      path:'/display',
      name:'DisplayVideo',
      component:DisplayVideo
    }
    
  ]
})

export default router
