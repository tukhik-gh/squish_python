# -*- coding: utf-8 -*-

import names


def main():
    startApplication("com.froglogic.addressbook")
    tapObject(waitForObject(names.address_Book_Add_Address_Button), 526, 72)
    tapObject(waitForObject(names.edit_Address_Forename_Edit), 217, 43)
    type(waitForObject(names.edit_Address_Forename_Edit, 20000), "Ani")
    tapObject(waitForObject(names.edit_Address_Surname_Edit), 234, 52)
    type(waitForObject(names.edit_Address_Surname_Edit), "Gevorgyan")
    tapObject(waitForObject(names.edit_Address_Email_Edit), 263, 54)
    type(waitForObject(names.edit_Address_Email_Edit), "maymay@mail.com")
    tapObject(waitForObject(names.edit_Address_Save_Button), 146, 78)
    test.compare(waitForObjectExists(names.addressList_Ani_Text).text, "Ani")
    test.compare(waitForObjectExists(names.addressList_Ani_Text).enabled, True)
