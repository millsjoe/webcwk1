from decimal import Decimal, ROUND_HALF_UP

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


@method_decorator(csrf_exempt, name='dispatch')
class GiveRating(APIView):
    permissions_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        lecturerCode = request.data['lecturer']
        module = request.data['code']
        rating = request.data['rating']
        year = request.data['year']
        semester = request.data['semester']

        moduleObj = ModuleInfo.objects.get(code=module, year=year, semester=semester)
        lecturerObj = LecturerInfo.objects.get(code=lecturerCode)

        created = Rating.objects.create(lecturer=lecturerObj, rating=rating, module=moduleObj)

        if created:
            return Response(status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class ListRatings(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]


@method_decorator(csrf_exempt, name='dispatch')
class LecturerModuleRating(APIView):

    def get(self, request):
        lecturerCode = request.data['lecturer']
        moduleCode = request.data['module']

        moduleInfo = ModuleInfo.objects.filter(code=moduleCode).values('code', 'title').get()
        lecturerInfo = LecturerInfo.objects.filter(code=lecturerCode).values().get()
        ratings = Rating.objects.filter(lecturer__code=lecturerCode, module__code=moduleCode).values('lecturer',
                                                                                                     'rating')
        total = 0
        numOfRatings = 0
        for rating in ratings:
            currentRating = rating['rating']
            total += currentRating
            numOfRatings += 1

        averageRating = Decimal(total / numOfRatings).to_integral_value(rounding=ROUND_HALF_UP)

        return JsonResponse({'average': averageRating, 'lecturer': lecturerInfo, 'module': moduleInfo}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AverageAllRatings(APIView):
    def get(self, request):
        lecturers = LecturerInfo.objects.values('code').values()
        toReturn = {}
        for lecturer in lecturers:

            average = 0
            thisLecturer = lecturer['code']
            lecturerRatings = Rating.objects.filter(lecturer__code=thisLecturer).values()
            total = 0
            numOfRatings = 0

            for rating in lecturerRatings:
                total += rating['rating']
                numOfRatings += 1

            if numOfRatings != 0:
                average = Decimal(total / numOfRatings).to_integral_value(rounding=ROUND_HALF_UP)

            toReturn["{}".format(lecturer['name']) + " ({}".format(lecturer['code']) + ")"] = int(average)

        return JsonResponse(toReturn, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ModuleViewAll(viewsets.ModelViewSet):
    queryset = ModuleInfo.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.AllowAny]


@method_decorator(csrf_exempt, name='dispatch')
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = LecturerInfo.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [permissions.AllowAny]
