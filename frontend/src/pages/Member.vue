<template>
  <ol>
    <li v-for="(item, index) of result" :id="index">
      <a :href="item.url">{{ item.name }}</a>
    </li>
  </ol>
</template>

<script setup>
import { createResource } from 'frappe-ui'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const result = ref([])

onMounted(async () => {
  const objects = {
    url: 'library_management.api.api_data.get_members',
    transform: function (data) {
      return data.map((item) => ({
        url: `${route.path}/${item.name}`,
        name: item.name,
      }))
    },
  }
  const res = createResource(objects)
  console.log(res)
  await res.fetch()
  result.value = res.data
  console.log(result.value)
})
</script>

<style scoped></style>
