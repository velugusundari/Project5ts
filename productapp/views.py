from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import product
# Create your views here.
class productInput(View):
    def get(self,request):
        return render(request,"productinput.html")
class productInsert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mfdt = request.GET["t4"]
        p_expdt = request.GET["t5"]
        p1=product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res = HttpResponse("Product inserted successfully")
        return res

