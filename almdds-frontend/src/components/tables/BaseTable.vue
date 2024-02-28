<template>
<div class="row my-5">
  <div class="col">
    <table class="table table-striped bg-white rounded shadow-sm table-hover">
      <thead class="thead-dark">
        <tr>
          <th scope="col" width="50">#</th>
          <th scope="col">Q (m³/s)</th>
          <th scope="col">Velocity X (m/s)</th>
          <th scope="col">Pressure (dbar)</th>
          <th scope="col">height (mca)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>1,83</td>
          <td>222</td>
          <td>1,8</td>
          <td>1,8</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>9,10</td>
          <td>223</td>
          <td>750</td>
          <td>750</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  name: "BaseTable"
}
</script>