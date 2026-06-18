[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.4. Equipment Network](7-4-equipment-network.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4.6. Vehicle Recognition in Equipment Network</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-4-5-exclusion-list.md">Prev</a> </td><th align="center" width="60%">7.4. Equipment Network</th><td align="right" width="20%"> <a accesskey="n" href="7-4-7-country-sessions-in-the-equipment-network.md">Next</a></td></tr></table>

---

#### <a id="ausstattungsnetz.fahrzeugerkennung"></a>7.4.6. Vehicle Recognition in Equipment Network

To optimize the vehicle recognition in the equipment network<a id="d4e11587"></a>on ODIS Service, other information about vehicle model, model code and model year can be managed. Content for the information are retrieved for each brand from the VPT list and made available through selection lists. The desired model names are specified on the vehicle model node (see [Figure 238, “Vehicle Recognition - Model Name”](7-4-6-vehicle-recognition-in-equipment-network.md#figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modellbezeichnung "Figure 238. Vehicle Recognition - Model Name"))<a id="d4e11590"></a>.

<a id="figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modellbezeichnung"></a>

![Image: vehicle recognition - model name](images/modellkennung.png)

**Figure 238. Vehicle Recognition - Model Name**

At the model year node, the model years<a id="d4e11602"></a>and the vehicle project<a id="d4e11605"></a>are selected. The available model years (see [Figure 239, “Vehicle Recognition by Model Year”](7-4-6-vehicle-recognition-in-equipment-network.md#figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modelljahr "Figure 239. Vehicle Recognition by Model Year")) depend on the selected model identifiers in the vehicle model node. The vehicle project depends on the selected identifier and the selected model year. The specification of the vehicle project is obligatory.

<a id="figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modelljahr"></a>

![Image: vehicle recognition by model year](images/modelljahr_fzgprojekt.png)

**Figure 239. Vehicle Recognition by Model Year**

If the **default** entry is selected at the model year ID<a id="d4e11619"></a>(see [Figure 240, “Vehicle Recognition by Model Year - Default”](7-4-6-vehicle-recognition-in-equipment-network.md#figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modelljahr.default "Figure 240. Vehicle Recognition by Model Year - Default")), all vehicle projects of the previously selected model ID are available.

<a id="figure.redaktion.ausstattungsnetz.fahrzeugerkennung.modelljahr.default"></a>

![Image: vehicle recognition by model year - default](images/modelljahr_fzgprojekt_default.png)

**Figure 240. Vehicle Recognition by Model Year - Default**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-4-5-exclusion-list.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-4-equipment-network.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-7-country-sessions-in-the-equipment-network.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.4.5. Exclusion List </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.7. Country Sessions in the Equipment Network</td></tr></table>
