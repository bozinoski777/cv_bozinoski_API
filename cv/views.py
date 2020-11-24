from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Contact, Education, Languages, Organizations, ProfessionalExperience, Skills, CodingProjects
from .serializers import ContactSerializer, EducationSerializer, LanguagesSerializer, OrganizationsSerializer, ProfessionalExperienceSerializer, SkillsSerializer, CodingProjectsSerializer

class ContactView(viewsets.ModelViewSet):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer

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
