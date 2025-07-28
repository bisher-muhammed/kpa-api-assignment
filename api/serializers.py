# serializers.py
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from .models import WheelSpecification

class WheelSpecificationFieldsSerializer(serializers.Serializer):
    """Serializer for the nested fields object"""
    axleBoxHousingBoreDia = serializers.CharField(max_length=100, help_text="Axle box housing bore diameter")
    bearingSeatDiameter = serializers.CharField(max_length=100, help_text="Bearing seat diameter")
    condemningDia = serializers.CharField(max_length=100, help_text="Condemning diameter")
    intermediateWWP = serializers.CharField(max_length=100, help_text="Intermediate WWP")
    lastShopIssueSize = serializers.CharField(max_length=100, help_text="Last shop issue size")
    rollerBearingBoreDia = serializers.CharField(max_length=100, help_text="Roller bearing bore diameter")
    rollerBearingOuterDia = serializers.CharField(max_length=100, help_text="Roller bearing outer diameter")
    rollerBearingWidth = serializers.CharField(max_length=100, help_text="Roller bearing width")
    treadDiameterNew = serializers.CharField(max_length=100, help_text="Tread diameter new")
    variationSameAxle = serializers.CharField(max_length=100, help_text="Variation same axle")
    variationSameBogie = serializers.CharField(max_length=100, help_text="Variation same bogie")
    variationSameCoach = serializers.CharField(max_length=100, help_text="Variation same coach")
    wheelDiscWidth = serializers.CharField(max_length=100, help_text="Wheel disc width")
    wheelGauge = serializers.CharField(max_length=100, help_text="Wheel gauge")
    wheelProfile = serializers.CharField(max_length=100, help_text="Wheel profile")

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Wheel Specification Request Example',
            summary='Complete wheel specification form',
            description='Example of a complete wheel specification submission',
            value={
                "fields": {
                    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                    "bearingSeatDiameter": "130.043 TO 130.068",
                    "condemningDia": "825 (800-900)",
                    "intermediateWWP": "20 TO 28",
                    "lastShopIssueSize": "837 (800-900)",
                    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                    "rollerBearingWidth": "93 (+0/-0.250)",
                    "treadDiameterNew": "915 (900-1000)",
                    "variationSameAxle": "0.5",
                    "variationSameBogie": "5",
                    "variationSameCoach": "13",
                    "wheelDiscWidth": "127 (+4/-0)",
                    "wheelGauge": "1600 (+2,-1)",
                    "wheelProfile": "29.4 Flange Thickness"
                },
                "formNumber": "WHEEL-2025-001",
                "submittedBy": "user_id_123",
                "submittedDate": "2025-07-03"
            },
            request_only=True,
        ),
    ]
)
class WheelSpecificationRequestSerializer(serializers.Serializer):
    """Serializer for incoming requests"""
    fields = WheelSpecificationFieldsSerializer()
    formNumber = serializers.CharField(max_length=100, help_text="Form number")
    submittedBy = serializers.CharField(max_length=100, help_text="User ID who submitted the form")
    submittedDate = serializers.DateField(help_text="Date of submission (YYYY-MM-DD)")

class WheelSpecificationResponseDataSerializer(serializers.Serializer):
    """Serializer for response data object"""
    formNumber = serializers.CharField()
    status = serializers.CharField()
    submittedBy = serializers.CharField()
    submittedDate = serializers.DateField()

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Success Response Example',
            summary='Successful submission response',
            description='Response when wheel specification is successfully submitted',
            value={
                "data": {
                    "formNumber": "WHEEL-2025-001",
                    "status": "Saved",
                    "submittedBy": "user_id_123",
                    "submittedDate": "2025-07-03"
                },
                "message": "Wheel specification submitted successfully.",
                "success": True
            },
            response_only=True,
        ),
    ]
)
class WheelSpecificationResponseSerializer(serializers.Serializer):
    """Serializer for API responses"""
    data = WheelSpecificationResponseDataSerializer()
    message = serializers.CharField()
    success = serializers.BooleanField()
