export default {
    template : `
    <div>
        <input placeholder="email"  v-model="email"/>  
        <input placeholder="password"  v-model="password"/>  
        <button class='btn btn-primary' @click="submitlogin"> Login </button>
    </div>
    `,
    data(){
        return {
            email:null,
            password:null,
                }
            },

    methods:{
        async submitlogin(){
            const res=await fetch(location.origin+'/login',
                {
                method:'POST',
                headers:{'Content-type':'application/json'},
                body:JSON.stringify({'email':this.email,'password':this.password})}
                                )
            if(res.ok){
                console.log('we are logged in')
                const data=await res.json()
                console.log(data)
                      }
                          }
}
}