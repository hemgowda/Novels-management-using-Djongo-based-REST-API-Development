from rest_framework import serializers 
from   hello.models import novel
 
class novelSerializer(serializers.ModelSerializer):
    class Meta:
        model = novel
        fields = (
                "id",
                  "name",
                  "cost",
                  "no_of_pages",
                  "author",
                  "publisher",
                  "published",
                  "edition",
                  )