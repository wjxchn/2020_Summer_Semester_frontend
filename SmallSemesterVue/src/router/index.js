import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'PersonalDoc' },
  { path: '/animation', component: 'Animation' },
  { path: '/article', component: 'Article' },
  { path: '/bottomguider', component: 'BottomGuider' },
  { path: '/carousel', component: 'Carousel' },
  { path: '/createteam', component: 'CreateTeam' },
  { path: '/editpersonaldoc', component: 'EditPersonalDoc' },
  { path: '/guider', component: 'Guider' },
  { path: '/help' , component: 'Help'},
  { path: '/login', component: 'Login' },
  { path: '/pagedemo', component: 'PageDemo' },
  { path: '/person' , component: 'Person'},
  { path: '/personaldoc', component:'PersonalDoc'},
  { path: '/plaintext_new', component:'PlainText_new'},
  { path: '/regi', component: 'Regi' },
  { path: '/showplaintext_new', component:'ShowPlainText_new'},
  { path: '/team', component:'Team'},
  { path: '/teammanagement', component:'TeamManagement'},
  { path: '/trash' , component: 'Trash'},
  { path: '*', component: 'NotFound' },
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
