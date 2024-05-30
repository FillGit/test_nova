from rest_framework import status

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project_nova.app.serializers import FileSerializer

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class NovaFilesViewSet(ModelViewSet):
    def _drive_file(self, gauth, name, data):
        try:
            drive = GoogleDrive(gauth)
            my_file = drive.CreateFile(
                {'parents': [{'id': '1TEUQgKZYpNKvbXT3iTDGffg-QpElPIGL'}],
                 'title': f'{name}'})
            my_file.SetContentString(data)
            my_file.Upload()
        except Exception:
            raise ValueError('Got some trouble, check your code please!')

    def _gauth(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        return gauth

    @action(detail=False, url_path='file', methods=['post'])
    def file(self, request, pk=None):
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        name = request.data['name']
        data = request.data['data']

        gauth = self._gauth()
        self._drive_file(gauth, name, data)

        return Response(f'File {name} was uploaded!',
                        status=status.HTTP_201_CREATED)
