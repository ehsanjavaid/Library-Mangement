<template>
  <div>
    <div v-if="isLoading">Loading dashboard data...</div>
    <div v-else-if="isError">
      <p style="color: red;">Error loading dashboard data.</p>
    </div>
    <div v-else>
      <div v-if="dashboard.role === 'Librarian'">
        <h2>Librarian Dashboard</h2>

        <h3>Chart Data (Visitors and Borrowers)</h3>
        <ul>
          <li v-for="(label, i) in dashboard.chart_data.labels" :key="i">
            {{ label }}: Visitors {{ dashboard.chart_data.visitors[i] }}, Borrowers {{ dashboard.chart_data.borrowers[i] }}
          </li>
        </ul>

        <h3>Overdue Books</h3>
        <table border="1" cellpadding="5">
          <thead>
            <tr>
              <th>ID</th><th>Member</th><th>Title</th><th>Author</th><th>Overdue</th><th>Return Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in dashboard.overdue_books" :key="book.id">
              <td>{{ book.id }}</td>
              <td>{{ book.member }}</td>
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.overdue }}</td>
              <td>{{ book.return_date }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else-if="dashboard.role === 'Library Member'">
        <h2>Library Member Dashboard</h2>

        <h3>Issued Books</h3>
        <table border="1" cellpadding="5">
          <thead>
            <tr>
              <th>Name</th><th>Book</th><th>Return Date</th><th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in dashboard.issued_books" :key="book.name">
              <td>{{ book.name }}</td>
              <td>{{ book.book }}</td>
              <td>{{ book.return_date }}</td>
              <td>{{ book.status }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else>
        <p>User role is not recognized or unauthorized.</p>
      </div>
    </div>
  </div>
</template>



    <script setup>
    import { useQuery } from '@tanstack/vue-query'

    const fetchDashboardData = async () => {
    const res = await fetch('/api/method/library_management.api.Dashboard.get_dashboard_data', {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json'
        },
        credentials: 'include' 
    });

    if (!res.ok) {
        throw new Error(`Failed to fetch: ${res.status}`);
    }

    const data = await res.json();
    return data.message;
    }

    const { data: dashboard, isLoading, isError } = useQuery({
    queryKey: ['dashboardData'],
    queryFn: fetchDashboardData
    })
    </script>