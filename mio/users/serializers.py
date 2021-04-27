from django.contrib.auth import get_user_model

from rest_auth.models import TokenModel

from rest_framework import serializers

from users.models import Profile, Stuff, Courier


class ProfileRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.DateField()
    avatar = serializers.ImageField()
    phone = serializers.CharField()
    address = serializers.CharField()
    balance = serializers.IntegerField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Profile.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            dob=validated_data.get('dob'),
            avatar=validated_data.get('avatar'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            balance=validated_data.get('balance'),
        )
        return profile


class StuffRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Stuff.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        return profile


class CourierRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    car = serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        courier = Courier.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            car=validated_data.get('car'),
        )
        return courier


class ProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class StuffLoginSerializer(ProfileLoginSerializer):
    pass


class CourierLoginSerializer(ProfileLoginSerializer):
    pass