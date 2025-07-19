<template>
    <div class="p-4 bg-[#F4F8FB]">
        <div class="mb-6">
            <strong>
                <h2 class="text-2xl font-semibold text-gray-800">Manage Members</h2>

            </strong>
        </div>
        <div class="p-4 bg-white rounded-lg shadow">
            <!-- SEARCH BAR AND ACTIONS -->
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-4">
                <div class="relative w-full sm:w-[40%]">
                    <input v-model="searchText" type="text" placeholder="Search by Membership ID or Full Name"
                        class="border px-4 py-2 pl-10 rounded-lg shadow w-full sm:w-full" />

                </div>
                <div class="w-1/4 flex justify-around">
                    <button
                        class="bg-blue-700 text-white px-4 py-2 rounded shadow hover:bg-blue-700 flex items-center gap-2"
                        @click="handleAddMember">
                        <Plus class="w-4 h-4" />
                        Add Member
                    </button>

                    <div class="relative inline-block text-left">
                        <button class="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800 disabled:opacity-50"
                            :disabled="!selectedMembers.length" @click="toggleDropdown">
                            Actions
                            <ChevronDown class="w-4 h-4 inline-block mr-1" />
                        </button>

                        <div v-if="dropdownOpen" class="absolute right-0 z-10 mt-2 w-40 bg-white border rounded shadow">
                            <ul>
                                <li>
                                    <button class="w-full text-left px-4 py-2 hover:bg-gray-100" @click="editMembers">
                                        Edit Selected
                                    </button>
                                </li>
                                <li>
                                    <button class="w-full text-left px-4 py-2 hover:bg-gray-100 text-red-600"
                                        @click="deleteMembers">
                                        Delete Selected
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="resource.loading" class="text-center py-4">Loading Members...</div>
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
                            <th class="px-4 py-2">Membership ID</th>
                            <th class="px-4 py-2">Full Name</th>
                            <th class="px-4 py-2">Phone Number</th>
                            <th class="px-4 py-2">Email</th>
                            <th class="px-4 py-2">Membership Type</th>
                            <th class="px-4 py-2">Payment Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="member in filteredMembers" :key="member.name" class="border-b hover:bg-gray-50">
                            <td class="px-4 py-2">
                                <input type="checkbox" :value="member" v-model="selectedMembers" />
                            </td>
                            <td class="px-4 py-2">{{ member.membership_id }}</td>
                            <td class="px-4 py-2 text-blue-700">{{ member.full_name }}</td>
                            <td class="px-4 py-2">{{ member.phone }}</td>
                            <td class="px-4 py-2">{{ member.email }}</td>
                            <td class="px-4 py-2">{{ member.membership_type }}</td>
                            <td class="px-4 py-2">
                                <span :class="`status-${member.status?.toLowerCase()}`">
                                    {{ member.payment_status }}
                                </span>
                            </td>
                        </tr>
                        <tr v-if="filteredMembers.length === 0">
                            <td colspan="8" class="text-center py-4">No Member found</td>
                        </tr>
                    </tbody>
                </table>
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
    url: "/api/method/library_management.api.members.get_members",
    auto: true,
    transform: (r) => r.message,
});

const members = computed(() => resource.data?.members || [])
const selectedMembers = ref([])

// Members FILTERS
const filteredMembers = computed(() => {
    const text = searchText.value.toLowerCase().trim()
    if (!text) return members.value

    return members.value.filter((member) => {
        return (
            member.membership_id?.toLowerCase().includes(text) ||
            member.full_name?.toLowerCase().includes(text)
        )
    })
})
// Add new member modal



const dropdownOpen = ref(false)
const toggleDropdown = () => {
    dropdownOpen.value = !dropdownOpen.value
}
document.addEventListener('click', (e) => {
    if (!e.target.closest('.relative')) dropdownOpen.value = false
})


const editMembes = () => {
    if (selectedMembers.value.length === 0) return
    alert(`Editing ${selectedMembers.value.length} Member(s)`)
}

const deleteMembers = () => {
    if (selectedMembers.value.length === 0) return
    const confirmDelete = confirm(`Are you sure you want to delete ${selectedMembers.value.length} member(s)?`)
    if (confirmDelete) {
        alert(`Deleted books (implement backend call here)`)
    }
}


const isAllSelected = computed(() =>
    filteredMembers.value.length > 0 &&
    filteredMembers.value.every((member) => selectedMembers.value.includes(member))
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