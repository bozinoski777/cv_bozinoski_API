from rest_framework import serializers
from .models import Cv, Education, Languages, Organizations, ProfessionalExperience, Skills, CodingProjects

class CvSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cv
    fields = ('id', 'name', 'email', 'mobile', 'birthday', 'citizenship', 'github', 'linkedin', 'introduction')

class EducationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Education
    fields = ('id', 'timespan', 'institution', 'city', 'country')

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
    fields = ('id', 'name', 'email', 'mobile', 'birthday', 'citizenship', 'github', 'linkedin', 'introduction')
