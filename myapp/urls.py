
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('verify_expert/', views.verify_expert),
    path('accept_expert/<id>',views.accept_expert),
    path('reject_expert/<id>',views.reject_expert),
    path('view_users/', views.view_users),
    path('change_password/', views.change_password),
    path('change_password_post/', views.change_password_post),
    path('view_complaint/', views.view_complaint),
    path('sent_reply/<id>/', views.sent_reply),
    path('sent_reply_post/', views.sent_reply_post),
    path('view_feedback/', views.view_feedback),
    path('forgot_pass/', views.forgot_pass),
    path('forgot_pass_post/', views.forgot_pass_post),
    path('login_get/', views.login_get),
    path('login_post/', views.login_post),
    path('admin_index1/', views.admin_index),



    path('register_get/',views.register_get),
    path('register_post/',views.register_post),
    path('add_new/',views.add_new),
    path('add_new_post/',views.add_new_post),
    path('addvdo/',views.addvdo),
    path('addvdo_post/',views.addvdo_post),
    path('changepass2/',views.changepass2),
    path('changepass2_post/',views.changepass2_post),
    path('doubts/',views.doubts),
    path('edit_profile/',views.edit_profile),
    path('edit_profile_post/',views.edit_profile_post),
    path('deletecert1/<id>',views.deletecert1),
    path('deletecert2/<id>',views.deletecert2),
    path('edittip/<id>',views.edittip),
    path('edittip_post/',views.edittip_post),
    path('manage_view/',views.manage_view),
    path('delete_tips/<id>',views.delete_tips),
    path('profile/',views.profile),
    path('send_reply/',views.send_reply),
    path('send_reply_post/',views.send_reply_post),
    path('video/',views.video),
    path('delete_vdo/<id>',views.delete_vdo),
    path('expert_index/',views.expert_index),
    path('expert_view_users/',views.expert_view_users),

    path('user_login/',views.user_login),
    path('registration/',views.registration),
    path('change_passwordpost/',views.change_passwordpost),
    path('viewexpert/',views.viewexpert),
    path('viewdoubt/',views.viewdoubt),
    path('senddoubt/',views.senddoubt),
    path('viewtip/',views.viewtip),
    path('User_viewchat/',views.User_viewchat),
    path('User_sendchat/',views.User_sendchat),
    path('forgotpasswordflutter/',views.forgotpasswordflutter),
    path('verifyOtpflutterPost/',views.verifyOtpflutterPost),
    path('changePasswordflutter/',views.changePasswordflutter),
    path('view_profile/',views.view_profile),
    path('update_profile/',views.update_profile),
    path('android_view_videos/',views.android_view_videos),
    path('check_phishing/',views.check_phishing),
    path('check_apk/',views.check_apk),
    path('file_checking_fn/',views.file_checking_fn),
    path('check_credentials/',views.check_credentials),




    path('expert_add_post/',views.expert_add_post),
    path('expert_view_post/',views.expert_view_post),
    path('expert_view_others_post/',views.expert_view_others_post),
    path('like/<int:post_id>/', views.toggle_like),
    path('comment/<int:post_id>/', views.add_comment),

    path("expert_change_password/", views.expert_change_password),


    path("user_viewprofile/", views.user_viewprofile),
    path("user_viewprofileandeditprofile/", views.user_viewprofileandeditprofile),
    path("useraddpost/", views.useraddpost),
    path("user_viewownpost/", views.user_viewownpost),
    path("postremove/", views.postremove),
    path("user_viewcommentsandreply/", views.user_viewcommentsandreply),
    path("user_addcomment/", views.user_addcomment),
    path("user_viewotherspost/", views.user_viewotherspost),
    path("likes/", views.likes),
    path("user_viewothersusers/", views.user_viewothersusers),
    path("user_sendfriendrequest/", views.user_sendfriendrequest),
    path("user_viewfriedrequest/", views.user_viewfriedrequest),
    path("user_followback/", views.user_followback),
    path("user_remove/", views.user_remove),
    path("viewfriends/", views.viewfriends),
    path("user_viewreject/", views.user_viewreject),
    path("user_viewapprovedrequest/", views.user_viewapprovedrequest),
    path("user_fromremovefromfriendlist/", views.user_fromremovefromfriendlist),
    path("user_viewnotification/", views.user_viewnotification),
    path("reject_notification/", views.reject_notification),
    path("accept_notification/", views.accept_notification),

    path("user_viewreply/", views.user_viewreply),
    path("user_sendcomplaint/", views.user_sendcomplaint),
    path("user_review_rating/", views.user_review_rating),

    path('question_list/', views.question_list),
    path('add_question/', views.add_question),
    path('quiz_results_view/', views.quiz_results_view),


    path('take_quiz_json/', views.take_quiz_json),
    path('submit_quiz/', views.submit_quiz),

    # chat
    path('expert_chat_to_user/<id>', views.expert_chat_to_user),
    path('chat_view', views.chat_view),
    path('expert_chat_to_user/<id>', views.expert_chat_to_user),
    path('chat_send/<msg>', views.chat_send),

]
