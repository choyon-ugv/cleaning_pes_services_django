from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, SubscribeForm, CommentForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import BlogPost, Service, Comment, Tag


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subscribe_form = SubscribeForm()
        if form.is_valid():
            # Process the form data (e.g., send email or save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Example: Send email (configure email settings in settings.py)
            try:
                send_mail(
                    subject,
                    f'Message from {name} ({email}):\n\n{message}',
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message was sent, thank you!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
        subscribe_form = SubscribeForm()
    
    return render(request, 'contact.html', {
        'form': form,
        'subscribe_form': subscribe_form
    })

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Process subscription (e.g., save to database or integrate with email service)
            # For now, we'll just show a success message
            messages.success(request, 'Thank you for subscribing!')
            return redirect('contact')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('contact')

def blog(request):
    post_list = BlogPost.objects.all()
    if 'q' in request.GET:
        post_list = post_list.filter(title__icontains=request.GET['q'])
    if 'tag' in request.GET:
        post_list = post_list.filter(tags__name=request.GET['tag'])
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    services = Service.objects.all()[:7]
    recent_posts = BlogPost.objects.all()[:3]
    tags = Tag.objects.all()
    return render(request, 'blog.html', {
        'posts': posts,
        'services': services,
        'recent_posts': recent_posts,
        'tags': tags
    })

def blog_single(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    services = Service.objects.all()[:7]
    recent_posts = BlogPost.objects.exclude(slug=slug)[:3]
    tags = Tag.objects.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                post=post,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                website=form.cleaned_data['website'],
                message=form.cleaned_data['message']
            )
            if 'parent_id' in request.POST and request.POST['parent_id']:
                parent = get_object_or_404(Comment, id=request.POST['parent_id'])
                comment.parent = parent
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('blog_single', slug=slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CommentForm()
        if 'reply_to' in request.GET:
            reply_to = get_object_or_404(Comment, id=request.GET['reply_to'])
            form.initial['name'] = request.GET.get('name', '')
            form.initial['email'] = request.GET.get('email', '')
        else:
            reply_to = None
    
    return render(request, 'blog-single.html', {
        'post': post,
        'form': form,
        'reply_to': reply_to,
        'services': services,
        'recent_posts': recent_posts,
        'tags': tags
    })