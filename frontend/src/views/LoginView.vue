<template>
    <h1>Login page</h1>

    <form @submit.prevent="submitLogin()">
            
        <label for="email">Email</label>
        <input v-model="email" type="email">

        <label for="password">Password</label>
        <input v-model="password" type="password">

        <button type="submit">Submit</button>

    </form>


    <p>Don't have an account? Click <a href="/register">here</a> to register!</p>
</template>

<script>
export default {
  // Data properties become reactive state
  data() {
    return {
      email: '',
      password: ''
    };
  },
  // Methods are functions that can be called in the template
  methods: {
    submitLogin() {
        fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            body: JSON.stringify({'email': this.email, 'password': this.password }),
            headers: {
                "Content-Type": "application/json",
            }})
            .then(response => {
                if (!response.ok) {
                }
                return response.json()
            })
            .then(data => {
                console.log('response from be', data)
                alert(data.msg)
                if (data.token) {
                    localStorage.setItem('token', data.token)
                    if (data.user.role === "user") {
                        this.$router.push('/user')
                    } else {
                        this.$router.push('/admin')
                    }
                }
            })
    }
  },
  // Lifecycle hooks are called at different stages of a component's lifecycle
  mounted() {
    console.log('Component mounted!');
  }
};
</script>