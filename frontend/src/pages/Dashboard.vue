<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <Header />
    <h1 class="text-2xl font-bold mb-4">Welcome Admin</h1>
    <div v-if="resource.loading" class="text-gray-500">Loading...</div>
    <div v-else class="grid gap-6 grid-cols-[repeat(auto-fit,minmax(250px,1fr))]">
      <div class="bg-yellow-100 text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2"> Total Books</h2>
        <p class="text-3xl font-bold">{{ resource.data.total_books }}</p>
      </div>
      <div class="bg-yellow-100 text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <Users class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Total Members</h2>
        <p class="text-3xl font-bold">{{ resource.data.members }}</p>
      </div>
      <div class="bg-yellow-100 text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Book Issued</h2>
        <p class="text-3xl font-bold">{{ resource.data.book_issue }}</p>
      </div>
      <div class="bg-yellow-100 text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Available Books</h2>
        <p class="text-3xl font-bold">{{ resource.data.available_books }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { createResource } from 'frappe-ui'
import { BookOpen, Users } from 'lucide-vue-next'
import Header from '@/components/Layout/Header.vue'
const resource = createResource({
  url: '/api/method/library_management.api.dashboard.get_dashboard_data',
  auto: true,
  transform: (response) => response.message
})
</script>
