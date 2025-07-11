<template>
    <div class="p-6 bg-[#F4F8FB] min-h-screen">
        <h2 class="text-xl font-semibold mb-4">📚 Add Book</h2>

        <div class="bg-white p-6 rounded shadow-md">
            <form @submit.prevent="submitForm" class="space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium">Book Title *</label>
                        <input v-model="form.title" type="text" required class="input" />
                    </div>

                    <div>
                        <label class="block text-sm font-medium">Author *</label>
                        <input v-model="form.author" type="text" required class="input" />
                    </div>

                    <div>
                        <label class="block text-sm font-medium">Category *</label>
                        <input v-model="form.category" type="text" required class="input" />
                    </div>

                    <div>
                        <label class="block text-sm font-medium">Location</label>
                        <input v-model="form.location" type="text" class="input" />
                    </div>

                    <div>
                        <label class="block text-sm font-medium">Total Copies *</label>
                        <input v-model="form.total_copies" type="number" required class="input" />
                    </div>

                    <div>
                        <label class="block text-sm font-medium">Status</label>
                        <select v-model="form.status" class="input">
                            <option>Available</option>
                            <option>Lended</option>
                            <option>Damaged</option>
                        </select>
                    </div>
                </div>

                <div class="flex justify-end gap-4 mt-4">
                    <button type="button" @click="cancel"
                        class="btn bg-gray-200 hover:bg-gray-300 text-black">Cancel</button>
                    <button type="submit" class="btn bg-purple-600 hover:bg-purple-700 text-white">Add Book</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { call } from 'frappe-ui'

const form = ref({
    title: '',
    author: '',
    category: '',
    status: 'Available',
    location: '',
    total_copies: 1,
})

const submitForm = async () => {
    try {
        const res = await call('/api/method/library_management.api.managebooks.add_book', {
            method: 'POST',
            args: form.value,
        })
        alert('Book added successfully!')
        // Optional: redirect
    } catch (err) {
        alert('Error adding book')
        console.error(err)
    }
}

const cancel = () => {
    window.history.back()
}
</script>

<style scoped>
.input {
    @apply border rounded px-3 py-2 w-full shadow-sm focus:outline-none focus:ring-1 focus:ring-blue-400;
}

.btn {
    @apply px-4 py-2 rounded font-medium;
}
</style>
