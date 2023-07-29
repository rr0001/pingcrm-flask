<template>
  <div class="flex items-center justify-center min-h-screen p-6 bg-indigo-800">
    <div class="w-full max-w-md">
      <logo class="block w-full max-w-xs mx-auto fill-white" height="50" />
      <form class="mt-8 overflow-hidden bg-white rounded-lg shadow-xl" @submit.prevent="login">
        <div class="px-10 py-12">
          <h1 class="text-3xl font-bold text-center">Welcome Back!</h1>
          <div class="w-24 mx-auto mt-6 border-b-2" />
          <text-input id="email" v-model="form.email" :error="form.errors.email" class="mt-10" label="Email" type="email" autofocus autocapitalize="off" />
          <text-input id="password" v-model="form.password" :error="form.errors.password" class="mt-6" label="Password" type="password" />
          <label class="flex items-center mt-6 select-none" for="remember">
            <input id="remember" v-model="form.remember" class="mr-1" type="checkbox" />
            <span class="text-sm">Remember Me</span>
          </label>
        </div>
        <div class="flex items-center justify-between px-10 py-4 bg-gray-100 border-t border-gray-100">
          <a class="hover:underline" tabindex="-1" href="#reset-password">Forgot password?</a>
          <loading-button :loading="form.processing" class="btn-indigo" type="submit">Login</loading-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useForm } from '@inertiajs/vue3'
import Logo from '@/common/Logo.vue'
import TextInput from '@/common/TextInput.vue'
import LoadingButton from '@/common/LoadingButton.vue'

export default defineComponent({
  name: 'Login',
  components: {
    LoadingButton,
    Logo,
    TextInput,
  },
  data() {
    return {
      form: useForm({
        email: 'johndoe@example.com',
        password: 'secret',
        remember: false,
      })
    }
  },
  methods: {
    login() {
      const form = this.form.transform(data => ({
        ...data,
        remember: data.remember ? 'on' : ''
      }))
      form.post(this.$route('auth.login'))
    },
  }
})
</script>
