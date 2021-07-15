from rest_framework import serializers
from .models import Task, BT,CH,CL,CE,CSE,DES,ECE,EEE,MA,ME,PH


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class BTSerializer(serializers.ModelSerializer):
    class Meta:
        model = BT
        fields = '__all__'

class CHSerializer(serializers.ModelSerializer):
    class Meta:
        model = CH
        fields = '__all__'

class CLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CL
        fields = '__all__'

class CESerializer(serializers.ModelSerializer):
    class Meta:
        model = CE
        fields = '__all__'
class CSESerializer(serializers.ModelSerializer):
    class Meta:
        model = CSE
        fields = '__all__'


class DESSerializer(serializers.ModelSerializer):
    class Meta:
        model = DES
        fields = '__all__'



class ECESerializer(serializers.ModelSerializer):
    class Meta:
        model = ECE
        fields = '__all__'


class EEESerializer(serializers.ModelSerializer):
    class Meta:
        model = EEE
        fields = '__all__'

class MASerializer(serializers.ModelSerializer):
    class Meta:
        model = MA
        fields = '__all__'


class MESerializer(serializers.ModelSerializer):
    class Meta:
        model = ME
        fields = '__all__'

class PHSerializer(serializers.ModelSerializer):
    class Meta:
        model = PH
        fields = '__all__'
