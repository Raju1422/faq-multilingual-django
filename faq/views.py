from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FAQSerializer
from .models import FAQ
# Create your views here.

class FAQView(APIView):
    def get(self,request):
        try:
            lang = request.query_params.get('lang','en')
            languages = ['hi', 'bn', 'te','en'] 
            if lang not in languages:
                return Response({"error": "Invalid language code",
                    "message": f"Supported languages are: {', '.join(languages)}",
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)
            faqs = FAQ.objects.all()
            serializer = FAQSerializer(faqs,many=True,context={"lang":lang})
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": "Internal server error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        
    def post(self,request):
        try :
            serializer = FAQSerializer(data=request.data)
            if serializer.is_valid():
                faq = serializer.save()
                return Response({'message': 'FAQ created successfully!','data': FAQSerializer(faq).data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Internal server error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        