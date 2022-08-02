from unicodedata import name
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from hello.models import novel
from hello.serializers import novelSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def novels_list(request):
    # GET list of novels, POST a new novel, DELETE all novels
    if request.method == 'GET':
            novels = novel.objects.all()
            name = request.GET.get('name', None)
            if name is not None:
                
                novels = novels.filter(name__icontains=name)
            
            novels_serializer = novelSerializer(novels, many=True)
            return JsonResponse(novels_serializer.data, safe=False)
    elif request.method == 'POST':
            novels_data = JSONParser().parse(request)
            #novels_data : JSON.stringify(request)
            novel_serializer = novelSerializer(data=novels_data)
            if novel_serializer.is_valid():
                novel_serializer.save()
                return JsonResponse(novel_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(novel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = novel.objects.all().delete()
        return JsonResponse({'message': '{} novels were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def novel_detail(request, pk):
    # find novel by pk (id)
    try: 
        novel = novel.objects.get(pk=pk)
        if request.method == 'GET': 
            novel_serializer = novelSerializer(novel) 
            return JsonResponse(novel_serializer.data)
        elif request.method == 'PUT': 
            novel_data = JSONParser().parse(request) 
            novel_serializer = novelSerializer(novel, data=novel_data) 
            if novel_serializer.is_valid(): 
                novel_serializer.save() 
                return JsonResponse(novel_serializer.data) 
            return JsonResponse(novel_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            novel.delete() 
            return JsonResponse({'message': 'novel was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    except novel.DoesNotExist: 
        return JsonResponse({'message': 'The novel does not exist'}, status=status.HTTP_404_NOT_FOUND) 