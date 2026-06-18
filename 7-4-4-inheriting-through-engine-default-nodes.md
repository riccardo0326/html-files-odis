[ODIS Creator Help](odis-creator-help.md) > [7. ODIS Creator Editing Process](7-odis-creator-editing-process.md) > [7.4. Equipment Network](7-4-equipment-network.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">7.4.4. Inheriting through Engine Default Nodes</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="7-4-3-inheriting-through-engine-code-nodes.md">Prev</a> </td><th align="center" width="60%">7.4. Equipment Network</th><td align="right" width="20%"> <a accesskey="n" href="7-4-5-exclusion-list.md">Next</a></td></tr></table>

---

#### <a id="ausstattungsnetz.mdk"></a>7.4.4. Inheriting through Engine Default Nodes

To optimize editing processes, an additional structure node called an engine default node can be added below a model year. The engine default nodes are not prepared. The object structure created under the engine default nodes is inherited completely from parallel versions that do not contain their own object structure. The inheriting takes places at the time of preparation. The engine default node inherits the market applicability from the model year above it.

Only one engine default node can be created per model year. When creating a new engine default node, if there is already one for that model year in the recycle bin, the nodes in the recycle bin will be permanently deleted. However, you can restore the nodes in the recycle bin.

All child objects are inherited (engine, traversal test, and auxiliary document). The inheriting mechanism only includes the variants that do not have their own object structure. For example, if a variant has a “traversal test” child node, then it will not inherit the child objects from a parallel engine default node. If the engine default node is not present or does not have any children, the engine code node will be inherited.

<a id="figure.redaktion.ausstattungsnetz.mdk"></a>

![Illustration: model year with engine default nodes](images/ausstattungsnetz_mdk.png)

**Figure 236. Model Year with Engine Default Nodes**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="7-4-3-inheriting-through-engine-code-nodes.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="7-4-equipment-network.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="7-4-5-exclusion-list.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">7.4.3. Inheriting through Engine Code Nodes </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 7.4.5. Exclusion List</td></tr></table>
