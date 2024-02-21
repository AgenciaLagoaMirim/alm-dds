import { createRouter, createWebHistory } from 'vue-router'
import DashBoardView from '../views/DashBoardView.vue'



const routes = [
  {
    path: '/',
    name: 'dash-board',
    component: DashBoardView

  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
