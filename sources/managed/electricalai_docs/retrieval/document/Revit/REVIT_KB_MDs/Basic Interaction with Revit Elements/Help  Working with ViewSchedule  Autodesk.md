---
created: 2026-01-28T20:52:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_ViewSchedule_Working_with_ViewSchedule_html
author: 
---

# Help | Working with ViewSchedule | Autodesk

> ## Excerpt
> The ScheduleDefinition class helps define the ViewSchedule.

---
The ScheduleDefinition class helps define the ViewSchedule.

The ScheduleDefinition class contains various settings related to the contents of a schedule view, including:

-   The schedule's category and other basic properties that determine the type of schedule.
-   A set of fields that become the columns of the schedule.
-   Sorting and grouping criteria.
-   Filters that restrict the set of elements visible in the schedule.
-   Settings to control visibility of the title, headers, and grid lines.

Most schedules contain a single ScheduleDefinition which is retrieved via the ViewSchedule.Definition property. In Revit, schedules of certain categories can contain an "embedded schedule" containing elements associated with the elements in the primary schedule, for example a room schedule showing the elements inside each room or a duct system schedule showing the elements associated with each system. An embedded schedule has its own category, fields, filters, etc. Those settings are stored in a second ScheduleDefinition object. When present, the embedded ScheduleDefinition is obtained from the ScheduleDefinition.EmbeddedDefinition property.

### Adding Fields

Once a ViewSchedule is created, fields can be added. The ScheduleDefinition.GetSchedulableFields() method will return a list of SchedulableField objects representing the non-calculated fields that may be included in the schedule. A new field can be added from a SchedulableField object or using a ScheduleFieldType. The following table describes the options available from the ScheduleFieldType enumeration.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__MEMBERLIST"><tbody><tr><td><b>Member name</b></td><td><b>Description</b></td></tr><tr><td>Instance</td><td>An instance parameter of the scheduled elements. All shared parameters also use this type, regardless of whether they are instance or type parameters.</td></tr><tr><td>ElementType</td><td>A type parameter of the scheduled elements.</td></tr><tr><td>Count</td><td>The number of elements appearing on the schedule row.</td></tr><tr><td>ViewBased</td><td>A specialized type of field used for a few parameters whose displayed values can change based on the settings of the view:<ul><li>ROOM_AREA and ROOM_PERIMETER in room and space schedules.</li><li>PROJECT_REVISION_REVISION_NUM in revision schedules.</li><li>KEYNOTE_NUMBER in keynote legends that are numbered by sheet.</li></ul></td></tr><tr><td>Formula</td><td>A formula calculated from the values of other fields in the schedule.</td></tr><tr><td>Percentage</td><td>A value indicating what percent of the total of another field each element represents.</td></tr><tr><td>Room</td><td>A parameter of the room that a scheduled element belongs to.</td></tr><tr><td>FromRoom</td><td>A parameter of the room on the "from" side of a door or window.</td></tr><tr><td>ToRoom</td><td>A parameter of the room on the "to" side of a door or window.</td></tr><tr><td>ProjectInfo</td><td>A parameter of the Project Info element in the project that the scheduled element belongs to, which may be a linked file. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>Material</td><td>In a material takeoff, a parameter of one of the materials of a scheduled element.</td></tr><tr><td>MaterialQuantity</td><td>In a material takeoff, a value representing how a particular material is used within a scheduled element. The parameter ID can be MATERIAL_AREA, MATERIAL_VOLUME, or MATERIAL_ASPAINT.</td></tr><tr><td>RevitLinkInstance</td><td>A parameter of the RevitLinkInstance that an element in a linked file belongs to. Currently RVT_LINK_INSTANCE_NAME is the only supported parameter. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>RevitLinkType</td><td>A parameter of the RevitLinkType that an element in a linked file belongs to. Currently RVT_LINK_FILE_NAME_WITHOUT_EXT is the only supported parameter. Only allowed in schedules that include elements from linked files.</td></tr><tr><td>StructuralMaterial</td><td>A parameter of the structural material of a scheduled element.</td></tr><tr><td>Space</td><td>A parameter of the space that a scheduled element belongs to.</td></tr></tbody></table>

Using one of the ScheduleDefinition.AddField() methods will add the field to the end of the field list. To place a new field in a specific location in the field list, use one of the ScheduleDefinition.InsertField() methods. Fields can also be ordered after the fact using ScheduleDefinition.SetFieldOrder().

The following is a simple example showing how to add fields to a view if they are not already in the view schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_B01907F3DB6E4BC2BA472F839B047368"><tbody><tr><td><b>Code Region: Adding fields to a schedule</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Add fields to view schedule.</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="schedules"&gt;List of view schedule.&lt;/param&gt;</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>AddFieldToSchedule</span><span>(</span><span>List</span><span>&lt;</span><span>ViewSchedule</span><span>&gt;</span><span> schedules</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>IList</span><span>&lt;</span><span>SchedulableField</span><span>&gt;</span><span> schedulableFields </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ViewSchedule</span><span> vs </span><span>in</span><span> schedules</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>//Get all schedulable fields from view schedule definition.</span><span>
        schedulableFields </span><span>=</span><span> vs</span><span>.</span><span>Definition</span><span>.</span><span>GetSchedulableFields</span><span>();</span><span>

        </span><span>foreach</span><span> </span><span>(</span><span>SchedulableField</span><span> sf </span><span>in</span><span> schedulableFields</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>bool</span><span> fieldAlreadyAdded </span><span>=</span><span> </span><span>false</span><span>;</span><span>
            </span><span>//Get all schedule field ids</span><span>
            </span><span>IList</span><span>&lt;</span><span>ScheduleFieldId</span><span>&gt;</span><span> ids </span><span>=</span><span> vs</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldOrder</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> id </span><span>in</span><span> ids</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>//If the GetSchedulableField() method of gotten schedule field returns same schedulable field,</span><span>
                </span><span>// it means the field is already added to the view schedule.</span><span>
                </span><span>if</span><span> </span><span>(</span><span>vs</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>id</span><span>).</span><span>GetSchedulableField</span><span>()</span><span> </span><span>==</span><span> sf</span><span>)</span><span>
                </span><span>{</span><span>
                    fieldAlreadyAdded </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                    </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            </span><span>//If schedulable field doesn't exist in view schedule, add it.</span><span>
            </span><span>if</span><span> </span><span>(</span><span>fieldAlreadyAdded </span><span>==</span><span> </span><span>false</span><span>)</span><span>
            </span><span>{</span><span>
                vs</span><span>.</span><span>Definition</span><span>.</span><span>AddField</span><span>(</span><span>sf</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ScheduleField class represents a single field in a ScheduleDefinition's list of fields. Each (non-hidden) field becomes a column in the schedule.

Most commonly, a field represents an instance or type parameter of elements appearing in the schedule. Some fields represent parameters of other related elements, like the room to which a scheduled element belongs. Fields can also represent data calculated from other fields in the schedule, specifically Formula and Percentage fields.

The ScheduleField class has properties to control column headings, both the text as well as the orientation. Column width and horizontal alignment of text within a column can also be defined.

The ScheduleField.IsHidden property can be used to hide a field. A hidden field is not displayed in the schedule, but it can be used for filtering, sorting, grouping, and conditional formatting and can be referenced by Formula and Percentage fields.

#### DisplayType

The ScheduleField has a DisplayType property which indicates the display type for the field. Possible values are:

-   **Standard** - Nothing is displayed if the values of the elements are different, otherwise, the common value will be displayed
-   **Totals** -Calculates and displays the total value
-   **MinMax** - Calculates and displays the minimum and maximum values
-   **Min** -Calculates and displays the maximum value
-   **Max** - Calculates and displays the minimum value The ScheduleField.CanDisplayMinMax() method indicates whether this field can display minimum and maximum values. In a non-itemized schedule, values for the non-Standard display types are displayed in regular rows when multiple elements appear on the same row.
    
    ### Style and Formatting of Fields
    

ScheduleField.GetStyle() and ScheduleField.SetStyle() use the TableCellStyle class to work with the style of fields in a schedule. Using SetStyle(), various attributes of the field can be set, including the line style for the border of the cell as well as the text font, color and size.

ScheduleField.SetFormatOptions() and ScheduleField.GetFormatOptions() use the FormatOptions class to work with the formatting of a field's data. The FormatOptions class contains settings that control how to format numbers with units as strings. It contains those settings that are typically chosen by an end user in the Format dialog and stored in the document.

In the following example, all length fields in a ViewSchedule are formatted to display in feet and fractional inches.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_2905AC04527B43AD8B0170FD38F078DB"><tbody><tr><td><b>Code Region: Formatting a field</b></td></tr><tr><td><pre><code><span>// format length units to display in feet and inches format</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>FormatLengthFields</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>int</span><span> nFields </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetFieldCount</span><span>();</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> n </span><span>=</span><span> </span><span>0</span><span>;</span><span> n </span><span>&lt;</span><span> nFields</span><span>;</span><span> n</span><span>++)</span><span>
    </span><span>{</span><span>
        </span><span>ScheduleField</span><span> field </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>.</span><span>GetField</span><span>(</span><span>n</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>field</span><span>.</span><span>GetSpecTypeId</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FormatOptions</span><span> formatOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>FormatOptions</span><span>();</span><span>
            formatOpts</span><span>.</span><span>UseDefault</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
            formatOpts</span><span>.</span><span>SetUnitTypeId</span><span>(</span><span>UnitTypeId</span><span>.</span><span>FeetFractionalInches</span><span>);</span><span>
            field</span><span>.</span><span>SetFormatOptions</span><span>(</span><span>formatOpts</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The example below applies both formatting and style overrides to a given field.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_4429DA0DE7734921A6F1CD04F05F30DA"><tbody><tr><td><b>Code Region: Apply formatting and style overrides to field</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ApplyFormattingToField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>int</span><span> fieldIndex</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the field.</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> field </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldIndex</span><span>);</span><span>

    </span><span>// Build unit formatting for the field.</span><span>
    </span><span>FormatOptions</span><span> options </span><span>=</span><span> field</span><span>.</span><span>GetFormatOptions</span><span>();</span><span>
    options</span><span>.</span><span>UseDefault</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    options</span><span>.</span><span>SetUnitTypeId</span><span>(</span><span>UnitTypeId</span><span>.</span><span>SquareInches</span><span>);</span><span>
    options</span><span>.</span><span>SetSymbolTypeId</span><span>(</span><span>SymbolTypeId</span><span>.</span><span>InCaret2</span><span>);</span><span>

    </span><span>// Build style overrides for the field</span><span>
    </span><span>// Use override options to indicate fields that are overridden and apply changes</span><span>
    </span><span>TableCellStyle</span><span> style </span><span>=</span><span> field</span><span>.</span><span>GetStyle</span><span>();</span><span>
    </span><span>TableCellStyleOverrideOptions</span><span> overrideOptions </span><span>=</span><span> style</span><span>.</span><span>GetCellStyleOverrideOptions</span><span>();</span><span>
    overrideOptions</span><span>.</span><span>BackgroundColor</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>BackgroundColor</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0xFF</span><span>);</span><span>
    overrideOptions</span><span>.</span><span>FontColor</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>TextColor</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0xFF</span><span>,</span><span> </span><span>0xFF</span><span>,</span><span> </span><span>0xFF</span><span>);</span><span>
    overrideOptions</span><span>.</span><span>Italics</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    style</span><span>.</span><span>IsFontItalic</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    style</span><span>.</span><span>SetCellStyleOverrideOptions</span><span>(</span><span>overrideOptions</span><span>);</span><span>

    </span><span>double</span><span> width </span><span>=</span><span> field</span><span>.</span><span>GridColumnWidth</span><span>;</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Set style etc"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        field</span><span>.</span><span>SetStyle</span><span>(</span><span>style</span><span>);</span><span>
        field</span><span>.</span><span>SetFormatOptions</span><span>(</span><span>options</span><span>);</span><span>
        </span><span>// Change column width (affects width in grid and on sheet) - units are in Revit length units - ft.</span><span>
        field</span><span>.</span><span>GridColumnWidth</span><span> </span><span>=</span><span> width </span><span>+</span><span> </span><span>0.5</span><span>;</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Title and Headers

Display of the schedule title and/or headers is optional. Whether the title or headers are shown can be controlled with the ScheduleDefinition properties ShowTitle and ShowHeaders.

### Grouping and Sorting in Schedules

A schedule may be sorted or grouped by one or more of the schedule's fields. Several methods can be used to control grouping and sorting of fields. The ScheduleSortGroupField class represents one of the fields that the schedule is sorted or grouped by. Sorting and grouping are related operations. In either case, elements appearing in the schedule are sorted based on their values for the field by which the schedule is sorted/grouped, which automatically causes elements with identical values to be grouped together. By enabling extra header, footer, or blank rows, visual separation between groups can be achieved.

If the ScheduleDefinition.IsItemized property is false, elements having the same values for all of the fields used for sorting/grouping will be combined onto the same row. Otherwise the schedule displays each element on a separate row

A schedule can be sorted or grouped by data that is not displayed in the schedule by marking the field used for sorting/grouping as hidden using the ScheduleField.IsHidden property.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_87FC42D71B464D72AD9B7CD81EA453A2"><tbody><tr><td><b>Code Region: Add grouping/sorting to schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddGroupingToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>,</span><span> </span><span>bool</span><span> withTotalsAndDecoration</span><span>,</span><span> </span><span>ScheduleSortOrder</span><span> order</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find field </span><span>
    </span><span>ScheduleField</span><span> field </span><span>=</span><span> </span><span>FindScheduleField</span><span>(</span><span>schedule</span><span>,</span><span> paramEnum</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>field </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Unable to find field."</span><span>);</span><span>

    </span><span>// Build sort/group field.</span><span>
    </span><span>ScheduleSortGroupField</span><span> sortGroupField </span><span>=</span><span> </span><span>new</span><span> </span><span>ScheduleSortGroupField</span><span>(</span><span>field</span><span>.</span><span>FieldId</span><span>,</span><span> order</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>withTotalsAndDecoration</span><span>)</span><span>
    </span><span>{</span><span>
        sortGroupField</span><span>.</span><span>ShowFooter</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowFooterTitle</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowFooterCount</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowHeader</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        sortGroupField</span><span>.</span><span>ShowBlankLine</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Add the sort/group field</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Add sort/group field"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        definition</span><span>.</span><span>AddSortGroupField</span><span>(</span><span>sortGroupField</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>ScheduleField</span><span> </span><span>FindScheduleField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> foundField </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ElementId</span><span> paramId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>paramEnum</span><span>);</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> fieldId </span><span>in</span><span> definition</span><span>.</span><span>GetFieldOrder</span><span>())</span><span>
    </span><span>{</span><span>
        foundField </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>foundField</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> foundField</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Headers can also be grouped. ViewSchedule.GroupHeaders() method can be used to specify which rows and columns to include in a grouping of the header section. The last parameter is a string for the caption of the grouped rows and columns.

In the following example, columns are grouped for a newly created single-category schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_C5591CE29409415D9EF7ED5B5AAE6C44"><tbody><tr><td><b>Code Region: Grouping headers</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>CreateSingleCategoryScheduleWithGroupedColumnHeaders</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create single-category with grouped column headers"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Build the schedule</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>ViewSchedule</span><span> vs </span><span>=</span><span> </span><span>ViewSchedule</span><span>.</span><span>CreateSchedule</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Windows</span><span>));</span><span>

        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_HEIGHT</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>WINDOW_WIDTH</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_MARK</span><span>));</span><span>
        </span><span>AddRegularField</span><span>(</span><span>vs</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ALL_MODEL_COST</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Group the headers in the body section using ViewSchedule methods</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>"Size"</span><span>);</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>"Other"</span><span>);</span><span>
        vs</span><span>.</span><span>GroupHeaders</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>"All"</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddRegularField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> paramId</span><span>)</span><span>
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

### Filtering

A ScheduleFilter can be used to filter the elements that will be displayed in a schedule. A filter is a condition that must be satisfied for an element to appear in the schedule. All filters must be satisfied for an element to appear in the schedule.

A schedule can be filtered by data that is not displayed in the schedule by marking the field used for filtering as hidden using the ScheduleField.IsHidden property.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_5A0B9ECD2D2148478BA767ECC8050860"><tbody><tr><td><b>Code Region: Add filter to schedule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddFilterToSchedule</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Find level field</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>

    </span><span>ScheduleField</span><span> levelField </span><span>=</span><span> </span><span>FindField</span><span>(</span><span>schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span>.</span><span>ROOM_LEVEL_ID</span><span>);</span><span>

    </span><span>// Add filter</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>schedule</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"Add filter"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// If field not present, add it</span><span>
        </span><span>if</span><span> </span><span>(</span><span>levelField </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            levelField </span><span>=</span><span> definition</span><span>.</span><span>AddField</span><span>(</span><span>ScheduleFieldType</span><span>.</span><span>Instance</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInParameter</span><span>.</span><span>ROOM_LEVEL_ID</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>// Set field to hidden</span><span>
        levelField</span><span>.</span><span>IsHidden</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>ScheduleFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ScheduleFilter</span><span>(</span><span>levelField</span><span>.</span><span>FieldId</span><span>,</span><span> </span><span>ScheduleFilterType</span><span>.</span><span>Equal</span><span>,</span><span> levelId</span><span>);</span><span>
        definition</span><span>.</span><span>AddFilter</span><span>(</span><span>filter</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>/// &lt;summary&gt;</span><span>
</span><span>/// Finds an existing ScheduleField matching the given parameter</span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="schedule"&gt;&lt;/param&gt;</span><span>
</span><span>/// &lt;param name="paramEnum"&gt;&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>static</span><span> </span><span>ScheduleField</span><span> </span><span>FindField</span><span>(</span><span>ViewSchedule</span><span> schedule</span><span>,</span><span> </span><span>BuiltInParameter</span><span> paramEnum</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ScheduleDefinition</span><span> definition </span><span>=</span><span> schedule</span><span>.</span><span>Definition</span><span>;</span><span>
    </span><span>ScheduleField</span><span> foundField </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ElementId</span><span> paramId </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>paramEnum</span><span>);</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>ScheduleFieldId</span><span> fieldId </span><span>in</span><span> definition</span><span>.</span><span>GetFieldOrder</span><span>())</span><span>
    </span><span>{</span><span>
        foundField </span><span>=</span><span> definition</span><span>.</span><span>GetField</span><span>(</span><span>fieldId</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>foundField</span><span>.</span><span>ParameterId</span><span> </span><span>==</span><span> paramId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span> foundField</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>null</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Multiple Value Formatting

The `ScheduleField` class has properties which allow customization of the multiple value indication per field:

-   ScheduleField.MultipleValuesDisplayType
-   ScheduleField.MultipleValuesText - The text to be used when a field has multiple values
-   ScheduleField.MultipleValuesCustomText - The text to be used when a field has multiple values and the display type is set to ScheduleFieldMultip leValuesDisplayType.Custom

The Enum `ScheduleFieldMultipleValuesDisplayType` defines how the schedule field's multiple value indication is displayed (using the project setting, a custom text, or a predefined text "<varies>").

### Working with Schedule Data

The following example shows how to determine the list of elements in a schedule.

<table summary="" id="GUID-F66DF1E1-7EF2-4CD5-AA3F-9DEA7D92DC49__TABLE_815A7CD21F094301BC3655148D8880F8"><tbody><tr><td><b>Code Region: Get a schedule's contents</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>GetScheduleContents</span><span>(</span><span>ViewSchedule</span><span> viewSchedule</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Collect types displayed in the schedule</span><span>
    </span><span>FilteredElementCollector</span><span> typeCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>viewSchedule</span><span>.</span><span>Document</span><span>,</span><span> viewSchedule</span><span>.</span><span>Id</span><span>);</span><span>
    typeCollector</span><span>.</span><span>WhereElementIsElementType</span><span>();</span><span>

    </span><span>int</span><span> numberOfTypes </span><span>=</span><span> typeCollector</span><span>.</span><span>Count</span><span>();</span><span>

    </span><span>// Collect instances displayed in the schedule</span><span>
    </span><span>FilteredElementCollector</span><span> instCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>viewSchedule</span><span>.</span><span>Document</span><span>,</span><span> viewSchedule</span><span>.</span><span>Id</span><span>);</span><span>
    instCollector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>

    </span><span>int</span><span> numberOfInstances </span><span>=</span><span> instCollector</span><span>.</span><span>Count</span><span>();</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Elements in schedule"</span><span>,</span><span> </span><span>String</span><span>.</span><span>Format</span><span>(</span><span>"Types {0} instances {1}"</span><span>,</span><span> numberOfTypes</span><span>,</span><span> numberOfInstances</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

To work with the actual data in the schedule, the ViewSchedule.GetTableData() returns a TableData object that holds most of the data that describe the style and contents of the rows, columns, and cells in a table. More information can be found under [TableView](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_TableView_html).
