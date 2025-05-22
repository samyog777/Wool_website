# import serializers
from rest_framework import serializers
from . import models

class ClipRuleSerializer(serializers.Serializer):
    image = serializers.ImageField()
    category = serializers.ChoiceField(choices=models.Clipath.CATEGORY_CHOICES)
    code = serializers.CharField()
    sender = serializers.EmailField(required=False, allow_blank=True)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return models.Clipath.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.code = validated_data.get('code', instance.code)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

# show all the clipath
class ClipathSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clipath
        fields = '__all__'
        read_only_fields = ['id', 'date']