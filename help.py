# help.py

# Django Commands
django_runserver = "python manage.py runserver"

# Django Database Commands
django_makemigrations = "python manage.py makemigrations"
django_migrate = "python manage.py migrate"

# Curl Commands for Testing APIs
curl_add_money = 'curl -X POST -H "Content-Type: application/json" -d '{"amount": 1900}' http://127.0.0.1:8000/add_money/'
curl_view_transactions = 'curl -X GET http://127.0.0.1:8000/view_transactions/'
curl_break_piggy_bank = 'curl -X POST http://127.0.0.1:8000/break_piggy_bank/'

# Postman Request Examples
postman_add_money = {
    "url": f"http://127.0.0.1:8000/add_money/",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "body": {"amount": 100, "piggy_bank_id": 1}
}

postman_view_transactions = {
    "url": "http://127.0.0.1:8000/view_transactions/",
    "method": "GET"
}

postman_break_piggy_bank = {
    "url": "http://127.0.0.1:8000/break_piggy_bank/",
    "method": "POST"
}

if __name__ == "__main__":
    print("Django Commands:")
    print(django_runserver)
    print(django_makemigrations)
    print(django_migrate)

    print("\nCurl Commands:")
    print(curl_add_money)
    print(curl_view_transactions)
    print(curl_break_piggy_bank)

    print("\nPostman Request Examples:")
    print(postman_add_money)
    print(postman_view_transactions)
    print(postman_break_piggy_bank)
