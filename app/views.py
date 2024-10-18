from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Question
import random

PRIZE_MONEY = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

@route_get(BASE_URL + 'start_game')
def start_session(args):
    Question.objects.all().update(answered_correctly=False)
    return {'Welcome To Who Wants To Be a Millionaire!': 'Type /next_question after /millionaire in the URL to get started! To answer a question, type /answer after millionaire with answer as your arg to answer. To get a hint, use /get_hint with the id of the question. For questions without a hint, feel free to add your own hint to help the experience of other players with /add_hint'}

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
            'message': 'Game Over, Type /start_game after /millionaire to start a new game!'
        }

@route_post(BASE_URL + 'add_question', args={'question_statement': str,'option_a': str,'option_b': str,'option_c': str,'option_d': str,'correct_answer': str,'hint': str,})
def add_question(args):
    if not all([args['question_statement'], args['option_a'], args['option_b'], 
                args['option_c'], args['option_d'], args['correct_answer']]):
        return {'error': 'Missing required fields'}

    new_question = Question(
        question_statement=args['question_statement'],
        option_a=args['option_a'],
        option_b=args['option_b'],
        option_c=args['option_c'],
        option_d=args['option_d'],
        correct_answer=args['correct_answer'],
        hint=args['hint']
    )
    new_question.save()

    return {
        'message': 'Question added successfully',
        'question': new_question.json_response()
    }

@route_get(BASE_URL + 'get_hint', args={'id': int})
def get_hint(args):
    if not args['id']:
        return {'error': 'Missing question_id'}

    try:
        question = Question.objects.get(id=args['id'])
    except Question.DoesNotExist:
        return {'error': 'Question not found'}

    if not question.hint:
        return {
            'error': 'No hint available for this question',
            'question': question.json_response()
        }

    question_response = question.json_response()
    question_response['hint'] = question.hint
    return question_response

@route_post(BASE_URL + 'add_hint', args={'id': int, 'hint': str})
def add_hint(args):
    if not args['id'] or not args['hint']:
        return {'error': 'Missing question_id or hint'}

    try:
        question = Question.objects.get(id=args['id'])
    except Question.DoesNotExist:
        return {'error': 'Question not found'}

    question.hint = args['hint']
    question.save()

    return {'message': 'Hint added successfully'}