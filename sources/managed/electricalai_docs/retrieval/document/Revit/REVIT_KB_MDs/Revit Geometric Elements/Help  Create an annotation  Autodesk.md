---
created: 2026-01-28T20:59:12 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Creating_elements_in_families_Create_an_annotation_html
author: 
---

# Help | Create an annotation | Autodesk

> ## Excerpt
> New annotations such as Dimensions and ModelText and TextNote objects can also be created in families, as well as curve annotation elements such as SymbolicCurve, ModelCurve, and DetailCurve. See Annotation Elements for more information on Annotation elements.

---
New annotations such as Dimensions and ModelText and TextNote objects can also be created in families, as well as curve annotation elements such as SymbolicCurve, ModelCurve, and DetailCurve. See [Annotation Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html) for more information on Annotation elements.

Additionally, a new Alignment can be added, referencing a View that determines the orientation of the alignment, and two geometry references.

The following example demonstrates how to create a new arc length Dimension.

<table summary="" id="GUID-01EE5DD8-6C69-41DB-BBCA-C5C624E826CB__TABLE_954B297407434A96A5A0F1364C67961B"><tbody><tr><td><b>Code Region: Creating a Dimension</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Dimension</span><span> </span><span>CreateArcDimension</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>SketchPlane</span><span> sketchPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>Application</span><span> appCreate </span><span>=</span><span> document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>;</span><span>
    </span><span>Line</span><span> gLine1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Line</span><span> gLine2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>4</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Arc</span><span> arctoDim </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    </span><span>Arc</span><span> arcofDim </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>2</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0.8</span><span>,</span><span> </span><span>2.8</span><span>,</span><span> </span><span>0</span><span>));</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyItemFactory</span><span> creationFamily </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>;</span><span>
    </span><span>ModelCurve</span><span> modelCurve1 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>gLine1</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelCurve2 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>gLine2</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelCurve3 </span><span>=</span><span> creationFamily</span><span>.</span><span>NewModelCurve</span><span>(</span><span>arctoDim</span><span>,</span><span> sketchPlane</span><span>);</span><span>
    </span><span>//get their reference</span><span>
    </span><span>Reference</span><span> ref1 </span><span>=</span><span> modelCurve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>
    </span><span>Reference</span><span> ref2 </span><span>=</span><span> modelCurve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>
    </span><span>Reference</span><span> arcRef </span><span>=</span><span> modelCurve3</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>;</span><span>

    </span><span>Dimension</span><span> newArcDim </span><span>=</span><span> creationFamily</span><span>.</span><span>NewArcLengthDimension</span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>,</span><span> arcofDim</span><span>,</span><span> arcRef</span><span>,</span><span> ref1</span><span>,</span><span> ref2</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>newArcDim </span><span>==</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Failed to create new arc length dimension."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> newArcDim</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-813DEE5B-AD67-4892-934A-EF192F72A5BB-low.png)

**Figure 51: Resulting arc length dimension**

Some types of dimensions can be labeled with a FamilyParameter. Dimensions that cannot be labeled will throw an Autodesk.Revit.Exceptions.InvalidOperationException if you try to get or set the Label property. In the following example, a new linear dimension is created between two lines and labeled as "width".

<table summary="" id="GUID-01EE5DD8-6C69-41DB-BBCA-C5C624E826CB__TABLE_F95E9433967249F6BBC1BA5A604287A9"><tbody><tr><td><b>Code Region: Labeling a dimension</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Dimension</span><span> </span><span>CreateLinearDimension</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// first create two lines</span><span>
    XYZ pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>
    </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>pt1</span><span>.</span><span>CrossProduct</span><span>(</span><span>pt2</span><span>),</span><span> pt2</span><span>);</span><span>
    </span><span>SketchPlane</span><span> skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve1 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>

    pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>5</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>
    plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>pt1</span><span>.</span><span>CrossProduct</span><span>(</span><span>pt2</span><span>),</span><span> pt2</span><span>);</span><span>
    skplane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>
    </span><span>ModelCurve</span><span> modelcurve2 </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewModelCurve</span><span>(</span><span>line</span><span>,</span><span> skplane</span><span>);</span><span>

    </span><span>// now create a linear dimension between them</span><span>
    </span><span>ReferenceArray</span><span> ra </span><span>=</span><span> </span><span>new</span><span> </span><span>ReferenceArray</span><span>();</span><span>
    ra</span><span>.</span><span>Append</span><span>(</span><span>modelcurve1</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>
    ra</span><span>.</span><span>Append</span><span>(</span><span>modelcurve2</span><span>.</span><span>GeometryCurve</span><span>.</span><span>Reference</span><span>);</span><span>

    pt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>5</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    pt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pt1</span><span>,</span><span> pt2</span><span>);</span><span>

    </span><span>Dimension</span><span> dim </span><span>=</span><span> document</span><span>.</span><span>FamilyCreate</span><span>.</span><span>NewLinearDimension</span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>,</span><span> line</span><span>,</span><span> ra</span><span>);</span><span>

    </span><span>// create a label for the dimension called "width"</span><span>
    </span><span>FamilyParameter</span><span> param </span><span>=</span><span> document</span><span>.</span><span>FamilyManager</span><span>.</span><span>AddParameter</span><span>(</span><span>"width"</span><span>,</span><span> 
        </span><span>GroupTypeId</span><span>.</span><span>Constraints</span><span>,</span><span>
        </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>,</span><span> </span><span>false</span><span>);</span><span>

    dim</span><span>.</span><span>FamilyLabel</span><span> </span><span>=</span><span> param</span><span>;</span><span>

    </span><span>return</span><span> dim</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

!\[\](../../../../images/GUID-802D577E-3791-4286-A288-0B7858C6459C-low.png)

**Figure 52: Labeled linear dimension**
