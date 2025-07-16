<template>

    <div class="p-4 bg-[#F4F8FB]">
        <div class="mb-6">
            <strong>
                <h2 class="text-xl">Manage Books</h2>
            </strong>
        </div>
        <div class="p-4 bg-white rounded-lg shadow">
            <!-- SEARCH BAR AND ACTIONS -->
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-4">
                <div class="relative w-full sm:w-[40%]">
                    <input v-model="searchText" type="text" placeholder="Search by ID, Title, or Author"
                        class="border px-4 py-2 pl-10 rounded shadow w-[58%]" />
                    <Search class="absolute left-3 top-2.5 text-gray-500 w-5 h-5" />
                </div>
                <div class="w-1/4 flex justify-around">
                    <button
                        class="bg-blue-700 text-white px-4 py-2 rounded shadow hover:bg-blue-700 flex items-center gap-2"
                        @click="handleAddBook">
                        <Plus class="w-4 h-4" />
                        Add Book
                    </button>


                    <div class="relative inline-block text-left">
                        <button class="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800 disabled:opacity-50"
                            :disabled="!selectedBooks.length" @click="toggleDropdown">
                            Actions
                            <ChevronDown class="w-4 h-4 inline-block mr-1" />
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
                            <th class="px-4 py-2">Book Title</th>
                            <th class="px-4 py-2">Author</th>
                            <th class="px-4 py-2">Category</th>
                            <th class="px-4 py-2">Location</th>
                            <th class="px-4 py-2">Total Copies</th>
                            <th class="px-4 py-2">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in filteredBooks" :key="book.name" class="border-b hover:bg-gray-50">
                            <td class="px-4 py-2">
                                <input type="checkbox" :value="book" v-model="selectedBooks" />
                            </td>
                            <td class="px-4 py-2">{{ book.name }}</td>
                            <td class="px-4 py-2 text-blue-700">{{ book.title }}</td>
                            <td class="px-4 py-2">{{ book.author }}</td>
                            <td class="px-4 py-2">{{ book.category }}</td>
                            <td class="px-4 py-2">{{ book.location }}</td>
                            <td class="px-4 py-2">{{ book.total_copies }}</td>
                            <td class="px-4 py-2">
                                <span :class="`status-${book.status?.toLowerCase()}`">
                                    {{ book.status }}
                                </span>
                            </td>
                        </tr>
                        <tr v-if="filteredBooks.length === 0">
                            <td colspan="8" class="text-center py-4">No books found</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <!-- Add Book Modal -->
            <div v-if="showAddModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
                    <h2 class="text-xl font-bold mb-4">Add New Book</h2>

                    <form @submit.prevent="submitBook">
                        <div class="mb-3">
                            <label class="block mb-1 font-medium">Title</label>
                            <input v-model="newBook.title" type="text" class="w-full border rounded px-3 py-2"
                                required />
                        </div>
                        <div class="mb-3">
                            <label class="block mb-1 font-medium">Author</label>
                            <input v-model="newBook.author" type="text" class="w-full border rounded px-3 py-2"
                                required />
                        </div>
                        <div class="mb-3">
                            <label class="block mb-1 font-medium">Category</label>
                            <input v-model="newBook.category" type="text" class="w-full border rounded px-3 py-2" />
                        </div>
                        <div class="mb-3">
                            <label class="block mb-1 font-medium">Location</label>
                            <input v-model="newBook.location" type="text" class="w-full border rounded px-3 py-2" />
                        </div>
                        <div class="mb-3">
                            <label class="block mb-1 font-medium">Total Copies</label>
                            <input v-model="newBook.total_copies" type="number" class="w-full border rounded px-3 py-2"
                                required />
                        </div>
                        <div class="mb-4">
                            <label class="block mb-1 font-medium">Status</label>
                            <select v-model="newBook.status" class="w-full border rounded px-3 py-2">
                                <option value="Available">Available</option>
                                <option value="Lended">Lended</option>
                                <option value="Damaged">Damaged</option>
                            </select>
                        </div>

                        <div class="flex justify-end gap-3">
                            <button type="button" @click="showAddModal = false"
                                class="text-gray-600 px-4 py-2">Cancel</button>
                            <button type="submit"
                                class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Save</button>
                        </div>
                    </form>
                </div>
            </div>

        </div>

    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { createResource } from 'frappe-ui'
import { Search, Plus, ChevronDown } from 'lucide-vue-next'


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
// Add new book modal



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
