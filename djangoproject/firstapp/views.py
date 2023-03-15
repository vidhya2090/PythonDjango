from django.shortcuts import render, redirect
from .models import Persons, Studentdata, Sales
from django.views import generic
from django.db.models import Sum, Count
from django.contrib import messages


# Create your views here.

class index(generic.ListView):
    model = Sales
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Display the KPI Counts and Trends for Sales data
        :param kwargs: Sales data
        :return: dictionary of sales data
        """
        sold_units_data = Sales.objects.values('region').order_by('region').annotate(
            units_sold=Sum('units_sold')).using(
            'default1')

        online_sales_data = Sales.objects.filter(sales_channel='Online').values('region').annotate(
            online_count=Count('sales_channel')).order_by('region').using(
            'default1')

        offline_sales_data = Sales.objects.filter(sales_channel='Offline').values('region').annotate(
            offline_count=Count('sales_channel')).order_by('region').using(
            'default1')

        region_count = Sales.objects.values('region').using('default1').distinct().count()
        sold_units_count = Sales.objects.all().using('default1').aggregate(sold_units_count=Sum('units_sold'))

        total_revenue = Sales.objects.all().using('default1').aggregate(total_revenue=Sum('total_revenue'))

        total_cost = Sales.objects.all().using('default1').aggregate(total_cost=Sum('total_profit'))

        sales_data = {'region_count': region_count, 'sold_units_count': sold_units_count,
                      'total_revenue': round(total_revenue['total_revenue'] / 100),
                      'total_cost': round(total_cost['total_cost'] / 100)}

        context = {'sold_units_data': sold_units_data, 'online_sales_data': online_sales_data,
                   'offline_sales_data': offline_sales_data, 'sales_data': sales_data}
        return context


class contact(generic.ListView):
    def get(self, request, *args, **kwargs):
        """
        Display my contact Details
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        contact_data = {"email": "vidhyaraviei@gmail", "linkedin": "https://www.linkedin.com/in/vidhya-r-440938217/",
                        "github": "", }
        context = {'data': contact_data}
        return render(request, 'contact.html', context)

class records(generic.ListView):
    template_name = 'records.html'

    def get_queryset(self):
        return Studentdata.objects.all().using('default1')

def get_profile(request):
    return render(request, 'profile.html')

def post_form(request):
    if (request.POST):
        studentdata_obj = Studentdata()
        studentdata_obj.name = request.POST.get('name')
        studentdata_obj.emailid = request.POST.get('emailid')
        studentdata_obj.qualification = request.POST.get('qualification')
        studentdata_obj.save(using='default1')
        messages.success(request, "successfully updated")
        return redirect('/firstapp/records/')

    return render(request, 'form.html')


def edit_form(request, pk):
    print(pk)
    studentdata_obj = Studentdata.objects.using('default1').get(num=pk)

    if (request.POST):
        studentdata_obj.name = request.POST.get('name')
        studentdata_obj.emailid = request.POST.get('emailid')
        studentdata_obj.qualification = request.POST.get('qualification')
        studentdata_obj.save()
        messages.success(request, "successfully updated")
        return redirect('/firstapp/records/')
    context = {'data': studentdata_obj}
    return render(request, 'form_edit.html', context)


def delete_form(request, pk):
    print(pk)
    studentdata_obj = Studentdata.objects.using('default1').get(num=pk)
    studentdata_obj.delete()
    messages.success(request, "deleted successfully")
    return redirect('/firstapp/records/')



