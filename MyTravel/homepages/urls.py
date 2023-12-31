from django.urls import path 
from .views import indexPageView
from .views import aboutPageView
from .views import empPageView
from .views import searchEmpPageView
from .views import findEmpPageView
from .views import addEmpPageView
from .views import storeEmpPageView
from .views import showCustomersPageView
from .views import showSingleCustomerPageView
from .views import updateCustomersPageView
from .views import deleteCustomerPageView
from .views import addCustomerPageView
from .views import addCustomerDestinationPageView
from .views import addCustDestPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("emp/", empPageView, name="employee"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"), 
    path("addemp/", addEmpPageView, name="addemp"),  
    path("storeemp/", storeEmpPageView, name="storeemp"),
    path("customers/" , showCustomersPageView, name="customers"),
    path("showCustomers/<int:cust_id>/" , showSingleCustomerPageView, name="showSingleCustomer"),
    path("updateCustomers/", updateCustomersPageView, name="updateCust"),
    path("deleteCustomers/<int:cust_id>/", deleteCustomerPageView, name="deleteCustomer"),
    path("addCustomers/", addCustomerPageView, name="addCustomer"),
    path("addCustomerDestination/<int:cust_id>/", addCustomerDestinationPageView, name="addCustomerDestination"),
    path("addCustDest/", addCustDestPageView, name="addCustDest"),


]

