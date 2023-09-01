from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Profile
from django.contrib.auth.models import User
# from .models import MyModel
from .serializers import UserSerializer,ProfileSerializer
from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import ImageModel
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'api/users'},
        {'GET':'api/projects/:id'},
        {'GET':'api/profiles'},
        {'GET':'api/posts'},
        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data)
@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ImageReceive(request):
    form = ImageModel()
    if request.method == "POST":
        form = ImageModel(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'Med_Insight/api/index.html',{'form':form})



from PIL import Image
import pytesseract

from pytesseract import Output
import numpy as np

import openai
import json


# print(text)


def initialise():
    # add your api key here
    api_key = "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"

    if api_key is not None:
        openai.api_key = api_key
    else:
        exit(0)


def update_chat(role, content, chat_history):
    chat_history.append({"role": role, "content": content})


def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response


def chat(content, chat_history):
    try:
        update_chat("user", content, chat_history)
        model_response = get_response(chat_history).choices[0].message.content.strip("\n")
        print(model_response)
        return model_response
    except openai.error.InvalidRequestError as e:
        print(f"Error with OpenAi: {e}")
    except openai.error.RateLimitError as e:
        print(f"Error with openAi: {e}")
    except Exception as e:
        print(f'Error: {e}')
    finally:
        # func = 'punctuation_len'
        # with open(f'{func}.json', mode='w') as file:
        #     json.dump(message_history, file)
        exit(0)


def generate_insight(filename):
    # filename = '/Users/sivasakthivel/Desktop/Med_Insighto/Med_Insight/users/images/MM_figure1.jpg'
    file_path = '/Users/sivasakthivel/Desktop/Med_Insighto/Med_Insight/users/images/' + filename
    print("File name :",file_path)
    message_history = [{"role": "system", "content": """You are an expert medical insight provider who provides accurate summary based on the given report,
                you will be provided with an OCR data of the report. The report should contain the following:\n
                1) Diagnosis of the patient based on the report\n
                2) Further analysis and test required based on the data, if no further test required then you can skip this\n
                3) Best Dietary practices and what food or drinks the patient should have.
                4) Give a detailed summary of each of the values in report"""}]

    img1 = np.array(Image.open(file_path))
    text = pytesseract.image_to_string(img1)
    initialise()

    return chat(text, message_history)




@api_view(['POST'])
def sendInsight(request,filename):
    pass