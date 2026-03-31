---
created: 2026-01-28T20:52:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_View_Types_ViewSheet_html
author: 
---

# Help | ViewSheet | Autodesk

> ## Excerpt
> A sheet contains views and a title block. When creating a sheet view with the ViewSheet.Create() method, a title block family symbol Id is a required parameter for the method. A title block family symbol can be found using a FilteredElementCollector.

---
A sheet contains views and a title block. When creating a sheet view with the ViewSheet.Create() method, a title block family symbol Id is a required parameter for the method. A title block family symbol can be found using a FilteredElementCollector.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_7705E6512C3D47419E87909721D60B7D"><tbody><tr><td><b>Code Region: ViewSheet.Create()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>ViewSheet</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> titleBlockTypeId</span><span>);</span></code></pre></td></tr></tbody></table>

The newly created sheet has no views. The Viewport.Create() method is used to add views. The Viewport class is used to add regular views to a view sheet, i.e. plan, elevation, drafting and three dimensional. To add schedules to a view, use ScheduleSheetInstance.Create() instead.

The `View.GetPlacementOnSheetStatus` method returns a `ViewPlacementOnSheetStatus` enum that describes if the view is placed on a sheet. Some views, such as schedules, can be partially placed on a sheet by divided them into segments and placing only some of those segments on a sheet.

The property `Viewport.LabelOffset` controls the two-dimensional label offset from left bottom corner of the viewport (as established with Rotation set to None) to the left end of the viewport label line. The property `Viewport.LabelLineLength` controls the length of the viewport label line in sheet space.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_119C0C6953834413A5BC13C8917CF9AE"><tbody><tr><td><b>Code Region: Add two views aligned at left corner</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>PlaceAlignedViewsAtLeftCorner</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> fec </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    fec</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>ViewPlan</span><span>));</span><span>
    </span><span>var</span><span> viewPlans </span><span>=</span><span> fec</span><span>.</span><span>Cast</span><span>&lt;</span><span>ViewPlan</span><span>&gt;().</span><span>Where</span><span>&lt;</span><span>ViewPlan</span><span>&gt;(</span><span>vp </span><span>=&gt;</span><span> </span><span>!</span><span>vp</span><span>.</span><span>IsTemplate</span><span> </span><span>&amp;&amp;</span><span> vp</span><span>.</span><span>ViewType</span><span> </span><span>==</span><span> </span><span>ViewType</span><span>.</span><span>CeilingPlan</span><span>);</span><span>

    </span><span>ViewPlan</span><span> vp1 </span><span>=</span><span> viewPlans</span><span>.</span><span>ElementAt</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>ViewPlan</span><span> vp2 </span><span>=</span><span> viewPlans</span><span>.</span><span>ElementAt</span><span>(</span><span>1</span><span>);</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Place on sheet"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Add two viewports distinct from one another</span><span>
        </span><span>ViewSheet</span><span> vs </span><span>=</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>);</span><span>
        </span><span>Viewport</span><span> viewport1 </span><span>=</span><span> </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> vs</span><span>.</span><span>Id</span><span>,</span><span> vp1</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        </span><span>Viewport</span><span> viewport2 </span><span>=</span><span> </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> vs</span><span>.</span><span>Id</span><span>,</span><span> vp2</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        doc</span><span>.</span><span>Regenerate</span><span>();</span><span>

        </span><span>// Calculate the necessary move vector to align the lower left corner</span><span>
        </span><span>Outline</span><span> outline1 </span><span>=</span><span> viewport1</span><span>.</span><span>GetBoxOutline</span><span>();</span><span>
        </span><span>Outline</span><span> outline2 </span><span>=</span><span> viewport2</span><span>.</span><span>GetBoxOutline</span><span>();</span><span>
        XYZ boxCenter </span><span>=</span><span> viewport2</span><span>.</span><span>GetBoxCenter</span><span>();</span><span>
        XYZ vectorToCenter </span><span>=</span><span> boxCenter </span><span>-</span><span> outline2</span><span>.</span><span>MinimumPoint</span><span>;</span><span>
        XYZ newCenter </span><span>=</span><span> outline1</span><span>.</span><span>MinimumPoint</span><span> </span><span>+</span><span> vectorToCenter</span><span>;</span><span>

        </span><span>// Move the viewport to the new location</span><span>
        viewport2</span><span>.</span><span>SetBoxCenter</span><span>(</span><span>newCenter</span><span>);</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

-   The XYZ location parameter identifies where the added views are located. It points to the added view's center coordinate (measured in inches).
-   The coordinates, \[0, 0\], are relative to the sheet's lower left corner.

Viewports placed on sheets can have the associated view swapped for another view in the model by editing the `Viewport.ViewId` property. When this swap is done, the `Viewport.ViewportPositioning` property specifies how the viewport will be positioned on the sheet when swapped to another view by maintaining either the viewport center or the view origin.

Each sheet has a unique sheet number in the complete drawing set. The number is displayed before the sheet name in the Project Browser. It is convenient to use the sheet number in a view title to cross-reference the sheets in your drawing set. You can retrieve or modify the number using the SheetNumber property. The number must be unique; otherwise an exception is thrown when you set the number to a duplicate value.

The following example illustrates how to create and print a sheet view. Begin by finding an available title block in the document (using a filter in this case) and use it to create the sheet view. Next, add a 3D view. The view is placed with its lower left-hand corner at the center of the sheet. Finally, print the sheet by calling the View.Print() method.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_F482645A2CCD43E18C862DAF950546CF"><tbody><tr><td><b>Code Region: Creating a sheet view</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateSheetView</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View3D</span><span> view3D</span><span>)</span><span>
</span><span>{</span><span>

    </span><span>// Get an available title block from document</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>));</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_TitleBlocks</span><span>);</span><span>

    </span><span>FamilySymbol</span><span> fs </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>fs </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create a new ViewSheet"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            </span><span>try</span><span>
            </span><span>{</span><span>
                </span><span>// Create a sheet view</span><span>
                </span><span>ViewSheet</span><span> viewSheet </span><span>=</span><span> </span><span>ViewSheet</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> fs</span><span>.</span><span>Id</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> viewSheet</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create new ViewSheet."</span><span>);</span><span>
                </span><span>}</span><span>

                </span><span>// Add passed in view onto the center of the sheet</span><span>
                UV location </span><span>=</span><span> </span><span>new</span><span> UV</span><span>((</span><span>viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Max</span><span>.</span><span>U </span><span>-</span><span> viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Min</span><span>.</span><span>U</span><span>)</span><span> </span><span>/</span><span> </span><span>2</span><span>,</span><span>
                                        </span><span>(</span><span>viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Max</span><span>.</span><span>V </span><span>-</span><span> viewSheet</span><span>.</span><span>Outline</span><span>.</span><span>Min</span><span>.</span><span>V</span><span>)</span><span> </span><span>/</span><span> </span><span>2</span><span>);</span><span>

                </span><span>//viewSheet.AddView(view3D, location);</span><span>
                </span><span>Viewport</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> viewSheet</span><span>.</span><span>Id</span><span>,</span><span> view3D</span><span>.</span><span>Id</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>location</span><span>.</span><span>U</span><span>,</span><span> location</span><span>.</span><span>V</span><span>,</span><span> </span><span>0</span><span>));</span><span>

                </span><span>// Print the sheet out</span><span>
                </span><span>if</span><span> </span><span>(</span><span>viewSheet</span><span>.</span><span>CanBePrinted</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span>
                    taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"Print the sheet?"</span><span>;</span><span>
                    </span><span>TaskDialogCommonButtons</span><span> buttons </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Yes</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>No</span><span>;</span><span>
                    taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> buttons</span><span>;</span><span>
                    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> taskDialog</span><span>.</span><span>Show</span><span>();</span><span>

                    </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Yes</span><span>)</span><span>
                    </span><span>{</span><span>
                        viewSheet</span><span>.</span><span>Print</span><span>();</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>

                t</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>catch</span><span>
            </span><span>{</span><span>
                t</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: You cannot add a sheet view to another sheet and you cannot add a view to more than one sheet; otherwise an argument exception occurs.

### Duplicating a sheet

When duplicating a sheet, the SheetDuplicateOption enum allows you to indicate what information should be copied when duplicating a sheet. Its values are:

-   DuplicateEmptySheet - Only copies the title block.
-   DuplicateSheetWithDetailing - Copies the title block and details.
-   DuplicateSheetWithViewsOnly- Copies the title block, details, viewports and contained views. The newly created sheet will reference the newly duplicated views.
-   DuplicateSheetWithViewsAndDetailing - Copies the title block, details, and viewports. Duplicates the sheet's contained views with detailing. The newly created sheet will reference the newly duplicated views.
-   DuplicateSheetWithViewsAsDependent - Copies the title block, details, and viewports. Duplicates the sheet's contained views as dependent. The newly created sheet will reference the newly duplicated dependent views.

### Revisions on Sheets

The ViewSheet class has several methods for working with revision and revision clouds on sheets.

-   **GetAllRevisionIds()**\- Gets the ordered array of Revisions which participate in the sheet's revision schedules.
-   **GetAdditionalRevisionIds()**\- Gets the Revisions that are additionally included in the sheet's revision schedules.
-   **SetAdditionalRevisionIds()**\- Sets the Revisions to additionally include in the sheet's revision schedules.
-   **GetCurrentRevision()**\- Returns the most recent numbered Revision shown on this ViewSheet.
-   **GetRevisionCloudNumberOnSheet()**\- Gets the Revision Number for a RevisionCloud on this sheet when the numbering in the project is by sheet.
-   **GetRevisionNumberOnSheet()** - Gets the Revision Number for a particular Revision as it will appear on this sheet when the numbering in the project is by sheet. The Revisions are ordered according to the revision sequence in the project. Additionally included Revisions will always participate in the sheet's revision schedules. Normally a Revision is scheduled in the revision schedule because one of its associated RevisionClouds is present on the sheet.

The following code sample demonstrates how to add additional revisions to the sheet that match a given criteria.

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_CAF21DDC99F144ED962F6C3822552118"><tbody><tr><td><b>Code Region: Add additional revisions to sheet</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>AddAdditionalRevisionsToSheet</span><span>(</span><span>ViewSheet</span><span> viewSheet</span><span>,</span><span> </span><span>String</span><span> toMatch</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> viewSheet</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> revisions </span><span>=</span><span> viewSheet</span><span>.</span><span>GetAdditionalRevisionIds</span><span>();</span><span>

    </span><span>// Find revisions whose description matches input string</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Revisions</span><span>);</span><span>
    collector</span><span>.</span><span>WhereElementIsNotElementType</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>revisions</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        collector</span><span>.</span><span>Excluding</span><span>(</span><span>revisions</span><span>);</span><span>

    </span><span>// Check if revision should be added</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> revision </span><span>in</span><span> collector</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Parameter</span><span> descriptionParam </span><span>=</span><span> revision</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ProjectRevisionRevisionDescription</span><span>);</span><span>
        </span><span>String</span><span> description </span><span>=</span><span> descriptionParam</span><span>.</span><span>AsString</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>description</span><span>.</span><span>Contains</span><span>(</span><span>toMatch</span><span>))</span><span>
            revisions</span><span>.</span><span>Add</span><span>(</span><span>revision</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>if</span><span> </span><span>(</span><span>revisions</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Apply the new list of revisions</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add revisions to sheet"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            viewSheet</span><span>.</span><span>SetAdditionalRevisionIds</span><span>(</span><span>revisions</span><span>);</span><span>
            t</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Printer Setup

You may want to change the settings of the printer before printing a sheet. The API exposes the settings for the printer with the PrintManager class, and related Autodesk.Revit.DB classes:

<table summary="" id="GUID-48DFC75D-66DC-434C-B592-D60D40E29348__TABLE_6738648BCDFC439CA3B1D2A3CCF21462"><tbody><tr><td><b>Class</b></td><td><b>Functionality</b></td></tr><tr><td>Autodesk.Revit.DB.PrintManager</td><td>Represents the Print information in Print Dialog (File-&gt;Print) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PrintParameters</td><td>An object that contains settings used for printing the document.</td></tr><tr><td>Autodesk.Revit.DB.PrintSetup</td><td>Represents the Print Setup (File-&gt;Print Setup...) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PaperSize</td><td>An object that represents a Paper Size of Print Setup within the Autodesk Revit project.</td></tr><tr><td>Autodesk.Revit.DB.PaperSizeSet</td><td>A set that can contain any number of paper size objects.</td></tr><tr><td>Autodesk.Revit.DB.PaperSource</td><td>An object that represents a Paper Source of Print Setup within the Autodesk Revit project.</td></tr><tr><td>Autodesk.Revit.DB.PaperSourceSet</td><td>A set that can contain any number of paper source objects.</td></tr><tr><td>Autodesk.Revit.DB.ViewSheetSetting</td><td>Represents the View/Sheet Set (File-&gt;Print) within the Revit UI.</td></tr><tr><td>Autodesk.Revit.DB.PrintSetting</td><td>Represents the Print Setup (File-&gt;Print Setup...) within the Revit UI.</td></tr></tbody></table>

For an example of code that uses these objects, see the ViewPrinter sample application that is included with the Revit Platform SDK.
