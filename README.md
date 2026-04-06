# pdfkit

## 📁 PDFKit Generator: Генерация PDF документов из HTML

PDFKit Generator — это демонстрационный проект, показывающий возможности библиотеки pdfkit для генерации PDF документов из HTML, URL и Jinja2 шаблонов. Вместо сложных PDF библиотек вы получаете простой способ создавать профессиональные документы с помощью HTML/CSS.

Проект создан для наглядной демонстрации возможностей pdfkit: генерация из HTML строк, файлов, URL, использование Jinja2 шаблонов, кастомизация страниц и поддержка кириллицы.

## 💡 Моё мнение о библиотеке pdfkit

pdfkit — это обёртка над wkhtmltopdf, которая позволяет создавать PDF из HTML с помощью простого Python кода. Вместо того чтобы мучиться с низкоуровневыми PDF библиотеками, вы просто пишете HTML и CSS — и получаете готовый PDF.

Библиотека невероятно проста в использовании — достаточно вызвать `pdfkit.from_string(html, 'output.pdf')` и всё готово. Под капотом — движок wkhtmltopdf (тот же, что используется в браузере), который рендерит HTML в точности так, как вы ожидаете.

Для бизнес-отчётности, счетов, сертификатов и любой документации pdfkit — идеальное решение. Он поддерживает все CSS свойства, JavaScript, сложные таблицы, колонтитулы и автоматическую нумерацию страниц. Простота в сочетании с мощью HTML/CSS делает эту библиотеку незаменимой.

## 🚀 Быстрый старт

### Требования

- Python 3.7+
- wkhtmltopdf (движок для рендеринга PDF)

### Установка wkhtmltopdf

**Windows:**
1. Скачайте установщик с [официального сайта](https://wkhtmltopdf.org/downloads.html)
2. При установке **обязательно** поставьте галочку "Add to PATH"
3. Или установите через winget: `winget install wkhtmltopdf`

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

**macOS:**
```
brew install wkhtmltopdf
```

## Установка проекта

1. Клонируйте репозиторий:
```
git clone <your-repo-url>
cd pdfkit-project
```

2. Создайте виртуальное окружение (рекомендуется):
```
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

## 📋 Справка по командам

```
# Базовая генерация PDF
python main.py

# Простой тестовый пример
python test_pdf.py

# Создание своего PDF
python my_first_pdf.py

# Проверка установки wkhtmltopdf
wkhtmltopdf --version
```

## 📊 Примеры вывода

**Успешный запуск**

```
PDFKit PDF Generator
==================================================
✓ pdfkit is installed
✓ Using wkhtmltopdf from: C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe
✓ PDF generated successfully: output/sample_from_string.pdf
✓ PDF generated from template: output/sample_from_template.pdf
```

## 📄 Сгенерированный PDF документ

| Элемент | Описание |
|---------|----------|
| Заголовок | "PDF Generated with pdfkit" |
| Дата | Автоматическая подстановка текущей даты |
| Таблица | Данные о продуктах с итогами |
| Колонтитул | Нумерация страниц |
| Стили | Профессиональное оформление на CSS |

<img width="937" height="984" alt="Снимок экрана (1145)" src="https://github.com/user-attachments/assets/7c7d78fc-2515-4da8-a113-d089d53e8214" />
<img width="931" height="980" alt="Снимок экрана (1144)" src="https://github.com/user-attachments/assets/8c68489b-51c0-4b5c-a492-c572ea5ed7ad" />


## 🔧 Детали реализации

```
pdfkit/
├── pdf_generator.py      # Основной класс для генерации PDF
├── config.py             # Конфигурация (размер страницы, пути)
├── main.py               # Демонстрация всех возможностей
├── test_pdf.py           # Простой тест для проверки
├── requirements.txt      # Зависимости (pdfkit, jinja2)
├── templates/
│   └── example.html      # Jinja2 шаблон с примерами
├── output/               # Папка для сгенерированных PDF
│   └── .gitkeep          # Сохраняет папку в репозитории
└── README.md             # Документация
```

## 📦 Назначение файлов

| Файл | Что делает |
|------|------------|
| `pdf_generator.py` | Главный класс с методами: `generate_from_html()`, `generate_from_file()`, `generate_from_url()`, `generate_from_template()` |
| `config.py` | Настройки: размер страницы (A4), отступы, кодировка UTF-8, путь к wkhtmltopdf |
| `main.py` | Демонстрация: генерация из HTML строки и из Jinja2 шаблона |
| `test_pdf.py` | Простая проверка работоспособности установки |
| `templates/example.html` | HTML шаблон с таблицей, стилями и колонтитулами |
| `output/` | Директория для сохранения сгенерированных PDF файлов |
| `requirements.txt` | Зависимости: pdfkit, jinja2 |

## 🧠 Ключевые концепции

1. Генерация из HTML строки
```
from pdf_generator import PDFGenerator

pdf_gen = PDFGenerator()

html = """
<html>
    <body>
        <h1>Привет, мир!</h1>
        <p>Это мой первый PDF</p>
    </body>
</html>
"""

pdf_gen.generate_from_html(html, "output/hello.pdf")

```

2. Генерация из Jinja2 шаблона
```
context = {
    'title': 'Месячный отчёт',
    'date': '2024-01-15',
    'items': ['Товар 1', 'Товар 2', 'Товар 3']
}

pdf_gen.generate_from_template('report.html', context, 'report.pdf')
```

3. Генерация из URL
```
pdf_gen.generate_from_url('https://example.com', 'webpage.pdf')
```

4. Кастомизация PDF параметров
```
custom_options = {
    'page-size': 'Letter',
    'orientation': 'Landscape',
    'margin-top': '0.5in',
    'margin-bottom': '0.5in'
}

pdf_gen.generate_from_html(html, 'custom.pdf', options=custom_options)
```

5. Работа с кириллицей
```
# Убедитесь, что в HTML указана кодировка:
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Русский текст корректно отображается</h1>
</body>
</html>
"""
```

## 🎨 Настройка стилей

**В HTML можно использовать любые CSS свойства:**
```
@page {
    size: A4;
    margin: 2cm;
}

.header {
    text-align: center;
    border-bottom: 2px solid #333;
    margin-bottom: 20px;
}

.footer {
    position: fixed;
    bottom: 0;
    text-align: center;
    font-size: 12px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #007bff;
    color: white;
}
```

## 🐛 Обработка ошибок

Утилита корректно обрабатывает различные проблемные ситуации:

| Ситуация | Сообщение |
|----------|-----------|
| wkhtmltopdf не установлен | `No wkhtmltopdf executable found: "b''"` |
| Неправильный путь в config.py | `FileNotFoundError: [WinError 2]` |
| Нет прав на запись | `Permission denied` |
| Некорректный HTML | `PDF generation failed: Exit code 1` |
| Путь к wkhtmltopdf указан неверно | `[Errno 2] No such file or directory` |

## Решение типичных проблем

Проблема: No wkhtmltopdf executable found

```
# Решение: Укажите правильный путь в config.py
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

Проблема: Киррилица отображается как "????"

```
# Решение: Добавьте в HTML и config.py:
# config.py: 'encoding': 'UTF-8'
# HTML: <meta charset="UTF-8">
```

Проблема: OSError: [WinError 2]
```
# Решение: Перезагрузите терминал после установки wkhtmltopdf
# Или укажите абсолютный путь в config.py
```

## ⚙️ Конфигурация

Все настройки хранятся в config.py:
```
# Параметры PDF по умолчанию
PDFKIT_CONFIG = {
    'options': {
        'page-size': 'A4',           # Формат страницы
        'margin-top': '0.75in',      # Верхний отступ
        'margin-right': '0.75in',    # Правый отступ
        'margin-bottom': '0.75in',   # Нижний отступ
        'margin-left': '0.75in',     # Левый отступ
        'encoding': 'UTF-8',         # Кодировка
        'no-outline': None,          # Без обводки
        'enable-local-file-access': None  # Доступ к локальным файлам
    }
}

# Путь к wkhtmltopdf (раскомментируйте при необходимости)
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

## 🎯 Заключение

PDFKit Generator — это пример того, как с помощью pdfkit можно организовать профессиональную генерацию PDF документов в Python. Вместо того чтобы изучать сложные PDF библиотеки, проект использует простой и понятный HTML/CSS подход.

Этот подход:

Ускоряет разработку — пишите HTML, а не код для PDF

Даёт полный контроль — любые CSS стили и JavaScript

Поддерживает шаблоны — динамическое содержимое через Jinja2

Обеспечивает качество — рендеринг на движке браузера

Проще в отладке — можно проверить в браузере перед генерацией

