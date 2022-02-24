from rest_framework_simplejwt.serializers import TokenObtainSerializer, api_settings, RefreshToken
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model
from rest_framework import serializers
# from django.contrib.auth.models import User
from post.models import User as UserModel
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = get_user_model().USERNAME_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):

        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        resp = {'message': 'Login Successful!', 'data': data}
        return resp


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'password', 'email',)
        extra_kwargs = {
            'name': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #
    #     return attrs

    def create(self, validated_data):
        user = UserModel.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
