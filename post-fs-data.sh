#!/system/bin/sh

FAKE_IMAGE_PATH="/data/local/tmp/fake_camera.jpg"
CAMERA_DEVICE="/dev/video0"

# Criar diretório se não existir
mkdir -p /data/local/tmp

# Verificar se a imagem fake existe
if [ -f "$FAKE_IMAGE_PATH" ]; then
    mount -o bind "$FAKE_IMAGE_PATH" "$CAMERA_DEVICE"
    echo "Fake camera ativada!"
else
    echo "Erro: Imagem fake não encontrada!"
fi