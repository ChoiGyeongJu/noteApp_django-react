from django.db import models

# Create your models here.

class Note(models.Model) :
    body    = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)      # auto_now는 업데이트 할 때마다 계속 사용?
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add 는 생성할때 한번 사용?

    def __str__(self) :
        return self.body[0:50]

        