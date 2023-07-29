<template>
  <h1 class="mb-8 text-3xl font-bold">
    <Link class="text-indigo-400 hover:text-indigo-600" :href="$route('organization.search')">Organizations</Link>
    <span class="font-medium text-indigo-400">/</span> Create
  </h1>
  <div class="max-w-3xl overflow-hidden bg-white rounded-md shadow">
    <form @submit.prevent="store">
      <div class="flex flex-wrap p-8 -mb-8 -mr-6">
        <text-input v-model="form.name" :error="form.errors.name" class="w-full pb-8 pr-6 lg:w-1/2" label="Name" />
        <text-input v-model="form.email" :error="form.errors.email" class="w-full pb-8 pr-6 lg:w-1/2" label="Email" />
        <text-input v-model="form.phone" :error="form.errors.phone" class="w-full pb-8 pr-6 lg:w-1/2" label="Phone" />
        <text-input v-model="form.address" :error="form.errors.address" class="w-full pb-8 pr-6 lg:w-1/2" label="Address" />
        <text-input v-model="form.city" :error="form.errors.city" class="w-full pb-8 pr-6 lg:w-1/2" label="City" />
        <text-input v-model="form.region" :error="form.errors.region" class="w-full pb-8 pr-6 lg:w-1/2" label="Province/State" />
        <select-input v-model="form.country" :error="form.errors.country" class="w-full pb-8 pr-6 lg:w-1/2" label="Country">
          <option value=""></option>
          <option value="CA">Canada</option>
          <option value="US">United States</option>
        </select-input>
        <text-input v-model ="form.postal_code" :error="form.errors.postal_code" class="w-full pb-8 pr-6 lg:w-1/2" label="Postal code" />
      </div>
      <div class="flex items-center justify-end px-8 py-4 border-t border-gray-100 bg-gray-50">
        <loading-button :loading="form.processing" class="btn-indigo" type="submit">Create Organization</loading-button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Link, useForm } from '@inertiajs/vue3'
import Layout from '@/common/Layout.vue'
import TextInput from '@/common/TextInput.vue'
import SelectInput from '@/common/SelectInput.vue'
import LoadingButton from '@/common/LoadingButton.vue'

export default defineComponent({
  metaInfo: { title: 'Create Organization' },
  components: {
    Link,
    LoadingButton,
    SelectInput,
    TextInput,
  },
  layout: Layout,
  data() {
    return {
      form: useForm({
        name: '',
        email: '',
        phone: '',
        address: '',
        city: '',
        region: '',
        country: '',
        postal_code: '',
      }),
    }
  },
  methods: {
    store() {
      this.form.post(this.$route('organization.create'))
    },
  },
})
</script>
