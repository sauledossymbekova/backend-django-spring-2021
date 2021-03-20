from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Task, Todo
from main.serializers import TodoSerializer, TodoListSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'create':
            return Task.objects.all()       # create only tasks
        return Todo.objects.all()           # show, update all todos with their tasks

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskSerializer
        elif self.action == 'list':
            return TodoListSerializer
        return TodoSerializer               # serializer for retrieve

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        # passed context separate, coz only tasks may be marked as completed
        serializer = TodoSerializer(self.get_queryset().filter(id=kwargs['pk']), many=True,
                                    context={"only_completed": True})
        return Response(serializer.data)


