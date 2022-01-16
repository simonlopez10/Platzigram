"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# # # POSTS = [
# # #     {
# # #         'TITLE': 'MONT BLANC',
# # #         'USER': {
# # #             'NAME': 'YÉSICA CORTÉS',
# # #             'PICTURE': 'HTTPS://PICSUM.PHOTOS/60/60/?IMAGE=1027'
# # #         },
# # #         'TIMESTAMP': DATETIME.NOW().STRFTIME('%B %DTH, %Y - %H:%M HRS'),
# # #         'PHOTO': 'HTTPS://PICSUM.PHOTOS/800/600?IMAGE=1036',
# # #     },
# # #     {
# # #         'TITLE': 'VIA LÁCTEA',
# # #         'USER': {
# # #             'NAME': 'CHRISTIAN VAN DER HENST',
# # #             'PICTURE': 'HTTPS://PICSUM.PHOTOS/60/60/?IMAGE=1005'
# # #         },
# # #         'TIMESTAMP': DATETIME.NOW().STRFTIME('%B %DTH, %Y - %H:%M HRS'),
# # #         'PHOTO': 'HTTPS://PICSUM.PHOTOS/800/800/?IMAGE=903',
# # #     },
# # #     {
# # #         'TITLE': 'NUEVO AUDITORIO',
# # #         'USER': {
# # #             'NAME': 'URIEL (THESPIANARTIST)',
# # #             'PICTURE': 'HTTPS://PICSUM.PHOTOS/60/60/?IMAGE=883'
# # #         },
# # #         'TIMESTAMP': DATETIME.NOW().STRFTIME('%B %DTH, %Y - %H:%M HRS'),
# # #         'PHOTO': 'HTTPS://PICSUM.PHOTOS/500/700/?IMAGE=1076',
# # #     }
# # # ]


@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )