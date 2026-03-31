---
created: 2026-01-28T20:59:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Visibility_of_family_elements_html
author: 
---

# Help | Visibility of family elements | Autodesk

> ## Excerpt
> The FamilyElementVisibility class can be used to control the visibility of family elements in the project document. For example, if you have a door family, you may only want the door swing to be visible in plan views in the project document in which doors are placed, not 3D views. By setting the visibility on the curves of the door swing, you can control their visibility. FamilyElementVisibility is applicable to the following family element classes which have the SetVisibility() function:

---
The FamilyElementVisibility class can be used to control the visibility of family elements in the project document. For example, if you have a door family, you may only want the door swing to be visible in plan views in the project document in which doors are placed, not 3D views. By setting the visibility on the curves of the door swing, you can control their visibility. FamilyElementVisibility is applicable to the following family element classes which have the SetVisibility() function:

-   GenericForm, which is the base class for form classes such as Sweep and Extrusion
    
-   SymbolicCurve
    
-   ModelText
    
-   CurveByPoints
    
-   ModelCurve
    
-   ReferencePoint
    
-   ImportInstance
    

In the example below, the resulting family document will display the text "Hello World" with a line under it. When the family is loaded into a Revit project document and an instance is placed, in plan view, only the line will be visible. In 3D view, both the line and text will be displayed, unless the Detail Level is set to Course, in which case the line will disappear.

<table summary="" id="GUID-3148B66A-44F4-4D68-BDAA-0791CDD121E3__TABLE_5940D4D71B734F87AD0BE5D62C49D102"><tbody><tr><td><b>Code Region 13-10: Setting family element visibility</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateAndSetVisibility</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> familyDocument</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a new ModelCurve in the family document</span><span>
    XYZ p0 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> line1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p0</span><span>,</span><span> p1</span><span>);</span><span>

    </span><span>ModelCurve</span><span> modelCurve1 </span><span>=</span><span> familyDocument</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line1</span><span>,</span><span> sketchPlane</span><span>);</span><span>

    </span><span>// create a new ModelText along ModelCurve line</span><span>
    </span><span>ModelText</span><span> text </span><span>=</span><span> familyDocument</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelText</span><span>(</span><span>"Hello World"</span><span>,</span><span> </span><span>null</span><span>,</span><span> sketchPlane</span><span>,</span><span> p0</span><span>,</span><span> </span><span>HorizontalAlign</span><span>.</span><span>Center</span><span>,</span><span> </span><span>0.1</span><span>);</span><span>

    </span><span>// set visibility for text</span><span>
    </span><span>FamilyElementVisibility</span><span> textVisibility </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyElementVisibility</span><span>(</span><span>FamilyElementVisibilityType</span><span>.</span><span>Model</span><span>);</span><span>
    textVisibility</span><span>.</span><span>IsShownInTopBottom</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    text</span><span>.</span><span>SetVisibility</span><span>(</span><span>textVisibility</span><span>);</span><span>

    </span><span>// set visibility for line</span><span>
    </span><span>FamilyElementVisibility</span><span> curveVisibility </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyElementVisibility</span><span>(</span><span>FamilyElementVisibilityType</span><span>.</span><span>Model</span><span>);</span><span>
    curveVisibility</span><span>.</span><span>IsShownInCoarse</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    modelCurve1</span><span>.</span><span>SetVisibility</span><span>(</span><span>curveVisibility</span><span>);</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>
