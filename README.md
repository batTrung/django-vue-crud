# djangovue-crud

> Xây dựng Crud với Django Rest Framework và Vuejs


## Thiết đặt Django Server

``` bash
# Clone Repo về
git clone https://github.com/batTrung/django-vue-crud.git

# Đi tới thư mục dự án
cd django-vue-crud

# Cài đặt các phụ thuộc với pip
pip install requirements.txt

# Khởi tạo migrations cho CustomUser
python manage.py makemigrations accounts

# Run migrate to apply
python manage.py migrate

# Khởi tạo một vài dữ liệu để test
python manage.py init

# Xem kết quả tại localhost:8000/api/v1/
python manage.py runserver

```

Mở một termial mới cùng thư mục

## Thiết đặt Vue 

``` bash
# Cài đặt các phụ thuộc
npm install

# Xem kết quả tại localhost:8080
npm run dev

```

## DEMO

[DEMO]


[DEMO]: https://djangovue-crud.herokuapp.com/