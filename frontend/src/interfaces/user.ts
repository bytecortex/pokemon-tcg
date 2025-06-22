export interface User {
  id: number
  name: string
  email: string
  role: string
}

export interface UserWithOrders {
  id: number
  name: string
  email: string
  created_at: string
  total_orders: number
}