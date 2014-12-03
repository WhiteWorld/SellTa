server {
	listen 80;
	server_name sellta.fabuhui.info;
	access_log  /var/log/nginx/sellta.fabuhui.info.log;

	location / {
		proxy_pass http://127.0.0.1:8000;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
}