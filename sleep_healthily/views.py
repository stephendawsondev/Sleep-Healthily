from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 -Server error """
    return render(request, "errors/500.html", status=500)


def privacy_policy(request):
    """ Privacy Policy """
    return render(request, "policies/privacy_policy.html")


def shipping_policy(request):
    """ Shipping Policy """
    return render(request, "policies/shipping_policy.html")


def contact(request):
    """ Contact """
    return render(request, "contact.html")


def about(request):
    """ About us """
    return render(request, "about.html")
