<script setup>
</script>

<template>
  <div class="home-container">
    <div class="content-box">
      <h1>Welcome to InspireDaily</h1>
      <p class="intro-text">
        A place where words change lives. Discover, save, and share powerful quotes that uplift, motivate, and inspire.
      </p>
      <p class="cta-text">
        Ready to get inspired? 
        <a href="/login" class="btn">Login</a> or 
        <a href="/register" class="btn btn-primary">Register</a>
      </p>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(120deg, #f6d365, #fda085);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.content-box {
  background: white;
  padding: 3rem;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 500px;
}

h1 {
  margin-bottom: 1rem;
  color: #333;
  font-size: 2.2rem;
}

.intro-text {
  font-size: 1.1rem;
  color: #555;
  margin-bottom: 2rem;
}

.cta-text {
  font-size: 1rem;
}

a.btn {
  text-decoration: none;
  padding: 0.6rem 1.2rem;
  margin: 0 0.4rem;
  border-radius: 6px;
  background-color: #ddd;
  color: #333;
  transition: background 0.3s ease;
}

a.btn:hover {
  background-color: #ccc;
}

a.btn-primary {
  background-color: #ff7f50;
  color: white;
}

a.btn-primary:hover {
  background-color: #ff5722;
}
</style>
