from rest_framework import serializers
from django import forms

from newsletter.models import Join

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['email']

    def validate_email(self, value):
        email = value
        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email already exists")
        return email
