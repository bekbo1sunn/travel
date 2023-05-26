# from celery import shared_task
# from django.core.mail import send_mail


# @shared_task
# def send_activation_code(email, activation_code):
#     activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
#     message = f'Активируйте аккаунт, перейдя по ссылке\n{activation_link}'
#     send_mail('Activate account', message, 'odosumbekov@gmail.com', [email])
#     return "Отправленно"



from django.core.mail import send_mail
from decouple import config
from celery import shared_task


@shared_task
def send_activation_code(email: str, code: str):
	message = ""
	html = f"""
<h1>для активации нажмите на кнопку</h1>
<a href="{config('LINK')}api/v1/account/activate/{code}">
<button>Activate</button>
</a>
"""
	send_mail(
		subject="Активация аккаунта",
		message=message,
		from_email="a@gmail.com",
		recipient_list=[email],
		html_message=html
	)

