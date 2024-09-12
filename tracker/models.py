from django.db import models
import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    
    def isNegative(self):
        return self.amount < 0
    def __str__(self):
        return f"{self.description} = {self.amount}"