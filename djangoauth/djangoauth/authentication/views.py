from django.shortcuts import render
from rest_framework import permissions, viewsets
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get_permission(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(),IsAccountOwner())

