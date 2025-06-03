<template>
  <div class="flex">
    <Sidebar />
    <router-view class="flex-1 p-6 bg-gray-100" />
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
</script>
