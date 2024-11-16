const Home={
    template:`<h1>this is home page</h1>`
}

import loginfrom from "../pages/loginfrom.js"
import registerform from "../pages/registerform.js"

const routes=[
    {path:'/',component : Home},
    {path:'/login',component : loginfrom},
    {path:'/register',component : registerform},
            ]
const router=new VueRouter({
    routes
})

export default router;