<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-transparent py-4 px-4">
    <ToggleButton :title="title" :onClick="toggleMenu" />
  </nav>
</template>

<script>
import ToggleButton from '@/components/buttons/ToggleButton.vue';

export default {
  name: 'NavBar',
  components: {
    ToggleButton
  },
  data() {
    return {
      title: 'Dashboard'
    };
  },
  methods: {
    toggleMenu() {
      const el = document.getElementById("wrapper");
      el.classList.toggle("toggled");
    }
  }
}
</script>
