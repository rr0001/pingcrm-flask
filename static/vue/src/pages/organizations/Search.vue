<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">Organizations</h1>
    <div class="flex items-center justify-between mb-6">
      <search-filter v-model="form.search" class="w-full max-w-md mr-4" @reset="reset" @updateSearch="updateSearch">
        <label class="block text-gray-700">Trashed:</label>
        <select v-model="form.trashed" class="w-full mt-1 form-select">
          <option :value="null" />
          <option value="with">With Trashed</option>
          <option value="only">Only Trashed</option>
        </select>
      </search-filter>
      <Link class="btn-indigo" :href="$route('organization.create')">
        <span>Create</span>
        <span class="hidden md:inline">&nbsp;Organization</span>
      </Link>
    </div>
    <div class="overflow-x-auto bg-white rounded-md shadow">
      <table class="w-full whitespace-nowrap">
        <thead>
          <tr class="font-bold text-left">
            <th class="px-6 pt-6 pb-4">Name</th>
            <th class="px-6 pt-6 pb-4">City</th>
            <th class="px-6 pt-6 pb-4" colspan="2">Phone</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="organization in organizations.data" :key="organization.id" class="hover:bg-gray-100 focus-within:bg-gray-100">
            <td class="border-t">
              <Link class="flex items-center px-6 py-4 focus:text-indigo-500" :href="$route('organization.edit', organization.id)">
                {{ organization.name }}
                <icon v-if="organization.deleted_at" name="trash" class="shrink-0 w-3 h-3 ml-2 fill-gray-400" />
              </Link>
            </td>
            <td class="border-t">
              <Link class="flex items-center px-6 py-4" :href="$route('organization.edit', organization.id)" tabindex="-1">
                {{ organization.city }}
              </Link>
            </td>
            <td class="border-t">
              <Link class="flex items-center px-6 py-4" :href="$route('organization.edit', organization.id)" tabindex="-1">
                {{ organization.phone }}
              </Link>
            </td>
            <td class="w-px border-t">
              <Link class="flex items-center px-4" :href="$route('organization.edit', organization.id)" tabindex="-1">
                <icon name="cheveron-right" class="block w-6 h-6 fill-gray-400" />
              </Link>
            </td>
          </tr>
          <tr v-if="organizations.data.length === 0">
            <td class="px-6 py-4 border-t" colspan="4">No organizations found.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <pagination class="mt-6" :links="organizations.links" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Link as LinkModel, Organization, SearchFilters } from '@/models'
import { Link } from '@inertiajs/vue3'
import Icon from '@/common/Icon.vue'
import Layout from '@/common/Layout.vue'
import Pagination from '@/common/Pagination.vue'
import SearchFilter from '@/common/SearchFilter.vue'

type OrganizationSearch = {
  data: Organization[],
  links: LinkModel[],
}

export default defineComponent({
  metaInfo: { title: 'Organizations' },
  components: {
    Link,
    Icon,
    Pagination,
    SearchFilter,
  },
  layout: Layout,
  props: {
    organizations: {
      type: Object as PropType<OrganizationSearch>,
      required: true
    },
    filters: {
      type: Object as PropType<SearchFilters>,
      required: true
    }
  },
  data() {
    return {
      form: {
        search: this.filters.search,
        trashed: this.filters.trashed,
      },
    }
  },
  watch: {
    form: {
      handler(form) {
        let url = this.$route('organization.search')
        let params = []
        if (form.search) {
          params.push(`search=${form.search}`)
        }
        if (form.trashed) {
          params.push(`trashed=${form.trashed}`)
        }

        if (params) {
          url = `${url}?${params.join('&')}`
        }

        this.$inertia.get(url)
      },
      deep: true,
    },
  },
  methods: {
    reset() {
      this.form.search = ''
      this.form.trashed = ''
    },
    updateSearch(value: string) {
      this.form.search = value
    }
  },
})
</script>
