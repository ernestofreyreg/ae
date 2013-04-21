from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        self.symbol = self.symbol.upper()
        super(Country, self).save(force_insert, force_update, using)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.symbol)

class Airline(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name = "Airline"
        verbose_name_plural = "Airlines"

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        super(Airline, self).save(force_insert, force_update, using)

    def __unicode__(self):
        return "%s (%s)"%(self.name, self.country.symbol)

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        super(State, self).save(force_insert, force_update, using)

    def __unicode__(self):
        return "%s (%s)"%(self.name, self.country.name)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        super(City, self).save(force_insert, force_update, using)

    def __unicode__(self):
        return "%s (%s)"%(self.name, self.state.name)

class Airport(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    city = models.ForeignKey(City)
    lat = models.FloatField()
    lng = models.FloatField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Airport"
        verbose_name_plural = "Airports"

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        self.symbol = self.symbol.upper()
        super(Airport,self).save(force_insert, force_update, using)

    def __unicode__(self):
        return "%s"%(self.symbol)

class Airplane(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    passengers = models.IntegerField(default=0, blank=True)
    fuelcapacity = models.FloatField(default=0, blank=True)
    fuelconsumption = models.FloatField(default=0, blank=True)

    class Meta:
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"

    def __unicode__(self):
        return "%s %s"%(self.brand, self.model)

    def save(self, force_insert=False, force_update=False, using=None):
        self.brand = self.brand.upper()
        self.model = self.model.upper()
        super(Airplane,self).save(force_insert, force_update, using)




DAY_OF_WEEK = (
    (1, 'MONDAY'),
    (2, 'TUESDAY'),
    (3, 'WEDNESDAY'),
    (4, 'THURSDAY'),
    (5, 'FRIDAY'),
    (6, 'SATURDAY'),
    (7, 'SUNDAY')
)

DAYS_ABREV = ['Mon','Tue','Wed','Thu','Fri', 'Sat', 'Sun']

class Flight(models.Model):
    name = models.CharField(max_length=20)
    airline = models.ForeignKey(Airline)
    day = models.IntegerField(choices=DAY_OF_WEEK)
    origin = models.ForeignKey(Airport, related_name="origin")
    destination = models.ForeignKey(Airport, related_name='destination')
    departure = models.TimeField()
    arrival = models.TimeField()
    airplane = models.ForeignKey(Airplane)

    def arrival_minutes(self):
        return self.arrival.hour*60 + self.arrival.minute

    def departure_minutes(self):
        return self.departure.hour*60 + self.departure.minute

    def duration(self):
        return self.arrival_minutes() - self.departure_minutes()

    def name_day(self):
        return "%s %s"%(self.name, DAYS_ABREV[self.day-1])

    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"

    def __unicode__(self):
        return "%s %s"%(self.airline.name,self.name)

    def save(self, force_insert=False, force_update=False, using=None):
        self.name = self.name.upper()
        super(Flight,self).save(force_insert, force_update, using)




