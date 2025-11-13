"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from minicom import api, views

urlpatterns = [
    # Original test endpoints
    path('foo', api.verify),
    path('bar', api.verify),

    # Customer chat interface (HTML view)
    path('chat/<str:customer_id>/', views.chat_view, name='chat'),

    # Agent interfaces (HTML views)
    path('agent/dashboard/', views.agent_dashboard_view, name='agent_dashboard_view'),
    path('agent/chat/<str:customer_id>/', views.agent_chat_view, name='agent_chat_view'),

    # API endpoints
    path('api/conversation/<str:customer_id>/', views.get_conversation, name='get_conversation'),
    path('api/agent/dashboard/', views.agent_dashboard_api, name='agent_dashboard_api'),
    path('api/agent/takeover/<str:customer_id>/', views.agent_takeover, name='agent_takeover'),
]
