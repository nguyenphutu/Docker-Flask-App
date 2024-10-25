# SETUP
Pull source:
```bash
git clone https://github.com/nguyenphutu/Docker-Flask-App.git
```
## 1: Chạy docker compose
```bash
docker compose up 
```
Sau đó hệ thống sẽ tạo các container web, db, jenkins, ngrok
## 2: Cấu hình jenkins
Truy cập: http://ip-sever:8080/ để thực hiện cấu hình jenkins

2.1 Unlocking Jenkins
Trong container thực hiện lấy admin pass để gắn vào:
```bash
docker exec -it (jenkins or container_id) bash

cat /var/lib/jenkins/secrets/initialAdminPassword
```
2.2 Add ssh vào docker hosh
- Tạo ssh public key: đường dẫn mặc định để lưu khóa ~/.ssh/id_rsa
```bash
ssh-keygen -t rsa
```
Copy nội dung khóa công khai từ file ~/.ssh/id_rsa.pub:
```bash
cat ~/.ssh/id_rsa.pub
```
Đăng nhập vào server docker host - :
```
ssh user@remote_server_ip
```
Tạo hoặc thêm khóa công khai vào file ~/.ssh/authorized_keys trên server đích:
```
echo "nội_dung_khóa_công_khai" >> ~/.ssh/authorized_keys
```
Kiểm tra kết nối ssh từ container Jenkins
```
ssh user@remote_server_ip(172.17.0.1)
```

2.3 Setup Manage Jenkins / Credentials / SSH
- Install Plugin: SSH Agent Plugin
- Thêm Credentials: Dashboard/ Manage Jenkins/ Credentials/ System/ Global credentials (unrestricted).
Chọn New credentials -> Chọn SSH username with private key
Nhập thông tin và copy Private key từ container Jenkins vào.
```
cat ~/.ssh/id_rsa
```

## 2: Cấu hình github webhook
- Tại repo quản lý source trên github chọn Setting -> webhook
- Nhập địa chỉ public của Jenkins vào: Lấy địa chỉ public từ container ngrok
```
docker exec -it ngrok-container-id bash
```
Sau khi cấu hình xong, các thay đổi từ source code sẽ được Jenkin nhận và rebuild lại web.