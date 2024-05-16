# Recipe parser
## Requirements
- Python 3.8+
- Pip
- Docker (optional)
- Virtualenv (optional)
## Usage
You need to build docker image:
```
docker build -t recipes-parser .
```
Then you can run the command in container:
```
docker run recipes-parser
```
or run Unit tests:
```
docker run -it recipes-parser python -m unittest tests.test_recipe_normalizer
```
Alternatively you can use your local Python interpreter:
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
python -m unittest tests.test_recipe_normalizer
```