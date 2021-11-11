#Paybright Assignment

>pip install selenium   
>pip install pytest
>pip install pytest-bdd
>pip install webdriver_manager

for running 
> python -m pytest

with report
> python -m pytest -junitxml=/path/for/output/report_name

removing cache 
>clear ; find .-name '__pycache__'-type d -exec rm -rf {} \ ; python -m pytest