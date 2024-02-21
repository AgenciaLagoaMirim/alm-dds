<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-transparent py-4 px-4">
    <div class="d-flex align-items-center">
      <i class="fas fa-align-left primary-text fs-4 me-3" id="menu-toggle" @click="toggleMenu"></i>
      <h2 class="fs-2 m-0">Dashboard</h2>
    </div>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

  </nav>
</template>
<script>
export default {
  name: 'NavBar',
  methods: {
    toggleMenu() {
      const el = document.getElementById("wrapper");
      el.classList.toggle("toggled")
  }
}
}
</script>