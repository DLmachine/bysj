<template>
  <div>
    <a-modal
      title="手机登录（网易云音乐账号）"
      centered
      v-model="modalShow"
      :footer="false"
      ：maskClosable="false"
      @cancel="onCancel"
    >
      <a-form layout="horizontal" :form="form" @submit="handleSubmit">
        <a-form-item :validate-status="phoneError() ? 'error' : ''" :help="phoneError() || ''">
          <a-input
            v-decorator="[
          'phone',
          {rules: [{ required: true,len: 11, pattern: /^1(3|4|5|6|7|8|9)\d{9}$/, message: '请输入正确的手机号!' }]}
        ]"
            placeholder="手机号"
          >
            <a-icon slot="prefix" type="phone" style="color:rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item
          :validate-status="passwordError() ? 'error' : ''"
          :help="passwordError() || ''"
        >
          <a-input
            v-decorator="[
          'password',
          {rules: [{ required: true, message: '请输入密码!' }]}
        ]"
            type="password"
            placeholder="Password"
          >
            <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-button
            type="primary"
            html-type="submit"
            :disabled="hasErrors(form.getFieldsError())"
            @click="login"
            style="width:100%"
          >登录123</a-button>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script>
function hasErrors(fieldsError) {
  return Object.keys(fieldsError).some(field => fieldsError[field]);
}
import { mapState, mapMutations, mapActions } from "vuex";
export default {
  name: "",
  props: [],
  data() {
    return {
      hasErrors,
      form: this.$form.createForm(this),
      modalShow: false
    };
  },

  components: {},

  computed: { ...mapState(["account"]) },

  watch: {},

  beforeMount() {},

  mounted() {
    this.modalShow = true;
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
  },

  methods: {
    ...mapActions(["LOGIN", "LOGIN_STATUS"]),
    // Only show error after a field is touched.
    phoneError() {
      const { getFieldError, isFieldTouched } = this.form;
      return isFieldTouched("phone") && getFieldError("phone");
    },
    // Only show error after a field is touched.
    passwordError() {
      const { getFieldError, isFieldTouched } = this.form;
      return isFieldTouched("password") && getFieldError("password");
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          this.loginShow = false;
        }
      });
    },
    async login() {
      // loginApi
      let userInfo = {
        phone: this.form
          .getFieldValue("phone")
          .toString()
          .trim(),
        password: this.form
          .getFieldValue("password")
          .toString()
          .trim()
      };
      await this.LOGIN(userInfo)
        .then(res => {
          this.$emit("confirmLogin");
          this.modalShow = false;
        })
        .catch(err => {
          console.log(err,123123)
          this.$message.error("登录失败，密码错误！");
        });
      await this.LOGIN_STATUS()
        .then()
        .catch();
    },
    onCancel() {
      this.$emit("confirmLogin");
      this.modalShow = false;
    }
  }
};
</script>
<style lang='scss' scoped>
</style>
