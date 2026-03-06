class DisableCSRFMiddleware:
    """
    Middleware to disable CSRF protection for API endpoints.
    This allows DRF views to work without CSRF tokens when using token authentication.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Disable CSRF for API endpoints
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        
        response = self.get_response(request)
        return response