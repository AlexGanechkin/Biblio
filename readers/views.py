from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from readers.models import Reader
from readers.permissions import ReaderPermission
from readers.serializers import ReaderListSerializer, ReaderDetailSerializer, ReaderCreateSerializer, \
    ReaderUpdateSerializer, ReaderDestroySerializer


class ReaderListView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderListSerializer
    permission_classes = [IsAuthenticated]


class ReaderDetailView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
    permission_classes = [IsAuthenticated, ReaderPermission]


class ReaderCreateView(CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderCreateSerializer
    permission_classes = [AllowAny]


class ReaderUpdateView(UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer
    permission_classes = [IsAuthenticated, ReaderPermission]


class ReaderDeleteView(DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDestroySerializer
    permission_classes = [IsAuthenticated, ReaderPermission]


class ReaderLogout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
