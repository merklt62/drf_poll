from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    poll_name = models.CharField('Название опросника', max_length=200)

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    ONE = 'Radio'
    MULTIPLE = 'Checkbox'

    choices = (
        (ONE, 'Radio'),
        (MULTIPLE, 'Checkbox'),
    )

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField('Текст вопроса', max_length=200)
    type = models.CharField('Тип вопроса', max_length=20, choices=choices,
                            default=ONE)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('Текст ответа', max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class FillPoll(models.Model):
    user = models.ForeignKey(User, related_name='user_answer',
                             on_delete=models.CASCADE)
    answer_choice = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_choice
