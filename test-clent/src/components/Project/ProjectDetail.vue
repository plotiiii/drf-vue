<template>
<div class="">
  <el-tabs v-model="activeName">
    <el-tab-pane label="项目介绍" name="1">
      <ProjectInfo :project="project"></ProjectInfo>
    </el-tab-pane>
    <el-tab-pane label="项目Host" name="2">
      <HostList :project="project"></HostList>
    </el-tab-pane>
    <el-tab-pane label="API接口" name="3">
      <ApiEntry :project="project"></ApiEntry>
    </el-tab-pane>
    <el-tab-pane label="测试用例" name="4">
      <CaseEntry :project="project"></CaseEntry>
    </el-tab-pane>
    <el-tab-pane label="任务列表" name="5">
      <TaskList :project="project"></TaskList>
    </el-tab-pane>
    <el-tab-pane label="运行记录" name="6">
      <RecordList :project="project"></RecordList>
    </el-tab-pane>
  </el-tabs>
</div>
</template>

<script type="text/ecmascript-6">
import ProjectInfo from "./ProjectInfo"
import HostList from "./HostList"
import ApiEntry from "./Api/ApiEntry"
import CaseEntry from "./Case/CaseEntry"
import RecordList from "./Record/RecordList"
import TaskList from "./TaskList"
export default {
  name: "ProjectDetail",
  data() {
    return {
      activeName: "1",
      project: {}
    }
  },
  components: {
    [ProjectInfo.name]: ProjectInfo,
    HostList,
    ApiEntry,
    CaseEntry,
    RecordList,
    TaskList
  },
  mounted(){
    const project_id = this.$route.params.project_id
    this.$http.getProjectDetail(project_id).then(res => {
      const project = res.data
      this.project = project
      console.log(this.project);
    })
  }
}
</script>

<style scoped lang='scss'>
</style>