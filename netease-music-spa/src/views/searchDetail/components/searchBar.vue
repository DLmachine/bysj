<template>
  <div>
    <a-row type="flex" justify="space-around" class="search-top">
      <a-col :span="16" class="certain-category-search-wrapper">
        <a-input-search
          placeholder="音乐/歌手/专辑/歌单/MV"
          @search="getSearchResult"
          enterButton
          v-model="keywords"
        />
      </a-col>
    </a-row>
  </div>
</template>

<script>
import Bus from "@/utils/bus.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      keywords: ""
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {},

  methods: {
    getSearchResult(val) {
      this.$emit("search",val);
    }
  }
};
</script>
<style lang='scss' scoped>
.certain-category-search-wrapper {
  margin: 26px 0;
  .certain-category-search {
    border-radius: 20px;
  }
}
.certain-category-search-dropdown .ant-select-dropdown-menu-item-group-title {
  color: #666;
  font-weight: bold;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item-group {
  border-bottom: 1px solid #f6f6f6;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item {
  padding-left: 16px;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item.show-all {
  text-align: center;
  cursor: default;
}

.certain-category-search-dropdown .ant-select-dropdown-menu {
  max-height: 300px;
}

.certain-category-search-wrapper
  >>> .certain-category-search.ant-select-auto-complete
  .ant-input-affix-wrapper
  .ant-input-suffix {
  right: 12px;
}
.certain-category-search-wrapper >>> .certain-search-item-count {
  position: absolute;
  color: #999;
  right: 16px;
}
.certain-category-search-wrapper
  >>> .certain-category-search.ant-select-focused
  .certain-category-icon {
  color: #108ee9;
}
.certain-category-search-wrapper >>> .certain-category-icon {
  color: #6e6e6e;
  transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  font-size: 16px;
}
</style>