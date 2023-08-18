
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from readers.models import Reader
from readers.serializers import ReaderListSerializer, ReaderDetailSerializer, ReaderCreateSerializer, \
    ReaderUpdateSerializer, ReaderDestroySerializer


class ReaderListView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderListSerializer


class ReaderDetailView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer


class ReaderCreateView(CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderCreateSerializer


class ReaderUpdateView(UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer


class ReaderDeleteView(DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDestroySerializer
