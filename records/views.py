from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User



class recordCreatView(LoginRequiredMixin,CreateView):
    # user ayad to add to the record 

    # 
    model       = FinalRecord
    form_class  = FinalRecordForm
    template_name   = 'records/record_create_form.html'
    success_url = reverse_lazy('records:record_create')

    def get_context_data(self, **kwargs):
        context                     = super().get_context_data(**kwargs)
        userId                        = self.request.user.id
        context['userAyada']        = UserAyada.objects.get(pk=userId).name
        context['recordsCount']     = UserAyada.objects.get(pk=userId).count
        return context

## services Views
## to add login required  LoginRequiredMixin
class ServiceListView(ListView):
    model = FinalRecord
    recordsCount = FinalRecord.objects.all()
    template_name = 'records/records_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(naId=search_query) | Q(hioId=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context                     = super().get_context_data(**kwargs)
        context['recordsCount']     = FinalRecord.objects.all().count()
        return context