---
created: 2026-01-28T21:02:46 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html
author: 
---

# Help | Geometry Helper Classes | Autodesk

> ## Excerpt
> Several Geometry Helper classes are in the API. The Helper classes are used to describe geometry information for certain elements, such as defining a CropBox for a view using the BoundingBoxXYZ class.

---
Several Geometry Helper classes are in the API. The Helper classes are used to describe geometry information for certain elements, such as defining a CropBox for a view using the BoundingBoxXYZ class.

-   BoundingBoxXYZ - A 3D rectangular box used in cases such as defining a 3D view section area.
    
-   Transform - Transforming the affine 3D space.
    
-   Reference - A stable reference to a geometric object in a Revit model, which is used when creating elements like dimensions.
    
-   Plane - A flat surface in geometry.
    
-   Options - User preferences for parsing geometry.
    
-   XYZ - Object representing coordinates in 3D space.
    
-   UV - Object representing coordinates in 2D space.
    
-   BoundingBoxUV - A 2D rectangle parallel to the coordinate axes.
    
    ## Transform
    

Transforms are limited to 3x4 transformations (Matrix) in the Revit application, transforming an object's place in the model space relative to the rest of the model space and other objects. The transforms are built from the position and orientation in the model space. Three direction Vectors (BasisX, BasisY and BasisZ properties) and Origin point provide all of the transform information. The matrix formed by the four values is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-362AC8B3-CB53-4DB6-8606-5D90F2C8BFC4-low.png)Applying the transformation to the point is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5ABFA7C5-22F5-4A86-9878-CB0812834EB8-low.png)The Transform OfPoint method implements the previous function.

The Geometry.Transform class properties and methods are identified in the following sections.

### Identity

Transform the Identity.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4AD4178C-E897-44E0-93CD-AA8C1FD39AC4-low.png)CreateReflection()

### Reflect a specified plane.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DCA42587-9FD4-4AE3-95A8-1D45ED472D14-low.png)**Figure 112: Wall Reflection relationship**

As the previous picture shows, one wall is mirrored by a reference plane. The CreateReflection() method needs the geometry plane information for the reference plane.

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_55F4D5B52B234A66AB018E35EB6FEE0E"><tbody><tr><td><b>Code Region 20-8: Using the Reflection property</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>Transform</span><span> </span><span>Reflect</span><span>(</span><span>ReferencePlane</span><span> refPlane</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Transform</span><span> mirTrans </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateReflection</span><span>(</span><span>refPlane</span><span>.</span><span>GetPlane</span><span>());</span><span>

    </span><span>return</span><span> mirTrans</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### CreateRotation() and CreateRotationAtPoint()

Rotate by a specified angle around a specified axis at (0,0,0) or at a specified point.

### CreateTranslation()

Translate by a specified vector. Given a vector XYZ data, a transformation is created as follow:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E661E3C-0609-44C0-A7D5-52E993FEA94C-low.png)

### Determinant

Transformation determinant.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4570D0C0-0834-4A9E-AB7C-751F771AAE5B-low.png)

### HasReflection

This is a Boolean value that indicates whether the transformation produces a reflection.

### Scale

A value that represents the transformation scale.

### Inverse

An inverse transformation. Transformation matrix A is invertible if a transformation matrix B exists such that A_B = B_A = I (identity).

### IsIdentity

Boolean value that indicates whether this transformation is an identity.

### IsTranslation

Boolean value that indicates whether this transformation is a translation.

Geometry.Transform provides methods to perform basal matrix operations.

### Multiply

Multiplies a transformation by a specified transformation and returns the result.

Operator\* - Multiplies two specified transforms.

### ScaleBasis

Scales the basis vectors and returns the result.

### ScaleBasisAndOrigin

Scales the basis vectors and the transformation origin returns the result.

### OfPoint

Applies the transformation to the point. The Origin property is used.

### OfVector

Applies the transform to the vector. The Origin property is not used.

### AlmostEqual

Compares two transformations. AlmostEqual is consistent with the computation mechanism and accuracy in the Revit core code. Additionally, Equal and the == operator are not implemented in the Transform class.

The API provides several shortcuts to complete geometry transformation. The Transformed property in several geometry classes is used to do the work, as shown in the following table.

**Table 48: Transformed Methods**

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_9D788AF115DF454981260EDB01B11D2E"><tbody><tr><td><b>Class Name</b></td><td><b>Function Description</b></td></tr><tr><td>Curve.get_Transformed(Transform transform)</td><td>Applies the specified transformation to a curve</td></tr><tr><td>GeometryElement.GetTransformed(Transform transform)</td><td>Transforms a copy of the geometry in the original element.</td></tr><tr><td>Profile.get_Transformed(Transform transform)</td><td>Transforms the profile and returns the result.</td></tr><tr><td>Mesh.get_Transformed(Transform transform)</td><td>Transforms the mesh and returns the result.</td></tr></tbody></table>

Note: The transformed method clones itself then returns the transformed cloned result.

In addition to these methods, the Instance class (which is the parent class for elements like family instances, link instances, and imported CAD content) has two methods which provide the transform for a given Instance . The GetTransform() method obtains the basic transform for the instance based on how the instance is placed, while GetTotalTransform() provides the transform modified with the true north transform, for instances like import instances.

## Reference

The Reference is very useful in element creation.

-   Dimension creation requires references.
    
-   The reference identifies a path within a geometric representation tree in a flexible manner.
    
-   The tree is used to view specific geometric representation creation.
    

The API exposes four types of references based on different Pick pointer types. They are retrieved from the API in different ways:

1.  For Point - Curve.GetEndPointReference method
    
2.  For Curve (Line, Arc, and etc.) - Curve.Reference property
    
3.  For Face - Face.Reference property
    
4.  For Cut Edge - Edge.Reference property
    

Different reference types cannot be used arbitrarily. For example:

-   The NewLineBoundaryConditions() method requires a reference for Line
    
-   The NewAreaBoundaryConditions() method requires a reference for Face
    
-   The NewPointBoundaryConditions() method requires a reference for Point.
    

The Reference.ConvertToStableRepresentation() method can be used to save a reference to a geometry object, for example a face, edge, or curve, as a string, and later in the same Revit session (or even in a different session where the same document is present) use ParseFromStableRepresentation() method to obtain an identical Reference using the string as input.

## Options

Geometry is typically extracted from the indexed property Element.Geometry. The original geometry of a beam, column or brace, before the instance is modified by joins, cuts, coping, extensions, or other post-processing, can be extracted using the FamilyInstance.GetOriginalGeometry() method. Both Element.Geometry and FamilyInstance.GetOriginalGeometry() accept an options class which you must supply. The options class customizes the type of output you receive based on its properties:

-   ComputeReferences - Indicates whether to compute the geometry reference when retrieving geometry information. The default value is false, so if this property is not set to true, the reference will not be accessible.
    
-   IncludeNonVisibleObjects - Indicates to also return geometry objects which are not visible in a default view.
    
-   View - Gets geometry information from a specific view. Note that if a view is assigned, the detail level for this view will be used in place of "DetailLevel".
    
-   DetailLevel - Indicates the preferred detail level. The default is Medium.
    
    ### ComputeReferences
    

If you set this property to false, the API does not compute a geometry reference. All Reference properties retrieved from the geometry tree return nothing. For more details about references, refer to the Reference section. This option cannot be set to true when used with FamilyInstance.GetOriginalGeometry().

### IncludeNonVisibleObjects

Most of the non-visible geometry is construction and conditional geometry that the user sees when editing the element (i.e., the center plane of a window family instance). The default for this property is false. However, some of this conditionally visible geometry represents real-world objects, such as insulation surrounding ducts in Revit, and it should be extracted.

### View

If users set the View property to a different view, the retrieved geometry information can be different. Review the following examples for more information:

1.  In Revit, draw a stair in 3D view then select the Crop Region, Crop Region Visible, and Section Box properties in the 3D view. In the Crop Region, modify the section box in the 3D view to display a portion of the stair. If you get the geometry information for the stair using the API and set the 3D view as the Options.View property, only a part of the stair geometry can be retrieved. The following pictures show the stair in the Revit application (left) and one drawn with the API (right).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F6123E3E-4B46-4502-915A-5FC399B34045-low.png)**Figure 113: Different section boxes display different geometry**

Draw a stair in Revit then draw a section as shown in the left picture. If you get the information for this stair using the API and set this section view as the Options.View property, only a part of the stair geometry can be retrieved. The stair drawn with the API is shown in the right picture.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1095389D-A7C6-4AB8-A6C6-FC8CC3C05EAB-low.png)**Figure 114: Retrieve Geometry section view**

### DetailLevel

The API defines three enumerations in Geometry.Options.DetailLevels. The three enumerations correspond to the three Detail Levels in the Revit application, shown as follows.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-81B8A84A-2F7B-4019-8CC8-4DA11B7A176A-low.png)**Figure 115: Three detail levels**

Different geometry information is retrieved based on different settings in the DetailLevel property. For example, draw a beam in the Revit application then get the geometry from the beam using the API to draw it. The following pictures show the drawing results:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B1C82974-A3D1-4893-9DF9-E9396C7D6352-low.png)**Figure 116: Detail geometry for a beam**

## BoundingBoxXYZ

BoundingBoxXYZ defines a 3D rectangular box that is required to be parallel to any coordinate axis. Similar to the Instance class, the BoundingBoxXYZ stores data in the local coordinate space. It has a Transform property that transforms the data from the box local coordinate space to the model space. In other words, to get the box boundary in the model space (the same one in Revit), transform each data member using the Transform property. The following sections illustrate how to use BoundingBoxXYZ.

### Define the View Boundaries

BoundingBoxXYZ can be used to define the view boundaries through View.CropBox property. The following pictures use a section view to show how BoundingBoxXYZ is used in the Revit application.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C517106E-BC7F-4E89-90C4-7FFF1D6B3FD2-low.png)**Figure 117: BoundingBoxXYZ in section view**

The dash lines in the previous pictures show the section view boundary exposed as the CropBox property (a BoundingBoxXYZ instance).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-22E284B3-C514-4EB4-B322-91454006173E-low.png)**Figure 118: Created section view**

The previous picture displays the corresponding section view. The wall outside the view boundary is not displayed.

### Define a Section Box

BoundingBoxXYZ is also used to define a section box for a 3D view retrieved from the View3D.GetSectionBox() method. Select the Section Box property in the Properties Dialog box. The section box is shown as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1EA1F70A-FFC5-4C58-9446-48E73E9C5606-low.png)**Figure 119: 3D view section box**

### Other Uses

-   Defines a box around an element's geometry. (Element.BoundingBox Property). The BoundingBoxXYZ instance retrieved in this way is parallel to the coordinate axes.
    
-   Used in the ViewSection.CreateDetail () method .
    

The following table identifies the main uses for this class.

**Table 49: BoundingBoxXYZ properties**

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_79392360B14C423FB50AC7D57E87889B"><tbody><tr><td><b>Property Name</b></td><td><b>Usage</b></td></tr><tr><td>Max/Min</td><td>Maximum/Minimum coordinates. These two properties define a 3D box parallel to any coordinate axis. The Transform property provides a transform matrix that can transform the box to the appropriate position.</td></tr><tr><td>Transform</td><td>Transform from the box coordinate space to the model space.</td></tr><tr><td>Enabled</td><td>Indicates whether the bounding box is turned on.</td></tr><tr><td>MaxEnabled/ MinEnabled</td><td>Defines whether the maximum/minimum bound is active for a given dimension.<ul><li>If the Enable property is false, these two properties should also return false.</li></ul><pre><code><span>&lt;table</span><span> </span><span>cellpadding</span><span>=</span><span>"4"</span><span> </span><span>cellspacing</span><span>=</span><span>"0"</span><span> </span><span>summary</span><span>=</span><span>""</span><span> </span><span>id</span><span>=</span><span>"GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_4B666584884A4DFCA168F8AADC62FAA6"</span><span> </span><span>class</span><span>=</span><span>"table"</span><span> </span><span>frame</span><span>=</span><span>"border"</span><span> </span><span>border</span><span>=</span><span>"1"</span><span> </span><span>rules</span><span>=</span><span>"all"</span><span>&gt;</span><span>

</span><span>&lt;tbody</span><span> </span><span>class</span><span>=</span><span>"tbody"</span><span>&gt;</span><span>

</span><span>&lt;tr</span><span> </span><span>class</span><span>=</span><span>"row"</span><span>&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;&lt;img</span><span> </span><span>src</span><span>=</span><span>"../../../images/GUID-ADBBC034-E8AA-4A96-AE95-9D9F82DB5080-low.png"</span><span>/&gt;&lt;/td&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;</span><span>If the crop view is turned on, both </span><span>&lt;b&gt;&lt;i&gt;</span><span>MaxEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property and </span><span>&lt;b&gt;&lt;i&gt;</span><span>MinEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property return true.

</span><span>&lt;/td&gt;</span><span>

</span><span>&lt;/tr&gt;</span><span>

</span><span>&lt;tr</span><span> </span><span>class</span><span>=</span><span>"row"</span><span>&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;&lt;img</span><span> </span><span>src</span><span>=</span><span>"../../../images/GUID-7050609C-8AAF-40C4-A9A8-F8920B6AD022-low.png"</span><span>/&gt;&lt;/td&gt;</span><span>

</span><span>&lt;td</span><span> </span><span>class</span><span>=</span><span>"entry"</span><span> </span><span>valign</span><span>=</span><span>"top"</span><span>&gt;</span><span>If the crop view is turned off, both </span><span>&lt;b&gt;&lt;i&gt;</span><span>MaxEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property and </span><span>&lt;b&gt;&lt;i&gt;</span><span>MinEnabled</span><span>&lt;/i&gt;&lt;/b&gt;</span><span> property return false.

</span><span>&lt;/td&gt;</span><span>

</span><span>&lt;/tr&gt;</span><span>

</span><span>&lt;/tbody&gt;</span><span>

</span><span>&lt;/table&gt;</span></code></pre><ul><li>This property indicates whether the view's crop box face can be used to clip the element's view.</li><li>If BoundingBoxXYZ is retrieved from the View3D.GetSectionBox() method, the return value depends on whether the Section Box property is selected in the 3D view Properties dialog box. If so, all Enabled properties return true.</li><li>If BoundingBoxXYZ is retrieved from the Element.BoundingBox property, all the Enabled properties are true.</li></ul></td></tr><tr><td>Bounds</td><td>Wrapper for the Max/Min properties.</td></tr><tr><td>BoundEnabled</td><td>Wrapper for the MaxEnabled/MinEnabled properties.</td></tr></tbody></table>

The following code sample illustrates how to rotate BoundingBoxXYZ to modify the 3D view section box.

<table summary="" id="GUID-78445211-E211-4E27-B080-BE9FA3C50631__TABLE_BB466252BE8B4EE389A296D445E730B1"><tbody><tr><td><b>Code Region 20-9: Rotating BoundingBoxXYZ</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>RotateBoundingBox</span><span>(</span><span>View3D</span><span> view3d</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>view3d</span><span>.</span><span>IsSectionBoxActive</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The section box for View3D isn't active."</span><span>);</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>BoundingBoxXYZ</span><span> box </span><span>=</span><span> view3d</span><span>.</span><span>GetSectionBox</span><span>();</span><span>

    </span><span>// Create a rotation transform to apply to the section box </span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ axis </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>

    </span><span>// Rotate 30 degrees</span><span>
    </span><span>Transform</span><span> rotate </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateRotationAtPoint</span><span>(</span><span>axis</span><span>,</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>/</span><span>6.0</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// Transform the View3D's section box with the rotation transform</span><span>
    box</span><span>.</span><span>Transform</span><span> </span><span>=</span><span> box</span><span>.</span><span>Transform</span><span>.</span><span>Multiply</span><span>(</span><span>rotate</span><span>);</span><span>

    </span><span>// Set the section box back to the view (requires an open transaction)</span><span>
    view3d</span><span>.</span><span>SetSectionBox</span><span>(</span><span>box</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## BoundingBoxUV

BoundingBoxUV is a value class that defines a 2D rectangle parallel to the coordinate axes. It supports the Min and Max data members. Together they define the BoundingBoxUV's boundary. BoundingBoxUV is retrieved from the View.Outline property which is the boundary view in the paper space view.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3CDBA6D9-E139-482E-816C-640D56DE5E63-low.png)**Figure 120: View outline**

Two points define a BoundingBoxUV.

-   Min point - The bottom-left endpoint.
    
-   Max point - The upper-right endpoint.
    

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-71827A01-D568-4770-9457-A279F252DBFD-low.png)**Figure 121: BoundingBoxUV Max and Min**

Note: BoundingBoxUV cannot present a gradient rectangle as the following picture

shows.![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1A52815E-11F5-4305-B68E-B0A63A06718D-low.png)**Figure 122: Gradient rectangle**
