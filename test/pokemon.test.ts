import { describe, it, expect, beforeEach } from 'vitest'

let cardsData: any[] = []

describe('API Pokemon TCG - testes da API e tempo de resposta', () => {
  // Teste simples direto na chamada da API
  it('deve retornar cartas ao buscar pela lista', async () => {
    const response = await fetch('https://api.pokemontcg.io/v2/cards?page=1&pageSize=5')
    expect(response.ok).toBe(true)
    const data = await response.json()
    expect(data).toHaveProperty('data')
    expect(Array.isArray(data.data)).toBe(true)
    expect(data.data.length).toBeGreaterThan(0)
  })

  // Teste complexo com beforeEach
  describe('testes avançados com dados carregados antes', () => {
    beforeEach(async () => {
      const response = await fetch('https://api.pokemontcg.io/v2/cards?page=1&pageSize=5')
      expect(response.ok).toBe(true)
      const json = await response.json()
      cardsData = json.data
    })

    it('deve retornar exatamente 5 cartas', () => {
      expect(cardsData.length).toBe(5)
    })

    it('cada carta deve ter id, name e tipos válidos', () => {
      for (const card of cardsData) {
        expect(card).toHaveProperty('id')
        expect(typeof card.id).toBe('string')

        expect(card).toHaveProperty('name')
        expect(typeof card.name).toBe('string')

        expect(card).toHaveProperty('types')
        expect(Array.isArray(card.types)).toBe(true)

        if (card.types.length > 0) {
          for (const type of card.types) {
            expect(typeof type).toBe('string')
            expect(type.length).toBeGreaterThan(0)
          }
        }
      }
    })

    it('deve retornar erro para endpoint inválido', async () => {
      const response = await fetch('https://api.pokemontcg.io/v2/cards-invalid')
      expect(response.ok).toBe(false)
      expect(response.status).toBe(404)
    })
  })

  // Teste de tempo de resposta da API
  it('deve responder em até 1 segundo', async () => {
    const start = performance.now()

    const response = await fetch('https://api.pokemontcg.io/v2/cards?page=1&pageSize=1')

    const end = performance.now()
    const duration = end - start

    expect(response.ok).toBe(true)
    expect(duration).toBeLessThan(1000) // 1000 ms = 1 segundo
  })
})
