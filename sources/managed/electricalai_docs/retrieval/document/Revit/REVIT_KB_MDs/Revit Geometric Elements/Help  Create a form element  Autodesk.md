---
created: 2026-01-28T20:59:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_a_form_element_html
author: 
---

# Help | Create a form element | Autodesk

> ## Excerpt
> The FamilyItemFactory class provides the ability to create form elements in families, such as extrusions, revolutions, sweeps, and blends. See the section on 3D Sketch for more information on these 3D sketch forms.

---
The FamilyItemFactory class provides the ability to create form elements in families, such as extrusions, revolutions, sweeps, and blends. See the section on [3D Sketch](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_3D_Sketch_html) for more information on these 3D sketch forms.

The following example demonstrates how to create a new Extrusion element. It creates a simple rectangular profile and then moves the newly created Extrusion to a new location.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_21A660DE8C3548309D47015C25B61CCD"><tbody><tr><td><b>Code Region: Creating a new Extrusion</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Extrusion</span><span> </span><span>CreateExtrusion</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Extrusion</span><span> rectExtrusion </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// make sure we have a family document</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// define the profile for the extrusion</span><span>
        </span><span>CurveArrArray</span><span> curveArrArray </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArrArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray1 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray2 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> curveArray3 </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>

        </span><span>// create a rectangular profile</span><span>
        XYZ p0 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
        XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>Line</span><span> line1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p0</span><span>,</span><span> p1</span><span>);</span><span>
        </span><span>Line</span><span> line2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>
        </span><span>Line</span><span> line3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p2</span><span>,</span><span> p3</span><span>);</span><span>
        </span><span>Line</span><span> line4 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p3</span><span>,</span><span> p0</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line1</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line2</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line3</span><span>);</span><span>
        curveArray1</span><span>.</span><span>Append</span><span>(</span><span>line4</span><span>);</span><span>

        curveArrArray</span><span>.</span><span>Append</span><span>(</span><span>curveArray1</span><span>);</span><span>

        </span><span>// create solid rectangular extrusion</span><span>
        rectExtrusion </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewExtrusion</span><span>(</span><span>true</span><span>,</span><span> curveArrArray</span><span>,</span><span> sketchPlane</span><span>,</span><span> </span><span>10</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> rectExtrusion</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// move extrusion to proper place</span><span>
            XYZ transPoint1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>16</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>ElementTransformUtils</span><span>.</span><span>MoveElement</span><span>(</span><span>document</span><span>,</span><span> rectExtrusion</span><span>.</span><span>Id</span><span>,</span><span> transPoint1</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new Extrusion failed."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a Family document before invoking this command."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> rectExtrusion</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following sample shows how to create a new Sweep from a solid ovoid profile in a Family Document.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_4FB266F3F8BA46A093E6C4D0F40CACB7"><tbody><tr><td><b>Code Region: Creating a new Sweep</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Sweep</span><span> </span><span>CreateSweep</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Sweep</span><span> sweep </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// make sure we have a family document</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> document</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Define a profile for the sweep</span><span>
        </span><span>CurveArrArray</span><span> arrarr </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArrArray</span><span>();</span><span>
        </span><span>CurveArray</span><span> arr </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>

        </span><span>// Create an ovoid profile</span><span>
        XYZ pnt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        arr</span><span>.</span><span>Append</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>pnt2</span><span>,</span><span> </span><span>1.0d</span><span>,</span><span> </span><span>0.0d</span><span>,</span><span> </span><span>180.0d</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>));</span><span>
        arr</span><span>.</span><span>Append</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>pnt1</span><span>,</span><span> pnt3</span><span>,</span><span> pnt2</span><span>));</span><span>
        arrarr</span><span>.</span><span>Append</span><span>(</span><span>arr</span><span>);</span><span>
        </span><span>SweepProfile</span><span> profile </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewCurveLoopsProfile</span><span>(</span><span>arrarr</span><span>);</span><span>

        </span><span>// Create a path for the sweep</span><span>
        XYZ pnt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ pnt5 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>Curve</span><span> curve </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt4</span><span>,</span><span> pnt5</span><span>);</span><span>

        </span><span>CurveArray</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveArray</span><span>();</span><span>
        curves</span><span>.</span><span>Append</span><span>(</span><span>curve</span><span>);</span><span>

        </span><span>// create a solid ovoid sweep</span><span>
        sweep </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewSweep</span><span>(</span><span>true</span><span>,</span><span> curves</span><span>,</span><span> sketchPlane</span><span>,</span><span> profile</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>ProfilePlaneLocation</span><span>.</span><span>Start</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> sweep</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// move to proper place</span><span>
            XYZ transPoint1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>11</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>ElementTransformUtils</span><span>.</span><span>MoveElement</span><span>(</span><span>document</span><span>,</span><span> sweep</span><span>.</span><span>Id</span><span>,</span><span> transPoint1</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create a new Sweep."</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Please open a Family document before invoking this command."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> sweep</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-169B9078-7508-4982-B10D-333FF97CA345-low.png)

**Figure 50: Ovoid sweep created by previous example**

The FreeFormElement class allows for the creation of non-parametric geometry created from an input solid outline. A FreeFormElement can participate in joins and void cuts with other combinable elements. Planar faces of the element can be offset interactively and programmatically in the face normal direction.

### Assigning Subcategories to forms

After creating a new form in a family, you may want to change the subcategory for the form. For example, you may have a Door family and want to create multiple subcategories of doors and assign different subcategories to different door types in your family.

The following example shows how to create a new subcategory, assign it a material, and then assign the subcategory to a form.

<table summary="" id="GUID-FBF9B994-ADCB-4679-B50B-2E9A1E09AA48__TABLE_9321DBB7592F4F1B9D92D156C09A5409"><tbody><tr><td><b>Code Region: Assigning a subcategory</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AssignSubCategory</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>GenericForm</span><span> extrusion</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a new subcategory</span><span>
    </span><span>Category</span><span> cat </span><span>=</span><span> document</span><span>.</span><span>OwnerFamily</span><span>.</span><span>FamilyCategory</span><span>;</span><span>
    </span><span>Category</span><span> subCat </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>Categories</span><span>.</span><span>NewSubcategory</span><span>(</span><span>cat</span><span>,</span><span> </span><span>"NewSubCat"</span><span>);</span><span>

    </span><span>// create a new material and assign it to the subcategory</span><span>
    </span><span>ElementId</span><span> materialId </span><span>=</span><span> </span><span>Material</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Wood Material"</span><span>);</span><span>
    subCat</span><span>.</span><span>Material</span><span> </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>// assign the subcategory to the element</span><span>
    extrusion</span><span>.</span><span>Subcategory</span><span> </span><span>=</span><span> subCat</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
