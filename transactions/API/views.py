from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .serialize import TransactionSerializer
from ..models import Transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .permissions import IsInstructor


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsInstructor]) #只有登陆了，并且是manager才可以在api里加东西
def api_transaction_list(request):
    if request.method == 'GET':
        courses = Transaction.objects.all() #models里objects = models.Manager()
        serialized_courses = TransactionSerializer(courses, many=True)
        return Response(serialized_courses.data)
    elif request.method == "POST":
        serialized_course = TransactionSerializer(data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsInstructor])
def api_transaction_detail(request, pk):
    course_found = Transaction.objects.filter(pk=pk).count() #models里objects = models.Manager()
    if not course_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    transaction = Transaction.objects.get(pk=pk) #models里objects = models.Manager()
    if request.method == 'GET':
        serialized_course = TransactionSerializer(transaction)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = TransactionSerializer(transaction, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        else:
            return Response(serialized_course.errors)
    elif request.method == 'DELETE':
        transaction.delete()
        return Response({'message': f' {transaction.transaction_type} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
@permission_classes([IsAuthenticated, IsInstructor])
class TransactionList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@permission_classes([IsAuthenticated, IsInstructor])
class NewPostReview(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Transaction.objects.filter(post_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        post = Transaction.objects.get(pk=pk)
        serializer.save(account=post)