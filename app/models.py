from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Question(Model):
    question_statement = StringField()
    option_a = StringField()
    option_b = StringField()
    option_c = StringField()
    option_d = StringField()
    correct_answer = StringField()
    answered_correctly = BooleanField(default=False)
    prize_money = IntegerField(default=0)  

    def json_response(self):
        return {
            'id': self.id,
            'question_statement': self.question_statement,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'prize_money': self.prize_money
        }