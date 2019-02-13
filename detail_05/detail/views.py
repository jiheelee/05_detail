from django.shortcuts import render

# Create your views here.
def mysite(request):
    return render(request,"detail/mysite.html")
    
def signup(request):
    return render(request,"detail/signup.html")

def mypage(request):
    return render(request,"detail/mypage.html")
    
def qna(request):
    return render(request, "detail/qna.html")
    
def not_found(request, not_found):
    return render(request, "detail/not_found.html", {"not_found":not_found})