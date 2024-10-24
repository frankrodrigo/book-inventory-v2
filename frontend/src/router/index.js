import { createRouter, createWebHistory } from 'vue-router';
import BookIndex from '../components/BookIndex.vue';
import AddBook from '../components/AddBook.vue';
import FilterBooks from '../components/FilterBooks.vue';
import ExportBooks from '../components/ExportBooks.vue';
import EditBooks from '../components/EditBooks.vue';

const routes = [
  { path: '/', component: BookIndex },
  { path: '/add', component: AddBook },
  { path: '/filter', component: FilterBooks },
  { path: '/export', component: ExportBooks },
  {
    path: '/edit',
    name: 'EditBooks',
    component: EditBooks,
    props: (route) => ({ books: route.params.books || [] }) // Ensure books are passed from params
  },

  {
    path: '/edit-book/:id',
    name: 'EditBook',
    component: () => import('@/components/EditBook.vue'),
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
