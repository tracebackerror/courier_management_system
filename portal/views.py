from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from .utils import getCourierRates, calculateFare
from .models import *
from .forms import *

    
class Login(LoginView):
    template_name = "login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("shipping")
        return super().get(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/login/")


class Register(CreateView):
    template_name = 'register.html'
    model = User
    form_class = RegisterForm
    success_url = "/login/"



class Shipping(LoginRequiredMixin, TemplateView):
    template_name = 'shipping.html'
    login_url = "/login/"
    extra_context = {}

    def get(self, request, *args, **kwargs):
        self.extra_context["name"] = request.user.first_name
        self.extra_context["email"] = request.user.email
        self.extra_context["mobile_no"] = ""
        self.extra_context["picking_address"] = ""
        self.extra_context["picking_city"] = ""
        self.extra_context["picking_pincode"] = ""
        self.extra_context["picking_date"] = ""
        self.extra_context["shipping_address"] = ""
        self.extra_context["shipping_city"] = ""
        self.extra_context["shipping_pincode"] = ""
        self.extra_context["goods_weight"] = ""
        self.extra_context["courier_type"] = ""
        self.extra_context["fast_delivery"] = ""
        self.extra_context["fare"] = None
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        post_data = self.request.POST.dict()
        action = post_data.pop("action")
        del post_data["csrfmiddlewaretoken"]
        if action == "book":
            shipment_obj = Shipment.objects.create(booked_by=request.user,**post_data)
            return redirect(f"/tracking/?bid={shipment_obj.id}")
        else:
            fare = calculateFare(post_data)
            self.extra_context["fare"] = fare
        self.extra_context.update(self.request.POST.dict())
        return super().get(request, *args, **kwargs)
        


class Tracking(TemplateView):
    template_name = 'tracking.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        bid = request.GET.get("bid")
        shipment = Shipment.objects.filter(id=bid)
        if shipment:
            shipment = shipment.first()
            status_list = [i[0] for i in STAIUS_CHOICES]
            self.extra_context["status_list"] = status_list
            self.extra_context["status_index"] = status_list.index(shipment.status) + 1
        self.extra_context["shipment"] = shipment
        return super().get(request, *args, **kwargs)
    

class RateCalculator(TemplateView):
    template_name = 'rate_calculator.html'
    extra_context = {}

    def post(self, request, *args, **kwargs):
        normal_rate, fast_rate = getCourierRates(request.POST["from_city"],request.POST["to_city"],request.POST["type"],request.POST["weight"])
        self.extra_context["normal_rate"] = normal_rate
        self.extra_context["fast_rate"] = fast_rate
        self.extra_context.update(self.request.POST.dict())
        return super().get(request, *args, **kwargs)