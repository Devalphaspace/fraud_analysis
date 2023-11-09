from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from data_manipulation.scripts import data_manipulation_script

# Create your views here.

class DataManipulationView(APIView):
    def post(self, request):
        if request.method == 'POST':
            try:
                originalImage = request.data['original_image']
                editedImage = request.data['edited_image']

                detectedChanges = data_manipulation_script.detect_image_changes(
                    original_img=originalImage,
                    edited_img=editedImage,
                )

                if detectedChanges:
                    response = {
                        "status": status.HTTP_200_OK,
                        "message": detectedChanges,
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