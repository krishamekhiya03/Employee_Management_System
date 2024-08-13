from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Employee
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import Http404
from django.db import IntegrityError

def index(request):
    return render(request, 'index.html')

def add_emp(request):
    email_validator = EmailValidator()
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            Date_Of_Birth = request.POST.get('Date_Of_Birth')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address', '')

            
            try:
                email_validator(email)  # Validate email
            except ValidationError:
                messages.error(request, 'Invalid email format.')
                return redirect('add_emp')

            
            if not phone_number.isdigit() or len(phone_number) != 10:   # Validation number
                messages.error(request, 'Phone number must be exactly 10 digits.')
                return redirect('add_emp')

            try:
                date_of_birth = datetime.strptime(Date_Of_Birth, '%Y-%m-%d').date()
            except (TypeError, ValueError):
                messages.error(request, 'Invalid date format. Use YYYY-MM-DD.')
                return redirect('add_emp')

            try:
                new_emp = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    Date_Of_Birth=date_of_birth,
                    email=email,
                    phone_number=phone_number,
                    address=address
                )
                new_emp.save()
                messages.success(request, 'Employee Added Successfully.')
                return redirect('list_emp')
            except IntegrityError:
                messages.error(request, 'This phone number is already in use by another employee.')
                return redirect('add_emp')

        elif request.method == 'GET':
            return render(request, 'add_emp.html')

        else:
            messages.error(request, 'An Exception Occurred! Employee Has Not Been Added.')
            return redirect('add_emp')

    except ValidationError as e:
        messages.error(request, f'Validation Error: {e}')
        return redirect('add_emp')
    except Exception as e:
        messages.error(request, f'An Unexpected Error Occurred: {e}')
        return redirect('add_emp')
def update_emp(request, emp_id=0):
    email_validator = EmailValidator()
    try:
        if request.method == 'POST':
            emp_id = request.POST.get('emp_id')
            emp = get_object_or_404(Employee, id=emp_id)

            email = request.POST.get('email')

          
            try:
                email_validator(email)    # Validate email
            except ValidationError:
                messages.error(request, 'Invalid email format.')
                return redirect(f'/update_emp/{emp_id}/')

            
            phone_number = request.POST.get('phone_number')     # Validation of number
            if not phone_number.isdigit() or len(phone_number) != 10:
                messages.error(request, 'Phone number must be exactly 10 digits.')
                return redirect(f'/update_emp/{emp_id}/')

           
            if Employee.objects.filter(phone_number=phone_number).exclude(id=emp_id).exists():  #check new number is exist?
                messages.error(request, 'This phone number is already in use by another employee.')
                return redirect(f'/update_emp/{emp_id}/')

            emp.first_name = request.POST.get('first_name')
            emp.last_name = request.POST.get('last_name')
            Date_Of_Birth = request.POST.get('Date_Of_Birth')
            emp.Date_Of_Birth = datetime.strptime(Date_Of_Birth, '%Y-%m-%d').date() if Date_Of_Birth else emp.Date_Of_Birth
            emp.email = email
            emp.phone_number = phone_number
            emp.address = request.POST.get('address')

            try:
                emp.save()
                messages.success(request, 'Employee Updated Successfully.')
                return redirect('list_emp')
            except IntegrityError:
                messages.error(request, 'This phone number is already in use. Please use different number.')
                return redirect(f'/update_emp/{emp_id}/')

        elif request.method == 'GET':
            if emp_id:
                emp = get_object_or_404(Employee, id=emp_id)
                context = {
                    'emp': emp
                }
                return render(request, 'update_emp.html', context)
            else:
                emps = Employee.objects.all()
                context = {
                    'emps': emps
                }
                return render(request, 'update_emp_list.html', context)

        else:
            messages.error(request, 'An Exception Occurred! Employee Has Not Been Updated.')
            return redirect('update_emp_list')

    except Http404:
        messages.error(request, 'Employee not found!')
        return redirect('update_emp_list')
    except ValidationError as e:
        messages.error(request, f'Validation Error: {e}')
        return redirect(f'/update_emp/{emp_id}/')
    except Exception as e:
        messages.error(request, f'An Unexpected Error Occurred: {e}')
        return redirect(f'/update_emp/{emp_id}/')

def delete_emp(request, emp_id=0):
    try:
        if request.method == 'POST':
            emp_to_be_removed = get_object_or_404(Employee, id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, 'Employee Removed Successfully.')
            return redirect('list_emp')
        
        elif request.method == 'GET' and emp_id:
            emp = get_object_or_404(Employee, id=emp_id)
            context = {
                'emp': emp
            }
            return render(request, 'confirm_delete.html', context)

        else:
            emps = Employee.objects.all()
            context = {
                'emps': emps
            }
            return render(request, 'delete_emp.html', context)
    
    except Http404:
        messages.error(request, 'Employee not found!')
        return redirect('delete_emp')
    except Exception as e:
        messages.error(request, f'An Unexpected Error Occurred: {e}')
        return redirect('delete_emp')
    
def list_emp(request):
    try:
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'list_emp.html', context)
    except Exception as e:
        messages.error(request, f'An Unexpected Error Occurred: {e}')
        return redirect('index')

def search_emp(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            emps = Employee.objects.all()

            if name:
                emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

            context = {
                'emps': emps
            }
            return render(request, 'list_emp.html', context)

        elif request.method == 'GET':
            return render(request, 'search_emp.html')

        else:
            messages.error(request, 'An Exception Occurred! Unable to search employees.')
            return redirect('search_emp')

    except Exception as e:
        messages.error(request, f'An Unexpected Error Occurred: {e}')
        return redirect('search_emp')