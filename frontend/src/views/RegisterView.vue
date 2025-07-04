<template>
    <h1>Register page</h1>

    <form @submit.prevent="submitRegister()">

        <label for="name">Name</label>
        <input type="text" v-model="name">
            
        <label for="email">Email</label>
        <input v-model="email" type="email">

        <label for="password">Password</label>
        <input v-model="password" type="password">

        <button type="submit">Submit</button>

    </form>


    <p>Have an account? Click <a href="/login">here</a> to login!</p>
</template>

<script>
export default {
  // Data properties become reactive state
  data() {
    return {
      name: '',
      email: '',
      password: ''
    };
  },
  // Methods are functions that can be called in the template
  methods: {
    submitRegister() {
        fetch("http://127.0.0.1:5000/register", {
            method: "POST",
            body: JSON.stringify({'email': this.email, 'password': this.password, 'name': this.name}),
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
            })
    }
  },
  // Lifecycle hooks are called at different stages of a component's lifecycle
  mounted() {
    console.log('Component mounted!');
  }
};
</script>