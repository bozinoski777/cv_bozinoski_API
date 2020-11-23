from django.shortcuts import render
from rest_framework import viewsets
from .models import Cv, Education, Languages, Organizations, ProfessionalExperience, Skills, CodingProjects
from .serializers import CvSerializer, EducationSerializer, LanguagesSerializer, OrganizationsSerializer, ProfessionalExperienceSerializer, SkillsSerializer, CodingProjectsSerializer

class CvView(viewsets.ModelViewSet):
  queryset = Cv.objects.all()
  serializer_class = CvSerializer

class EducationView(viewsets.ModelViewSet):
  queryset = Education.objects.all()
  serializer_class = EducationSerializer

class LanguagesView(viewsets.ModelViewSet):
  queryset = Languages.objects.all()
  serializer_class = LanguagesSerializer

class OrganizationsView(viewsets.ModelViewSet):
  queryset = Organizations.objects.all()
  serializer_class = OrganizationsSerializer

class ProfessionalExperienceView(viewsets.ModelViewSet):
  queryset = ProfessionalExperience.objects.all()
  serializer_class = ProfessionalExperienceSerializer

class SkillsView(viewsets.ModelViewSet):
  queryset = Skills.objects.all()
  serializer_class = SkillsSerializer

class CodingProjectsView(viewsets.ModelViewSet):
  queryset = CodingProjects.objects.all()
  serializer_class = CodingProjectsSerializer
