[ODIS Creator Help](odis-creator-help.md) > [6. ODIS Creator Order Management Process](6-odis-creator-order-management-process.md) > [6.4. Translation](6-4-translation.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6.4.2. Filtering Translations</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="6-4-1-define-translation-parameters.md">Prev</a> </td><th align="center" width="60%">6.4. Translation</th><td align="right" width="20%"> <a accesskey="n" href="6-4-3-sorting-translations.md">Next</a></td></tr></table>

---

#### <a id="uebersetzung.filter"></a>6.4.2. Filtering Translations

ODIS Creator can be filtered according to translations in the translation view. This will differentiate if it should be filtered according to translation requirements or translations packages.

<a id="table.hinweis.uebersetzung.filter"></a>

<table border="1" summary="Note for Translation Filter"><colgroup><col align="center"/><col align="left"/></colgroup><tbody valign="top"><tr><td align="center" valign="top"><span class="inlinemediaobject"><img alt="Note symbol" src="images/info.png"/></span></td><td align="left" valign="top"><span class="bold"><strong>Information:</strong></span> The filters from old versions are no longer available in the ODIS Creator 6.1.0 version. Due to the enhancements, the old filter format no longer exists.</td></tr></tbody></table>

**Table 34. Note for Translation Filter**

<a id="figure.auftragsverwaltung.uebersetzung.nav"></a>

![Image: translation navigator with buttons](images/uebersetzung_nav.jpg)

**Figure 150. Translation Navigator with Buttons**

There is a filter dialog for this in which it can be filtered according to translation requirement attributes at the top and can be filtered according to translation package attributes at the bottom (see [Figure 151, “Filter Dialog for Translation Objects”](6-4-2-filtering-translations.md#figure.auftragsverwaltung.uebersetzung.filter "Figure 151. Filter Dialog for Translation Objects")). This dialog can be started through the **View >> Translation object filter...** menu or with th button (1) in the translation navigator (see [Figure 150, “Translation Navigator with Buttons”](6-4-2-filtering-translations.md#figure.auftragsverwaltung.uebersetzung.nav "Figure 150. Translation Navigator with Buttons")).

<a id="figure.auftragsverwaltung.uebersetzung.filter"></a>

![Image: filter dialog for translation objects](images/uebersetzung-filter.jpg)

**Figure 151. Filter Dialog for Translation Objects**

You can select one of the following display levels first.

- **Location level:** this corresponds to the display filtered by location. It may be, that no difference is displayed if you are the assigned translation coordinator for a team for multiple locations.
- **Language level:** The target language node is displayed directly under the roof node (requirements or packages). This corresponds to the display if you are the assigned translation coordinator for a team for only one location.
- **Package level:** The translation packages will be displayed directly under the root node (translation packages).
- **Requirement level:** The date folder will be displayed directly under the root node (translation requirements). There is no mixture of requirements in relation to the locations and the target languages for a date folder.

The attributes which can be filtered are listed in the following. Various attributes are possible depending on the selected area in the filter dialog.

For translation requirements, the filter for object names also affects the elements displayed in the editor in addition to affecting the display of objects in the tree.

The following attributes can be set for the translation requirements:

- Location
- Source language
- Target language
- Initial deployment deadline
- Object name
- Market name

The filter based on the object names for translation packages only has effects on the display in the tree. The displayed content in the editor for translation packages is not changed by this.

You can set the following attributes for translation packages:

- Location
- Source language
- Target language
- Package creation date
- Package target date (scheduled end)
- Package number
- Package status
- Package import date
- Object name
- Market name

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="6-4-1-define-translation-parameters.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="6-4-translation.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="6-4-3-sorting-translations.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">6.4.1. Define Translation Parameters </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.4.3. Sorting Translations</td></tr></table>
