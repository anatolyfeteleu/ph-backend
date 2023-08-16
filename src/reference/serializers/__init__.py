from src.reference.serializers.base import CityBaseSerializer, WorkDayBaseSerializer, ServiceBaseSerializer


class CitySerializer(CityBaseSerializer):

    name: str


class WorkDaySerializer(WorkDayBaseSerializer):

    name: str
    short_name: str


class ServiceSerializer(ServiceBaseSerializer):

    name: str
