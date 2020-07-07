<template>
  <nav>
    <ul class="pagination">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: !hasPrevious }">
          <a class="page-link" @click.prevent="onClickPreviousPage" href="">Trang trước</a>
        </li>
        <li class="page-item" v-for="(page, index) in pages" :key="index" :class="{ active: page == currentPage }">
          <a class="page-link" v-if="page" @click.prevent="onClickPage(page)" href="">{{ page }}</a>
          <a class="page-link" v-else>&hellip;</a>
        </li>
        <li class="page-item" :class="{ disabled: !hasNext }">
          <a class="page-link" @click.prevent="onClickNextPage" href="">
            Trang sau
          </a>
        </li>
      </ul>
    </ul>
  </nav>
</template>
<script>
export default {
  name: 'Pagination',
  props: {
    hasPrevious: Boolean,
    hasNext: Boolean,
    currentPage: Number,
    numPage: Number,
  },
  computed: {
    pages() {
      let lastPage = this.numPage
      let delta = 2
      let left = this.currentPage - delta
      let right = this.currentPage + delta + 1
      let range = []
      let rangeWithNull = []
      let l = null

      for (let i = 1; i <= lastPage; i++) {
        let createPage = i === 1 || i === lastPage || (i >= left && i < right)
        if (createPage) {
          range.push(i)
        }
      }

      for (let i of range) {
        if (l) {
          if (i - l === 2) {
            rangeWithNull.push(l + 1)
          } else if (i - l !== 1) {
            rangeWithNull.push(null)
          }
        }
        rangeWithNull.push(i)
        l = i
      }
      return rangeWithNull
    },
  },
  methods: {
    onClickPreviousPage() {
      this.$emit('switchToPage', this.currentPage - 1)
    },
    onClickPage(page) {
      this.$emit('switchToPage', page)
    },
    onClickNextPage() {
      this.$emit('switchToPage', this.currentPage + 1)
    },
  },
}

</script>
