from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import serializers, status

from apps.staff import JobTextChoices, GenderTextChoices
from apps.staff.models import Staff
from apps.staff.selectors import list_staff
from apps.staff.services import create_staff, update_staff, delete_staff


class StaffListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        age = serializers.ReadOnlyField()

        class Meta:
            ref_name = 'StaffListOutputSerializer'
            model = Staff
            fields = '__all__'

    @swagger_auto_schema(operation_description='List Staff')
    def get(self, request: Request):
        staff = list_staff()
        serializer = self.OutputSerializer(instance=staff, many=True)
        return Response(data=serializer.data)


class StaffCreateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'StaffCreateInputSerializer'
            model = Staff
            fields = [
                'iin',
                'restaurant',
                'first_name',
                'last_name',
                'gender',
                'job',
                'email',
                'date_joined'
            ]

    class OutputSerializer(serializers.ModelSerializer):
        age = serializers.ReadOnlyField()

        class Meta:
            ref_name = 'StaffCreateOutputSerializer'
            model = Staff
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Create Staff',
        request_body=InputSerializer
    )
    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = create_staff(**serializer.validated_data)
        response_data = self.OutputSerializer(instance=staff).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class StaffUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        restaurant = serializers.IntegerField(required=False)
        job = serializers.ChoiceField(JobTextChoices.choices, required=False)
        gender = serializers.ChoiceField(GenderTextChoices.choices, required=False)

        class Meta:
            ref_name = 'StaffUpdateInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        age = serializers.ReadOnlyField()

        class Meta:
            ref_name = 'StaffUpdateOutputSerializer'
            model = Staff
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Update Staff',
        request_body=InputSerializer
    )
    def put(self, request: Request, iin):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant_id = serializer.validated_data.pop('restaurant', None)
        staff = update_staff(staff_iin=iin, restaurant_id=restaurant_id, **serializer.validated_data)
        response_data = self.OutputSerializer(instance=staff).data
        return Response(data=response_data)


class StaffDeleteApi(APIView):
    @swagger_auto_schema(operation_description='Delete Staff')
    def delete(self, request: Request, iin):
        delete_staff(staff_iin=iin)
        return Response(status=status.HTTP_204_NO_CONTENT)
