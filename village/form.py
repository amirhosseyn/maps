from django.forms import ModelForm
from django import forms
from .models import Village


class VillageForm(ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        fieldsets = [
            ('Group : General Information', {
                'fields': [
                    'name',
                    'latitude',
                    'longitude',
                    'population',
                    'household_count',
                    'climate',
                    'employment_percentage',
                    'historical_tourism_background',
                    'scientific_figures',
                    'cultural_figures',
                    'religious_figures',
                    'artistic_figures',
                    'sports_figures',
                    'migration_percentage',
                    'migration_reason',
                    'main_occupations',
                    'raw_products_men',
                    'processed_products_women',
                    'women_income',
                ],
                'description': 'Description for General Information',
            }),
            ('Group: Infrastructure of the village', {
                'fields': [
                    'drinking_water_available',
                    'well_water_available',
                    'canal_water_available',
                    'telephone_available',
                    'mobile_antenna_available',
                    'village_council_building_available',
                    'imam_available',
                    'school_available',
                    'number_of_students',
                    'post_office_available',
                    'bank_available',
                    'addiction_recovery_camp_available',
                    'bakery_available',
                    'electricity_available',
                    'gas_available',
                    'television_antenna_available',
                    'internet_available',
                    'village_head_available',
                    'basij_sister_available',
                    'basij_brother_available',
                    'mosque_available',
                    'police_available',
                    'sports_hall_available',
                    'teacher_house_available',
                    'road_available',
                    'asphalt_available',
                    'pathways_available',
                    'news_channel_available',
                    'park_available',
                    'historical_buildings_available',
                    'welfare_committee_coverage',
                    'shop_available',
                    'production_workshop_available',
                    'beautification_plan_available',
                    'fuel_station_available',
                    'transportation_services_available',
                    'ecotourism_infrastructure_available',
                    'doctor_available',
                    'nurse_available',
                    'health_center_available',
                    'youth_involvement',
                    'women_involvement',
                    'proximity_to_city',
                ],
                'description': 'Description for Infrastructure of the village',
            }),
            ('Group: Other', {
                'fields': [
                    'opportunities_potentials',
                    'issues_threats',
                    'development_priorities',
                    'investment_opportunities',
                    'people_needs_demands',
                    'women_needs_demands',
                    'youth_needs_demands',
                    'main_needs_solutions',
                ],
                'description': 'Description for Other',
            }),
        ]


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)