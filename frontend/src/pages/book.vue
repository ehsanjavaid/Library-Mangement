<template>
  <ol>
    <li v-for="(item, index) of book" :id="index">
      <a :href="item.url">{{ item.name }}</a>
    </li>
  </ol>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { createResource } from 'frappe-ui'

const book = ref([])
const route = useRoute()

onMounted(async () => {
  const objects = {
    url: 'library_management.api.api_data.get_books',
    transform: function (data) {
      return data.map((item) => ({
        url: `${route.path}/${item.name}`,
        name: item.name,
      }))
    },
  }
  const res = createResource(objects)
  await res.fetch()
  book.value = res.data
  console.log(book.value)
})
</script>
<style scoped></style>
