from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Question
import random

@route_get(BASE_URL + 'start_new_session')
def start_session(args):
    Question.objects.all().update(answered_correctly=False)
    return {'Welcome To Who Wants To Be a Millionaire!': 'Type /next_question after /millionaire in the URL to get started!'}

@route_get(BASE_URL + 'next_question')
def next_question(args):
    questions = Question.objects.filter(answered_correctly=False)  

    if not questions:
        return {'error': 'No questions available'}

    random_question = random.choice(questions)

    return random_question.json_response()

@route_post(BASE_URL + 'answer_question', args={'id':int, 'answer':str})
def answer_question(args):
    if not args['id'] or not args['answer']:
        return {'error': 'Missing question_id or answer'}

    try:
        question = Question.objects.get(id=args['id'])
    except Question.DoesNotExist:
        return {'error': 'Question not found'}

    if question.correct_answer == args['answer']:
        question.answered_correctly = True  
        question.save()
        return {'result': 'Correct'}
    else:
        return {'result': 'Incorrect'}