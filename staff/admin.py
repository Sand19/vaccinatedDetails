from django.contrib import admin
import csv
from django.http import HttpResponse

# Register your models here.
from staff.models import vaccineDetails 
# Register your models here.
class userRAdmin(admin.ModelAdmin):
    list_display = ("staff_name", "staff_no", "dp_code","branch_name")
    list_filter = ("ro_code", "circle_name","vaccinated")
    search_fields = ("staff_name__startswith", )
    list_per_page = 20
    actions = ["export_as_csv"]

    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment; filename={}.csv'.format(meta)
        #total = projects.count()
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj,field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected in Excel"

admin.site.register(vaccineDetails, userRAdmin)