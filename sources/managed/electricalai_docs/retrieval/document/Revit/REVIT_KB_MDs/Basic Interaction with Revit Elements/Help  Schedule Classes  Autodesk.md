---
created: 2026-01-28T20:52:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_Schedule_Classes_html
author: 
---

# Help | Schedule Classes | Autodesk

> ## Excerpt
> Schedule views use several supporting classes.

---
Schedule views use several supporting classes.

TableView is a class that represents a view that shows a table and it is the base class for ViewSchedule and PanelScheduleView. It has an associated TableData class which contains one or more sections. For ViewSchedule, there is only one header and one body section.

The TableSectionData class represents a contiguous set of cells arranged in rows and columns. For a ViewSchedule the cell contents of TableSectionData are generated from the ScheduleDefinition and parameters. Also, for ViewSchedules, while the header section has read/write permissions, the body section is read-only.

### Working with data in a schedule

The actual data for a table is contained in the TableData class. Although the TableData object cannot be obtained directly from the TableView class, both child classes have a GetTableData() method. For ViewSchedule, this method returns a TableData object. For a PanelScheduleView, GetTableData() returns a PanelScheduleData object, which derives from the TableData base class. The TableData class holds most of the data that describe the style of the rows, columns, and cells in a table. PanelScheduleData provides additional methods related specifically to panel schedules.

### Working with rows, columns and cells

Data in a table is broken down into sections. To work with the rows, columns and cells of the TableData, it is necessary to get the a TableSectionData object. TableData.GetSectionData() can be called with either an integer to the requested section data, or using the SectionType (i.e. Header or Body).

The TableSectionData class can be used to insert or remove rows or columns, format cells, and to get details of the cells that make up that section of the schedule, such as the cell type (i.e. Text or Graphic) or the cell's category id.

In the following example, a new row is added to the header section of the schedule and the text is set for the newly created cell. Note that the first row of the header section defaults to the title when created with the UI.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_EF29114353B64BFAAB5705A9B97E50F6"><tbody><tr><td><b>Code Region: Inserting a row</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateSubtitle</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>TableData</span><span> colTableData </span><span>=</span><span> schedule</span><span>.</span><span>GetTableData</span><span>();</span><span>

    </span><span>TableSectionData</span><span> tsd </span><span>=</span><span> colTableData</span><span>.</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>
    tsd</span><span>.</span><span>InsertRow</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>);</span><span>
    tsd</span><span>.</span><span>SetCellText</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> </span><span>"Schedule of column top and base levels with offsets"</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Also note, in the code example above, it uses the properties FirstRowNumber and FirstColumnNumber. In some sections the row or column numbers might start with 0, or they might start with 1. These properties should always be used in place of a hardcoded 0 or 1.

In the following example, a new single-category schedule is created with a custom header section.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_DF3F34074A0444F58E0D14AD9E616839"><tbody><tr><td><b>Code Region: Customizing the header section</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategoryScheduleWithSimpleHeaderSection</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category with custom headers"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Build schedule</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_MARK</span><span>));</span><span>
        </span><span>AddRegularFieldToSchedule</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_COST</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Get header section</span><span>
        </span><span>TableSectionData</span><span> data </span><span>=</span><span> vs</span><span>.</span><span>GetTableData</span><span>().</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>

        </span><span>int</span><span> rowNumber </span><span>=</span><span> data</span><span>.</span><span>LastRowNumber</span><span>;</span><span>
        </span><span>int</span><span> columnNumber </span><span>=</span><span> data</span><span>.</span><span>LastColumnNumber</span><span>;</span><span>

        </span><span>// Get the overall width of the table so that the new columns can be resized properly</span><span>
        </span><span>double</span><span> tableWidth </span><span>=</span><span> data</span><span>.</span><span>GetColumnWidth</span><span>(</span><span>columnNumber</span><span>);</span><span>

        data</span><span>.</span><span>InsertColumn</span><span>(</span><span>columnNumber</span><span>);</span><span>
        data</span><span>.</span><span>InsertColumn</span><span>(</span><span>columnNumber</span><span>);</span><span>

        </span><span>// Refresh data to be sure that schedule is ready for text insertion</span><span>
        vs</span><span>.</span><span>RefreshData</span><span>();</span><span>

        </span><span>//Set text to the first header cell</span><span>
        data</span><span>.</span><span>SetCellText</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> </span><span>"Special Window Schedule Text"</span><span>);</span><span>

        </span><span>// Set width of first column</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        </span><span>//Set a different parameter to the second cell - the project name</span><span>
        data</span><span>.</span><span>SetCellParamIdAndCategoryId</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>PROJECT_NAME</span><span>),</span><span>
                                            </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_ProjectInformation</span><span>));</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>FirstColumnNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        </span><span>//Set the third column as the schedule view name - use the special category for schedule parameters for this</span><span>
        data</span><span>.</span><span>SetCellParamIdAndCategoryId</span><span>(</span><span>rowNumber</span><span>,</span><span> data</span><span>.</span><span>LastColumnNumber</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>VIEW_NAME</span><span>),</span><span>
                                            </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_ScheduleViewParamGroup</span><span>));</span><span>
        data</span><span>.</span><span>SetColumnWidth</span><span>(</span><span>data</span><span>.</span><span>LastColumnNumber</span><span>,</span><span> tableWidth </span><span>/</span><span> </span><span>3.0</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularFieldToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>// Find a matching SchedulableField</span><span>
    </span><span>SchedulableField</span><span> schedulableField </span><span>=</span><span>
        definition</span><span>.</span><span>GetSchedulableFields</span><span>().</span><span>FirstOrDefault</span><span>&lt;</span><span>SchedulableField</span><span>&gt;(</span><span>sf </span><span>=&gt;</span><span> sf</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>schedulableField </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Add the found field</span><span>
        definition</span><span>.</span><span>AddField</span><span>(</span><span>schedulableField</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The style of rows, columns, or individual cells can be customized for schedules. This includes the ability to set the border line style for all four sides of cells, as well as cell color and text appearance (i.e. color, font, size). For regular schedules, this can only be done in the header section of the table.

In the example below, the font of the subtitle of a ViewSchedule (assumed to be the second row of the header section) is set to bold and the font size is set to 10.

<table summary="" id="GUID-76A3927E-6DA6-495F-A89C-00F760E3702C__TABLE_EA627D36449B46249B78B567B38A93B6"><tbody><tr><td><b>Code Region: Formatting cells</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FormatSubtitle</span><span>(</span><span>ViewSchedule</span><span> colSchedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>TableData</span><span> colTableData </span><span>=</span><span> colSchedule</span><span>.</span><span>GetTableData</span><span>();</span><span>

    </span><span>TableSectionData</span><span> tsd </span><span>=</span><span> colTableData</span><span>.</span><span>GetSectionData</span><span>(</span><span>SectionType</span><span>.</span><span>Header</span><span>);</span><span>
    </span><span>// Subtitle is second row, first column</span><span>
    </span><span>if</span><span> </span><span>(</span><span>tsd</span><span>.</span><span>AllowOverrideCellStyle</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>TableCellStyle</span><span> tcs </span><span>=</span><span> </span><span>new</span><span> </span><span>TableCellStyle</span><span>();</span><span>
        </span><span>TableCellStyleOverrideOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>TableCellStyleOverrideOptions</span><span>();</span><span>
        options</span><span>.</span><span>FontSize</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        options</span><span>.</span><span>Bold</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        tcs</span><span>.</span><span>SetCellStyleOverrideOptions</span><span>(</span><span>options</span><span>);</span><span>
        tcs</span><span>.</span><span>IsFontBold</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        tcs</span><span>.</span><span>TextSize</span><span> </span><span>=</span><span> </span><span>10</span><span>;</span><span>
        tsd</span><span>.</span><span>SetCellStyle</span><span>(</span><span>tsd</span><span>.</span><span>FirstRowNumber</span><span> </span><span>+</span><span> </span><span>1</span><span>,</span><span> tsd</span><span>.</span><span>FirstColumnNumber</span><span>,</span><span> tcs</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
