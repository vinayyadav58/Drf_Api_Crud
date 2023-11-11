from django.shortcuts import render
from books.models import Book
from rest_framework import generics
from .serializers import BookSerializer,DocumentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshSlidingView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminReadOnly

# Create your views here.

class BookListAPI(generics.ListAPIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateAPIView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetriveAPI(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,book_id):
        try:
            book = Book.objects.get(id=book_id)

        except Book.DoesNotExist:
            return Response({"detail":"Book not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class BookDeleteAPIView(APIView):
    def delete(self,request,book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"detail":"Book Does Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        book.delete()

        return Response({"detail":"Data Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    

class BookUpdateAPIView(APIView):
    def put(self,request,book_id):
        try:
            book = Book.objects.get(id=book_id)

        except Book.DoesNotExist:
            return Response({"detail":"Book Data Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serialize = BookSerializer(book,data=request.data,partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['POST'])
@authentication_classes([SessionAuthentication,BasicAuthentication,JWTAuthentication])
@permission_classes([IsAuthenticated,IsAdminReadOnly])
def upload_document(request):
    if request.method=="POST":
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)