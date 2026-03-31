---
created: 2026-01-28T21:04:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_DirectShape_html
author: 
---

# Help | DirectShape | Autodesk

> ## Excerpt
> This element type can store arbitrary geometry created by the Revit API or obtained from import operations or calculations in either a project or family document.

---
This element type can store arbitrary geometry created by the Revit API or obtained from import operations or calculations in either a project or family document.

The DirectShape element and related classes support the ability to store externally created geometric shapes in a Revit document. The geometry can include closed solids or meshes. DirectShape is primarily intended for importing shapes from other data formats such as IFC or STEP where not enough information is available to create a "real" Revit element.

A DirectShape object may be assigned a top-level Model category, such as the Wall category. Sub-categories cannot be assigned to DirectShape elements. The IsValidCategoryId() method can test a category id to make sure it is a top-level built-in category approved for use with DirectShape and the Category.CategoryType enumerated value will indicated if the category type is Model. Assigning a category will affect how that object is displayed in Revit and will grant the object a collection of available parameters and some limited behaviors.

## Creation

The static CreateElement() method will create a new instance-level DirectShape. It requires the document in which the DirectShape will be added and the id of an appropriate built-in category. DirectShape provides the ApplicationId and ApplicationDataId string parameters that provide context for the source of the created shape.

Once the DirectShape is created, the shape can be set using one of the overloaded SetShape() method. The shape can be set either directly from a ShapeBuilder object or from a list of GeometryObjects. If you are using a ShapeBuilder object to construct geometry for the DirectShape anyway, there may be a slight performance advantage to using the ShapeBuilder input, as Revit will bypass repetitive validation of the input geometry. It is also possible to append additional geometry objects to the DirectShape using versions of the AppendShape() method. Note that AppendShape() will not merge or join the incoming geometry with any geometry already present, the geometry will be stored independently.

DirectShapes accept the following geometry types as input:

-   Solid (this can be a closed or open shell)
-   Mesh
-   Curve
-   Point

In addition, you can specify geometry to be used in a view-specific representation of a DirectShape. This geometry is input along with the input of a DirectShapeTargetViewType. When setting a view-specific shape representation, it will only be used in views of that type. Currently the only view-specific representation supported is for Plan views.

`DirectShapeType.SetFamilyName()` provides the ability to set a custom Family name for a DirectShapeType. The validator: `DirectShapeType.CanChangeFamilyName()` provides the ability to check if a DirectShapeType supports a custom Family name because certain categories do not support custom Family names.

The following example demonstrates how to create a simple DirectShape from a sphere created using the GeometryCreationUtilities class. Note the use of a reference Frame in creating the geometry. Prior to using it to create geometry, it is good practice to call the static method Frame.CanDefineRevitGeometry() which tests whether the supplied Frame object may be used to define a Revit curve or surface. In order to satisfy the requirements the Frame must be orthonormal and its origin is expected to lie within the Revit design limits. (When creating geometry, it also can be useful to use the static XYZ. IsWithinLengthLimits() to ensure the point is within Revit design limits.)

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region: Create a DirectShape</b></td></tr><tr><td><pre><code><span>// Create a DirectShape Sphere</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreateSphereDirectShape</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> profile </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>

    </span><span>// first create sphere with 2' radius</span><span>
    XYZ center </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    </span><span>double</span><span> radius </span><span>=</span><span> </span><span>2.0</span><span>;</span><span>    
    XYZ profile00 </span><span>=</span><span> center</span><span>;</span><span>
    XYZ profilePlus </span><span>=</span><span> center </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> radius</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ profileMinus </span><span>=</span><span> center </span><span>-</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> radius</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    profile</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>profilePlus</span><span>,</span><span> profileMinus</span><span>));</span><span>
    profile</span><span>.</span><span>Add</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>profileMinus</span><span>,</span><span> profilePlus</span><span>,</span><span> center </span><span>+</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>radius</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>)));</span><span>

    </span><span>CurveLoop</span><span> curveLoop </span><span>=</span><span> </span><span>CurveLoop</span><span>.</span><span>Create</span><span>(</span><span>profile</span><span>);</span><span>
    </span><span>SolidOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>SolidOptions</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>,</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>);</span><span>

    </span><span>Frame</span><span> frame </span><span>=</span><span> </span><span>new</span><span> </span><span>Frame</span><span>(</span><span>center</span><span>,</span><span> XYZ</span><span>.</span><span>BasisX</span><span>,</span><span> </span><span>-</span><span>XYZ</span><span>.</span><span>BasisZ</span><span>,</span><span> XYZ</span><span>.</span><span>BasisY</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>Frame</span><span>.</span><span>CanDefineRevitGeometry</span><span>(</span><span>frame</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Solid</span><span> sphere </span><span>=</span><span> </span><span>GeometryCreationUtilities</span><span>.</span><span>CreateRevolvedGeometry</span><span>(</span><span>frame</span><span>,</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>[]</span><span> </span><span>{</span><span> curveLoop </span><span>},</span><span> </span><span>0</span><span>,</span><span> </span><span>2</span><span> </span><span>*</span><span> </span><span>Math</span><span>.</span><span>PI</span><span>,</span><span> options</span><span>);</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create sphere direct shape"</span><span>))</span><span>
        </span><span>{</span><span>
            t</span><span>.</span><span>Start</span><span>();</span><span>
            </span><span>// create direct shape and assign the sphere shape</span><span>
            </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>

            ds</span><span>.</span><span>ApplicationId</span><span> </span><span>=</span><span> </span><span>"Application id"</span><span>;</span><span>
            ds</span><span>.</span><span>ApplicationDataId</span><span> </span><span>=</span><span> </span><span>"Geometry object id"</span><span>;</span><span>
            ds</span><span>.</span><span>SetShape</span><span>(</span><span>new</span><span> </span><span>GeometryObject</span><span>[]</span><span> </span><span>{</span><span> sphere </span><span>});</span><span>
            t</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The geometry for a DirectShape can also be created using a subclass of the ShapeBuilder class or from a TessellatedShapeBuilder.

## ShapeBuilder

ViewShapeBuilder and WireframeBuilder can be used to create geometry to store in a DirectShape class. The ViewShapeBuilder class builds and verifies a view-specific shape representation. It is limited to curve-based representations for plan views. WireframeBuilder constructs a 3D shape representation consisting of points and curves. Both types of ShapeBuilders can be applied to a DirectShape element using the DirectShape.SetShape() or DirectShape.AppendShape() overload that takes a ShapeBuilder parameter.

## TessellatedShapeBuilder

TessellatedShapeBuilder can be used create solid, shell, or polymeshes bounded by a set of connected planar facets, created by adding TessellatedFace objects one by one. Faces can only be added to the build while a face set is "open". Use the OpenConnectedFaceSet() method to open a face set. After adding all the TessellatedFaces, call CloseConnectedFaceSet() to close the face set. The builder allows for the possibility of multiple face sets - in such cases the first set should represent the outer 'surface' of a body and all following sets represent interior voids. The builder tries to create a geometry valid in Revit despite inconsistencies or omissions in the input data.

After defining all faces and closing the face set, call the Build() method to build the designated geometrical objects from the stored face sets. The Target, Fallback and GraphicsStyleId properties of the TessellatedShapeBuilder can be set prior to calling Build() or default options will be used. The results of Build() are stored in the TessellatedShapeBuilder and can be retrieved by calling GetBuildResult(). The TessellatedShapeBuilderResult.GetGeometricalObjects() method will return a list of GeometryObjects which can be used with the corresponding DirectShape.SetShape() or DirectShape.AppendShape() overload, as shown in the example below.

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_D4E6AFECC0AB4FD0A2BB788053860ED3"><tbody><tr><td><b>Code Region: Create a DirectShape using TessellatedShapeBuilder</b></td></tr><tr><td><pre><code><span>// Create a pyramid-shaped DirectShape using given material for the faces</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>CreateTessellatedShape</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> materialId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> loopVertices </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>4</span><span>);</span><span>

    </span><span>TessellatedShapeBuilder</span><span> builder </span><span>=</span><span> </span><span>new</span><span> </span><span>TessellatedShapeBuilder</span><span>();</span><span>

    builder</span><span>.</span><span>OpenConnectedFaceSet</span><span>(</span><span>true</span><span>);</span><span>
    </span><span>// create a pyramid with a square base 4' x 4' and 5' high</span><span>
    </span><span>double</span><span> length </span><span>=</span><span> </span><span>4.0</span><span>;</span><span>
    </span><span>double</span><span> height </span><span>=</span><span> </span><span>5.0</span><span>;</span><span>

    XYZ basePt1 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ basePt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ basePt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length</span><span>,</span><span> length</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ basePt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> length</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ apex </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>length </span><span>/</span><span> </span><span>2</span><span>,</span><span> length </span><span>/</span><span> </span><span>2</span><span>,</span><span> height</span><span>);</span><span>

    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt2</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt3</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    loopVertices</span><span>.</span><span>Clear</span><span>();</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt4</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>apex</span><span>);</span><span>
    loopVertices</span><span>.</span><span>Add</span><span>(</span><span>basePt1</span><span>);</span><span>
    builder</span><span>.</span><span>AddFace</span><span>(</span><span>new</span><span> </span><span>TessellatedFace</span><span>(</span><span>loopVertices</span><span>,</span><span> materialId</span><span>));</span><span>

    builder</span><span>.</span><span>CloseConnectedFaceSet</span><span>();</span><span>
    builder</span><span>.</span><span>Target</span><span> </span><span>=</span><span> </span><span>TessellatedShapeBuilderTarget</span><span>.</span><span>Solid</span><span>;</span><span>
    builder</span><span>.</span><span>Fallback</span><span> </span><span>=</span><span> </span><span>TessellatedShapeBuilderFallback</span><span>.</span><span>Abort</span><span>;</span><span>
    builder</span><span>.</span><span>Build</span><span>();</span><span>

    </span><span>TessellatedShapeBuilderResult</span><span> result </span><span>=</span><span> builder</span><span>.</span><span>GetBuildResult</span><span>();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create tessellated direct shape"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>
        ds</span><span>.</span><span>ApplicationId</span><span> </span><span>=</span><span> </span><span>"Application id"</span><span>;</span><span>
        ds</span><span>.</span><span>ApplicationDataId</span><span> </span><span>=</span><span> </span><span>"Geometry object id"</span><span>;</span><span>

        ds</span><span>.</span><span>SetShape</span><span>(</span><span>result</span><span>.</span><span>GetGeometricalObjects</span><span>());</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The image below is the result of running the example above with a concrete material id specified.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/Pyramid.png)

## BRepBuilder

The BRepBuilder class offers the ability to construct Revit boundary representation geometry (solids, open shells, etc.) as a result of inputs of surfaces, edges, and boundary loops of edges. If the construction of the boundary representation is successful, the resulting geometry objects can be used directly in any other Revit tool that accepts geometry, or the BRepBuilder can be passed directly to populate a DirectShape via the SetShape() and AppendShape() methods of the DirectShape class. Below is an example of using the SetShape() method to assign a cylinder shape to a new DirectShape object.

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_E5B535EB5616463799438793E978063A"><tbody><tr><td><b>Code Region: Create a DirectShape using BRepBuilder</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateDirectShapeFromCylinder</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Naming convention for faces and edges: we assume that x is to the left and pointing down, y is horizontal and pointing to the right, z is up</span><span>
    </span><span>BRepBuilder</span><span> brepBuilder </span><span>=</span><span> </span><span>new</span><span> </span><span>BRepBuilder</span><span>(</span><span>BRepType</span><span>.</span><span>Solid</span><span>);</span><span>

    </span><span>// The surfaces of the four faces.</span><span>
    </span><span>Frame</span><span> basis </span><span>=</span><span> </span><span>new</span><span> </span><span>Frame</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>));</span><span>
    </span><span>CylindricalSurface</span><span> cylSurf </span><span>=</span><span> </span><span>CylindricalSurface</span><span>.</span><span>Create</span><span>(</span><span>basis</span><span>,</span><span> </span><span>50</span><span>);</span><span>
    </span><span>Plane</span><span> top </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>100</span><span>));</span><span>  </span><span>// normal points outside the cylinder</span><span>
    </span><span>Plane</span><span> bottom </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span> </span><span>// normal points inside the cylinder</span><span>

    </span><span>// Add the four faces</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontCylFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>cylSurf</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backCylFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>cylSurf</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> topFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>top</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>false</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> bottomFaceId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddFace</span><span>(</span><span>BRepBuilderSurfaceGeometry</span><span>.</span><span>Create</span><span>(</span><span>bottom</span><span>,</span><span> </span><span>null</span><span>),</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// Geometry for the four semi-circular edges and two vertical linear edges</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> frontEdgeBottom </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>50</span><span>,</span><span> </span><span>0</span><span>)));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> backEdgeBottom </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>150</span><span>,</span><span> </span><span>0</span><span>)));</span><span>

    </span><span>BRepBuilderEdgeGeometry</span><span> frontEdgeTop </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>50</span><span>,</span><span> </span><span>100</span><span>)));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> backEdgeTop </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>Arc</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>50</span><span>,</span><span> </span><span>-</span><span>150</span><span>,</span><span> </span><span>100</span><span>)));</span><span>

    </span><span>BRepBuilderEdgeGeometry</span><span> linearEdgeFront </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>
    </span><span>BRepBuilderEdgeGeometry</span><span> linearEdgeBack </span><span>=</span><span> </span><span>BRepBuilderEdgeGeometry</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>-</span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>

    </span><span>// Add the six edges</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontEdgeBottomId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>frontEdgeBottom</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> frontEdgeTopId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>frontEdgeTop</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> linearEdgeFrontId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>linearEdgeFront</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> linearEdgeBackId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>linearEdgeBack</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backEdgeBottomId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>backEdgeBottom</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> backEdgeTopId </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddEdge</span><span>(</span><span>backEdgeTop</span><span>);</span><span>

    </span><span>// Loops of the four faces</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Top </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>topFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Bottom </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>bottomFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Front </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>frontCylFaceId</span><span>);</span><span>
    </span><span>BRepBuilderGeometryId</span><span> loopId_Back </span><span>=</span><span> brepBuilder</span><span>.</span><span>AddLoop</span><span>(</span><span>backCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the front face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> linearEdgeBackId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> frontEdgeTopId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> linearEdgeFrontId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Front</span><span>,</span><span> frontEdgeBottomId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Front</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>frontCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the back face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> linearEdgeBackId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> backEdgeBottomId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> linearEdgeFrontId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Back</span><span>,</span><span> backEdgeTopId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Back</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>backCylFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the top face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Top</span><span>,</span><span> backEdgeTopId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Top</span><span>,</span><span> frontEdgeTopId</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Top</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>topFaceId</span><span>);</span><span>

    </span><span>// Add coedges for the loop of the bottom face</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Bottom</span><span>,</span><span> frontEdgeBottomId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>AddCoEdge</span><span>(</span><span>loopId_Bottom</span><span>,</span><span> backEdgeBottomId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishLoop</span><span>(</span><span>loopId_Bottom</span><span>);</span><span>
    brepBuilder</span><span>.</span><span>FinishFace</span><span>(</span><span>bottomFaceId</span><span>);</span><span>

    brepBuilder</span><span>.</span><span>Finish</span><span>();</span><span>

    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> tr </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create a DirectShape"</span><span>))</span><span>
    </span><span>{</span><span>
        tr</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>DirectShape</span><span> ds </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_GenericModel</span><span>));</span><span>
        ds</span><span>.</span><span>SetShape</span><span>(</span><span>brepBuilder</span><span>);</span><span>
        tr</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## ShapeImporter

The ShapeImporter utility class supports conversion of geometry stored in external formats (such as SAT and Rhino) into a collection of GeometryObjects which can be used to set the shape for a DirectShape. Use ShapeImporter.Convert() to generate the geometry objects (and where possible, corresponding materials and graphics styles in the associated document).

<table summary="" id="GUID-DF7B9D4A-5A8A-4E39-8721-B7782CBD7730__TABLE_D5D17D249DC2417B8E406A17C21F8D63"><tbody><tr><td><b>Code Region: Create a DirectShape from SAT file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ReadSATFile</span><span>(</span><span>Document</span><span> revitDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Allow the user to select a SAT file.</span><span>
    </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>OpenFileDialog</span><span> ofd </span><span>=</span><span> </span><span>new</span><span> </span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>OpenFileDialog</span><span>();</span><span>
    ofd</span><span>.</span><span>Filter</span><span> </span><span>=</span><span> </span><span>"SAT Files (*.sat)|*.sat"</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>System</span><span>.</span><span>Windows</span><span>.</span><span>Forms</span><span>.</span><span>DialogResult</span><span>.</span><span>OK </span><span>==</span><span> ofd</span><span>.</span><span>ShowDialog</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>ShapeImporter</span><span> shapeImporter </span><span>=</span><span> </span><span>new</span><span> </span><span>ShapeImporter</span><span>();</span><span>
        shapeImporter</span><span>.</span><span>InputFormat</span><span> </span><span>=</span><span> </span><span>ShapeImporterSourceFormat</span><span>.</span><span>SAT</span><span>;</span><span> 
        </span><span>IList</span><span>&lt;</span><span>GeometryObject</span><span>&gt;</span><span> shapes </span><span>=</span><span> shapeImporter</span><span>.</span><span>Convert</span><span>(</span><span>revitDoc</span><span>,</span><span> ofd</span><span>.</span><span>FileName</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>shapes</span><span>.</span><span>Count</span><span> </span><span>!=</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> tr </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>revitDoc</span><span>,</span><span> </span><span>"Create a DirectShape"</span><span>))</span><span>
            </span><span>{</span><span>
                tr</span><span>.</span><span>Start</span><span>();</span><span>

                </span><span>DirectShape</span><span> dsImportedSat </span><span>=</span><span> </span><span>DirectShape</span><span>.</span><span>CreateElement</span><span>(</span><span>revitDoc</span><span>,</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>));</span><span>
                dsImportedSat</span><span>.</span><span>SetShape</span><span>(</span><span>shapes</span><span>);</span><span>

                tr</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Reference Curves, Planes, and Points

The methods:

-   DirectShape.AddReferenceCurve()
-   DirectShape.AddReferencePlane()
-   DirectShape.AddReferencePoint()
-   DirectShapeType.AddReferenceCurve()
-   DirectShapeType.AddReferencePlane()
-   DirectShapeType.AddReferencePoint()

enable the creation of reference curves, planes and points inside DirectShape elements. Explicit bounds can be provided for direct shape reference curves and planes. Revit tools that can use named references within families will also be able to select the references inside the DirectShape elements.

The overloads for these methods include an optional `DirectShapeReferenceOptions` input. Use `DirectShapeReferenceOptions.Name` to set the assigned name for the reference. If the name is specified, it is visible when picking the reference's geometry. Otherwise, the default DirectShape element name is displayed. The validator `DirectShapeReferenceOptions.IsValidReferenceName()` validates the name assigned to DirectShapeReferenceOptions.Name.

The validators:

-   DirectShape.IsValidReferenceCurve()
-   DirectShape.IsValidReferencePlaneBoundingBoxUV()
-   DirectShapeType.IsValidReferenceCurve()
-   DirectShapeType.IsValidReferencePlaneBoundingBoxUV()

validates the inputs needed for specifying a plane or curve explicit reference in the DirectShape.

## Options

The DirectShapeOptions class is used to control behavior of a DirectShape object. Use DirectShape.SetOptions() to set the options used by a DirectShape object. The GetOptions() method will return the DirectShapeOptions currently used by the DirectShape object.

DirectShape elements, by default, support element references, including dimensions, alignments, and face hosting, as well as snapping. This default behavior can be changed using the DirectShapeOptions.ReferencingOption property. If it is set to NotReferenceable, the geometry may not be used for dimensioning, snapping, alignment, or face-hosting. The element may still be selected by the user for operations which do not reference individual geometry objects.

DirectShape elements also support the ability to participate in room boundary calculations, if they are of an appropriate category for room boundary calculations, and if the associated "Room Bounding" parameter is set to true. The property DirectShapeOptions.RoomBoundingOption identifies whether the DirectShape supports an option for the "Room Bounding" parameter to permit participation in room boundary calculations. The default value is NotApplicable, but this will be changed automatically to SetByParameter for applicable DirectShapes.

## Tagging Direct Shape Geometry

References (such as dimensions) to DirectShape geometry can be maintained when the geometry changes. To do this, add geometry to the DirectShape using the `AddExternallyTaggedGeometry` method. The sample below shows how to create an instance of the `BRepBuilderPersistentIds` class and use `AddSubTag` to build a map of named `ExternalGeometryId`'s and their corresponding `BRepBuilderGeometryId`'s. When the geometry is modified, use `UpdateExternallyTaggedGeometry` and use the same names for the `ExternalGeometryId`'s that you will associate with the new geometry.

The _CreateDirectShape_ sample creates a direct shape with a face named "face1". After running this command, manually create a dimension that references this face. Then run _ModifyDirectShape_ to create a new face in the direct shape. Because the old and new faces are both named "face1", the dimension will survive the operation and reference the new face. If you change the _ModifyDirectShape_ code to give the face a different name, then the dimension will fail regeneration with the error that "One or more dimension references are or have become invalid.".

```
public DirectShape CreateDirectShape(Document doc)
{
    DirectShape ds;    
    using (Transaction tr = new Transaction(doc, "Create DirectShape"))
    {
        tr.Start();
        ds = DirectShape.CreateElement(doc, new ElementId(BuiltInCategory.OST_GenericModel));
        ds.AddExternallyTaggedGeometry(CreateTriangularFace("face1", 1));
        tr.Commit();
    }
    return ds;
}


public void ModifyDirectShape(DirectShape ds)
{
    using (Transaction tr = new Transaction(ds.Document, "Update DirectShape"))
    {
        tr.Start();
        ds.UpdateExternallyTaggedGeometry(CreateTriangularFace("face1", 10));
        tr.Commit();
    }
}

private ExternallyTaggedBRep CreateTriangularFace(string name, double x)
{
    BRepBuilder brepBuilder = new BRepBuilder(BRepType.OpenShell);

    XYZ pt0 = new XYZ(x, 0, 0);
    XYZ pt1 = new XYZ(x, 10, 0);
    XYZ pt2 = new XYZ(x, 10, 10);

    BRepBuilderGeometryId faceId = brepBuilder.AddFace(BRepBuilderSurfaceGeometry.Create(
        Plane.CreateByOriginAndBasis(pt0, XYZ.BasisZ, XYZ.BasisY), null), true);

    BRepBuilderGeometryId loopId = brepBuilder.AddLoop(faceId);
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt0, pt1)), false); 
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt1, pt2)), false); 
    brepBuilder.AddCoEdge(loopId, brepBuilder.AddEdge(BRepBuilderEdgeGeometry.Create(pt2, pt0)), false); 
    brepBuilder.FinishLoop(loopId);

    brepBuilder.FinishFace(faceId);
    brepBuilder.Finish();

    BRepBuilderPersistentIds persistentIds = new BRepBuilderPersistentIds(brepBuilder);
    persistentIds.AddSubTag(new ExternalGeometryId(name), faceId);
    ExternallyTaggedBRep result = brepBuilder.GetResult(new ExternalGeometryId("MyShape"), persistentIds);

    return result;
}
```
