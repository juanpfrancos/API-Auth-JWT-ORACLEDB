1. Instalar Certbot:

```
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

2. Configuración de Nginx:

```
sudo mkdir -p /var/www/html/.well-known/acme-challenge
sudo chown -R www-data:www-data /var/www/html
```

```
sudo nano /etc/nginx/sites-available/default
```

   ```
   server {
       listen 80;
       server_name site.domain.com;

       location /.well-known/acme-challenge/ {
           root /var/www/html;
       }

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   Asegúrate de que esta configuración esté en `/etc/nginx/sites-available/default` y que el sitio esté habilitado.

3. Reinicia Nginx:
   ```
   sudo systemctl restart nginx
   ```
4. Genera el certificado:   
    ```
    sudo certbot --nginx -d api.juanpfrancos.eu.org 
    ```