<template>
    <div class="p-4">
        <h1 class="text-2xl font-bold mb-4">Manage Books</h1>

        <div v-if="resource.loading" class="p-4 text-center">Loading books...</div>

        <div v-else-if="resource.error" class="p-4 text-center text-red-500">
            Error loading books: {{ resource.error.message || 'Unknown error' }}
        </div>

        <div v-else>
            <table class="table-auto w-full border">
                <thead>
                    <tr class="bg-gray-200 text-left">
                        <th class="px-4 py-2">Book Id</th>
                        <th class="px-4 py-2">Title</th>
                        <th class="px-4 py-2">Author</th>
                        <th class="px-4 py-2">Category</th>
                        <th class="px-4 py-2">Status</th>
                        <th class="px-4 py-2">Location</th>
                        <th class="px-4 py-2">Total Copies</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="book in books" :key="book.name" class="border-b hover:bg-gray-50">
                        <td class="px-4 py-2">{{ book.name }}</td>
                        <td class="px-4 py-2">{{ book.title }}</td>
                        <td class="px-4 py-2">{{ book.author }}</td>
                        <td class="px-4 py-2">{{ book.category }}</td>
                        <td class="px-4 py-2">
                            <span :class="`status-${book.status?.toLowerCase()}`">
                                {{ book.status }}
                            </span>
                        </td>
                        <td class="px-4 py-2">{{ book.location }}</td>
                        <td class="px-4 py-2">{{ book.total_copies }}</td>
                    </tr>
                    <tr v-if="books.length === 0">
                        <td colspan="6" class="px-4 py-2 text-center">No books found</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script setup>
import { createResource } from 'frappe-ui'
import { computed } from 'vue'
const resource = createResource({
    url: '/api/method/library_management.api.managebooks.get_books_list',
    auto: true,
    transform: (response) => response.message,
})

const books = computed(() => {
  return resource.data?.books || []
})

</script>

<style>
.status-available {
    @apply bg-green-100 text-green-800 px-2 py-1 rounded text-sm;
}

.status-borrowed {
    @apply bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-sm;
}

.status-lost {
    @apply bg-red-100 text-red-800 px-2 py-1 rounded text-sm;
}
</style>
