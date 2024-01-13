from django.db import models


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255)


class Word(models.Model):
    WordID = models.AutoField(primary_key=True)
    Word = models.CharField(max_length=255)
    Transcription = models.CharField(max_length=255, blank=True, null=True)
    Translation = models.CharField(max_length=255)
    Synonyms = models.CharField(max_length=255, blank=True, null=True)
    Examples = models.CharField(max_length=255, blank=True, null=True)


class UserWord(models.Model):
    UserWordID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    WordID = models.ForeignKey(Word, on_delete=models.CASCADE)
    Status = models.CharField(max_length=50)
