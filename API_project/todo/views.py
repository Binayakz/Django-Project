from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializers


class TodoList(APIView):

    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)

        return Response(serializer.data)


class CreateTodo(APIView):

    def post(self, request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateTodo(APIView):

    def put(self, request, pk):

        todo = Todo.objects.get(pk)

        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=todo, validated_data=serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteTodo(APIView):

    def delete(self, request):
        todo = Todo.objects.get(id=request.data["id"])
        todo.delete()

        return Response({"msg": "Successfully deleted the task"})
