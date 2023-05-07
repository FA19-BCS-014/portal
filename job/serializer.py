
from rest_framework.serializers import ModelSerializer , SerializerMethodField
from .models import *

from rest_framework import serializers
from common.enums import Message


class JobSerializer (ModelSerializer):
    class Meta : 
        model = Job
        fields = "__all__"


