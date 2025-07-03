<template>
  <header class="flex items-center justify-between px-6 py-4">
    <!-- Center: Search Bar -->
    <div class="flex-1 px-4">
      <input
        type="text"
        placeholder="Search"
        class=" px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>

    <!-- Right: Icons -->
    <div class="flex items-center space-x-5">
      <!-- Notification -->
      <button class="relative">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M15 17h5l-1.405-1.405C18.79 14.79 18 13.42 18 12V8a6 6 0 10-12 0v4c0 1.42-.79 2.79-1.595 3.595L3 17h5m7 0v1a3 3 0 11-6 0v-1m6 0H9" />
        </svg>
        <span class="absolute -top-1 -right-1 bg-red-500 text-white rounded-full text-xs w-4 h-4 flex items-center justify-center">3</span>
      </button>

      <!-- User Avatar -->
      <div class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center text-white">
        <span>A</span>
      </div>
    </div>
  </header>
</template>
