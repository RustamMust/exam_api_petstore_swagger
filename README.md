# exam_api_petstore_swagger

## Описание

Данный проект является экзаменационной работой по модулю requests.

## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/RustamMust/exam_api_petstore_swagger.git
```

2. Установите виртуальное окружение:
```
python3 -m venv venv
```

3. Установите зависимости:
```
pip install -r requirements.txt
```


## Инструкция по использованию проекта

1. Основной файл для запуска тестов
```
test_objects.py
```
2. Payloads для POST и PUT запросов
```
payloads.py
```
3. Для того, чтобы сгенерировать Allure отчет
```
pytest -s -v —-aluredir=allureresults
```
4. Для того, чтобы просмотреть Allure отчет
```
allure serve allureresults
```
