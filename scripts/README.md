
# Configuração do backend

### 1. Navegue até a pasta `scripts`:

```bash
cd scripts
```

---

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

---

### 3. Ativar o ambiente virtual

* **Windows**:

```bash
.venv\Scripts\activate
```

* **Linux/macOS**:

```bash
source .venv/bin/activate
```

---

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Rodar o servidor 

* Com o ambiente virtual **ativo**, execute:

```bash
uvicorn main:app --reload
```

---

## ⚠️ Observações

Antes de rodar o servidor, é necessário garantir que você terá acesso ao banco de dados. Caso utilize um túnel ssh o comando abaixo pode ser útil:
> ssh -f -N -L 3307:localhost:3306 [server-username]@[server-ip] -p [ssh port]

---