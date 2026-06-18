[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.4. Importing Control Module Descriptions</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-3-3-assignment-of-meta-roles.md">Prev</a> </td><th align="center" width="60%">5. ODIS Creator Administration Process</th><td align="right" width="20%"> <a accesskey="n" href="5-4-1-initiating-the-import-of-control-module-descriptions.md">Next</a></td></tr></table>

---

### <a id="sgbimport"></a>5.4. Importing Control Module Descriptions

The control module descriptions are imported by a location administrator (see [Section 3.3, “Roles and Teams”](3-3-roles-and-teams.md "3.3. Roles and Teams")) in ODIS Creator. The import is done with the reference table (for base control modules) and through an import similar to ODX from the control module extractor. The grouping occurs based on the assigned vehicle projects. Control module objects in ODIS Creator contain all information about jobs, services, parameters, data types, range of values, etc. KWP control modules are generally handled like UDS control modules and contain Logical Links. There are control module descriptions given as XML files for every KWP control module. The base control module descriptions were broken down to the separate control module variants. The structure of KWP control module objects was based on ODX. The names of control modules, jobs, services, parameters are based on ODX for all KWP types, and therefore they are now authored in the English shortened version, for example "EnginContrModul1KWP2000" for the KWP engine control module.

The import of a vehicle project is performed either as a complete import or incremental important, as determined by the metadata in the control module extracts. With incremental imports, the amount to be imported is restricted to the modified control modules compared to the total scope of the vehicle project. This also reduces the update effort in ODIS Creator. There are no abilities to influence this on the part of ODIS Creator.

When importing control modules, the system will check if the control module extracts to be imported contain Cyclone data so that they can be processed appropriately. The Cyclone extracts will be marked with an “Cyclone-INFO.xml” and processed as Cyclone data.

<a id="figure.sgbimport.navigator"></a>

![Control module import view](images/sgbimport.png)

**Figure 65. Control module import view**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-3-3-assignment-of-meta-roles.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-odis-creator-administration-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-4-1-initiating-the-import-of-control-module-descriptions.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.3.3. Assignment of Meta Roles </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.4.1. Initiating the Import of Control Module Descriptions</td></tr></table>
