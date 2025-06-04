
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

## ⚠️ Observações importantes

* O comando `uvicorn app:app` pressupõe que dentro da pasta `scripts` existe um arquivo `app.py` ou uma pasta `app` com `__init__.py` e um objeto `app` exposto.
* O parâmetro `--reload` é útil para desenvolvimento, pois recarrega automaticamente o servidor quando o código é alterado.
* Em produção, **não** use `--reload` e avalie se realmente precisa expor `--host 0.0.0.0`.

---