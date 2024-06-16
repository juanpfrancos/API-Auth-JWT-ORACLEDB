4. **Instala Docker en la instancia**
   - Ejecuta los siguientes comandos para instalar Docker en la instancia:
     ```
     sudo apt-get update
     sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
     sudo apt-get update
     sudo apt-get install -y docker-ce
     sudo systemctl start docker
     ```

5. **Clona tu proyecto en la instancia**
   - Una vez conectado a la instancia, crea un directorio para tu proyecto:
     ```
     mkdir ~/mi-proyecto
     cd ~/mi-proyecto
     ```
   - Clona tu repositorio de Git en este directorio:
     ```
     git clone https://github.com/tu-usuario/tu-repositorio.git .
     ```

6. **Construye y ejecuta la imagen Docker**
   - En el directorio `~/mi-proyecto`, construye la imagen Docker:
     ```
     docker build -t tu-imagen-fastapi .
     ```
   - Ejecuta el contenedor Docker:
     ```
     docker run --env-file .env -p 8000:8000 tu-imagen-fastapi
     ```

6. **Instala Nginx como proxy inverso**:
   - Instala Nginx ejecutando:
     ```
     sudo apt-get update
     sudo apt-get install -y nginx
     ```

7. **Configura Nginx como proxy inverso**:
   - Abre el archivo de configuración de Nginx:
     ```
     sudo nano /etc/nginx/sites-available/default
     ```
   - Agrega la siguiente configuración dentro del bloque `server`:
     ```
     location / {
         proxy_pass http://localhost:8000;
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection 'upgrade';
         proxy_set_header Host $host;
         proxy_cache_bypass $http_upgrade;
     }
     ```
   - Guarda y cierra el archivo.
   - Reinicia Nginx:
     ```
     sudo systemctl restart nginx
     ```
