from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from .models import WheelSpecification
from .serializers import (
    WheelSpecificationRequestSerializer,
    WheelSpecificationResponseSerializer,
    WheelSpecificationResponseDataSerializer
)

class WheelSpecificationCreateView(APIView):
    
    @extend_schema(
        request=WheelSpecificationRequestSerializer,
        responses={
            201: WheelSpecificationResponseSerializer,
            400: {
                'type': 'object',
                'properties': {
                    'errors': {'type': 'object'},
                    'message': {'type': 'string'},
                    'success': {'type': 'boolean'}
                }
            },
        },
        description="Submit a new wheel specification form",
        summary="Create Wheel Specification",
        tags=["Wheel Specifications"]
    )
    def post(self, request):
        serializer = WheelSpecificationRequestSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            
            # Extract fields and main data
            fields_data = validated_data.pop('fields')
            
            # Create the wheel specification instance
            wheel_spec = WheelSpecification.objects.create(
                form_number=validated_data['formNumber'],
                submitted_by=validated_data['submittedBy'],
                submitted_date=validated_data['submittedDate'],
                # Map the camelCase fields to snake_case model fields
                axle_box_housing_bore_dia=fields_data['axleBoxHousingBoreDia'],
                bearing_seat_diameter=fields_data['bearingSeatDiameter'],
                condemning_dia=fields_data['condemningDia'],
                intermediate_wwp=fields_data['intermediateWWP'],
                last_shop_issue_size=fields_data['lastShopIssueSize'],
                roller_bearing_bore_dia=fields_data['rollerBearingBoreDia'],
                roller_bearing_outer_dia=fields_data['rollerBearingOuterDia'],
                roller_bearing_width=fields_data['rollerBearingWidth'],
                tread_diameter_new=fields_data['treadDiameterNew'],
                variation_same_axle=fields_data['variationSameAxle'],
                variation_same_bogie=fields_data['variationSameBogie'],
                variation_same_coach=fields_data['variationSameCoach'],
                wheel_disc_width=fields_data['wheelDiscWidth'],
                wheel_gauge=fields_data['wheelGauge'],
                wheel_profile=fields_data['wheelProfile'],
            )
            
            # Prepare response data
            response_data = {
                "data": {
                    "formNumber": wheel_spec.form_number,
                    "status": "Saved",
                    "submittedBy": wheel_spec.submitted_by,
                    "submittedDate": wheel_spec.submitted_date
                },
                "message": "Wheel specification submitted successfully.",
                "success": True
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response({
            "errors": serializer.errors,
            "message": "Validation Failed",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='formNumber', 
                description='Filter by form number', 
                required=False, 
                type=OpenApiTypes.STR, 
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name='submittedBy', 
                description='Filter by submitter', 
                required=False, 
                type=OpenApiTypes.STR, 
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name='submittedDate', 
                description='Filter by submission date (YYYY-MM-DD)', 
                required=False, 
                type=OpenApiTypes.DATE, 
                location=OpenApiParameter.QUERY
            ),
        ],
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'formNumber': {'type': 'string'},
                                'submittedBy': {'type': 'string'},
                                'submittedDate': {'type': 'string', 'format': 'date'},
                                'fields': {
                                    'type': 'object',
                                    'properties': {
                                        'axleBoxHousingBoreDia': {'type': 'string'},
                                        'bearingSeatDiameter': {'type': 'string'},
                                        'condemningDia': {'type': 'string'},
                                        'intermediateWWP': {'type': 'string'},
                                        'lastShopIssueSize': {'type': 'string'},
                                        'rollerBearingBoreDia': {'type': 'string'},
                                        'rollerBearingOuterDia': {'type': 'string'},
                                        'rollerBearingWidth': {'type': 'string'},
                                        'treadDiameterNew': {'type': 'string'},
                                        'variationSameAxle': {'type': 'string'},
                                        'variationSameBogie': {'type': 'string'},
                                        'variationSameCoach': {'type': 'string'},
                                        'wheelDiscWidth': {'type': 'string'},
                                        'wheelGauge': {'type': 'string'},
                                        'wheelProfile': {'type': 'string'}
                                    }
                                }
                            }
                        }
                    },
                    'message': {'type': 'string'},
                    'success': {'type': 'boolean'}
                }
            }
        },
        description="Get list of submitted wheel specifications with optional filters",
        summary="List Wheel Specifications",
        tags=["Wheel Specifications"]
    )
    def get(self, request):
        form_number = request.GET.get('formNumber')
        submitted_by = request.GET.get('submittedBy')
        submitted_date = request.GET.get('submittedDate')

        queryset = WheelSpecification.objects.all()
        if form_number:
            queryset = queryset.filter(form_number=form_number)
        if submitted_by:
            queryset = queryset.filter(submitted_by=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submitted_date=submitted_date)

        # Format the response to match the expected structure
        data = []
        for spec in queryset:
            data.append({
                'formNumber': spec.form_number,
                'submittedBy': spec.submitted_by,
                'submittedDate': spec.submitted_date,
                'fields': {
                    'axleBoxHousingBoreDia': spec.axle_box_housing_bore_dia,
                    'bearingSeatDiameter': spec.bearing_seat_diameter,
                    'condemningDia': spec.condemning_dia,
                    'intermediateWWP': spec.intermediate_wwp,
                    'lastShopIssueSize': spec.last_shop_issue_size,
                    'rollerBearingBoreDia': spec.roller_bearing_bore_dia,
                    'rollerBearingOuterDia': spec.roller_bearing_outer_dia,
                    'rollerBearingWidth': spec.roller_bearing_width,
                    'treadDiameterNew': spec.tread_diameter_new,
                    'variationSameAxle': spec.variation_same_axle,
                    'variationSameBogie': spec.variation_same_bogie,
                    'variationSameCoach': spec.variation_same_coach,
                    'wheelDiscWidth': spec.wheel_disc_width,
                    'wheelGauge': spec.wheel_gauge,
                    'wheelProfile': spec.wheel_profile,
                }
            })

        return Response({
            "data": data,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True
        }, status=status.HTTP_200_OK)