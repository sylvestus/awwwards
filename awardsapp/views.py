from email import message
from unicodedata import name
from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import newPost,ratesForm,UprofileForm,UuserForm
from awardsapp.models import Post,Ratings,Profile,User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import PostSerializer,ProfileSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Profile.objects.filter(user=current_user.id).all
    return render(request, 'profile.html', {"projects": projects})
# def profile(request):
#     current_user = request.user
#     images = Image.objects.filter(profile=current_user.id).all

#     return render(request, "profile.html", {"images": images})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostList(APIView):
    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='/accounts/login/')
def uprofile(request, id):
    current_user = request.user
    user_object = get_object_or_404(User, id=id)
    profile_object = get_object_or_404(Profile, user_id=id)
    profile_update = UprofileForm(request.POST or None, instance=profile_object)
    user_update = UuserForm(request.POST or None, instance=user_object)
    if profile_update.is_valid() and user_update.is_valid():
        user_update.save()
        profile_update.save()
        return HttpResponseRedirect("/showProfile")

    return render(
        request, "uprofile.html",{"profile_update": profile_update, "user_update": user_update})

@login_required(login_url='/accounts/login/')
def landingPage(request):
    message='welcome to the landing page'
    projects = Post.objects.all()

    return render(request,'landingPage.html',{'message':message,'projects':projects})

@login_required(login_url='/accounts/login/')
def more_on_pic(request,id):
    project = Post.objects.get(id=id)
    rate = Ratings.objects.filter(user=request.user, post=project).first()
    ratings = Ratings.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = ratesForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            userbility = form.cleaned_data['userbility']
            content = form.cleaned_data['content']
            review = Ratings()
            review.post = project
            review.user = current_user
            review.design = design
            review.userbility = userbility
            review.content = content
            review.average = (
                review.design + review.userbility + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('more', args=(project.id,)))
    else:
        form = ratesForm()
       
    return render(request, 'more.html',{'ratings': rate,'project': project,'form': form,'rating_status': rating_status,'reviews': ratings,})




@login_required(login_url='/accounts/login/')
def rate(request):

    if request.method == "POST":
        form = ratesForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.cleaned_data["design"]
            userbility=form.cleaned_data["userbility"]
            content=form.cleaned_data["content"]
            average=(int(design) + int(userbility)+ int(content))/3

            ratings=Ratings(design=design,userbility=userbility,content=content,average=average)

            ratings.objects.filter(post=id).save()
            return redirect('more')

    else:
        form = ratesForm()
    return render(request, "rate.html", {"ratesForm": form})



    # if request.method == "POST":
    #     form = ratesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #          design = form.cleaned_data["design"]
    #          userbility=form.cleaned_data["userbility"]
    #          content=form.cleaned_data["content"]
    #          average=(int(design) + int(userbility)+ int(content))/3

    #          ratings=Ratings(design=design,userbility=userbility,content=content)
    #          ratings.save()
    #     return redirect("landingPage")
    # else:
    #     form=ratesForm()

    # return render(request,'rate.html',{'message':message,"ratesForm":form})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    if request.method == "POST":
        form = newPost(request.POST, request.FILES)
        if form.is_valid():
            
            title = form.cleaned_data["title"]
            project_image = form.cleaned_data["project_image"]
            description = form.cleaned_data["description"]
            url = form.cleaned_data["url"]
            post = Post(title=title,project_image=project_image,description=description,url=url,)
            post.save()
        return redirect("landingPage")

    else:
        form = newPost()
    return render(request, "new_post.html", {"postForm": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    message='user profile'
    return render(request,'profile.html',{'message':message}) 
def updateProfile(request):
    message='update user profile'
    return render(request,'updateProfile.html',{'message':message})
def search(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})