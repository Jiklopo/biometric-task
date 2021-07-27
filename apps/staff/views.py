from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import serializers, status

from apps.restaurants.selectors import get_restaurant
from apps.staff import JobChoices, GenderChoices
from apps.staff.models import Staff
from apps.staff.selectors import list_staff, get_staff
from apps.staff.services import create_staff, update_staff, delete_staff


class StaffListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        age = serializers.ReadOnlyField()

        class Meta:
            ref_name = 'StaffListOutputSerializer'
            model = Staff
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='List Staff',
        responses={200: OutputSerializer()}
    )
    def get(self, request: Request):
        staff = list_staff()
        serializer = self.OutputSerializer(instance=staff, many=True)
        return Response(data=serializer.data)


class StaffCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        iin = serializers.CharField(max_length=12)
        restaurant = serializers.IntegerField()
        first_name = serializers.CharField(max_length=128)
        last_name = serializers.CharField(max_length=128)
        gender = serializers.ChoiceField(choices=GenderChoices)
        job = serializers.ChoiceField(choices=JobChoices)
        email = serializers.EmailField()
        date_joined = serializers.DateField()

        class Meta:
            ref_name = 'StaffCreateInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        age = serializers.ReadOnlyField()

        class Meta:
            ref_name = 'StaffCreateOutputSerializer'
            model = Staff
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Create Staff',
        request_body=InputSerializer,
        responses={201: OutputSerializer()}
    )
    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        restaurant = get_restaurant(restaurant_id=serializer.validated_data.pop('restaurant'))
        iin = serializer.validated_data.pop('iin', None)
        staff = create_staff(iin=iin, restaurant=restaurant, **serializer.validated_data)

        response_data = self.OutputSerializer(instance=staff).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class StaffUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        restaurant = serializers.IntegerField(required=False)
        job = serializers.ChoiceField(JobChoices.choices, required=False)
        gender = serializers.ChoiceField(GenderChoices.choices, required=False)

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
        request_body=InputSerializer,
        responses={200: OutputSerializer()}
    )
    def post(self, request: Request, iin):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = get_staff(staff_iin=iin)

        data = {}
        if 'restaurant' in serializer.validated_data:
            data['restaurant'] = get_restaurant(restaurant_id=serializer.validated_data.pop('restaurant'))

        data.update(serializer.validated_data)
        staff = update_staff(staff=staff, **data)
        response_data = self.OutputSerializer(instance=staff).data
        return Response(data=response_data)


class StaffDeleteApi(APIView):
    @swagger_auto_schema(
        operation_description='Delete Staff',
        responses={204: ''}
    )
    def delete(self, request: Request, iin):
        staff = get_staff(staff_iin=iin)
        delete_staff(staff=staff)
        return Response(status=status.HTTP_204_NO_CONTENT)
