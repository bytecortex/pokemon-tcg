
# Configuração do backend

Peça ajuda pra mim (Ithallo) 😀

Pretendo migrar para Docker até 12/06... vai facilitar a configuração (assim espero)

1. Criar .venv
2. Ativar venv
3. Instalar requirements
4. Criar .env e túnel ssh
5. Rodar uvicorn

## Criar tunel ssh

> ssh -f -N -L 3307:localhost:3306 [server-username]@[server-ip] -p [ssh port]

---