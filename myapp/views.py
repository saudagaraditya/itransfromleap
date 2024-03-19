# views.py
from django.shortcuts import render, redirect
from .models import Question, Option, Response
from .forms import QuestionnaireForm


def intro(request):
    return render(request, 'intro.html')


def questionnaire(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        responses = []
        total_score = 0  # Initialize total score
        
        # Iterate through the submitted form data
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[-1])
                option_id = int(value)
                
                # Retrieve the option and add its marks to the total score
                option = Option.objects.get(pk=option_id)
                total_score += option.marks
                request.total_score = total_score
                
                # Create a response object
                response = Response(question_id=question_id, option_id=option_id, user=user)
                responses.append(response)
        
        # Bulk create response objects
        Response.objects.bulk_create(responses)
        
        # Redirect to scores page with total score as a query parameter
        return redirect('scores', total_score=total_score,user_name=user)
    else:
        questions = Question.objects.all()
        options = Option.objects.all()
        return render(request, 'index.html', {'questions': questions, 'options': options})
    

from django.shortcuts import render

def scores(request, total_score, user_name):
    # Handle GET requests and render the score.html template with the provided total_score and user_name
    return render(request, 'score.html', {'total_score': total_score, 'user_name': user_name})
