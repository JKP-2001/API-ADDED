from rest_framework import serializers
from .models import Task, BT, CH, CL, CE, CSE, DES, ECE, EEE, MA, ME, PH, CODINGCLUB, SWC, AEROCLUB, ASTROCLUB, CACLUB, \
    EECLUB, PRAKRITICLUB, FNCCLUB, ROBOTICSCLUB, EDCLUB, UGCLUB


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


class SWCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWC
        fields = '__all__'



class CODINGCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CODINGCLUB
        fields = '__all__'


class AEROCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = AEROCLUB
        fields = '__all__'

class ASTROCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASTROCLUB
        fields = '__all__'


class CACLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CACLUB
        fields = '__all__'

class EECLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = EECLUB
        fields = '__all__'


class PRAKRITICLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRAKRITICLUB
        fields = '__all__'

class FNCCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = FNCCLUB
        fields = '__all__'


class ROBOTICSCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROBOTICSCLUB
        fields = '__all__'

class EDCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDCLUB
        fields = '__all__'

class UGCLUBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UGCLUB
        fields = '__all__'
