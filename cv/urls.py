from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cv', views.CvView)
router.register('education', views.EducationView)
router.register('languages', views.LanguagesView)
router.register('organizations', views.OrganizationsView)
router.register('professional_experience', views.ProfessionalExperienceView)
router.register('skills', views.SkillsView)
router.register('coding_projects', views.CodingProjectsView)


urlpatterns = [
  path('', include(router.urls))
]
