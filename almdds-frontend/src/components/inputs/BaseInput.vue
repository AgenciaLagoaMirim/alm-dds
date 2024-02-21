<template>
  <div>
    <label>{{ label }}</label>
    <input
      :placeholder="label"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    >
  </div>
</template>
<script>
export default {
  props: {
    label: {
      type: String,
      default: ""
    },
    modelValue: {
      type: [String, Number],
      default: ""
    }
  },
}
</script>