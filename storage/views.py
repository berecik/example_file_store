from datetime import date
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from .forms import FileModelForm, PasswordForm
from .models import File


def upload_file(request):
    if request.method == 'POST':
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.file_name = request.FILES['file'].name
            if len(form.data['password'].strip()) > 0:
                file_obj.set_password(form.data['password'])
            file_obj.save()
            url = request.build_absolute_uri(reverse('download', args=(file_obj.hash,)))
            return JsonResponse({
                'url': url,
                'filename': file_obj.file_name
            })
        else:
            return JsonResponse({'errors': []})
    else:
        form = FileModelForm(initial={'password': ''})
    return render(request, 'storage/upload.html', {'form': form})


def download_file(request, file_hash):
    file_obj, create = File.objects.get_or_create(hash=file_hash)
    if not create:
        if file_obj.date_to is None or file_obj.date_to < date.today():
            if file_obj.password:
                form = PasswordForm()
                if request.method == 'POST':
                    form = PasswordForm(request.POST)
                    if form.is_valid():
                        password = form.cleaned_data['password']
                        if not file_obj.check_password(password):
                            message = "Wrong password!"
                            return render(request, 'storage/check_password.html', {'form': form, 'message': message})
                else:
                    return render(request, 'storage/check_password.html', {'form': form, 'message': ''})
            if file_obj.file_name:
                filename = file_obj.file_name
            else:
                filename = file_obj.file.name.split('/')[-1]
            response = HttpResponse(file_obj.file, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response

    return Http404()
