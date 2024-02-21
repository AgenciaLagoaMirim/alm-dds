<template>
<div id="page-content-wrapper">
  <NavBar/>
  <BaseCard/>
  <BaseTable/>
</div>
</template>
<script>
import NavBar from "@/components/nav/NavBar.vue"
import BaseTable from "@/components/tables/BaseTable.vue"
import BaseCard from "@/components/cards/BaseCard.vue"
export default {
  name:"PageContent",
  components:{
    NavBar,
    BaseTable,
    BaseCard
  }
}
</script>
