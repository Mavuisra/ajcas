pip install -r requirements.txt, la commandes pour intaller les dépendances
vous devez vous rassurez que python est correctement installé dans votre ordinateur 

pour configuer le serveur ngnix 

sudo apt update
sudo apt install nginx

Créez une configuration pour votre site dans /etc/nginx/sites-available/ 
sudo nano /etc/nginx/sites-available/votre_site

Ajoutez la configuration suivante dans le fichier :

server {
    listen 80;
    server_name votre_domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /chemin/vers/votre/projet/staticfiles/;
    }

    location /media/ {
        alias /chemin/vers/votre/projet/media/;
    }

    # Autres configurations de sécurité et optimisations
}

Activez la configuration de votre site et redémarrez Nginx :

sudo ln -s /etc/nginx/sites-available/votre_site /etc/nginx/sites-enabled/
sudo systemctl restart nginx



Exécutez la commande suivante pour collecter tous les fichiers statiques dans le répertoire 

python manage.py collectstatic


Lancez votre application Django avec Waitress :

waitress-serve --port=8000 myproject.wsgi:application

Assurez-vous que les fichiers et répertoires ont les bonnes permissions pour que Nginx puisse y accéder :

sudo chown -R www-data:www-data /chemin/vers/votre/projet/staticfiles/
sudo chown -R www-data:www-data /chemin/vers/votre/projet/media/


