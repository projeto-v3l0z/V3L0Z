#!/bin/sh

certbot_dir="/etc/letsencrypt/live/v3l0z.com.br"
fullchain_file="$certbot_dir/fullchain.pem"
privkey_file="$certbot_dir/privkey.pem"

if [ ! -f "$fullchain_file" ] || [ ! -f "$privkey_file" ]; then
    echo "Certificados não encontrados. Executando Certbot para obter certificados SSL."

    apk update
    apk add --no-cache certbot certbot-nginx

    email="hesdrasviana@gmail.com"
    domains="v3l0z.com.br,www.v3l0z.com.br,zoounama.v3l0z.com.br,www.zoounama.v3l0z.com.br,campusconnect.v3l0z.com.br,www.campusconnect.v3l0z.com.br, lab.v3l0z.com.br,www.lab.v3l0z.com.br,api-verdin.v3l0z.com.br,www.api-verdin.v3l0z.com.br,suporte.v3l0z.com.br,www.suporte.v3l0z.com.br"

    certbot --nginx --non-interactive --agree-tos -m "$email" --domains "$domains"
else
    echo "Certificados já existem. Nenhuma ação necessária."
fi