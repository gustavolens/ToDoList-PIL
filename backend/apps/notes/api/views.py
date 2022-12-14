# Rest imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializer imports
from apps.notes.api.serializer import (
    NoteSerializer,
    UserNoteSerializer,
)

# Model import
from apps.notes.models import Note

# View
@api_view(['GET'])
def all_notes_api_view(request):
    """
    Listar todas las notas de todos los usuarios.
    """

    try:
        notes = Note.objects.all()
        assert len(notes) > 0 # Genera excepción
        notes_serializer = NoteSerializer(notes, many=True)

        return Response(data=notes_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(
            {'message': 'No se encontraron notas'},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'POST'])
def note_user_view(request, fk):
    """
    Listar de nota de usuario.
    """
    
    # List
    if request.method == 'GET':
        try:
            notes = Note.objects.all().values('id', 'name', 'completed').filter(id_user=fk)
            assert len(notes) > 0
            
            notes_serializer = UserNoteSerializer(notes, many=True)
            return Response(notes_serializer.data)
        except:
            return Response(
                {'message': 'No se encontraron notas. Verificar estado de usuario'},
                status=status.HTTP_400_BAD_REQUEST
            ) 

    
    elif request.method == 'POST':
        note_serializer = NoteSerializer(data=request.data)

        # Validación
        if note_serializer.is_valid():

            note_serializer.save()
            return Response(data=note_serializer.data, status=status.HTTP_201_CREATED)

        return Response(note_serializer.errors)   


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail_view(request, pk):
    """
    Listar, actualizar y eliminar nota.
    """
    try:
        note = Note.objects.get(id=pk)
    except:
        return Response(
            {'message': 'Nota no encontrada'},
            status=status.HTTP_400_BAD_REQUEST
        ) 
    # List
    if request.method == 'GET':
        note_serializer = NoteSerializer(note)

        return Response(note_serializer.data)

    # Update
    elif request.method == 'PUT':
        note_serializer = NoteSerializer(note, data=request.data)

        if note_serializer.is_valid():
            note_serializer.save()

            return Response(data=note_serializer.data)

        return Response(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    elif request.method == 'DELETE':
        note.delete()

        return Response(
            {'message': 'Nota eliminada correctamente'},
            status=status.HTTP_200_OK
        )
