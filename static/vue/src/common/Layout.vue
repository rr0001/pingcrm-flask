<template>
  <div>
    <div id="dropdown"></div>
    <div class="md:flex md:flex-col">
      <div class="md:h-screen md:flex md:flex-col">
        <div class="md:flex md:shrink-0">
          <div class="flex items-center justify-between px-6 py-4 bg-indigo-900 md:shrink-0 md:w-56 md:justify-center">
            <Link class="mt-1" href="/">
              <logo class="fill-white" width="120" height="28" />
            </Link>
            <dropdown class="md:hidden" placement="bottom-end">
              <svg class="w-6 h-6 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" /></svg>
              <template #dropdown>
                <div class="px-8 py-4 mt-2 bg-indigo-800 rounded shadow-lg">
                  <main-menu />
                </div>
              </template>
            </dropdown>
          </div>
          <div class="flex items-center justify-between w-full p-4 text-sm bg-white border-b md:py-0 md:px-12 md:text-md">
            <div class="mt-1 mr-4">{{ $page.props.auth.user.account.name }}</div>
            <dropdown class="mt-1" placement="bottom-end">
              <div class="flex items-center cursor-pointer select-none group">
                <div class="mr-1 text-gray-700 group-hover:text-indigo-600 focus:text-indigo-600 whitespace-nowrap">
                  <span>{{ $page.props.auth.user.first_name }}</span>
                  <span class="hidden md:inline">{{ $page.props.auth.user.last_name }}</span>
                </div>
                <icon class="w-5 h-5 group-hover:fill-indigo-600 fill-gray-700 focus:fill-indigo-600" name="cheveron-down" />
              </div>
              <template #dropdown>
                <div class="py-2 mt-2 text-sm bg-white rounded shadow-xl">
                  <Link class="block px-6 py-2 hover:bg-indigo-500 hover:text-white" :href="$route('users.edit', $page.props.auth.user.id)">
                    My Profile
                  </Link>
                  <Link class="block px-6 py-2 hover:bg-indigo-500 hover:text-white" :href="$route('users.search')">
                    Manage Users
                  </Link>
                  <Link
                    class="block w-full px-6 py-2 text-left hover:bg-indigo-500 hover:text-white"
                    @click="logout"
                  >
                    Logout
                  </Link>
                </div>
              </template>
            </dropdown>
          </div>
        </div>
        <div class="md:flex md:grow md:overflow-hidden">
          <main-menu class="hidden w-56 p-12 overflow-y-auto bg-indigo-800 shrink-0 md:block" />
          <div class="px-4 py-8 md:flex-1 md:p-12 md:overflow-y-auto" scroll-region>
            <flash-messages />
            <slot />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Link } from '@inertiajs/vue3'
import Icon from '@/common/Icon.vue'
import Logo from '@/common/Logo.vue'
import Dropdown from '@/common/Dropdown.vue'
import MainMenu from '@/common/MainMenu.vue'
import FlashMessages from '@/common/FlashMessages.vue'

export default defineComponent({
  name: 'Layout',
  components: {
    Link,
    Dropdown,
    FlashMessages,
    Icon,
    Logo,
    MainMenu,
  },
  methods: {
    logout() {
      const route = this.$route('auth.logout')
      this.$inertia.post(route)
    }
  }
})
</script>
