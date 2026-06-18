[ODIS Creator Help](odis-creator-help.md) >

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">6. ODIS Creator Order Management Process</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-8-3-status-model.md">Prev</a> </td><th align="center" width="60%"> </th><td align="right" width="20%"> <a accesskey="n" href="6-1-tasks.md">Next</a></td></tr></table>

---

## <a id="prozess.auftragsverwaltung"></a>6. ODIS Creator Order Management Process

The **order management** process contains all [tasks](6-1-tasks.md "6.1. Tasks") that are necessary for defining and managing [orders](6-2-orders.md "6.2. Orders") and for processing **editorial objects** in ODIS Creator.

**Editorial objects** are editorial contents that can be created, changed and deleted. Editorial objects are grouped into order steps. On the other hand, order steps are components of an [order](6-2-orders.md "6.2. Orders").

The creation and deletion of references between editorial objects are managed in an order. If a released editorial object is deleted, this object will be saved in the currently placed order in the table **Deleted release versions**.

The order management also facilitates the automated and user-controlled translation of editorial objects.

The order management process is conducted by the base roles of editing coordinator, author and translation coordinator.

The purpose of order management for the editorial tasks is summarized as follows:

- An order makes it possible for the editing coordinator team or authoring team to understand the scope, the duration and the current status of the editorial tasks.
- An order facilitates the process planning of individual order steps (causal and resource-related dependencies). This will ensure the foundation for a valid resource plan, an efficient operative process management and a valid check of performance growth (monitoring the stage of completion and milestones) in the authoring team.

  It is important to note that in this summary, the scope of a [scheduled order](6-2-1-scheduled-orders.md "6.2.1. Scheduled Orders") in correlation with the new introduction of a model, a model version or an engine is generally still unclear at the time when the editorial process begins.

  In addition to these scheduled tasks, there is a significant portion of the resource usage in the short-term and flexible maintenance, revision and additions to existing editorial objects. Here [Adhoc orders](6-2-2-ad-hoc-orders.md "6.2.2. Ad Hoc Orders") will help to keep the administrative costs at a minimum and then the following order steps can be controlled. It must therefore be ensured that the editorial objects identified and processed during the editing operation are integrated in the order.
- The **editorial objects** are created, verified and translated in different contexts. The order management must therefore support an appropriate grouping in orders and order steps.
- Order management makes deadline monitoring easier for the editing coordinator and the processing authoring teams and informs them automatically when deadlines are missed.
- An order makes it easier for the responsible editing coordinator and the processing authoring teams to determine the current status of the editorial objects. Together with a clear order structure, the order queue and the processed volume can be viewed at any time.

<a id="figure.diadnoseprozess"></a>

![Image: complete process of diagnosis preparation](images/DiagnoseProzess.png)

**Figure 114. Complete Process of Diagnosis Preparation**

The order management process is divided into four main components, that are described in the following.

- Tasks
- Orders
- Translation

<a id="figure.auftragsverwaltung"></a>

![Image: order management](images/Auftragsverwaltung.png)

**Figure 115. Order management**

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-8-3-status-model.md">Prev</a> </td><td align="center" width="20%"> </td><td align="right" width="40%"> <a accesskey="n" href="6-1-tasks.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.8.3. Status Model </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 6.1. Tasks</td></tr></table>
