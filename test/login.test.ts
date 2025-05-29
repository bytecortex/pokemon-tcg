import { describe, it, expect, vi, beforeEach } from 'vitest'
import axios from 'axios'
import { ref } from 'vue'

// Mock da store
const userStore = {
  setUser: vi.fn(),
}

// Criando refs para simular seu componente
const email = ref('')
const password = ref('')
const loading = ref(false)

// Função handleLogin copiada do seu código, adaptada para teste:
async function handleLogin() {
  loading.value = true
  try {
    const response = await axios.post('http://localhost:8000/login', {
      email: email.value,
      password: password.value,
    })

    alert(response.data.message)
    userStore.setUser(response.data.user)

    email.value = ''
    password.value = ''
  } catch (error: any) {
    if (error.response) {
      alert(error.response.data.detail)
    } else {
      alert('An error occurred')
    }
  } finally {
    loading.value = false
  }
}

// Mock global do alert
global.alert = vi.fn()

describe('handleLogin', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    email.value = 'user@example.com'
    password.value = '123456'
    loading.value = false
  })

  it('deve fazer login com sucesso', async () => {
    vi.spyOn(axios, 'post').mockResolvedValue({
      data: {
        message: 'Login successful',
        user: { id: 1, name: 'User Test' },
      },
    })

    await handleLogin()

    expect(axios.post).toHaveBeenCalledWith('http://localhost:8000/login', {
      email: 'user@example.com',
      password: '123456',
    })

    expect(global.alert).toHaveBeenCalledWith('Login successful')
    expect(userStore.setUser).toHaveBeenCalledWith({ id: 1, name: 'User Test' })
    expect(email.value).toBe('')
    expect(password.value).toBe('')
    expect(loading.value).toBe(false)
  })

  it('deve mostrar erro quando backend retorna erro', async () => {
    vi.spyOn(axios, 'post').mockRejectedValue({
      response: {
        data: { detail: 'Invalid credentials' },
      },
    })

    await handleLogin()

    expect(global.alert).toHaveBeenCalledWith('Invalid credentials')
    expect(loading.value).toBe(false)
  })

  it('deve mostrar erro genérico quando falha sem resposta', async () => {
    vi.spyOn(axios, 'post').mockRejectedValue({})

    await handleLogin()

    expect(global.alert).toHaveBeenCalledWith('An error occurred')
    expect(loading.value).toBe(false)
  })
})
