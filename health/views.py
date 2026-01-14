from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo

class TodoCrudView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        print(request)
        print(request.user)
        todos = Todo.objects.all().values()

        todos2 = Todo.objects.raw(
            "SELECT * FROM health_todo"
        )

        print("Puro: ", todos2)

        for todo2 in todos2:
            print("Puro:", todo2.id, todo2.title)

        print(todos)
        print(list(todos))
        print(len(todos))
        print(list(todos)[1])
        for todo in todos:
            print("Elemento:", todo)
        # SQL Executado
        print(Todo.objects.all().query)
        if not todos:
            return Response({"message": "Sem conteúdo."}, status=204)
        return Response(list(todos), status=200)

    def post(self, request):
        title = request.data.get('title')
        completed = request.data.get('completed', False)
        # fazer as validações necessárias
        todo = Todo()
        todo.title = title
        todo.completed = completed
        todo.full_clean()
        todo.save()
        # todo = Todo.objects.create(title=title, completed=completed)
        # SQL Executado
        print(Todo.objects.filter(id=todo.id).query)

        return Response(
            {
                "id": todo.id, 
                "title": todo.title, 
                "completed": todo.completed
            }, status=201)
    
    def put(self, request):
        todo_id = request.data.get('id')
        title = request.data.get('title')
        completed = request.data.get('completed', False)

        if not todo_id:
            return Response({"message": "ID é obrigatório."}, status=400)


        print(Todo.objects.filter(id=todo_id).query)
        if Todo.objects.filter(id=todo_id).count() == 0:
            return Response({"message": "Tarefa não encontrada."}, status=404)

        todo = Todo.objects.get(id=todo_id)
        print(Todo.objects.filter(id=todo_id).query)
        todo.title = title
        todo.completed = completed
        todo.full_clean()
        todo.save()
        # SQL Executado
        print(Todo.objects.filter(id=todo.id).query)

        return Response(
            {
                "id": todo.id, 
                "title": todo.title, 
                "completed": todo.completed
            }, status=200)
    
    def patch(self, request):
        todo_id = request.data.get('id')
        title = request.data.get('title', None)
        completed = request.data.get('completed', None)

        if not todo_id:
            return Response({"message": "ID é obrigatório."}, status=400)

        print(Todo.objects.filter(id=todo_id).query)
        if Todo.objects.filter(id=todo_id).count() == 0:
            return Response({"message": "Tarefa não encontrada."}, status=404)

        todo = Todo.objects.get(id=todo_id)
        print(Todo.objects.filter(id=todo_id).query)
        if title is not None:
            todo.title = title
        if completed is not None:
            todo.completed = completed
        todo.full_clean()
        todo.save()
        # SQL Executado
        print(Todo.objects.filter(id=todo.id).query)

        return Response(
            {
                "id": todo.id, 
                "title": todo.title, 
                "completed": todo.completed
            }, status=200)
    
    def delete(self, request):
        todo_id = request.data.get('id')

        if not todo_id:
            return Response({"message": "ID é obrigatório."}, status=400)

        print(Todo.objects.filter(id=todo_id).query)
        if Todo.objects.filter(id=todo_id).count() == 0:
            return Response({"message": "Tarefa não encontrada."}, status=404)

        todo = Todo.objects.get(id=todo_id)
        print(Todo.objects.filter(id=todo_id).query)
        todo.delete()
        # SQL Executado
        print(Todo.objects.filter(id=todo_id).query)

        return Response({"message": "Tarefa deletada com sucesso."}, status=200)