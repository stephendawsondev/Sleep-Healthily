from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm, CustomUserEditForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_form = CustomUserEditForm(instance=request.user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = CustomUserEditForm(request.POST, instance=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and form.is_valid():
            user_form.save()
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    template = 'profiles/profile.html'
    context = {
        'user_form': user_form,
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def account_delete(request):
    """ Deletes the user's account and logs them out."""
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect(reverse('home'))
    else:
        return redirect(reverse('profile'))
