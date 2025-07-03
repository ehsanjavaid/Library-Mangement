<script setup>
import { Book, BookOpenCheck, Users,LayoutDashboard } from 'lucide-vue-next'
</script>
<template>
  <aside class="w-64 h-screen bg-white border-r px-4 py-6">
    <div class="flex items-center">
      <img src="http://localhost:8000/files/library-management-high-resolution-logo-transparent.png" alt="Logo"
        class="w-[8.5rem] h-[7.5rem] object-contain" />
    </div>
    <nav class="flex flex-col gap-[2rem] mt-6">
      <router-link to="/" class="flex items-center text-blue-700 hover:underline">
        <LayoutDashboard class="w-6 h-6 mr-2" />
        Dashboard
      </router-link>
      <router-link to="/books" class="flex items-center text-gray-700 hover:underline">
        <Book class="w-6 h-6 mr-2" />
        Manage Books
      </router-link>
      <router-link to="/members" class="flex items-center text-gray-700 hover:underline">
        <Users class="w-6 h-6 mr-2" />
        Members
      </router-link>
      <router-link to="/issue" class="flex items-center text-gray-700 hover:underline">
        <BookOpenCheck class="w-6 h-6 mr-2" />
        Issue Book
      </router-link>
    </nav>
  </aside>
</template>
