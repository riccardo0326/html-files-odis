[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.1. Define Translation Parameters</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-translation.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-2-filtering-translations.md">Next</a></td></tr></table>

---

#### <a id="uebersetzungsparameter.definieren"></a>6.4.1. Define Translation Parameters

Translation coordinators can define the translation parameters for translators at their facilities. To do this, click on the **Insert** and **Define translation parameters** [buttons](2-2-general-definitions-and-glossaries.md#schaltflaeche) in the [menu bar](2-2-general-definitions-and-glossaries.md#menuleiste). The editor will open [Figure 149, “Translation Parameter Editor”](6-4-1-define-translation-parameters.md#figure.auftragsverwaltung.uebersetzung.konfig "Figure 149. Translation Parameter Editor"). The display can be used to configure after how many days a returned translation package from the translation should be deleted from the system. This is to obtain the overview in the translation navigator. The default value is 7 days.

The following mandatory fields/mandatory information can be defined for the DELS system:

- **Email address:** required for comparison with customer data in DELS. The email address must match the customer data in DELS.
- **Customer name:** required for comparison with the customer data in DELS. Customer name must match the customer data in DELS.
- **Department:** defines the department of the person whose email is specified in the email address field.
- **Cost type:** corresponds to the account assignment in GoCAT.
- **Cost center:** defines the cost center to be charged.

The Email address and Customer name fields cannot be left blank. The translation coordinator must complete at least one of the two fields.

In the language settings table, the translation coordinators can define the translation parameters for each language for automatic translation orders to their facilities. The columns have the following meaning:

- **Target language:** here is the code for the target language. This column cannot be edited.
- **Number (editing content):** maximum amount of content files per translation package during an automatic export before the editorial deadline. If more requirements exist, two are more packages will be created. As long as the editorial deadline has not been reached, requirements that exceed the limit are left undone and no new package with this limit is generated.
- **Number (editing text):** maximum amount of individual texts (such as display name) per object type per translation package during an automatic export before the editorial deadline. If more requirements exist, two are more packages will be created. As long as the editorial deadline has not been reached, requirements that exceed the limit are left undone and no new package with this limit is generated.
- **Translation period [d]:** number of days allotted for translation. The default value is 2 days.
- **Warning time [t]:** number of days that can give a green mark in the translation navigator before the translation package is due for delivery. This should make it possible for the translation coordinator to see which translation packages are to be delivered in the coming days. The default value is 2 days.
- **Min. amount (admin.) (Wolfsburg only):** minimum number of administrative objects that must be available to create an automatic translation package. The default value is three administrative objects.
- **Maximum (admin. text) (Wolfsburg only):** maximum number of administrative objects per translation package when exporting automatically. The default value is 10,000 administrative objects. If more requirements exist, two are more packages will be created.
- **Translation time (admin.) [d] (Wolfsburg only):** number of days planned for the translation of administrative objects.

Specifically at the Wolfsburg location, the system administrative texts are also translated (such as the default texts). For this reason, there are four additional columns here in the translation parameters (“duration (admin.)”, “min amount (admin.)” and “max (admin. text)” and “Translation duration (admin.)”). Similar to the editorial objects, the settings for administrative objects can be defined with this.

<a id="figure.auftragsverwaltung.uebersetzung.konfig"></a>

![Image: translation parameter editor](images/uebersetzung-konfiguration.png)

**Figure 149. Translation Parameter Editor**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-translation.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-2-filtering-translations.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4. Translation </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.2. Filtering Translations</td></tr></table>
