from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('designerform/',views.designerform,name='designerform'),
    path('designlog/',views.designlog,name='designlog'),
    path('login/', views.login,name='login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('addp',views.addp,name='addp'),
    path('logout/',views.logout,name="logout"),
    path('homelogout/',views.homelogout,name="homelogout"),
    path('load_data/',views.load_data,name="load_data"),
    path('wedding/',views.wedding,name="wedding"),
    path('wedding_men/',views.wedding_men,name="wedding_men"),
    path('ethnic_men/',views.ethnic_men,name="ethnic_men"),
    path('workout_men/',views.workout_men,name="workout_men"),
    path('party_men/',views.party_men,name="party_men"),
    path('formal_men/',views.formal_men,name="formal_men"),
    path('casual_men/',views.casual_men,name="casual_men"),
    path('ethnic_women/',views.ethnic_women,name="ethnic_women"),
    path('workout_women/',views.workout_women,name="workout_women"),
    path('party_women/',views.party_women,name="party_women"),
    path('formal_women/',views.formal_women,name="formal_women"),
    path('casual_women/',views.casual_women,name="casual_women"),
   
    path('designerlogins/',views.designerlogins,name="designerlogins"),
    path('dummy/',views.dummy,name="dummy"),
    path('search/',views.search,name="search"),
    path('edit/<str:productId>/',views.edit,name="edit"),
    path('gridindex/',views.gridindex,name="gridindex"),
    path('griddesigner/',views.griddesigner,name="griddesigner"),
    path('designer_admin/',views.designer_admin,name="designer_admin"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('header/',views.header,name="header"),
    path('fullproduct/<str:productId>',views.fullproduct,name="fullproduct"),
    path('extra/',views.extra,name="extra"),
    path('session/',views.session,name="session"),
    path('add_designer/',views.add_designer,name="add_designer"),
    path('kaali/',views.kaali,name="kaali"),
    path('profile/',views.profile,name="profile"),
    path('dashheader/',views.dashheader,name="dashheader"),
    path('editdesigner/<str:productId>/',views.editdesigner,name="editdesigner"),
    path('editprofile/<str:uname>', views.editprofile, name='editprofile'),
    path('addplogin/',views.addplogin,name='addplogin'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('delete/<str:productId>/',views.delete,name="delete"),
    path('userlogins/',views.userlogins,name="userlogins"),
    path('deletedesigner/<str:productId>/',views.deletedesigner,name="deletedesigner")

    
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)