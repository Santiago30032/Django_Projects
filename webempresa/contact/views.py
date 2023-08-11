from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('mensaje','')
            #Enviamos correo y redireccionamos
            email = EmailMessage(
                'La Caffetiera: Nuevo Mensaje de contaco', 
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ["santiago30032@gmail.com"],
                reply_to=[email]
            )
            try: 
                email.send()
                #todo salio bien
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo fallo
                return redirect(reverse('contact')+'?fail')
    return render(request,"contact/contact.html",{'form':contact_form})
