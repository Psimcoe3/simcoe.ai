---
created: 2026-01-28T21:08:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Mechanical_Settings_html
author: 
---

# Help | Mechanical Settings | Autodesk

> ## Excerpt
> Many of the settings available on the Manage tab under MEP Settings - Mechanical Settings are also available through the Revit API.

---
Many of the settings available on the Manage tab under MEP Settings - Mechanical Settings are also available through the Revit API.

### Pipe Settings

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSettings.png)

**Pipe Settings**

The PipeSettings class provides access to the settings shown above, such as Pipe Size Suffix and Pipe Connector Tolerance. There is one PipeSettings object per document and it is accessible through the static method PipeSettings.GetPipeSettings().

#### Fitting Angles

Fitting angle usage settings for pipes are available from the following property and methods of the PipeSettings class:

-   PipeSettings.FittingAngleUsage
-   PipeSettings.GetSpecificFittingAngles()
-   PipeSettings.GetSpecificFittingAngleStatus()
-   PipeSettings.SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeAngleSettings.png)

**Pipe Fitting Angles**

#### Segments and Sizes

The settings available in the UI under Pipe Settings - Segments and Sizes are available as well.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSizesSettings.png)

**Segments and Sizes**

This information is available through the Segment and MEPSize classes. A Segment represents a length of MEPCurve that contains a material and set of available sizes. The pipe sizes are represented by the MEPSize class. The Segments available can be found using a filter. The following example demonstrates how to get some of the information in the dialog above.

<table summary="" id="GUID-B9C38F9B-A11B-4369-B879-0A641A3E725F__TABLE_263A8421D9FB45E78F60EB85C3483449"><tbody><tr><td><b>Code Region: Traversing Pipe Sizes in Pipe Settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PipeSizes</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collectorPipeType </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collectorPipeType</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Segment</span><span>));</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>Segment</span><span>&gt;</span><span> segments </span><span>=</span><span> collectorPipeType</span><span>.</span><span>ToElements</span><span>().</span><span>Cast</span><span>&lt;</span><span>Segment</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Segment</span><span> segment </span><span>in</span><span> segments</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StringBuilder</span><span> strPipeInfo </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Segment: "</span><span> </span><span>+</span><span> segment</span><span>.</span><span>Name</span><span>);</span><span>

        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Roughness: "</span><span> </span><span>+</span><span> segment</span><span>.</span><span>Roughness</span><span>);</span><span>

        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Pipe Sizes:"</span><span>);</span><span>
        </span><span>double</span><span> dLengthFac </span><span>=</span><span> </span><span>304.8</span><span>;</span><span>  </span><span>// used to convert stored units from ft to mm for display</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>MEPSize</span><span> size </span><span>in</span><span> segment</span><span>.</span><span>GetSizes</span><span>())</span><span>
        </span><span>{</span><span>
            strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Nominal: {0:F3}, ID: {1:F3}, OD: {2:F3}"</span><span>,</span><span>
                                        size</span><span>.</span><span>NominalDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>,</span><span> size</span><span>.</span><span>InnerDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>,</span><span> size</span><span>.</span><span>OuterDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"PipeSetting Data"</span><span>,</span><span> strPipeInfo</span><span>.</span><span>ToString</span><span>());</span><span>
        </span><span>break</span><span>;</span><span>                  
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PipeSettingsExample.jpg)

**Output of previous example**

To add new sizes to the list, use the Segment.AddSize() method. Use Segment.RemoveSize() to remove a size by nominal diameter.

#### Slopes

The PipeSettings class also provides access to the slope values available in the UI under Pipe Settings - Slopes. Use GetPipeSlopes() to retreive a list of slope values. PipeSettings.SetPipeSlopes() provides the ability to set all the slope values at once, while PipeSettings.AddPipeSlope() adds a single pipe slope. Revit stores the slope value as a percentage (0-100).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSlopeSettings.png)

**Pipe Slope Values**

### Duct Settings

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechDuctSettings.png)

**Duct Settings**

The DuctSettings class provides access to the settings shown above, such as Duct Fitting Annotation Size and Air Density. There is one DuctSettings object per document and it is accessible through the static method DuctSettings.GetDuctSettings().

#### Duct Fitting Angles

Fitting angle usage settings for ducts are available from the following property and methods of the DuctSettings class:

-   DuctSettings.FittingAngleUsage
-   DuctSettings.GetSpecificFittingAngles()
-   DuctSettings.GetSpecificFittingAngleStatus()
-   DuctSettings.SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechDuctAngleSettings.png)

**Duct Fitting Angles**

### MEP Hidden Line Settings

The `MEPHiddenLineSettings` class represents the settings of the mechanical hidden line display (e.g. ducts and pipes). It can be obtained from the static method: `MEPHiddenLineSettings.GetMEPHiddenLineSettings(Document)` It offers the following properties:

-   MEPHiddenLineSettings.DrawHiddenLine
-   MEPHiddenLineSettings.LineStyle
-   MEPHiddenLineSettings.InsideGap
-   MEPHiddenLineSettings.OutsideGap
-   MEPHiddenLineSettings.SingleLineGap
