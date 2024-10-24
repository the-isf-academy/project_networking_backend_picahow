from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

# Defining the Question model that represents a quiz question
class Question(Model):
    # The statement of the question being asked
    question_statement = StringField()
    
    # Possible answer options for the question
    option_a = StringField()
    option_b = StringField()
    option_c = StringField()
    option_d = StringField()
    
    # The correct answer to the question
    correct_answer = StringField()
    
    # Boolean field to track if the question was answered correctly
    answered_correctly = BooleanField(default=False)
    
    # Prize money awarded for answering the question correctly
    prize_money = IntegerField(default=0)
    
    # Hint that can be provided for the question
    hint = StringField(default="")  

    # Method to return a JSON response of the question details
    def json_response(self):
        return {
            'id': self.id,  # Unique identifier for the question
            'question_statement': self.question_statement,  # The text of the question
            'option_a': self.option_a,  # First answer option
            'option_b': self.option_b,  # Second answer option
            'option_c': self.option_c,  # Third answer option
            'option_d': self.option_d,  # Fourth answer option
            'prize_money': self.prize_money,  # Amount of prize money
            'hint_available': bool(self.hint)  # Indicates that a hint is available
        }