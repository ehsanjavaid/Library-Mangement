<template>
  <aside class="w-64 h-screen bg-white border-r px-4 py-6">
    <h2 class="text-2xl font-bold mb-6">📘 Librarian</h2>
    <nav class="flex flex-col gap-4">
      <router-link to="/" class="text-blue-700 hover:underline">Dashboard</router-link>
      <router-link to="/books" class="text-gray-700 hover:underline">Manage Books</router-link>
      <router-link to="/members" class="text-gray-700 hover:underline">Members</router-link>
      <router-link to="/issue" class="text-gray-700 hover:underline">Issue Book</router-link>
    </nav>
  </aside>
</template>
