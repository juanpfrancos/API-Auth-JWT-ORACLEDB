
Inicia sesión en Cloudflare y selecciona tu dominio juanpfrancos.eu.org.
Ve a la sección DNS y asegúrate de que el registro A para api esté configurado correctamente:
Tipo: A
Nombre: myapp
Contenido: La dirección IP pública .
Proxy status: Desactivado (nube gris) inicialmente para evitar problemas de proxy.

```
sudo nano /etc/nginx/sites-available/default
```

```
server {
    listen 80;
    server_name myapp.juanpfrancos.eu.org;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}    
```


```
sudo systemctl restart nginx
```


# Permitir tráfico HTTP (puerto 80)
```
sudo ufw allow 80
```

# Permitir tráfico HTTPS (puerto 443)
```
sudo ufw allow 443
```

# Permitir tráfico en un rango de puertos (por ejemplo, del 8000 al 8080)
```
sudo ufw allow 8000:8080/tcp
```

# Activar UFW (si no está activado)
```
sudo ufw enable
```

# Verificar reglas configuradas
```
sudo ufw status
```