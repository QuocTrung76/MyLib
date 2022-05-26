from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Book


class ProductSerializer(serializers.ModelSerializer):
    my_url = serializers.SerializerMethodField(read_only=True)
    my_genre = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'author',
            'summary',
            'isbn',
            'genre',
        ]
    
    def get_my_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request) 
    
    def get_my_genre(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.display_genre()