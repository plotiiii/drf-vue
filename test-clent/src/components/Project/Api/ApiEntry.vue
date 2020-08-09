<template>
<div class="">
  <ApiList v-if="page==pagetype.API_LIST" :project="project" @page-changed="onPageChanged"></ApiList>
  <AddApi v-if="page==pagetype.ADD_API" :project="project" @page-changed="onPageChanged" :api="api"></AddApi>
</div>
</template>

<script type="text/ecmascript-6">
import AddApi from "./AddApi"
import ApiList from "./ApiList"
import pagetype from "./pagetype"
export default {
  name: "ApiEntry",
  props: ['project'],
  data() {
    return {
      page: pagetype.API_LIST,
      pagetype,
      api: null
    }
  },
  components: {
    AddApi,
    ApiList
  },
  methods:{
    onPageChanged(page,api){
      this.page = page
      this.api = api
    }
  }
}
</script>

<style scoped lang='scss'>
</style>