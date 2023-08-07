from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import GalleryModelForm
from .models import GalleryModel
from django.core.paginator import Paginator
from django.utils.translation import gettext as _

from django.db.models import Q 

class Homepage(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'main/index.html')





def All_of_pictues(request):
    picture=GalleryModel.objects.all()
    page=Paginator(picture, 4)
    page_number = request.GET.get("page")
    page_obj = page.get_page(page_number)
    return render(request,'main/pictures.html',{'page_obj':(page_obj)})


def Gallery(request):
    form = GalleryModelForm()
    if request.method == 'POST':
        form=GalleryModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
  
        
                            
        
   
    return render(request,'main/gallery.html', {'form':(form)})







def delete_picture(request,pk):
    model_pk=GalleryModel.objects.filter(id=pk).first()
    model_pk.delete()
    return redirect('pi')






