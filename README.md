
# 📌 Yatube API

**Yatube API** — это backend-приложение на Django и Django REST Framework, предоставляющее API-доступ к социальной платформе для публикации постов, комментариев, подписок и групп.  
Проект позволяет пользователям:

- публиковать посты;
- подписываться на других пользователей;
- комментировать запис;
- просматривать ленту подписок.

## ✅ Польза

API может быть использован для создания мобильного клиента, frontend-интерфейса или интеграции с другими сервисами.

---

## 🚀 Установка

1. **Клонируйте репозиторий и перейдите в папку проекта:**
   ```bash
   git clone https://github.com/khasanovmma/api_final_yatube
   cd api_final_yatube/
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # для Linux/Mac
   venv\Scripts\activate    # для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Перейдите в папку yatube_api:**
   ```bash
   cd yatube_api/
   ```

5. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя (по желанию):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

---

## 📡 Примеры API-запросов

### 🔐 Авторизация

Получить JWT-токен:
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

### 📄 Получить список постов

```http
GET /api/v1/posts/
Authorization: Bearer <access_token>
```

### ➕ Создать пост

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Мой первый пост!",
  "group": 1
}
```

### 💬 Добавить комментарий к посту

```http
POST /api/v1/posts/1/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Отличная статья!"
}
```

### ➕ Подписаться на пользователя

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "username"
}
```

---
