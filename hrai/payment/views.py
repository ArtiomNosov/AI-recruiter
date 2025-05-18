from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Tariff, UserTariff  # Импорт ваших моделей

def payment_page(request):
    return render(request, 'payment/payment.html')


def select_tariff(request):
    tariffs = Tariff.objects.all()
    return render(request, 'payment/select_tariff.html', {'tariffs': tariffs})
def confirm_tariff(request, tariff_slug):
    tariff = get_object_or_404(Tariff, slug=tariff_slug)

    if request.method == "POST":
        # Сохраняем выбор пользователя
        UserTariff.objects.update_or_create(
            user=request.user,
            defaults={
                "tariff": tariff,
                "end_date": timezone.now() + timezone.timedelta(days=tariff.duration_days)
            }
        )
        return redirect("payment_success")  # Перенаправление после успеха

    return render(request, "payment/confirm.html", {"tariff": tariff})