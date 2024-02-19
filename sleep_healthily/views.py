from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def privacy_policy(request):
    """ Privacy Policy """
    return render(request, "policies/privacy_policy.html")


def shipping_policy(request):
    """ Shipping Policy """
    return render(request, "policies/shipping_policy.html")
