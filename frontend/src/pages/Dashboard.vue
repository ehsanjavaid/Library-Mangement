<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <Header />
    <h1 class="text-2xl font-bold mb-4">Welcome Admin</h1>
    <div v-if="resource.loading" class="text-gray-500">Loading...</div>
    <div v-else class="grid gap-6 grid-cols-[repeat(auto-fit,minmax(250px,1fr))]">
      <div class="bg-[#FEF8E8] text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2"> Total Books</h2>
        <p class="text-3xl font-bold">{{ resource.data.total_books }}</p>
      </div>
      <div class="bg-[#EEEEFE] text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <Users class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Total Members</h2>
        <p class="text-3xl font-bold">{{ resource.data.members }}</p>
      </div>
      <div class="bg-[#E7F9F9] text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Book Issued</h2>
        <p class="text-3xl font-bold">{{ resource.data.book_issue }}</p>
      </div>
      <div class="bg-[#FFF1F6] text-center p-6 rounded-xl shadow">
        <div class="flex justify-center mb-2">
          <BookOpen class="w-10 h-10" />
        </div>
        <h2 class="text-lg font-semibold mb-2">Available Books</h2>
        <p class="text-3xl font-bold">{{ resource.data.available_books }}</p>
      </div>
    </div>
    <!-- chart -->
    <div class="flex flex-row w-100%">
      <div class="bg-white p-6 rounded-xl shadow mt-8 w-[50%] mr-4">
        <h2 class="text-lg font-bold mb-4">Books Allocation by Locations</h2>
        <v-chart v-if="pieChartOptions && pieChartOptions.series" class="chart" :option="pieChartOptions" autoresize />
      </div>
      <!-- Books Availability -->
      <div class="bg-white p-6 rounded-xl shadow mt-8 w-[50%] mr-4">
        <h2 class="text-lg font-bold mb-4">Books by Status</h2>
        <v-chart class="chart" v-if="booksAvailabilityOptions && booksAvailabilityOptions.series"
          :option="booksAvailabilityOptions" autoresize />
        <pre v-else>Loading or no data...</pre>
      </div>
    </div>
  </div>
</template>
<style scoped>
.chart {
  width: 100%;
  height: 300px;
  min-height: 300px;
  display: block;
}
</style>

<script setup>
import { createResource } from 'frappe-ui'
import { BookOpen, Users } from 'lucide-vue-next'
import Header from '@/components/Layout/Header.vue'
import { computed } from 'vue'
import VChart from 'vue-echarts'
import * as echarts from 'echarts/core'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import { watchEffect } from 'vue'
//  Dashboard Stats Resource
const resource = createResource({
  url: '/api/method/library_management.api.dashboard.get_dashboard_data',
  auto: true,
  transform: (response) => response.message
})

echarts.use([
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  CanvasRenderer
])
const locationChart = createResource({
  url: '/api/method/library_management.api.dashboard.get_books_by_location',
  auto: true,
  transform: (response) => response.message
})


const pieChartOptions = computed(() => {
  const data = (locationChart.data || []).map(item => ({
    name: item.name,
    value: item.count
  }))

  if (!data.length) return {}

  return {
    color: ['#5470C6', '#91CC75', '#FAC858', '#EE6666', '#73C0DE', '#3BA272'],
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [
      {
        name: 'Books by Location',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        renderMode: 'canvas',
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 16,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data
      }
    ]
  }
})
// Books Availability
const booksAvailability = createResource({
  url: '/api/method/library_management.api.dashboard.get_books_availability',
  auto: true,
  transform: (response) => response.message
})

const booksAvailabilityOptions = computed(() => {
  const data = (booksAvailability.data || []).map(item => ({
    name: item.name,
    value: item.count
  }))
  if (!data.length) return {}

  return {
    color: ['#91CC75', '#5470C6', '#FAC858'],
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)' // 👈 shows value + percent
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [
      {
        name: 'Book Status',
        type: 'pie',
        radius: ['40%', '70%'], // Donut shape
        avoidLabelOverlap: false,
        label: {
          show: true,
          formatter: '{b}: {d}%', // 👈 inside chart: name + percent
          position: 'outside'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 15,
            fontWeight: 'bold'
          }
        },
        labelLayout: {
          hideOverlap: true
        },
        labelLine: {
          show: true,
          length: 5,
          length2:5,
        },
        data // ✅ converted values
      }
    ]
  }
})
</script>
