from rest_framework import serializers
from app.models import *

class CandidateSerializers(serializers.ModelSerializer):

    class Meta:
        model=candidate
        fields=['id','name','email','address']