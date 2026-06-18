[ODIS Creator Help](odis-creator-help.md) > [5. ODIS Creator Administration Process](5-odis-creator-administration-process.md) > [5.6. Text Library](5-6-text-library.md)

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">5.6.4. Sorting and Filtering in the Text Library</th></tr><tr><td align="left" width="20%"><a accesskey="p" href="5-6-3-text-id.md">Prev</a> </td><th align="center" width="60%">5.6. Text Library</th><td align="right" width="20%"> <a accesskey="n" href="5-6-5-translation-process-for-text-ids.md">Next</a></td></tr></table>

---

#### <a id="textbib.sortieren"></a>5.6.4. Sorting and Filtering in the Text Library

The entries can be sorted and filtered in the "text library" navigator.

Like at other points in ODIS Creator, you can sort the text library objects alphabetically using the button in the navigator. As default, the objects are sorted alphanumerically in ascending order, and you can sort the objects in descending order by pressing the button.

If you resort the objects, all categories and the text IDs underneath it are always resorted.

The filter in the "text library" navigator functions like at other points, such as the [editor](7-1-5-apply-filter.md "7.1.5. Apply Filter"). There is one filter for categories and one for text IDs in the text library.

Categories can be filtered according to the following attributes: category name in German or English, creator or last editor. The attributes of text IDs are given in the following table:

<a id="table.textbib.filter"></a>

<table border="1" summary="Filter Attributes of Text IDs"><colgroup><col align="left"/><col align="left"/><col align="left"/></colgroup><thead><tr bgcolor="#EEEEEE"><th align="left">Attribute</th><th align="left">Permitted operation</th><th align="left">Value input</th></tr></thead><tbody valign="top"><tr><td align="left" valign="top">Text ID</td><td align="left" valign="top">=; LIKE; &lt;&gt;</td><td align="left" valign="top">Free text</td></tr><tr><td align="left" valign="top">Version</td><td align="left" valign="top">=; LIKE; &lt;&gt;</td><td align="left" valign="top">Free text</td></tr><tr><td align="left" valign="top">Status</td><td align="left" valign="top">=; &lt;&gt;</td><td align="left" valign="top">
<p>Selection from range of values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>In processing</p>
</li><li>
<p>Being completed</p>
</li><li>
<p>Confirmed completed</p>
</li><li>
<p>Released</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left" valign="top">Status date</td><td align="left" valign="top">=; &lt;&gt;; &gt;=; &gt;; &lt;=; &lt;</td><td align="left" valign="top">Dialog for date input</td></tr><tr><td align="left" valign="top">Approval date</td><td align="left" valign="top">=; &lt;&gt;; &gt;=; &gt;; &lt;=; &lt;</td><td align="left" valign="top">Dialog for date input</td></tr><tr><td align="left" valign="top">Translation status</td><td align="left" valign="top">=; &lt;&gt;</td><td align="left" valign="top">
<p>Selection from range of values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>&lt;empty&gt;</p>
</li><li>
<p>Not translated</p>
</li><li>
<p>Ready for translation</p>
</li><li>
<p>Complete</p>
</li></ul></div><p>
</p>
</td></tr><tr><td align="left" valign="top">Creator</td><td align="left" valign="top">=; LIKE; &lt;&gt;</td><td align="left" valign="top">Free text</td></tr><tr><td align="left" valign="top">Last editor</td><td align="left" valign="top">=; LIKE; &lt;&gt;</td><td align="left" valign="top">Free text</td></tr><tr><td align="left" valign="top">Consistency</td><td align="left" valign="top">=; &lt;&gt;</td><td align="left" valign="top">
<p>Selection from range of values:</p>
<p>
</p><div class="itemizedlist"><ul type="disc"><li>
<p>Canceled</p>
</li><li>
<p>Unchecked</p>
</li><li>
<p>In testing</p>
</li><li>
<p>Note</p>
</li><li>
<p>Warning</p>
</li><li>
<p>Error</p>
</li><li>
<p>Consistent</p>
</li></ul></div><p>
</p>
</td></tr></tbody></table>

**Table 28. Filter Attributes of Text IDs**

##### <a id="textbib.tabellen.filtern"></a>5.6.4.1. Filter Tables

It is possible to filter the column contents for the following tables.

- Overview of text IDs from this category
- Text formatting overview
- Overview of usage locations/editing view
- Overview of usage locations/function test editor

<a id="figure.admin.textbib.filtern"></a>

![Filters in the Usage Locations](images/textbib_Verwendung_filtern.png)

**Figure 102. Filters in the Usage Locations**

In [Figure 102, “Filters in the Usage Locations”](5-6-4-sorting-and-filtering-in-the-text-library.md#figure.admin.textbib.filtern "Figure 102. Filters in the Usage Locations"), a column filter for supplemental documents is given in the upper section and column 7 is in the lower section. The known filter label from ODIS Creator is given at the column.

To be able to set a column filter, you must select the header of the column to be filtered in the **filter** context menu. All column contents are listed in the open dialog. Duplicate entries in the column are already combined into one entry, disregarding capitalized and lower case letters.

There are two available options to filter the column content. For one, you can hide the content that should not be displayed be removing the check mark. For the other, you can limit the content with the search term. Note that the entered search term will be searched for exactly as is. For example, if searching for "following component", it will not show any entry with a word between "following" and "component".

The auto filter offers the option to remove an already existing filter again. When entering a search term for this, the currently selected filter quantity are marked and hidden. While a search term is entered, a temporary list is displayed which results from the search term. Two entries are also placed at the beginning of the results list.

- **Select all search results:** This corresponds to "Select all" in the unfiltered results list.
- **Add the current selection to the filter:** With this item, you can add the temporary filter list currently selected in the view, or the existing filter list that existed before entering the search term.

The filter is set after confirming the dialog. There is no results preview in the table.

It is likewise possible to filter multiple columns. The filter will be marked individually for each column. The entries which satisfy both filters will be the result.

A set column filter can be removed again via the context menu on the column header with **Delete filter**.

---

<table summary="Navigation footer" width="100%"><tr><td align="left" width="40%"><a accesskey="p" href="5-6-3-text-id.md">Prev</a> </td><td align="center" width="20%"><a accesskey="u" href="5-6-text-library.md">Up</a></td><td align="right" width="40%"> <a accesskey="n" href="5-6-5-translation-process-for-text-ids.md">Next</a></td></tr><tr><td align="left" valign="top" width="40%">5.6.3. Text ID </td><td align="center" width="20%"><a accesskey="h" href="odis-creator-help.md">Home</a></td><td align="right" valign="top" width="40%"> 5.6.5. Translation Process for Text IDs</td></tr></table>
