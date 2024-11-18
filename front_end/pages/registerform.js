export default {
    template : `
    <div class="d-flex justify-content-center align-items-center vh-100">
      <div class="card shadow p-4">
        <h3 class="card-title text-center mb-4">Sign Up</h3>
        <div class="form-group mb-3">
          <input v-model="email" type="email" class="form-control" placeholder="Email" required/>
        </div>
        <div class="form-group mb-4">
          <input v-model="password" type="password" class="form-control" placeholder="Password" required/>
        </div>
        <div class="form-group mb-4" placeholder="Role">
          <select v-model="role" class="form-control" placeholder="Role" >
            <option value="stud" placeholder="Role">Customer</option>
            <option value="inst">Service Professional</option>
          </select>
        </div>
        <button class="btn btn-primary w-100" @click="submitregister">Submit</button>
      </div>
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