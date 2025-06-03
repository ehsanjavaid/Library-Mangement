<template>
  <div class="bg-white shadow rounded p-4 text-center">
    <div class="text-3xl">{{ icon }}</div>
    <div class="text-xl font-bold">{{ value }}</div>
    <div class="text-gray-500">{{ title }}</div>
  </div>
</template>

<script setup>
defineProps(['title', 'value', 'icon'])
</script>
