<template>
  <div>
    <div class="row">
      <div class="col-12 mb-4">
        <div class="my-4">
          <h1 class="d-inline">Books</h1>
        </div>
        <div class="card border-light pt-3 pb-2 px-3 bg-light">
          <form class="row" action="." method="get" @submit.enter.prevent="onSubmitSearchForm">
            <div class="col-12 col-lg-6">
              <div class="form-group">
                <input type="text" name='search' placeholder="Tên sách, miêu tả..." class="form-control">
              </div>
            </div>
            <div class="col-12 col-lg-4">
              <select name="" class="custom-select">
                <option value="">Tác giả</option>
                <option value="C">C</option>
                <option value="E">E</option>
              </select>
            </div>
            <div class="col-12 col-lg-2">
              <button class="btn btn-primary btn-block" type="submit">
                <i class="fas fa-search mr-1"></i> Tìm kiếm
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <VMessage :message="message" v-show="message" />
        <div class="d-flex justify-content-between mb-4">
          <h6>Tổng số sách: <span class="font-weiht-bolder text-success">{{ booksCount }}</span></h6>
          <button class="btn btn-success" @click="showAddBookModal"><i class="fa fa-plus mr-1"></i> Thêm sách</button>
        </div>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">STT</th>
              <th scope="col" @click="orderingBook('name')">
                <i class="fas fa-sort"></i> Tên sách
              </th>
              <th scope="col" @click="orderingBook('author')">
                <i class="fas fa-sort"></i> Tác giả</th>
              <th scope="col" @click="orderingBook('created')">
                <i class="fas fa-sort"></i> Ngày tạo</th>
              <th scope="col" @click="orderingBook('price')">
                <i class="fas fa-sort"></i> Giá</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ book.name|capitalize }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.timesince }}</td>
              <td v-if="book.price">{{ book.price | intcomma }}đ</td>
              <td v-else>Free</td>
              <td v-if="currentUser.username == book.author">
                <div class="d-flex">
                  <button type="button" class="btn btn-warning btn-sm mr-2" @click="showEditModal(book.slug)">
                    <i class="far fa-edit"></i> Chỉnh sửa
                  </button>
                  <button type="button" class="btn btn-danger btn-sm mr-2" @click="showDeleteModal(book.slug)">
                    <i class="far fa-trash-alt"></i> Xóa
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-12 d-flex justify-content-center">
        <VPagination :hasNext="hasNext" :hasPrevious="hasPrevious" :currentPage="currentPage" :numPage="numPage" @switchToPage="switchToPage">
        </VPagination>
      </div>
    </div>
    <b-modal ref="addBookModal" id="book-modal" title="Add a new Book" size="lg" hide-footer>
      <b-form @submit.prevent="onSubmitAddBook" @reset="onResetAddBook" class="w-100">
        <b-form-group id="form-name-input" label="Name" label-for="id_name">
          <b-form-input id="id_name" name='name' v-model.lazy="$v.addBookForm.name.$model" @keyup="checkDuplicateName($event.target.value)" placeholder="Enter name">
          </b-form-input>
          <ul class="list-unstyled text-danger" v-show="$v.addBookForm.name.$anyDirty">
            <li v-if="!$v.addBookForm.name.required">Trường này là bắt buộc</li>
            <li v-if="nameBookExists">Tên sách đã tồn tại. Vui lòng chọn tên khác</li>
            <li v-if="!$v.addBookForm.name.maxLength">Tên sách tối đa là {{ $v.addBookForm.name.$params.maxLength.max }} ký tự</li>
          </ul>
        </b-form-group>
        <b-form-group id="form-description-input" label="Description" label-for="id_description">
          <b-form-textarea id="id_description" v-model.lazy="$v.addBookForm.description.$model" placeholder="Enter description" rows="5">
          </b-form-textarea>
          <ul class="list-unstyled text-danger" v-show="$v.addBookForm.description.$anyDirty">
            <li v-if="!$v.addBookForm.description.maxLength">Miêu tả sách tối thiểu là {{ $v.addBookForm.description.$params.maxLength.max }} ký tự</li>
            <li v-if="!$v.addBookForm.description.required">Trường này là bắt buộc</li>
          </ul>
        </b-form-group>
        <b-form-group id="form-photo-input" label="Photo" label-for="id_photo">
          <b-form-input id="id_photo" v-model.lazy="$v.addBookForm.photo.$model" placeholder="Enter photo link" rows="5">
          </b-form-input>
          <ul class="list-unstyled text-danger" v-show="$v.addBookForm.photo.$anyError">
            <li v-if="!$v.addBookForm.photo.required">Trường này là bắt buộc</li>
            <li v-if="!$v.addBookForm.photo.url">
              Photo phải là một link hợp hệ
            </li>
          </ul>
        </b-form-group>
        <b-form-group id="form-status-input" label="Status" label-for="id_status">
          <b-form-select id="id_status" v-model.lazy="$v.addBookForm.status.$model">
            <b-form-select-option value="D">Draft</b-form-select-option>
            <b-form-select-option value="P">Published</b-form-select-option>
          </b-form-select>
          <ul class="list-unstyled text-danger" v-show="$v.addBookForm.status.$anyError">
            <li v-if="!$v.addBookForm.status.required">Trường này là bắt buộc</li>
          </ul>
        </b-form-group>
        <b-button type="submit" variant="primary" class="mr-2" :disabled="$v.addBookForm.$invalid || nameBookExists">Save</b-button>
        <b-button type="reset" variant="secondary" @click="$refs.addBookModal.hide()">Cancel</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="deleteBookModal" id="delete-book-modal" title="Delete Book" centered>
      <template v-slot:default>
        Xác nhận xóa sách "{{ bookSelected.name }}"-{{ bookSelected.author }}
      </template>
      <template v-slot:modal-footer="{ ok, cancel }">
        <b-button variant="secondary" @click="cancel()">Cancel</b-button>
        <b-button variant="danger" @click="onSubmitDeleteBook()">Delete</b-button>
      </template>
    </b-modal>
    <b-modal ref="editBookModal" id="edit-book-modal" title="Update Book" size="lg" hide-footer>
      <b-form @submit.prevent="onSubmitEditBook()" class="w-100">
        <b-form-group id="form-name-input" label="Name" label-for="id_name">
          <b-form-input id="id_name" name='name' @keyup="checkDuplicateName(`${$event.target.value}/${bookSelected.slug}`)" v-model.lazy="$v.editBookForm.name.$model" placeholder="Enter name">
          </b-form-input>
          <ul class="list-unstyled text-danger" v-show="$v.editBookForm.name.$anyDirty">
            <li v-if="!$v.editBookForm.name.required">Trường này là bắt buộc</li>
            <li v-if="nameBookExists">Tên sách đã tồn tại. Vui lòng chọn tên khác</li>
            <li v-if="!$v.editBookForm.name.maxLength">Tên sách tối đa là {{ $v.editBookForm.name.$params.maxLength.max }} ký tự</li>
          </ul>
        </b-form-group>
        <b-form-group id="form-description-input" label="Description" label-for="id_description">
          <b-form-textarea id="id_description" v-model.lazy="$v.editBookForm.description.$model" placeholder="Enter description" rows="5">
          </b-form-textarea>
          <ul class="list-unstyled text-danger" v-show="$v.editBookForm.description.$anyDirty">
            <li v-if="!$v.editBookForm.description.maxLength">Miêu tả sách tối thiểu là {{ $v.editBookForm.description.$params.maxLength.max }} ký tự</li>
            <li v-if="!$v.editBookForm.description.required">Trường này là bắt buộc</li>
          </ul>
        </b-form-group>
        <b-form-group id="form-photo-input" label="Photo" label-for="id_photo">
          <b-form-input id="id_photo" v-model.lazy="$v.editBookForm.photo.$model" placeholder="Enter photo link" rows="5">
          </b-form-input>
          <ul class="list-unstyled text-danger" v-show="$v.editBookForm.photo.$anyError">
            <li v-if="!$v.editBookForm.photo.required">Trường này là bắt buộc</li>
            <li v-if="!$v.editBookForm.photo.url">
              Photo phải là một link hợp hệ
            </li>
          </ul>
        </b-form-group>
        <b-form-group id="form-status-input" label="Status" label-for="id_status">
          <b-form-select id="id_status" v-model.lazy="$v.editBookForm.status.$model">
            <b-form-select-option value="D">Draft</b-form-select-option>
            <b-form-select-option value="P">Published</b-form-select-option>
          </b-form-select>
          <ul class="list-unstyled text-danger" v-show="$v.editBookForm.status.$anyError">
            <li v-if="!$v.editBookForm.status.required">Trường này là bắt buộc</li>
          </ul>
        </b-form-group>
        <b-button type="submit" variant="primary" class="mr-2" :disabled="$v.editBookForm.$invalid || nameBookExists">Update</b-button>
        <b-button type="reset" variant="secondary" @click="$refs.editBookModal.hide()">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { required, maxLength, url } from 'vuelidate/lib/validators'
import ApiService, { BooksService } from '@/common/api.service'

import {
  FETCH_BOOKS,
  BOOK_CREATE,
  BOOK_UPDATE,
} from '@/store/actions.type'

import VPagination from '@/components/VPagination'
import VMessage from '@/components/VMessage'

export default {
  name: 'BookList',
  title: 'Books',
  data() {
    return {
      message: '',
      bookSelected: {},
      ordering: {
        name: false,
        author: false,
        created: false,
        price: false,
      },
      addBookForm: {
        name: '',
        description: '',
        photo: '',
        status: 'D',
      },
      editBookForm: {
        name: '',
        description: '',
        photo: '',
        status: 'D',
      },
      submitted: false,
      nameBookExists: false,
    }
  },
  components: {
    VPagination,
    VMessage,
  },
  validations: {
    addBookForm: {
      name: {
        required,
        maxLength: maxLength(50),
      },
      description: {
        required,
        maxLength: maxLength(1000),
      },
      photo: {
        required,
        url,
      },
      status: {
        required,
      },
    },
    editBookForm: {
      name: {
        required,
        maxLength: maxLength(50),
      },
      description: {
        required,
        maxLength: maxLength(1000),
      },
      photo: {
        required,
        url,
      },
      status: {
        required,
      },
    },
  },
  computed: {
    ...mapGetters(['books', 'currentPage', 'numPage', 'hasNext', 'hasPrevious', 'booksCount', 'isAuthenticated', 'currentUser'])
  },
  methods: {
    pushQuery(newQuery) {
      let query = { ...this.$route.query, ...newQuery }
      this.$store.dispatch(FETCH_BOOKS, query)
      this.$router.push({ query: query })
    },
    onSubmitSearchForm(event) {
      let textSearch = event.target.elements.search.value
      let queryForm = { search: textSearch }
      if (this.$route.query.search !== textSearch) {
        this.$store.dispatch(FETCH_BOOKS, queryForm)
        this.$router.replace({ query: queryForm })
      }
    },
    orderingBook(field) {
      this.ordering[field] = !this.ordering[field]
      field = this.ordering[field] ? field : `-${field}`
      if (this.$route.query.ordering !== field) {
        this.pushQuery({ ordering: field })
      }
    },
    switchToPage(page) {
      if (this.$route.query.page !== page) {
        this.pushQuery({ page: page })
      }
    },
    showAddBookModal() {
      if (this.isAuthenticated) {
        this.$refs.addBookModal.show()
      } else {
        this.$router.push({ name: 'login', query: { redirect: this.$route.path } })
      }
    },
    onSubmitAddBook() {
      const valid = !this.$v.addBookForm.$anyError && !this.nameBookExists
      if (valid) {
        this.$refs.addBookModal.hide()
        this.$store.dispatch(BOOK_CREATE, this.addBookForm)
        this.$store.dispatch(FETCH_BOOKS)
        this.onResetAddBook()
        this.message = 'Sách đã được tạo thành công'
      }
    },
    showDeleteModal(bookSlug) {
      this.bookSelected = this.books.find(book => book.slug === bookSlug)
      this.$refs.deleteBookModal.show()
    },
    onSubmitDeleteBook() {
      BooksService.destroy(this.bookSelected.slug)
      this.bookSelected = {}
      this.$store.dispatch(FETCH_BOOKS)
      this.$refs.deleteBookModal.hide()
      this.message = 'Sách đã được xóa thành công'
    },
    onResetAddBook() {
      this.addBookForm = {
        name: '',
        description: '',
        photo: '',
        status: 'D',
      }
      this.$v.$reset()
      this.nameBookExists = false
    },
    showEditModal(bookSlug) {
      this.bookSelected = this.books.find(book => book.slug === bookSlug)
      this.editBookForm = Object.assign({}, this.bookSelected)
      this.$refs.editBookModal.show()
    },
    onSubmitEditBook() {
      if (!this.$v.editBookForm.$anyError) {
        this.$refs.editBookModal.hide()
        this.$store.dispatch(BOOK_UPDATE, {
          slug: this.editBookForm.slug,
          book: this.editBookForm,
        })
        this.$store.dispatch(FETCH_BOOKS)
        this.onResetEditBook()
        this.message = 'Sách đã được cập nhật thành công'
      }
    },
    onResetEditBook() {
      this.$v.$reset()
      this.nameBookExists = false
    },
    checkDuplicateName(slug) {
      ApiService.get('book', slug)
        .then(({ data }) => {
          this.nameBookExists = data.invalid
        })
    },
  },
  mounted() {
    this.$store.dispatch(FETCH_BOOKS)
  },
}
</script>
