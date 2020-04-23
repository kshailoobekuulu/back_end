from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import Company
from .serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanySearchSerializer,
)
from .permissions import DoesNotHaveCompanyOrDeny


# Create your views here.

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    permission_classes = (permissions.IsAuthenticated, DoesNotHaveCompanyOrDeny,)
    serializer_class = CompanyCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = CompanyDetailSerializer


class UserDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        print(request)
        user_info = {
            'username': request.user.username,
            'is_company': False,
        }
        if hasattr(request.user, 'company'):
            user_info['is_company'] = True
            user_info['company_name'] = request.user.company.company_name

        return JsonResponse(user_info)


class CompanySearchView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CompanySearchSerializer

    def get_queryset(self):
        queryset_list = Company.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(company_name__contains=query)
            ).distinct()
        return queryset_list

