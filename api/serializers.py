
from website.models import CustomUser,Batch

from rest_framework import serializers



class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields=('batch_id')


class ListUserSerializer(serializers.ModelSerializer):
      batch=serializers.SerializerMethodField()
     
      class Meta:
        model= CustomUser
        fields=("username","batch","role",)
      def get_batch(self,custom_user):
          if(custom_user.batch!=None):
            return custom_user.batch.batch_code