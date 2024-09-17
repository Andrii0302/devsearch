from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile 
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
@receiver(post_save, sender=Profile)
def updatePUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created == False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()
# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile saved!')
#     print('Instance:', instance)
#     print('Created:', created)

@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    user=instance.user
    user.delete()

# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile)