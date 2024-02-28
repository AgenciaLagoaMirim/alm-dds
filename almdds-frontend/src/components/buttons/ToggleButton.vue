<template>
  <div class="d-flex align-items-center">
    <i class="fas fa-align-left primary-text fs-4 me-3" @click="onClick"></i>
    <h2 class="fs-2 m-0">{{ title }}</h2>
  </div>
</template>

<script>
export default {
  name: 'ToggleButton',
  props: {
    title: String,
    onClick: Function
  }
}
</script>
