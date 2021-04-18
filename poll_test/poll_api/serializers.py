from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, FillPoll, Answer, Poll


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['order', 'title', 'type', 'poll']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['order', 'text', 'question']


class FillPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillPoll
        fields = '__all__'
