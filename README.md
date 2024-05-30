# test_nova

Installation
------------


    python3.8 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

    python manage.py migrate

    python manage.py createsuperuser --username admin --email admin@example.com


Для того, чтобы поместить файл в Google Drive, нужно сделать следующее:
    
    python manage.py runserver
    
    Вызвать:
        curl  -H 'Content-Type: application/json' --data '{"name":"test_test","data":"Hello Friend!"}' http://127.0.0.1:8000/nova_files/file/

    во время выполнения API у вас попросят аккаунт. Укажите testnova201@gmail.com c паролем losos_098.
    
    В https://drive.google.com/drive/folders/1TEUQgKZYpNKvbXT3iTDGffg-QpElPIGL?hl=ru будет файл test_test.

