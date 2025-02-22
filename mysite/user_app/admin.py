from django.contrib import admin
from .models import Profile, Profit, Proxies, TradeResult


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_register', 'subscription_status', 'wallet_address', 'api_key', 'api_secret',
                    'bybit_user_id',
                    'email', 'mailing']
    verbose_name = 'профили'


class ProfitsAdmin(admin.ModelAdmin):
    list_display = ['user', 'day', 'month', 'year', 'sum_paid']
    verbose_name = 'профиты'


class ProxiesAdmin(admin.ModelAdmin):
    list_display = ['proxy']
    verbose_name = 'прокси'


class TradeResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'result', 'wallet_balance_morning']
    verbose_name = 'результаты торговли'


# Register your models here.
admin.site.register(Profile, ProfilesAdmin)
admin.site.register(Profit, ProfitsAdmin)
admin.site.register(Proxies, ProxiesAdmin)
admin.site.register(TradeResult, TradeResultAdmin)
