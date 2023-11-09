from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from data_forgery.scripts import data_forgery_script
from PIL import Image
import os

class DataForgeryView(APIView):
    def get(self, request):
        if request.method == 'GET':
            try:
                originalImage = request.data['original_image']
                editedImage = request.data['edited_image']

                filepath = os.path.join(os.getcwd(), 'media')

                with Image.open(originalImage) as img:
                    img.save(f"{filepath}/originalImage.png")

                with Image.open(editedImage) as img:
                    img.save(f"{filepath}/editedImage.png")

                print(f"{filepath}/originalImage.png")

                detectedChanges = data_forgery_script.detect_tampered_regions(
                    original_img=f"{filepath}/originalImage.png",
                    edited_img=f"{filepath}/editedImage.png",
                    save_directory=filepath+'/',
                )

                print('Detected Changes: ',detectedChanges)

                if detectedChanges:
                    response = {
                        "status": status.HTTP_200_OK,
                        "message": 'http://localhost:8000/media/tampered_regions.jpg',
                    }

                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "response not found!",
                    }

                    return Response(response, status=status.HTTP_404_NOT_FOUND)
                
            except Exception as e:
                print("Exception: ", e)
                response = {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": str(e),
                }

                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            response = {
                "status": status.HTTP_405_METHOD_NOT_ALLOWED,
                "message": f"{request.method} is not allowed!",
            }

            return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)