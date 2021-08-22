from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import traceback

from .models import User, Session

# Create your views here.


@csrf_exempt
def signup(request):
    try:
        if request.method != 'POST':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)

        signup_form = json.loads(request.body)

        # check for empty values
        if (not signup_form['email']) or (not signup_form['username']) or (not signup_form['password']):
            return JsonResponse({
                'message': 'Please enter valid details!'
            }, status=401)

        # check to find if user already exists
        user = User.objects.filter(email=signup_form['email'])
        if user.count() > 0:
            return JsonResponse({
                'message': 'User already exists! Please try to sign in'
            }, status=401)

        # create new user
        User.objects.create(
            name=signup_form['username'],
            email=signup_form['email'],
            password=signup_form['password']
        )

        return JsonResponse({
            'message': 'Signed Up successfully! Please try to sign in.'
        }, status=201)
    except Exception as e:

        return JsonResponse({
            'message': str(e)
        }, status=500)


@csrf_exempt
def login(request):
    try:
        if request.method != 'POST':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)

        login_form = json.loads(request.body)
        user = User.objects.filter(email=login_form['email'])

        # check if user exists
        if user.count() == 0:
            return JsonResponse({
                'message': f'User with {login_form["email"]} does not exists! Please Sign Up and try again.'
            },status=401)

        # check if password matches with user found
        if user.values()[0]['password'] != login_form['password']:
            return JsonResponse({
                'message': 'Invalid username or password! Please try again'
            }, status=401)

        # check for existing session
        prev_session_exists = True
        session = None
        prev_session = Session.objects.filter(user__email=login_form['email'], is_logged_in=True)
        if prev_session.count() == 0:
            prev_session_exists = False
            session = Session.objects.create(
                user=user[0]
            )
        session_final = prev_session.values()[0]['session_id'] if prev_session_exists else session.session_id
        # print(session_final, type(session_final))
        # print(dir(session_final))
        return JsonResponse({
            'message': 'Logged in successfully!',
            'session_id': str(session_final)
        })
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)


@csrf_exempt
def logout(request, session_id):
    try:
        if request.method != 'PATCH':
            return JsonResponse({
                'message': 'This method is not allowed'
            }, status=405)

        # check if session exists
        session = Session.objects.filter(session_id=session_id)
        if session.count() == 0:
            return JsonResponse({
                'message': 'Invalid session ID!'
            }, status=401)

        # update session to logout user
        session.update(is_logged_in=False)

        return JsonResponse({
            'message': 'Logged out successfully!'
        }, status=200)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            'message': str(e)
        }, status=500)


