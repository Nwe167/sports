from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "ACLEDA University of Business"
admin.site.site_title = "ACLEDA University of Business Admin Panel"
admin.site.index_title = "ACLEDA University of Business Admin Panel"

admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)

admin.site.register(Category)
admin.site.register(Customer)