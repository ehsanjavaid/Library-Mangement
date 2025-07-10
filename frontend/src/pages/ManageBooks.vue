<template>
    <div class="p-4">
        <!-- SEARCH BAR AND ACTIONS -->
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-4">
            <input v-model="searchText" type="text" placeholder="Search by ID, Title, or Author"
                class="border px-4 py-2 rounded shadow w-full sm:w-[40%]" />
            <div class = "w-1/4 flex justify-around">
                <button class="bg-blue-600 text-white px-4 py-2 rounded shadow hover:bg-blue-700"
                    @click="handleAddBook">
                    + Add Book
                </button>

                <div class="relative inline-block text-left">
                    <button class="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800 disabled:opacity-50"
                        :disabled="!selectedBooks.length" @click="toggleDropdown">
                        Actions ▾
                    </button>

                    <div v-if="dropdownOpen" class="absolute right-0 z-10 mt-2 w-40 bg-white border rounded shadow">
                        <ul>
                            <li>
                                <button class="w-full text-left px-4 py-2 hover:bg-gray-100" @click="editBooks">
                                    Edit Selected
                                </button>
                            </li>
                            <li>
                                <button class="w-full text-left px-4 py-2 hover:bg-gray-100 text-red-600"
                                    @click="deleteBooks">
                                    Delete Selected
                                </button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="resource.loading" class="text-center py-4">Loading books...</div>
        <div v-else-if="resource.error" class="text-center text-red-500 py-4">
            Error loading books: {{ resource.error.message || 'Unknown error' }}
        </div>

        <!-- TABLE -->
        <div v-else>
            <table class="table-auto w-full border">
                <thead>
                    <tr class="bg-gray-200 text-left">
                        <th class="px-4 py-2">
                            <input type="checkbox" @change="toggleSelectAll" :checked="isAllSelected" />
                        </th>
                        <th class="px-4 py-2">Book ID</th>
                        <th class="px-4 py-2">Title</th>
                        <th class="px-4 py-2">Author</th>
                        <th class="px-4 py-2">Category</th>
                        <th class="px-4 py-2">Status</th>
                        <th class="px-4 py-2">Location</th>
                        <th class="px-4 py-2">Total Copies</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="book in filteredBooks" :key="book.name" class="border-b hover:bg-gray-50">
                        <td class="px-4 py-2">
                            <input type="checkbox" :value="book" v-model="selectedBooks" />
                        </td>
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
                    <tr v-if="filteredBooks.length === 0">
                        <td colspan="8" class="text-center py-4">No books found</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { createResource } from 'frappe-ui'

const searchText = ref('')


const resource = createResource({
    url: '/api/method/library_management.api.managebooks.get_books_list',
    auto: true,
    transform: (r) => r.message,
})


const books = computed(() => resource.data?.books || [])
const selectedBooks = ref([])

// BOOKS FILTERS
const filteredBooks = computed(() => {
    const text = searchText.value.toLowerCase().trim()
    if (!text) return books.value

    return books.value.filter((book) => {
        return (
            book.name?.toLowerCase().includes(text) ||
            book.title?.toLowerCase().includes(text) ||
            book.author?.toLowerCase().includes(text)
        )
    })
})


const handleAddBook = () => {
    alert('Redirecting to add book page or open modal...')
}


const dropdownOpen = ref(false)
const toggleDropdown = () => {
    dropdownOpen.value = !dropdownOpen.value
}
document.addEventListener('click', (e) => {
    if (!e.target.closest('.relative')) dropdownOpen.value = false
})


const editBooks = () => {
    if (selectedBooks.value.length === 0) return
    alert(`Editing ${selectedBooks.value.length} book(s)`)
}

const deleteBooks = () => {
    if (selectedBooks.value.length === 0) return
    const confirmDelete = confirm(`Are you sure you want to delete ${selectedBooks.value.length} book(s)?`)
    if (confirmDelete) {
        alert(`Deleted books (implement backend call here)`)
    }
}


const isAllSelected = computed(() =>
    filteredBooks.value.length > 0 &&
    filteredBooks.value.every((book) => selectedBooks.value.includes(book))
)

const toggleSelectAll = () => {
    if (isAllSelected.value) {
        selectedBooks.value = []
    } else {
        selectedBooks.value = [...filteredBooks.value]
    }
}
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
