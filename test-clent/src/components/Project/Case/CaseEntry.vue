<template>
<div class="">
  <CaseList v-if="page==pagetype.CASE_LIST" :project="project" @page-changed="onPageChanged"></CaseList>
  <AddCase v-if="page==pagetype.ADD_CASE" :project="project" :caseobj="caseobj" @page-changed="onPageChanged"></AddCase>
</div>
</template>

<script type="text/ecmascript-6">
import AddCase from "./AddCase"
import CaseList from "./CaseList"
import pagetype from "./pagetype"
export default {
  name: "CaseEntry",
  props: ['project'],
  data() {
    return {
      page: pagetype.CASE_LIST,
      pagetype,
      caseobj: null
    }
  },
  components: {
    AddCase,
    CaseList
  },
  methods: {
    onPageChanged(page,caseobj){
      this.page = page
      this.caseobj = caseobj
    }
  }
}
</script>

<style scoped lang='scss'>
</style>
