[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4. Equipment Network</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-3-4-search-results.md">Prev</a> </td><th align="center" width="60%">7. ODIS Creator Editing Process</th><td align="right" width="20%"> <a accesskey="n" href="7-4-1-create-new-brand.md">Next</a></td></tr></table>

---

### <a id="ausstattungsnetz"></a>7.4. Equipment Network

Equipment characteristics for the vehicle models are described for the individual brands in the equipment network. The navigator permits the access to the features that are structured in a hierarchical tree. Within the navigator tree, you can access information on the individual levels. Depending on the level selection, the assigned selection options in the context or selection menu will change. ODIS Creator assists you in the allocation by checking at which locations new objects are permitted and the corresponding commands are also only then offered.

Each equipment network object can be labeled as **internal**<a id="d4e11283"></a>. This label regulates the visibility on the interface of the processing system. As **internally** labeled objects, they are also prepared as the other objects, however they are not displayed in the processing system.

The additional attributes are described for the individual object types. To identify equipment characteristics that actually exist in a real vehicle, a traversal test can be assigned to an equipment characteristic (see [Section 7.4.11, “Create Traversal Test”](7-4-11-create-traversal-test.md "7.4.11. Create Traversal Test")).

<a id="figure.ausstattungsnetz"></a>

![Image: navigator tree for equipment network](images/ausstattungsnetz.png)

**Figure 232. Navigator Tree for Equipment Network**

The structure tree hierarchy is structured as follows:

- Brand<a id="d4e11302"></a>

  - Vehicle type<a id="d4e11308"></a>

    - Model year<a id="d4e11314"></a>

      - Version<a id="d4e11320"></a>

        - Motor<a id="d4e11326"></a>

          - XOR Nodes<a id="d4e11332"></a>

            - Control Module Configuration<a id="d4e11338"></a>
            - Equipment without diagnostic interface<a id="d4e11343"></a>
          - Control Module Configuration
          - Equipment without diagnostic interface
      - Engine code nodes<a id="d4e11352"></a>

        - Motor<a id="d4e11358"></a>

          - XOR Nodes<a id="d4e11364"></a>

            - Control Module Configuration<a id="d4e11370"></a>
            - Equipment without diagnostic interface<a id="d4e11375"></a>
          - Control Module Configuration
          - Equipment without diagnostic interface
      - Engine default nodes<a id="d4e11384"></a>

        - Motor<a id="d4e11390"></a>

          - XOR Nodes<a id="d4e11396"></a>

            - Control Module Configuration<a id="d4e11402"></a>
            - Equipment without diagnostic interface<a id="d4e11407"></a>
          - Control Module Configuration
          - Equipment without diagnostic interface

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-3-4-search-results.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-odis-creator-editing-process.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-1-create-new-brand.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.3.4. Search Results </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.1. Create New Brand</td></tr></table>
