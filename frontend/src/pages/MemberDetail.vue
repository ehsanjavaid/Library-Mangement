<template>
  <div v-if="result">
    <h1>User ID: {{ $route.params.id }}</h1>
    
    <!-- Name Section -->
    <div class="form-group">
      <label for="full_name">Full Name</label>
      <input
        type="text"
        :value="result.full_name"
        name="full_name"
        id="full_name"
        readonly
      />
    </div>
    
    <!-- Membership ID Section -->
    <div class="form-group">
      <label for="membership_id">Membership ID</label>
      <input
        type="text"
        :value="result.membership_id"
        name="membership_id"
        id="membership_id"
        readonly
      />
    </div>
    
    <!-- Membership Type Section -->
    <div class="form-group">
      <label for="membership_type">Membership Type</label>
      <input
        type="text"
        :value="result.membership_type"
        name="membership_type"
        id="membership_type"
        readonly
      />
    </div>
    
    <!-- Payment Status Section -->
    <div class="form-group">
      <label for="payment_status">Payment Status</label>
      <input
        type="text"
        :value="result.payment_status"
        name="payment_status"
        id="payment_status"
        readonly
      />
    </div>
    
    <!-- Amount Paid Section -->
    <div class="form-group">
      <label for="amount">Amount Paid</label>
      <input
        type="number"
        :value="result.amount"
        name="amount"
        id="amount"
        readonly
      />
    </div>
    
    <!-- Payment Date Section -->
    <div class="form-group">
      <label for="payment_date">Payment Date</label>
      <input
        type="text"
        :value="result.payment_date"
        name="payment_date"
        id="payment_date"
        readonly
      />
    </div>
    
    <!-- Membership Expiry Section -->
    <div class="form-group">
      <label for="membership_expiry">Membership Expiry</label>
      <input
        type="text"
        :value="result.membership_expiry"
        name="membership_expiry"
        id="membership_expiry"
        readonly
      />
    </div>
  </div>

  <!-- Loading or Error State -->
  <div v-else>
    <p>Loading member details...</p>
  </div>
</template>

<script setup>
import { createResource } from 'frappe-ui'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const result = ref()

onMounted(async () => {
  try {
    const res = createResource({
      url: `library_management.api.api_data.get_member`,
      params: {
        id: route.params.id,
      },
    })
    await res.fetch()
    result.value = res.data
    console.log(result.value)
  } catch (error) {
    console.error("Error fetching member details:", error)
  }
})
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}

label {
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[readonly] {
  background-color: #f5f5f5;
}
</style>
