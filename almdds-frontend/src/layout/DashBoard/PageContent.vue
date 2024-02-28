<template>
<div id="page-content-wrapper">
  <NavBar/>
  <BaseTable :tableData="apiData"/>
</div>
</template>
<script>
import NavBar from "@/components/nav/NavBar.vue"
import BaseTable from "@/components/tables/BaseTable.vue"
import DataService from "@/services/DataServices"
export default {
  name:"PageContent",
  components:{
    NavBar,
    BaseTable,
  },
  data() {
    return {
      apiData: []
    }
  },
  created() {
    DataService.getData()
    .then(response => {
      this.apiData = response.data
    })
    .catch(error => {
      console.error("Erro ao buscar dados da API:", error)
    })
  }
}
</script>
