from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import Question, FillPoll, Answer, Poll
from .serializers import QuestionSerializer, FillPollSerializer, AnswerSerializer, PollSerializer
from .permisisions import IsAdminOrReadOnly
from django.views import generic

# Poll


class IndexView(generic.ListView):
    model = Poll
    template_name = 'poll_api/index.html'
    context_object_name = 'polls_list'

    def get_queryset(self):
        return Poll.objects.order_by('id')


class IndexDetailView(generic.DetailView):

    model = Poll
    template_name = 'poll_api/questions.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Poll.objects.all()


# class Qview(generic.DetailView):
#     model = Question
#     template_name = 'poll_api/q.html'
#     lookup_url_kwarg = 'q_order'
#     context_object_name = 'q'
#
#     def get_queryset(self):
#         p = Poll.objects.get(pk=self.kwargs['pk'])
#         return Question.objects.filter(poll=p)[:1]

# API


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    lookup_url_kwarg = 'poll_id'
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]

    def get_queryset(self):
        p = Poll.objects.get(pk=self.kwargs['poll_id'])
        return Question.objects.filter(poll=p)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    lookup_url_kwarg = 'question_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]

    def get_queryset(self):
        p = Poll.objects.get(pk=self.kwargs['poll_id'])
        return Question.objects.filter(poll=p)


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]

    def get_queryset(self):
        q = Question.objects.get(pk=self.kwargs['question_id'])
        return Answer.objects.filter(question=q)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    lookup_url_kwarg = 'answer_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly]

    def get_queryset(self):
        q = Question.objects.get(pk=self.kwargs['question_id'])
        return Answer.objects.filter(question=q)


class FillPollList(generics.ListAPIView):
    queryset = FillPoll.objects.all()
    serializer_class = FillPollSerializer


from .forms import LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # user = autenticate
            form.save()
    context = {'form': form}
    return render(request, 'poll_api/login.html', context)


def result(request):
    f = FillPoll()
