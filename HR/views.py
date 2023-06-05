import csv
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from Notifications.models import Notification
from HR.forms import ManagerForm, CompanyForm
from HR.models import Manager, Company


def Base_information_Manager(request):
    if request.method == "POST":
        manager_form = ManagerForm(request.POST, request.FILES)
        if manager_form.is_valid():
            manager_form.save()
            messages.success(request,'ثبت مدیر با موفقیت انجام شد')
        else:
            messages.error(request, 'مشکلی در ورودی اطلاعات.لطفا مجدد تلاش کنید')

        return redirect("Base_information_Manager")
    manager_form = ManagerForm()
    managers = Manager.objects.all()
    return render(request=request, template_name="HR/Base_Information.html", context={'manager_form': manager_form, 'managers': managers})

def export_managers_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="managers.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    writer.writerow(['id','persian_name', 'english_name', 'code', 'order', 'manager_status', 'queue_id', 'headquarter_id'])

    managers = Manager.objects.all().values_list('id','persian_name', 'english_name', 'code', 'order', 'manager_status', 'queue_id', 'headquarter_id')
    for manager in managers:
        writer.writerow(manager)

    return response


def delete_manager(request, id):
    manager = Manager.objects.get(id=id)
    manager.delete()
    return HttpResponseRedirect(reverse('Base_information_Manager'))


def update_manager(request, id):
    manager = Manager.objects.get(id=id)
    template = loader.get_template('HR/Base_Information_Manager_Update.html')
    context = {
        'manager': manager,
    }
    return HttpResponse(template.render(context, request))


def update_manager_record(request, id):
      persian_name = request.POST['persian_name']
      code = request.POST['code']
      english_name = request.POST['english_name']
      order = request.POST['order']
      manager_status = request.POST['manager_status']
      manager = Manager.objects.get(id=id)
      manager.persian_name = persian_name
      manager.english_name = english_name
      manager.code = code
      manager.order = order
      manager.manager_status = manager_status

      manager.save()
      Notification.objects.create(title="ویرایش مدیریت",description=f" ویرایش شد{manager.persian_name}مدیر ")


      return HttpResponseRedirect(reverse('Base_information_Manager'))


def Company_Base_Information(request):
    if request.method == "POST":
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form.save()
            messages.success(request,'ثبت شرکت با موفقیت انجام شد')
        else:
            messages.error(request, 'مشکلی در ورودی اطلاعات.لطفا مجدد تلاش کنید')

        return redirect("Company_Base_Information")
    company_form = CompanyForm()
    companies = Company.objects.all()
    return render(request=request, template_name="HR/Company/Company.html", context={'company_form': company_form, 'companies': companies})


def Update_Company_Base_Information(request, id):
    title = request.POST['title']
    code = request.POST['code']
    english_title = request.POST['english_title']
    company_status = request.POST['company_status']
    company = Company.objects.get(id=id)
    company.persian_name = title
    company.english_name = english_title
    company.code = code
    company.manager_status = company_status

    company.save()
    Notification.objects.create(title="ویرایش شرکت", description=f" ویرایش شد{company.title}شرکت ")

    return HttpResponseRedirect(reverse('Company_Base_Information'))

def Update_Company(request, id):
    company_form = CompanyForm()
    company = Company.objects.get(id=id)
    template = loader.get_template('HR/Company/Company_Base_Information_Update.html')
    context = {
        'company': company,
        'company_form':company_form
    }
    return HttpResponse(template.render(context, request))