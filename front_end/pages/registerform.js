export default {
    template : `
    <div>
        <input placeholder="Email"  v-model="email"/>  
        <input placeholder="Password"  v-model="password"/>  
        <input placeholder="Role"  v-model="role"/>
        <button class='btn btn-primary' @click="submitregister"> Sign Up </button>
    </div>
    `,
    data(){
        return {
            email:null,
            password:null,
            role:null,
                }
            },

    methods:{
        async submitregister(){
            const res=await fetch(location.origin+'/register',
                {
                method:'POST',
                headers:{'Content-type':'application/json'},
                body:JSON.stringify({'email':this.email,'password':this.password,'role':this.role})}
                                )
            if(res.ok){
                console.log('We are Registerd')
                      }
                          }
}
}