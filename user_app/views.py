from rest_framework.decorators import APIView
from user_app.serializers import RegistrationSerializer
from rest_framework.response import Response



class registration_view(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
            

