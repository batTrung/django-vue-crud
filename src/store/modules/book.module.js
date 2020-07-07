import { BooksService } from '@/common/api.service'
import {
  FETCH_BOOKS,
  BOOK_CREATE,
  BOOK_UPDATE,
  FETCH_BOOK,
} from '@/store/actions.type'
import {
  SET_BOOKS
} from '@/store/mutations.type'

const state = {
  books: [],
  currentPage: 1,
  numPage: null,
  hasNext: null,
  hasPrevious: null,
  booksCount: 0,
}

const getters = {
  books(state) {
    return state.books
  },
  currentPage(state) {
    return state.currentPage
  },
  numPage(state) {
    return state.numPage
  },
  hasNext(state) {
    return state.hasNext
  },
  hasPrevious(state) {
    return state.hasPrevious
  },
  booksCount(state) {
    return state.booksCount
  },
}

const mutations = {
  [SET_BOOKS](state, data) {
    state.books = data.results
    state.currentPage = data.page
    state.numPage = data.num_page
    state.hasNext = data.has_next
    state.hasPrevious = data.has_previous
    state.booksCount = data.count
  },
}

const actions = {
  [FETCH_BOOKS]({ commit }, params) {
    return BooksService.query(params)
      .then(({ data }) => {
        commit(SET_BOOKS, data)
      })
      .catch(error => {
        throw new Error(error)
      })
  },
  [FETCH_BOOK](context, slug) {
    return BooksService.get(slug)
  },
  [BOOK_CREATE](context, params) {
    return BooksService.create(params)
  },
  [BOOK_UPDATE](context, payload) {
    return BooksService.update(payload.slug, payload.book)
  },
}

export default {
  state,
  getters,
  mutations,
  actions,
}
