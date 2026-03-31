---
created: 2026-01-28T21:03:15 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Room_and_Space_Geometry_html
author: 
---

# Help | Room and Space Geometry | Autodesk

> ## Excerpt
> The Revit API provides access to the 3D geometry of spatial elements (rooms and spaces).

---
The Revit API provides access to the 3D geometry of spatial elements (rooms and spaces).

The SpatialElementGeometryCalculator class can be used to calculate the geometry of a spatial element and obtain the relationships between the geometry and the element's boundary elements. There are 2 options which can be provided to this utility:

-   SpatialElementBoundaryLocation – whether to use finish faces or boundary element centerlines for calculation
-   StoredFreeBoundaryFaces – whether to include faces which don’t map directly to a boundary element in the results.

The results of calculating the geometry are contained in the class SpatialElementGeometryResults. From the SpatialElementGeometryResults class, you can obtain:

-   The Solid volume representing the geometry (GetGeometry() method)
-   The boundary face information (a collection SpatialElementBoundarySubfaces)

Each subface offers:

-   The face of the spatial element
-   The matching face of the boundary element
-   The subface (the portion of the spatial element face bounded by this particular boundary element)
-   The subface type (bottom, top, or side)

Some notes about the use of this utility:

-   The calculator maintains an internal cache for geometry it has already processed. If you intend to calculate geometry for several elements in the same project you should use a single instance of this class. Note that the cache will be cleared when any change is made to the document.
-   Floors are almost never included in as boundary elements. Revit uses the 2D outline of the room to form the bottom faces and does not match them to floor geometry.
-   Openings created by wall-cutting features such as doors and windows are not included in the returned faces.
-   The geometry calculations match the capabilities offered by Revit. In some cases where Revit makes assumptions about how to calculate the volumes of boundaries of rooms and spaces, these assumptions will be present in the output of the utility.

The following example calculates a room's geometry and finds its boundary faces

<table summary="" id="GUID-E7B451BB-21DC-4D72-AD26-75F0C2E911E4__TABLE_4F3221B134B3434CA295DA59DA3ACAB9"><tbody><tr><td><b>Code Region: Face Area using SpatialElementGeometryCalculator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SpaceArea</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>Room</span><span> room</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>SpatialElementGeometryCalculator</span><span> calculator </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementGeometryCalculator</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// compute the room geometry</span><span>
    </span><span>SpatialElementGeometryResults</span><span> results </span><span>=</span><span> calculator</span><span>.</span><span>CalculateSpatialElementGeometry</span><span>(</span><span>room</span><span>);</span><span>

    </span><span>// get the solid representing the room's geometry</span><span>
    </span><span>Solid</span><span> roomSolid </span><span>=</span><span> results</span><span>.</span><span>GetGeometry</span><span>();</span><span> 

    </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> roomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>double</span><span> faceArea </span><span>=</span><span> face</span><span>.</span><span>Area</span><span>;</span><span>

        </span><span>// get the sub-faces for the face of the room</span><span>
        </span><span>IList</span><span>&lt;</span><span>SpatialElementBoundarySubface</span><span>&gt;</span><span> subfaceList </span><span>=</span><span> results</span><span>.</span><span>GetBoundaryFaceInfo</span><span>(</span><span>face</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>SpatialElementBoundarySubface</span><span> subface </span><span>in</span><span> subfaceList</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>subfaceList</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span> </span><span>// there are multiple sub-faces that define the face</span><span>
            </span><span>{</span><span>
                </span><span>// get the area of each sub-face</span><span>
                </span><span>double</span><span> subfaceArea </span><span>=</span><span> subface</span><span>.</span><span>GetSubface</span><span>().</span><span>Area</span><span>;</span><span>             

                </span><span>// sub-faces exist in situations such as when a room-bounding wall has been</span><span>
                </span><span>// horizontally split and the faces of each split wall combine to create the </span><span>
                </span><span>// entire face of the room</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example calculates a room's geometry and finds its the material of faces that belong to the elements that define the room.

<table summary="" id="GUID-E7B451BB-21DC-4D72-AD26-75F0C2E911E4__TABLE_4896E7E727404ECEB22C3F74F8CB3E78"><tbody><tr><td><b>Code Region: Face Material using SpatialElementGeometryCalculator</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MaterialFromFace</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> s </span><span>=</span><span> </span><span>""</span><span>;</span><span>
        </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>doc</span><span>);</span><span>
        </span><span>Room</span><span> room </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>uidoc</span><span>.</span><span>Selection</span><span>.</span><span>PickObject</span><span>(</span><span>ObjectType</span><span>.</span><span>Element</span><span>).</span><span>ElementId</span><span>)</span><span> </span><span>as</span><span> </span><span>Room</span><span>;</span><span>

        </span><span>SpatialElementBoundaryOptions</span><span>  spatialElementBoundaryOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementBoundaryOptions</span><span>();</span><span>
        spatialElementBoundaryOptions</span><span>.</span><span>SpatialElementBoundaryLocation</span><span> </span><span>=</span><span> </span><span>SpatialElementBoundaryLocation</span><span>.</span><span>Finish</span><span>;</span><span>
        </span><span>SpatialElementGeometryCalculator</span><span> calculator </span><span>=</span><span> </span><span>new</span><span> </span><span>SpatialElementGeometryCalculator</span><span>(</span><span>doc</span><span>,</span><span> spatialElementBoundaryOptions</span><span>);</span><span>
        </span><span>SpatialElementGeometryResults</span><span> results </span><span>=</span><span> calculator</span><span>.</span><span>CalculateSpatialElementGeometry</span><span>(</span><span>room</span><span>);</span><span>
        </span><span>Solid</span><span> roomSolid </span><span>=</span><span> results</span><span>.</span><span>GetGeometry</span><span>();</span><span> 

        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> roomSolidFace </span><span>in</span><span> roomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>SpatialElementBoundarySubface</span><span> subface </span><span>in</span><span> results</span><span>.</span><span>GetBoundaryFaceInfo</span><span>(</span><span>roomSolidFace</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>Face</span><span> boundingElementface </span><span>=</span><span> subface</span><span>.</span><span>GetBoundingElementFace</span><span>();</span><span>
                </span><span>ElementId</span><span> id </span><span>=</span><span> boundingElementface</span><span>.</span><span>MaterialElementId</span><span>;</span><span>
                s </span><span>+=</span><span>  doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>).</span><span>Name</span><span> </span><span>+</span><span> </span><span>", id = "</span><span> </span><span>+</span><span> id</span><span>.</span><span>IntegerValue</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"revit"</span><span>,</span><span>s</span><span>);</span><span>                 
</span><span>}</span></code></pre></td></tr></tbody></table>
