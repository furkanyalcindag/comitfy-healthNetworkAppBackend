from rest_framework import serializers

from carService.models.Car import Car
from carService.models.Service import Service
from carService.models.Situation import Situation
from carService.models.ServiceType import ServiceType


class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = '__all__'


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceSerializer(serializers.Serializer):
    carUUID = serializers.UUIDField()
    serviceType = serializers.CharField()
    serviceKM = serializers.IntegerField()
    complaint = serializers.CharField()
    serviceSituation = serializers.CharField(read_only=True)
    responsiblePerson = serializers.CharField(allow_null=True, allow_blank=True)
    creationDate = serializers.DateTimeField(read_only=True)
    serviceman = serializers.CharField(allow_blank=False)

    def create(self, validated_data):
        try:
            service = Service()
            service.complaint = validated_data.get('complaint')
            service.car = Car.objects.get(uuid=validated_data.get('carUUID'))
            service.serviceType = ServiceType.objects.get(id=int(validated_data.get('serviceType')))
            service.responsiblePerson = validated_data.get('responsiblePerson')
            service.save()
        except:
            raise serializers.ValidationError("lütfen tekrar deneyiniz")

    def update(self, instance, validated_data):
        pass


class ServicePageSerializer(serializers.Serializer):
    data = ServiceSerializer(many=True)
    recordsTotal = serializers.IntegerField()
    recordsFiltered = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
