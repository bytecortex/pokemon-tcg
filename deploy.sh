#!/bin/bash
set -e

# Carrega variáveis do .env (se disponível)
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
else
  echo "❌ Arquivo .env não encontrado. Crie um com base em .env.example"
  exit 1
fi

# Carrega variáveis do .env.production (se disponível)
if [ -f .env.production ]; then
  export $(grep -v '^#' .env.production | xargs)
else
  echo "⚠️ Arquivo .env.production não encontrado. Continuando com as variáveis do .env"
fi

# Verifica variável SERVICE_NAME
if [ -z "$SERVICE_NAME" ]; then
  echo "❌ Variável SERVICE_NAME não definida no .env"
  exit 1
fi


# BUILD FRONT
echo "🔧 Fazendo build do front-end..."
cd "$LOCAL_FRONT_DIR" || { echo "❌ Pasta do front não encontrada"; exit 1; }

pnpm install
pnpm run build || { echo "❌ Build do front falhou"; exit 1; }

# SYNC FRONTEND
echo "🚀 Subindo front-end buildado para o servidor..."
rsync -avz -e "ssh -p $SSH_PORT" --delete "$LOCAL_FRONT_BUILD_DIR/" "$SSH_USER@[$SSH_HOST]:$REMOTE_FRONT_PATH"


# SYNC BACKEND
echo "📦 Subindo back-end (excluindo .venv e .env)..."
rsync -avz -e "ssh -p $SSH_PORT" --delete --exclude='.venv' --exclude='.env' "$LOCAL_BACK_DIR/" "$SSH_USER@[$SSH_HOST]:$REMOTE_BACK_PATH"


# SERVER DEPLOY STEP 
echo "⚙️  Instalando dependências no servidor e reiniciando serviço $SERVICE_NAME..."
ssh -t -p "$SSH_PORT" "$SSH_USER@$SSH_HOST" "
  SERVICE_NAME=$SERVICE_NAME
  cd $REMOTE_BACK_PATH &&
  python3 -m venv .venv &&
  source .venv/bin/activate &&
  pip install --upgrade pip &&
  if [ -f requirements.txt ]; then
    pip install -r requirements.txt
  else
    echo '⚠️  requirements.txt não encontrado'
  fi &&
  sudo systemctl restart \$SERVICE_NAME
"

echo "✅ Deploy finalizado com sucesso."
