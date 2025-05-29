
# Configuração do backend

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
````

---

### 2. Ativar o ambiente virtual

* **Windows**:

```bash
.venv\Scripts\activate
```

* **Linux/macOS**:

```bash
source .venv/bin/activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o backend

* Navegue até a pasta `backend` (se aplicável):

```bash
cd backend
```

* Com o ambiente virtual **ativo**, execute:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## ⚠️ Observações importantes

* O comando `uvicorn app:app` pressupõe que dentro da pasta `backend` existe um arquivo `app.py` ou uma pasta `app` com `__init__.py` e um objeto `app` exposto.
* O parâmetro `--reload` é útil para desenvolvimento, pois recarrega automaticamente o servidor quando o código é alterado.
* Em produção, **não** use `--reload` e avalie se realmente precisa expor `--host 0.0.0.0`.

---