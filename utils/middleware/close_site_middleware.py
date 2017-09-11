from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from utils.site_settings import is_site_closed
from utils.permission import is_admin_or_root


class CloseSiteMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        force_closed = view_kwargs.pop('force_closed', False)
        if is_site_closed() and force_closed and not is_admin_or_root(request.user):
            return render(request, 'error/closed.jinja2')
        else:
            return view_func(request, *view_args, **view_kwargs)
