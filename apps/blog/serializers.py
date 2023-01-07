from rest_framework import serializers
from blog.models import Blog, Tag
from file.serializers import FileUrlSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('created_datetime', 'modified_datetime')


class BlogListSerializer(serializers.ModelSerializer):
    previous_blog_id = serializers.SerializerMethodField(read_only=True)
    next_blog_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        exclude = ('modified_datetime', 'title', 'content')

    def to_representation(self, instance: Blog):
        self.fields['tag'] = TagSerializer(many=True)
        self.fields['image'] = FileUrlSerializer()
        return super(BlogListSerializer, self).to_representation(instance)

    def get_previous_blog_id(self, instance: Blog):
        previous_blog = Blog.objects.filter(id__lt=instance.id).values('id').order_by('-id').first()
        if previous_blog:
            return previous_blog['id']

    def get_next_blog_id(self, instance: Blog):
        next_blog = Blog.objects.filter(id__gt=instance.id).values('id').order_by('id').first()
        if next_blog:
            return next_blog['id']
