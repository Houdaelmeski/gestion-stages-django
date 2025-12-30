
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views 

#reset password....
from django.contrib.auth import views as authviews
#reset password....
from django.contrib.auth import views as authviews


urlpatterns = [
    path('',views.home1,name='home'),
    path('stagiere/<str:pk>',views.stagiere,name='stagiaire'),
    path('encadrant/<str:pk>',views.encadrant,name='encadrant'),
    path('stage/<str:pk>',views.stage,name='stage'),
    path('n_encadrent/',views.n_encadrent,name='n_encadrent'),
    path('u_encadrent/<str:pk>',views.u_encadrent,name='u_encadrent'),
    path('creeStage/',views.creeStage,name='creeStage'),
    path('recherche/',views.recherche,name='recherche'),
    path('edituser/',views.edit_user,name='edit_user'),
    path('n_stagiere/',views.registeretud,name='n_stagiere'),
    path('login/',views.loginn,name='loginn'),
    path('logout/',views.logoutt,name='logoutt'),

    path('notallowed/',views.nnn,name='nnn'),

    path('u_stagiere/<str:pk>',views.u_stagiere,name='u_stagiere'),
    path('delete/',views.delete,name='delete'),
    #path('deleteEncadrent/<str:pk>',views.deleteEncadrent,name='deleteEncadrent'),
    path('upload_documents/<str:pk>', views.upload_documents, name='upload_documents'),


    path('reset_password/',authviews.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',authviews.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',authviews.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',authviews.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('edit_stage/<str:pk>/', views.edit_stage, name='edit_stage'),
    path('delete_stage/<str:pk>/', views.delete_stage, name='delete_stage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
