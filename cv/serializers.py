from rest_framework import serializers
from .models import Contact, Education, Languages, Organizations, ProfessionalExperience, Skills, CodingProjects

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('id', 'introduction', 'name', 'email', 'mobile', 'birthday', 'citizenship', 'github', 'linkedin')

class EducationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Education
    fields = ('id', 'degree', 'timespan', 'institution', 'city', 'country')

class LanguagesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Languages
    fields = ('id', 'language', 'proficiency', 'comment')

class OrganizationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organizations
    fields = ('id', 'timespan', 'institution', 'title', 'city', 'country', 'description')

class ProfessionalExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProfessionalExperience
    fields = ('id', 'timespan', 'institution', 'title', 'city', 'country', 'description')

class SkillsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = ('id', 'skill', 'description')

class CodingProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = CodingProjects
    fields = ('id', 'title', 'tagline', 'description', 'live_demo', 'repository')
