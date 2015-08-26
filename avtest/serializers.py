from rest_framework import serializers
# from threat import IPDetails


class DetailsSerializer(serializers.Serializer):
    is_valid       = serializers.ReadOnlyField()
    address        = serializers.ReadOnlyField(default='ip')
    id             = serializers.ReadOnlyField(source='_id.$id', default='')
    first_activity = serializers.ReadOnlyField(default=None)
    last_activity  = serializers.ReadOnlyField(default=None)
    activities     = serializers.ReadOnlyField(default=[])
    activity_types = serializers.ReadOnlyField(default=[])
    reputation_val = serializers.ReadOnlyField(default=0)
