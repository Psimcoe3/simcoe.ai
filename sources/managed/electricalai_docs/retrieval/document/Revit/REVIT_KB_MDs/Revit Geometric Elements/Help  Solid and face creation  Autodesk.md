---
created: 2026-01-28T21:02:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Solid_and_face_creation_html
author: 
---

# Help | Solid and face creation | Autodesk

> ## Excerpt
> Solids and faces are sometimes used as inputs to other utilities. The Revit API provides several routines which can be used to create such geometry from scratch or to derive it from other inputs.

---
Solids and faces are sometimes used as inputs to other utilities. The Revit API provides several routines which can be used to create such geometry from scratch or to derive it from other inputs.

### _Transformed geometry_

The method

-   GeometryElement.GetTransformed()

returns a copy of the input geometry element with a transformation applied. Because this geometry is a copy, its members cannot be used as input references to other Revit elements, but it can be used geometric analysis and extraction.

### _Geometry creation utilities_

The GeometryCreationUtilities class is a utility class that allows construction of basic solid shapes:

-   Extrusion
-   Loft
-   Revolution
-   Sweep
-   Blend
-   SweptBlend

The resulting geometry is not added to the document as a part of any element. However, the created Solid can be used as inputs to other API functions, including:

-   As the input face(s) to the methods in the Analysis Visualization framework (SpatialFieldManager.AddSpatialFieldPrimitive()) – this allows the user to visualize the created shape relative to other elements in the document
-   As the input solid to finding 3D elements by intersection
-   As one or more of the inputs to a Boolean operation
-   As a part of a geometric calculation (using, for example, Face.Project(), Face.Intersect(), or other Face, Solid, and Edge geometry methods)

The following example uses the GeometryCreationUtilities class to create cylindrical shapes based on a location and height. This might be used, for example, to create volumes around the ends of a wall in order to find other walls within close proximity to the wall end points:

<table summary="" id="GUID-602B5423-953C-4EB0-9475-A8B76B726DE8__TABLE_0860632902034A54B3FF48179F4DC114"><tbody><tr><td><b>Code Region: Create cylindrical solid</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeCyl</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ endPoint</span><span>,</span><span> </span><span>double</span><span> height</span><span>,</span><span> </span><span>double</span><span> elevation</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Build cylinder centered at wall end point, extending 3' in diameter</span><span>
    </span><span>CurveLoop</span><span> cylinderLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
    XYZ arcCenter </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>endPoint</span><span>.</span><span>X</span><span>,</span><span> endPoint</span><span>.</span><span>Y</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>Application</span><span> application </span><span>=</span><span> wall</span><span>.</span><span>Document</span><span>.</span><span>Application</span><span>;</span><span>
    </span><span>Arc</span><span> firstArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>arcCenter</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>
    </span><span>Arc</span><span> secondArc </span><span>=</span><span> </span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>arcCenter</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>

    cylinderLoop</span><span>.</span><span>Append</span><span>(</span><span>firstArc</span><span>);</span><span>
    cylinderLoop</span><span>.</span><span>Append</span><span>(</span><span>secondArc</span><span>);</span><span>

    </span><span>List</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> singleLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>CurveLoop</span><span>&gt;();</span><span>
    singleLoop</span><span>.</span><span>Add</span><span>(</span><span>cylinderLoop</span><span>);</span><span>

    </span><span>Solid</span><span> proximityCylinder </span><span>=</span><span> </span><span>GeometryCreationUtilities</span><span>.</span><span>CreateExtrusionGeometry</span><span>(</span><span>singleLoop</span><span>,</span><span> XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> height</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### _Boolean operations_

The BooleanOperationsUtils class provides methods for combining a pair of solid geometry objects.

The ExecuteBooleanOperation() method takes a copy of the input solids and produces a new solid as a result. Its first argument can be any solid, either obtained directly from a Revit element or created via another operation like GeometryCreationUtils.

The method ExecuteBooleanOperationModifyingOriginalSolid() performs the boolean operation directly on the first input solid. The first input must be a solid which is not obtained directly from a Revit element. The property GeometryObject.IsElementGeometry can identify whether the solid is appropriate as input for this method.

Options to both methods include the operations type: Union, Difference, or Intersect. The following example demonstrates how to get the intersection of two solids and then find the volume.

<table summary="" id="GUID-602B5423-953C-4EB0-9475-A8B76B726DE8__TABLE_F939877456144C2E9923658BD21FEB17"><tbody><tr><td><b>Code Region: Volume of Solid Intersection</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ComputeIntersectionVolume</span><span>(</span><span>Solid</span><span> solidA</span><span>,</span><span> </span><span>Solid</span><span> solidB</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Solid</span><span> intersection </span><span>=</span><span> </span><span>BooleanOperationsUtils</span><span>.</span><span>ExecuteBooleanOperation</span><span>(</span><span>solidA</span><span>,</span><span> solidB</span><span>,</span><span> </span><span>BooleanOperationsType</span><span>.</span><span>Intersect</span><span>);</span><span>

    </span><span>double</span><span> volumeOfIntersection </span><span>=</span><span> intersection</span><span>.</span><span>Volume</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The methods CutWithHalfSpace() and CutWithHalfSpaceModifyingOriginalSolid() produce a solid which is the intersection of the input Solid with the half-space on the positive side of the given Plane. The positive side of the plane is the side to which Plane.Normal points. The first method creates a new Solid with the results, while the second modifies the existing solid (which must be a solid created by the application instead of one obtained from a Revit element).
