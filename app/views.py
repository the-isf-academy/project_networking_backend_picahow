from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Question
import random

PRIZE_MONEY = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

@route_get(BASE_URL + 'start_new_session')
def start_session(args):
    Question.objects.all().update(answered_correctly=False)
    return {'Welcome To Who Wants To Be a Millionaire!': 'Type /next_question after /millionaire in the URL to get started!'}

@route_get(BASE_URL + 'next_question')
def next_question(args):
    questions = Question.objects.filter(answered_correctly=False)  

    if not questions:
        return {'message': 'Congratulations! You have won the game!', 'total_prize': '£1,000,000'}

    random_question = random.choice(questions)
    
    question_number = Question.objects.filter(answered_correctly=True).count()
    if question_number < len(PRIZE_MONEY):
        random_question.prize_money = PRIZE_MONEY[question_number]
        random_question.save()

    return random_question.json_response()

@route_post(BASE_URL + 'answer', args={'id':int, 'answer':str})
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
        
        total_prize = sum(PRIZE_MONEY[:Question.objects.filter(answered_correctly=True).count()])
        
        return {
            'result': 'Correct',
            'prize_money': f'£{question.prize_money:,}',
            'total_prize': f'£{total_prize:,}'
        }
    else:
        total_prize = sum(PRIZE_MONEY[:Question.objects.filter(answered_correctly=True).count()])
        
        return {
            'result': 'Incorrect',
            'total_prize': f'£{total_prize:,}',
            'message': 'Game Over'
        }