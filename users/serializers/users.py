from drf_yasg.utils import serializers

from users.models.users import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]
