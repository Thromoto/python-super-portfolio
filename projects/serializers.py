from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution
    )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificate = CertificateSerializer()

    class Meta:
        model = CertifyingInstitution
        fields = ["name", "url", "certificates"]

    def create(self, validated_data):
        current_user = self.context['request'].user

        certificate = validated_data.pop('certificates')
        certificate['certifying_institution'] = current_user
        certificate['profiles'] = Certificate.objects.create(**validated_data)
        CertifyingInstitutionSerializer().create(validated_data=certificate)
        return certificate['profiles']
