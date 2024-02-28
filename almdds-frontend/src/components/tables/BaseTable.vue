<template>
  <div class="m-2">
    <table class="table table-striped bg-white rounded shadow-sm table-hover">
      <thead class="thead-dark">
        <tr>
          <th scope="col" width="50">#</th>
          <th scope="col">Data</th>
          <th scope="col">Vazão (m³/s)</th>
          <th scope="col">Velocity X (m/s)</th>
          <th scope="col">Level (m)</th>
          <th scope="col">Average Velocity (m/s)</th>
          <th scope="col">Area (m²)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in tableData" :key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ item.data }}</td>
          <td>{{ item.vazao }}</td>
          <td>{{ item.velocityx }}</td>
          <td>{{ item.level }}</td>
          <td>{{ item.mean_q_over_a }}</td>
          <td>{{ item.mean_area }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "BaseTable",
  props: {
    tableData: {
      type: Array,
      required: true
    }
  }
}
</script>
