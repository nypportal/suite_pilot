from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from Coding.models import MaterialGroup, IdentityGroup, Child, Values


def coding_view(request):
    material_group_qs = MaterialGroup.objects.all()
    return render(request, 'Coding/Coding_New_Style.html', {'material_group_qs':material_group_qs})

def json_material_group_data(request):
    material_qs_val = list(MaterialGroup.objects.values())
    return JsonResponse({'data':material_qs_val})

def json_material_group_selected_data(request,*args, **kwargs):
    selected_material_group = kwargs.get('material_group')
    # print(selected_material_group)
    obj_identity_group = list(IdentityGroup.objects.filter(material_group__material_group=selected_material_group).values())
    return JsonResponse({'data': obj_identity_group})

def json_identity_group_selected_data(request,*args, **kwargs):
    selected_identity = kwargs.get('identity_group')
    obj_child_group = list(Child.objects.filter(identity_group__identity_group=selected_identity).values('child_group'))
    print(obj_child_group)

    # obj_child_child = list(Values.objects.all().values_list('child_id_as_child'))
    # obj_value_group = list(Values.objects.filter(child_group__child_group= 'Anchor Bolts with shape of L'))
    return JsonResponse({'data': obj_child_group})

def json_child_group_data(request,*args, **kwargs):
    obj_value_group = list(Values.objects.values_list('value','child_id_as_child'))
    obj_parent_group = list(Values.objects.values_list('value','child_id_as_child'))

    print(obj_value_group)
    return JsonResponse({'data': obj_value_group})
