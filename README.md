# exam_api_petstore_swagger

## Description

This project is an examination work for the module requests.

## Installation

1. Clone the repository:
```
git clone https://github.com/RustamMust/exam_api_petstore_swagger.git
```

2. Install the virtual environment:
```
python3 -m venv venv
```

3. Establish dependencies:
```
pip install -r requirements.txt
```


## How to use the project

1. Main file for running tests:
```
test_objects.py
```
2. Payloads for POST and PUT requests:
```
payloads.py
```
3. Generate an Allure report:
```
pytest -s -v —-aluredir=allureresults
```
4. View the Allure report:
```
allure serve allureresults
```
