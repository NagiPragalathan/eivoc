from base.models import UserProfile


def generate_registration_number(user_profile):
    prefix = 'R' if user_profile.category == 'Regular' else 'U' if user_profile.category == 'Undergraduate' else 'P'
    count = UserProfile.objects.filter(category=user_profile.category).count() + 1
    return f"{count:03d}{prefix}{user_profile.id}EIVOC2025"
