from django.db import models


class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255)


class Words(models.Model):
    WordID = models.AutoField(primary_key=True)
    Word = models.CharField(max_length=255)
    # Transcription = models.CharField(max_length=255, blank=True, null=True)
    # Translation = models.CharField(max_length=255)
    # Synonyms = models.CharField(max_length=255, blank=True, null=True)
    # Examples = models.CharField(max_length=255, blank=True, null=True)


class UserWords(models.Model):
    UserWordID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    WordID = models.ForeignKey(Words, on_delete=models.CASCADE)
    IsLearned = models.BooleanField(default=False)

    class Meta:
        unique_together = (('UserID', 'WordID'),)
