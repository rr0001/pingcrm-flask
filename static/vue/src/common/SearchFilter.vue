<template>
  <div class="flex items-center">
    <div class="flex w-full bg-white rounded shadow">
      <dropdown :auto-close="false" class="px-4 border-r rounded-l md:px-6 hover:bg-gray-100 focus:border-white focus:ring focus:z-10" placement="bottom-start">
        <div class="flex items-baseline">
          <span class="hidden text-gray-700 md:inline">Filter</span>
          <svg class="w-2 h-2 fill-gray-700 md:ml-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 961.243 599.998">
            <path d="M239.998 239.999L0 0h961.243L721.246 240c-131.999 132-240.28 240-240.624 239.999-.345-.001-108.625-108.001-240.624-240z" />
          </svg>
        </div>
        <template #dropdown>
          <div class="w-screen px-4 py-6 mt-2 bg-white rounded shadow-xl" :style="{ maxWidth: `${maxWidth}px` }">
            <slot />
          </div>
        </template>
      </dropdown>
      <input class="relative w-full px-6 py-3 rounded-r focus:ring" autocomplete="off" type="text" name="search" placeholder="Search…" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" />
    </div>
    <button class="ml-3 text-sm text-gray-500 hover:text-gray-700 focus:text-indigo-500" type="button" @click="$emit('reset')">Reset</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import Dropdown from '@/common/Dropdown.vue'

export default defineComponent({
  name: 'SearchFilter',
  components: {
    Dropdown,
  },
  props: {
    modelValue: {
      type: String as PropType<string>,
      required: true
    },
    maxWidth: {
      type: Number as PropType<number>,
      default: 300,
    },
  },
  emits: ['update:modelValue', 'reset'],
})
</script>
