from rest_framework import serializers
from ..models import UserProfile, creditcard
from django.contrib.auth.models import User
from datetime import date


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    account = serializers.CharField(max_length=256)
    balance = serializers.CharField()

class UserHyperLinkedSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='transaction_vfs_detail')
    course = serializers.HyperlinkedRelatedField(read_only=True, view_name='transaction_vfs_detail')
    student = serializers.HyperlinkedRelatedField(read_only=True, view_name='transaction_vfs_detail')

    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_field = ['id']
        # extra_kwargs = {
        #     'url': {'view_name': 'student_course_detail'},
        #     'student': {'view_name': 'user_admin_user_detail'},
        #     'course': {'view_name': 'courses_vfs_detail'},
        # }

class CreditcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = creditcard
        fields = "__all__"
        read_only_field = ['id']

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def save(self):
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({'error': 'Password mismatch. Please try again'})
#
#         if User.objects.filter(email=self.validated_data['email']).exists():
#             raise serializers.ValidationError({'error': f"A user with {self.validated_data['email']} already exists"})
#
#         new_user = User(email=self.validated_data['email'], username=self.validated_data['username'])
#         new_user.set_password(password)
#         new_user.save()
#         return new_user