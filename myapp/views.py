from django.shortcuts import render, redirect
from .forms import*
from .models import*

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def gallery(request):
    packages = Package.objects.all()
    return render(request, 'gallery.html', {'packages': packages})

def detailGallery(request, id):
    packageSlideImage = PackageSlideImage.objects.filter(package = id)
    package = Package.objects.get(id = id)
    context = {
        'package': package,
        'packageSlideImage': packageSlideImage,
    }
    return render(request, 'detail.html', context)

def home(request):
    packages = Package.objects.all()
    return render(request, 'index.html', {'packages': packages})

def book(request, id):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AnonymousBookingForm()
            form.instance.package = Package.objects.get(id = id)
            if form.is_valid():
                form.save()
                return redirect('/booked-tour/')
        else:
            form = AnonymousBookingForm()
    else:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            form.instance.package = Package.objects.get(id = id)
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                return redirect('/booked-tour/')
        else:
            form = BookingForm()
    return render(request, 'book.html', {'form': form})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        packages = Package.objects.filter(placeName__contains = search)
        return render(request, 'search.html', {'search': search, 'packages': packages})
    return render(request, 'search.html')

def bookedTour(request):
    tours = Booking.objects.filter(user = request.user)
    return render(request, 'bookedTour.html', {'tours': tours})