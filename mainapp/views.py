import uuid, os, datetime, contextlib
from datetime import timezone

from django.http import FileResponse
from django.shortcuts import render
from django.conf import settings

from rest_framework import permissions, viewsets, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import pagination, filters

from .models import Book
from .serializers import BookSerializer


class PostPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

    def get_page_number(self, request, paginator):
        # return super().get_page_number(request, paginator)
        page_number = request.data.get(self.page_query_param) or 1
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number
    
    def get_page_size(self, request):
        # return super().get_page_size(request)
        if self.page_size_query_param:
            with contextlib.suppress(KeyError, ValueError):
                return pagination._positive_int(
                    request.data[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
        return self.page_size


class PostOrderingFilter(filters.OrderingFilter):
    def get_ordering(self, request, queryset, view):
        params = request.data.get(self.ordering_param)
        if params:
            ordering = self.remove_invalid_fields(queryset, params, view, request)
            if ordering:
                return ordering

        # No ordering was included, or all the ordering fields were invalid
        return self.get_default_ordering(view)
    
class BookView(viewsets.ModelViewSet):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated] #TODO IsAuthenticated
    pagination_class = PostPagination
    filter_backends = [PostOrderingFilter]
    
    def retrieve(self, request, *args, **kwargs):
        # try:
        UUID = request.data['uuid']
        # except:
        #     return Response("Error")
        
        # try:
        query = Book.objects.get(uuid=UUID)
        return Response(BookSerializer(query).data)

    def update(self, request, pk=None):
        robot_UUID=request.data['uuid']
        instance = Book.objects.get(uuid=robot_UUID)
        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)