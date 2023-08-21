from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import UserViewSet, SnippetViewSet, api_root
from rest_framework.routers import DefaultRouter

# snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
# snippet_detail = SnippetViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# snippet_highlight = SnippetViewSet.as_view({"get": "highlight"})
# user_list = UserViewSet.as_view({"get": "list"})
# user_detail = UserViewSet.as_view({"get": "retrieve"})

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    # path("", views.api_root),
    # path("snippets/", snippet_list, name="snippet-list"),
    # path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    # path(
    #     "snippets/<int:pk>/highlight/",
    #     snippet_highlight,
    #     name="snippet-highlight",
    # ),
    # path("users/", user_list, name="user-list"),
    # path("users/<int:pk>/", user_detail, name="user-detail"),
    path("", include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)
