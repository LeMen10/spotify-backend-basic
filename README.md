# Spotify Backend Basic

## Giới thiệu
Dự án này là backend cơ bản cho Spotify, được xây dựng bằng Django và hỗ trợ WebSocket với Daphne.

## Cài đặt và chạy trên WSL
### 1. **Cài đặt môi trường**
Mở WSL và điều hướng đến thư mục chứa dự án:
```sh
cd spotify-backend-basic
```

Tạo môi trường ảo Python:
```sh
python3 -m venv my_env
```

Kích hoạt môi trường ảo:
```sh
source my_env/bin/activate
```

Cài đặt các thư viện cần thiết:
```sh
pip install -r requirements.txt
```

### 2. **Cài đặt PostgreSQL**
Cập nhật danh sách package:
```sh
sudo apt update
```

Cài đặt PostgreSQL:
```sh
sudo apt install postgresql postgresql-contrib
```

### 3. **Cấu hình cơ sở dữ liệu**
Chạy lệnh migrate:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

### 4. **Cài đặt Redis**
```sh
sudo apt install redis-server -y
```

### 5. **Chạy server**
Khi đã kích hoạt môi trường ảo và ở thư mục `djangoMNM`, chạy lệnh sau:

Thiết lập biến môi trường `PYTHONPATH` (thay đổi đường dẫn nếu cần):
```sh
cd djangoMNM
export PYTHONPATH=/mnt/f/diskD/Workspace/spotify-backend-basic:$PYTHONPATH
```

Chạy server với Daphne:
```sh
daphne djangoMNM.asgi:application --port 8000
```

## Thông tin bổ sung
- Hệ thống sử dụng **Django Channels** để hỗ trợ WebSocket.
- Redis được sử dụng làm message broker.
- PostgreSQL là cơ sở dữ liệu chính.

Chúc bạn cài đặt thành công! 🚀

