<template>
  <div class="d-flex" id="wrapper">
    <!-- <NavBar/> -->
    <SideBar/>
    <PageContent/>
  </div>
</template>
<script>
import SideBar from "@/layout/DashBoard/SideBar.vue"
// import NavBar from "@/layout/DashBoard/NavBar.vue"
import PageContent from "@/layout/DashBoard/PageContent.vue"

export default {
  name: "DashBoardView",
  components: {
    SideBar,
    PageContent,
    // NavBar,
  }
}
</script>

<style>
#wrapper {
  overflow-x: hidden;
  background-image: linear-gradient(
    to right,
    #baf3d7,
    #c2f5de,
    #cbf7e4,
    #d4f8ea,
    #ddfaef
  );
}
</style>