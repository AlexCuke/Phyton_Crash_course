from survey import AnonymousSurvey

question ='What language did you first learn to speak?'
language_survey=AnonymousSurvey(question)

language_survey.show_question()
print('Enter q at any time to quit. \n')
while True:
    response=input('Language: ')
    if response == 'q':
        break
    language_survey.store_response(response)
    
print('\n Thank you to everyone who participated oin the survey!')
language_survey.show_results()