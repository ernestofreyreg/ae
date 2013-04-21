from django.contrib import admin
from air.models import Country, Airline, Airport, State, City, Airplane, Flight


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    ordering = ('name',)
    search_fields = ('name','symbol')

admin.site.register(Country, CountryAdmin)

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    ordering = ('name',)
    search_fields = ('name','country__name')

admin.site.register(Airline, AirlineAdmin)

class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'city', 'lat', 'lng')
    ordering = ('name',)
    search_fields = ('name','symbol', 'city__name')

admin.site.register(Airport, AirportAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    ordering = ('name',)
    search_fields = ('name','country__name')

admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    ordering = ('name',)
    search_fields = ('name','stat__name')

admin.site.register(City, CityAdmin)

class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'passengers','fuelcapacity','fuelconsumption')
    ordering = ('brand','model')
    search_fields = ('brand','model')

admin.site.register(Airplane, AirplaneAdmin)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('name_day', 'airline', 'day', 'origin', 'destination', 'departure', 'arrival', 'airplane')
    ordering = ('airline', 'name', 'day')
    search_fields = ('name','airline__name')
    list_filter = ('origin','destination','airline','airplane','day')

admin.site.register(Flight, FlightAdmin)
