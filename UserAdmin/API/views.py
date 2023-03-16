from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serialize import UserSerializer, UserHyperLinkedSerializer, CreditcardSerializer
from ..models import UserProfile, creditcard
from rest_framework import mixins
from rest_framework import generics
from transactions.API.permissions import IsInstructor
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsInstructor])
def api_user_list(request):
    if request.method == 'GET':
        courses = UserProfile.objects.all()
        serialized_courses = UserSerializer(courses, many=True)
        return Response(serialized_courses.data)
    elif request.method == "POST":
        serialized_course = UserSerializer(data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsInstructor])
# @authentication_classes([TokenAuthentication])
def api_user_detail(request, pk):
    course_found = UserProfile.objects.filter(pk=pk).count()
    if not course_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    course = UserProfile.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_course = UserSerializer(course)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = UserSerializer(course, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)
    elif request.method == 'DELETE':
        course.delete()
        return Response({'message': f' {course.account_id} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
@permission_classes([IsAuthenticated, IsInstructor])
class UserHyperLinkedList(APIView):
    def get(self, request):
        enrollments = UserProfile.objects.all()
        serialized_enrollments = UserHyperLinkedSerializer(enrollments, many=True, context={'request': request})
        return Response(serialized_enrollments.data)
@permission_classes([IsAuthenticated, IsInstructor])
class ContactUsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserHyperLinkedSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
@permission_classes([IsAuthenticated, IsInstructor])
class ContactUsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # print("Request.data = ", request.data)
        # print("Request.user = ", request.user)
        # print("self.initial = ", self.initial)

        print("args = ", args)
        print("kwargs = ", kwargs)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsInstructor])
# @authentication_classes([TokenAuthentication])
def api_creditcard_list(request):
    if request.method == 'GET':
        credit = creditcard.objects.all()
        serialized_credit = CreditcardSerializer(credit, many=True)
        return Response(serialized_credit.data)
    elif request.method == "POST":
        serialized_credit = CreditcardSerializer(data=request.data)
        if serialized_credit.is_valid():
            serialized_credit.save()
            return Response(serialized_credit.data)
        else:
            return Response(serialized_credit.errors)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsInstructor])
# @authentication_classes([TokenAuthentication])
def api_creditcard_detail(request, pk):
    course_found = creditcard.objects.filter(pk=pk).count()
    if not course_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    course = creditcard.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_course = CreditcardSerializer(course)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = CreditcardSerializer(course, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)
    elif request.method == 'DELETE':
        course.delete()
        return Response({'message': f' record {course.id} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
# @api_view(['POST', 'GET'])
# def user_registration_view(request):
#     if request.method == 'GET':
#         courses = UserRegistrationSerializer.objects.all()
#         serialized_courses = UserRegistrationSerializer(courses, many=True)
#         return Response(serialized_courses.data)
#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             new_user = serializer.save()
#
#             data['response'] = "New user registration successfully!!"
#             data['username'] = new_user.username
#             data['email'] = new_user.email
#
#             token = Token.objects.get_or_create(user=new_user)
#             data['token'] = token[0].key
#         else:
#             data = serializer.errors
#         return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)