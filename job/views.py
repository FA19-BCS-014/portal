from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from common.helper import encode_token , create_response , social_auth_token , decode_token
from rest_framework.response import Response
from common.enums import Message
from .models import *
from django.utils import timezone
from .serializer import *
from common.baselayer.baseAuth import UserAuthentication


class JobView(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = [AllowAny]
    model = Job

    def create_job(self, request):
        try:
            serialized_data = JobSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_response(False, Message.success.value, []))

            return Response(create_response(True, Message.try_with_correct_data.value, []))

        except Exception as e:
            print(e)
            return Response(create_response(True, Message.server_error.value, []))


    def get_job(self, request):
        try:
            jobs = request.user.posted_jobs.all()
            if jobs.exists():
                serialized_data = JobSerializer(jobs, many=True).data
                return Response(create_response(False, Message.success.value, serialized_data))

            return Response(create_response(True, Message.record_not_found.value, []))

        except Exception as e:
            print(e)
            return Response(create_response(True, Message.server_error.value, []))




