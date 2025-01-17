<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">Users</h1>
    <div class="flex items-center justify-between mb-6">
      <search-filter v-model="form.search" class="w-full max-w-md mr-4" @reset="reset">
        <label class="block text-gray-700">Role:</label>
        <select v-model="form.role" class="w-full mt-1 form-select">
          <option :value="null" />
          <option value="user">User</option>
          <option value="owner">Owner</option>
        </select>
        <label class="block mt-4 text-gray-700">Trashed:</label>
        <select v-model="form.trashed" class="w-full mt-1 form-select">
          <option :value="null" />
          <option value="with">With Trashed</option>
          <option value="only">Only Trashed</option>
        </select>
      </search-filter>
      <Link class="btn-indigo" :href="$route('users.create')">
        <span>Create</span>
        <span class="hidden md:inline">&nbsp;User</span>
      </Link>
    </div>
    <div class="overflow-x-auto bg-white rounded-md shadow">
      <table class="w-full whitespace-nowrap">
        <tr class="font-bold text-left">
          <th class="px-6 pt-6 pb-4">Name</th>
          <th class="px-6 pt-6 pb-4">Email</th>
          <th class="px-6 pt-6 pb-4" colspan="2">Role</th>
        </tr>
        <tr v-for="user in users.data" :key="user.id" class="hover:bg-gray-100 focus-within:bg-gray-100">
          <td class="border-t">
            <Link class="flex items-center px-6 py-4 focus:text-indigo-500" :href="$route('users.edit', user.id)">
              <img v-if="user.photo_path" class="block w-5 h-5 mr-2 -my-2 rounded-full" :src="user.photo_path" />
              {{ user.last_name }}&nbsp;{{ user.first_name }}
              <icon v-if="user.deleted_at" name="trash" class="w-3 h-3 ml-2 shrink-0 fill-gray-400" />
            </Link>
          </td>
          <td class="border-t">
            <Link class="flex items-center px-6 py-4" :href="$route('users.edit', user.id)" tabindex="-1">
              {{ user.email }}
            </Link>
          </td>
          <td class="border-t">
            <Link class="flex items-center px-6 py-4" :href="$route('users.edit', user.id)" tabindex="-1">
              {{ user.owner ? 'Owner' : 'User' }}
            </Link>
          </td>
          <td class="w-px border-t">
            <Link class="flex items-center px-4" :href="$route('users.edit', user.id)" tabindex="-1">
              <icon name="cheveron-right" class="block w-6 h-6 fill-gray-400" />
            </Link>
          </td>
        </tr>
        <tr v-if="users.data.length === 0">
          <td class="px-6 py-4 border-t" colspan="4">No users found.</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Link } from '@inertiajs/vue3'
import { Link as LinkModel, SearchFilters, User } from '@/models'
import mapValues from 'lodash/mapValues'
import Icon from '@/common/Icon.vue'
import Layout from '@/common/Layout.vue'
import SearchFilter from '@/common/SearchFilter.vue'
import { pickBy } from 'lodash'

type UserSearch = {
  data: User[],
  links: LinkModel[],
}

export default defineComponent({
  components: {
    Icon,
    Link,
    SearchFilter,
  },
  layout: Layout,
  props: {
    filters: {
      type: Object as PropType<SearchFilters>,
      required: true
    },
    users: {
      type: Object as PropType<UserSearch>,
      required: true
    },
  },
  data() {
    return {
      form: {
        search: this.filters.search,
        role: this.filters.role,
        trashed: this.filters.trashed,
      }
    }
  },
  watch: {
    form: {
      handler() {
        const url = this.$route('users.search')

        this.$inertia.get(url, pickBy(this.form), { preserveState: true })
      },
      deep: true,
    },
  },
  methods: {
    reset() {
      this.form = mapValues(this.form, () => undefined)
    }
  },
})
</script>
