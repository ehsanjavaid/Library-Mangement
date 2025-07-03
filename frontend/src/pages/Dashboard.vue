<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
    <div v-if="resource.loading" class="text-gray-500">Loading...</div>
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="bg-yellow-100 text-center p-6 rounded-xl shadow">
        <h2 class="text-lg font-semibold mb-2">📚 Total Books</h2>
        <p class="text-3xl font-bold">{{ resource.data.total_books }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { createResource } from 'frappe-ui'

const resource = createResource({
  url: '/api/method/library_management.api.dashboard.get_dashboard_data',
  auto: true,
  transform: (response) => response.message
})
</script>
