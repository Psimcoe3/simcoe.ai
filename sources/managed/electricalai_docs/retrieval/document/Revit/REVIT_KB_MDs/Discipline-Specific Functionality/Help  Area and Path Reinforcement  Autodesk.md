---
created: 2026-01-28T21:09:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Area_and_Path_Reinforcement_html
author: 
---

# Help | Area and Path Reinforcement | Autodesk

> ## Excerpt
> The Revit API provides classes representing area and path reinforcement in the structural features of Revit.

---
The Revit API provides classes representing area and path reinforcement in the structural features of Revit.

Find the AreaReinforcementCurves for AreaReinforcement by calling the GetBoundaryCurveIds() method which returns an IList of ElementIds that represent AreaReinforcementCurves.

While the AreaReinforcement.GetBoundaryCurveIds() method returns a set of ElementIds representing AreaReinforcementCurves, which have a property that returns a Curve, the PathReinforcement.GetCurveElementIds() method returns a collection of ElementIds that represent ModelCurves. There is no way to flip the PathReinforcement except by on creation using the PathReinforcement.Create() method. PathReinforcment can only be created using an array of curves.

For more details about retrieving an Element's Geometry, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

Note: Project-wide settings related to area and path reinforcement are accessible from the [ReinforcementSettings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Settings_html "Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.") class.

The API provides access to the layers of Area Reinforcement elements and allows the individual lines exposed through those layers to be moved and removed.

The overloaded AreaReinforcement.Create() method provides two ways to create new AreaReinforcement: based on a host boundary or from an array of curves. The Major Direction of the area reinforcement can be set when creating a new AreaReinforcement using either of the overloaded Create() methods, but the AreaReinforcment.Direction property is read-only.

<table summary="" id="GUID-8AD6CFC8-A065-4108-B700-E523575169C3__TABLE_D2975572CF144E9582C227C448096E39"><tbody><tr><td><b>Creating area reinforcement</b></td></tr><tr><td><pre><code><span>AreaReinforcement</span><span> </span><span>CreateAreaReinforcementInWall</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the wall analytical profile whose curves will define the boundary of the the area reinforcement </span><span>
     </span><span>AnalyticalPanel</span><span> analytical </span><span>=</span><span> </span><span>(</span><span>AnalyticalPanel</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>)</span><span>
</span><span>.</span><span>GetAssociatedElementId</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>));</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> analytical</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Can't get AnalyticalModel from the selected wall"</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> analytical</span><span>.</span><span>GetOuterContour</span><span>().</span><span>Cast</span><span>&lt;</span><span>Curve</span><span>&gt;().</span><span>ToList</span><span>();</span><span>

    </span><span>//define the Major Direction of AreaReinforcement,</span><span>
    </span><span>//we get direction of first Line on the Wall as the Major Direction</span><span>
    </span><span>Line</span><span> firstLine </span><span>=</span><span> </span><span>(</span><span>Line</span><span>)(</span><span>curves</span><span>[</span><span>0</span><span>]);</span><span>
    XYZ majorDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X</span><span>,</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y</span><span>,</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z</span><span>);</span><span>

    </span><span>// Obtain the default types</span><span>
    </span><span>ElementId</span><span> defaultRebarBarTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>RebarBarType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultAreaReinforcementTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>AreaReinforcementType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultHookTypeId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// Create the area reinforcement</span><span>
    </span><span>AreaReinforcement</span><span> rein </span><span>=</span><span> </span><span>AreaReinforcement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wall</span><span>,</span><span> curves</span><span>,</span><span> majorDirection</span><span>,</span><span> defaultAreaReinforcementTypeId</span><span>,</span><span> defaultRebarBarTypeId</span><span>,</span><span> defaultHookTypeId</span><span>);</span><span>

    </span><span>return</span><span> rein</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Creating path reinforcement

The overloaded static method PathReinforcement.Create() method provides two ways to create path reinforcement. Both create path reinforcement in a host object from an array of curves, but one will use the default rebar shape while the other takes a Rebar Shape id as a parameter. The example below uses the default rebar shape.

<table summary="" id="GUID-8AD6CFC8-A065-4108-B700-E523575169C3__TABLE_03C405B4DCD042B88DB2270995530831"><tbody><tr><td><b>Creating path reinforcement</b></td></tr><tr><td><pre><code><span>PathReinforcement</span><span> </span><span>CreatePathReinforcement</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a geometry line in the selected wall as the path</span><span>
    </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
    </span><span>LocationCurve</span><span> location </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ start </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
    curves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>));</span><span>

    </span><span>// Obtain the default types</span><span>
    </span><span>ElementId</span><span> defaultRebarBarTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>RebarBarType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultPathReinforcementTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>PathReinforcementType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultHookTypeId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// Begin to create the path reinforcement</span><span>
    </span><span>PathReinforcement</span><span> rein </span><span>=</span><span> </span><span>PathReinforcement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wall</span><span>,</span><span> curves</span><span>,</span><span> </span><span>true</span><span>,</span><span> defaultPathReinforcementTypeId</span><span>,</span><span> defaultRebarBarTypeId</span><span>,</span><span> defaultHookTypeId</span><span>,</span><span> defaultHookTypeId</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> rein</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create path reinforcement failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Create path reinforcement succeed."</span><span>);</span><span>

    </span><span>return</span><span> rein</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When specifying the rebar shape id for a new PathReinforcement, if there are no rebar shapes in the project or you are not initially concerned with the rebar shape, you can use the static PathReinforcement method GetOrCreateDefaultRebarShape() to obtain a valid rebar shape for use with PathReinforcement. If you would like to check whether an existing rebar shape is valid for use with path reinforcement, you can call the static method PathReinforcement.IsValidRebarShapeId().

New shape types may be queried, or assigned to the path reinforcement by using the PathReinforcement properties PrimaryBarShapeId and AlternatingBarShapeId. The static method IsValidRebarShapeId() can be used to determine if you have a valid shape before attempting to set the shape id on a path reinforcement object. Note that before attempting to set alternating bars, the alternating bars parameter must be enabled in the Path Reinforcement by setting PATH\_REIN\_ALTERNATING BuiltInParameter to true.

The orientation of the primary and alternating bars may also be queried, or set through the properties PrimaryBarOrientation and AlternatingBarOrientation which take a value from the ReinforcementBarOrientation enumeration. You may check whether an orientation is valid for a particular path reinforcement object by calling the class method IsValidPrimaryBarOrientation() or IsValidAlternatingBarOrientation().

You may query the state of the alternating layer by calling the IsAlternatingLayerEnabled() method. The alternating layer is controlled via the built in parameter PATH\_REIN\_ALTERNATING on the path reinforcing element.

The API provides access to move, include, or remove individual bars for RebarInSystem elements that are owned by PathReinforcement.
