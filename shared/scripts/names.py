# encoding: UTF-8

from objectmaphelper import *

address_Book_Activity = {"text": "Address Book", "type": "Activity", "visible": True}
address_Book_Add_Address_Button = {"container": address_Book_Activity, "resourceName": "addAddressButton", "text": "Add Address", "type": "Button", "visible": True}
edit_Address_Activity = {"text": "Edit Address", "type": "Activity", "visible": True}
edit_Address_Forename_Text = {"container": edit_Address_Activity, "text": "Forename", "type": "Text", "visible": True}
edit_Address_Forename_Edit = {"aboveObject": edit_Address_Forename_Text, "container": edit_Address_Activity, "resourceName": "foreNameEditText", "type": "Edit", "visible": True}
edit_Address_Surname_Text = {"container": edit_Address_Activity, "text": "Surname", "type": "Text", "visible": True}
edit_Address_Surname_Edit = {"aboveObject": edit_Address_Surname_Text, "container": edit_Address_Activity, "resourceName": "surNameEditText", "type": "Edit", "visible": True}
edit_Address_Phone_Text = {"container": edit_Address_Activity, "text": "Phone", "type": "Text", "visible": True}
edit_Address_Phone_Edit = {"aboveObject": edit_Address_Phone_Text, "container": edit_Address_Activity, "resourceName": "phoneEdit", "type": "Edit", "visible": True}
edit_Address_Email_Text = {"container": edit_Address_Activity, "text": "Email", "type": "Text", "visible": True}
edit_Address_Email_Edit = {"aboveObject": edit_Address_Email_Text, "container": edit_Address_Activity, "resourceName": "emailEdit", "type": "Edit", "visible": True}
edit_Address_Save_Button = {"container": edit_Address_Activity, "resourceName": "addressSaveButton", "text": "Save", "type": "Button", "visible": True}
address_Book_addressList_List = {"container": address_Book_Activity, "resourceName": "addressList", "type": "List", "visible": True}
addressList_Gharagyozyan_Text = {"container": address_Book_addressList_List, "resourceName": "surNameEditText", "text": "Gharagyozyan", "type": "Text", "visible": True}
addressList_Tukhik_Text = {"container": address_Book_addressList_List, "resourceName": "foreNameEditText", "text": "Tukhik", "type": "Text", "visible": True}
addressList_Ani_Text = {"container": address_Book_addressList_List, "resourceName": "foreNameEditText", "text": "Ani", "type": "Text", "visible": True}
