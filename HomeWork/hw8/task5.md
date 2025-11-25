# Запустити свою програму на ресурсі PythonAnywhere.

**Мета:** Реально розгорнути додаток на PythonAnywhere (PA), навчитися налаштовувати web app, venv, static files.

## Покрокова інструкція:

1. Зареєструйся на PythonAnywhere.
2. В розділі Consoles: git clone або scp проєкт у ~/yourusername/.
3. Створи virtualenv у PA:

```
python3.10 -m venv ~/venv/myenv
source ~/venv/myenv/bin/activate
pip install -r requirements.txt
```

4. У Dashboard → Web → Add a web app → вибери Manual configuration → Python 3.10.
5. У Web → Virtualenv path: /home/yourusername/venv/myenv.
6. Вкажи модуль WSGI — відредагуй wsgi.py шлях до твого проєкту.
7. Static files: додай /static/ -> /home/yourusername/yourproject/staticfiles.
8. У Consoles виконай: python manage.py migrate і python manage.py collectstatic.
9. Перезапусти Web app у панелі.

---

## Автозапуск після перезавантаження:

На PythonAnywhere web app запускається автоматично при першому запиті для безкоштовних акаунтів. Для постійної роботи використовуй платні функції (Always-on) або Tasks (+ scheduled tasks).

---

## Типові помилки:
    - ImportError — вказано невірний virtualenv.
    - DB locked — SQLite блокування, особливо при concurrent access; для production краще Postgres.

---