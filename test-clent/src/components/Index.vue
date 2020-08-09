<template>
<div class="">
    <h1 class="page-title">接口API测试平台</h1>
    <div class="card-list-group">
    <el-row :gutter="20">
      <el-col :span="4">
        <el-card>
        <div slot="header">项目总数</div>
        <div class="card-body">{{count.project}}</div>
      </el-card>
      </el-col>
      <el-col :span="4">
        <el-card>
          <div slot="header">API总数</div>
          <div class="card-body">{{count.api}}</div>
        </el-card>
      </el-col>
      <el-col :span="4">
        <el-card>
          <div slot="header">用例总数</div>
          <div class="card-body">{{count.case}}</div>
        </el-card>
      </el-col>
      <el-col :span="4">
        <el-card>
          <div slot="header">节省人力</div>
          <div class="card-body">{{count.api_record+count.case_record}}</div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</div>
</template>

<script type="text/ecmascript-6">
export default {
  name: "Index",
  data() {
    return {
      count: {
        project: 0,
        api: 0,
        case: 0,
        api_record: 0,
        case_record: 0
      }
    }
  },
  components: {},
  mounted(){
    this.$http.getIndexData().then(res => {
      const count = res.data.count
      this.count = count
      this.count.run = count.api_record+count.case_record
    })
  }
}
</script>

<style scoped lang='scss'>
.page-title{
  font-size: 20px;
}
.card-list-group{
  padding-top: 20px;
  text-align: center;
  .card-body{
    font-weight: 600;
    font-size: 30px;
  }
}
</style>