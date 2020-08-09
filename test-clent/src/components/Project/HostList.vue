<template>
<div class="">
  <div class="top-group">
    <el-button type="primary" icon="el-icon-plus" @click="hostDialogVisible=true">新增Host</el-button>
  </div>

  <el-table
    :data="project.host_list"
    style="width: 100%">
    <el-table-column
      prop="name"
      label="名称">
    </el-table-column>
    <el-table-column
      prop="host"
      label="Host">
    </el-table-column>
    <el-table-column
      prop="description"
      label="描述">
    </el-table-column>
    <el-table-column
      label="操作" 
      width=300>
      <template slot-scope="scope">
        <el-button size="mini">编辑</el-button>
        <el-button type="danger" size="mini" @click="onDeleteHost(scope.row,scope.$index)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>

  <el-dialog title="新增Host" :visible.sync="hostDialogVisible">
    <el-form ref="hostForm" :model="hostForm" label-width="80px" :rules="hostRules">
      <el-form-item label="名称" prop="name">
        <el-input v-model="hostForm.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="host" prop="host">
         <el-input v-model="hostForm.host" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="描述" prop="description">
        <el-input type="textarea" v-model="hostForm.description" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="hostDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="onSubmitAddHost">确 定</el-button>
    </div>
  </el-dialog>
</div>
</template>

<script type="text/ecmascript-6">
export default {
  name: "HostList",
  props: ['project'],
  data() {
    return {
      hostDialogVisible: false,
      hostForm: {
        name: "",
        host: "",
        description: ""
      },
      hostRules: {
        name: [{required: true,trigger: "blur",message:"请输入host名称！"}],
        host:[{required: true,trigger: "blur",message:"请输入host！"}]
      }
    }
  },
  components: {},
  methods: {
    onSubmitAddHost(){
      this.$refs['hostForm'].validate(valid => {
        if(!valid){
          return
        }
        const params = JSON.parse(JSON.stringify(this.hostForm))
        params.project_id = this.project.id
        this.$loading.show()
        this.$http.addHost(params).then(res => {
          const host = res.data
          this.hostDialogVisible = false
          this.hostForm = {
            name: "",
            host: "",
            description: ""
          }
          this.project.host_list.push(host)
          this.$loading.hide()
          this.$message.success()
        })
      })
    },
    onDeleteHost(host,index){
      this.$messagebox.confirm({
        message: "您确定要删除这个Host吗？",
        confirmCallback: ()=> {
          this.$loading.show()
          this.$http.deleteHost(host.id).then(res => {
            this.project.host_list.splice(index,1)
            this.$loading.hide()
            this.$message.success()
          })
        }
      })
    }
  }
}
</script>

<style scoped lang='scss'>
.top-group{
  padding: 10px 0;
}
</style>