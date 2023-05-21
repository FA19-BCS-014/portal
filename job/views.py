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


class JobApiView(ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = Job

    def get_job(self, request):
        try:
            if request.query_params.get("id"):
                job = self.model.objects.filter(id=request.query_params.get("id"))
                if job.exists():
                    serialized_data = JobSerializer(job.first(), many=False).data
                    serialized_data['user'] = {"username": job.first().user.email}
                    try:
                        serialized_data['image'] = request.build_absolute_uri(job.first().image.url)
                    except :
                        serialized_data['image'] = None

                    return Response(create_response(False, Message.success.value, serialized_data))
            jobs = self.model.objects.all()
            if jobs.exists():
                serialized_data = JobSerializer(jobs, many=True).data
                return Response(create_response(False, Message.success.value, serialized_data))

            return Response(create_response(True, Message.record_not_found.value, []))

        except Exception as e:
            print(e)
            return Response(create_response(True, Message.server_error.value, []))


class ApplyView(ModelViewSet):
    authentication_classes = []
    model = Application

    def application(self, request):
        try:
            serialized_data = ApplicationSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_response(False, Message.success.value, serialized_data.data))

            return Response(create_response(True, Message.try_with_correct_data.value, []))

        except Exception as e:
            print(e)
            return Response(create_response(True, Message.server_error.value, []))