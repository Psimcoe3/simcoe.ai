---
created: 2026-01-28T21:01:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_GeometryInstances_html
author: 
---

# Help | GeometryInstances | Autodesk

> ## Excerpt
> A GeometryInstance represents a set of geometry stored by Revit in a default configuration, and then transformed into the proper location as a result of the properties of the element. The most common situation where GeometryInstances are encountered is in Family instances. Revit uses GeometryInstances to allow it to store a single copy of the geometry for a given family and reuse it in multiple instances.

---
A GeometryInstance represents a set of geometry stored by Revit in a default configuration, and then transformed into the proper location as a result of the properties of the element. The most common situation where GeometryInstances are encountered is in Family instances. Revit uses GeometryInstances to allow it to store a single copy of the geometry for a given family and reuse it in multiple instances.

Note that not all Family instances will include GeometryInstances. When Revit needs to make a unique copy of the family geometry for a given instance (because of the effect of local joins, intersections, and other factors related to the instance placement) no GeometryInstance will be encountered; instead the Solid geometry will be found at the top level of the hierarchy.

A GeometryInstance offers the ability to read its geometry through the GetSymbolGeometry() and GetInstanceGeometry() methods. These methods return another Autodesk.Revit.DB.GeometryElement which can be parsed just like the first level return.

GetSymbolGeometry() returns the geometry represented in the coordinate system of the family. Use this, for example, when you want a picture of the “generic” table without regards to the orientation and placement location within the project. This is also the only overload which returns the actual Revit geometry objects to you, and not copies. This is important because operations which use this geometry as input to creating other elements (for example, dimensioning or placement of face-based families) require the reference to the original geometry.

GetInstanceGeometry() returns the geometry represented in the coordinate system of the project where the instance is placed. Use this, for example, when you want a picture of the specific geometry of the instance in the project (for example, ensuring that tables are placed parallel to the walls of the room). This always returns a copy of the element geometry, so while it would be suitable for implementation of an exporter or a geometric analysis tool, it would not be appropriate to use this for the creation of other Revit elements referencing this geometry.

There are also overloads for both GetInstanceGeometry() and GetSymbolGeometry() that transform the geometry by any arbitrary coordinate system. These methods always return copies similar to GetInstanceGeometry().

The GeometryInstance also stored a transformation from the symbol coordinate space to the instance coordinates. This transform is accessible as the Transform property. It is also the transformation used when extracting a the copy of the geometry via GetInstanceGeometry(). For more details, refer to [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/instances_transformed.png)**2 family instances placed with different transforms - the same geometry will be acquired from both**

Instances may be nested several levels deep for some families. If you encounter nested instances they may be parsed in a similar manner as the first level instance.

Two samples are presented to explain how geometry of instances can be parsed.

In this sample, curves are extracted from the GeometryInstance method GetInstanceGeometry().

<table summary="" id="GUID-B4F83374-0DF6-4737-91EB-900E676E862B__TABLE_957B57BD7CD6475E8E425AE0B967168A"><tbody><tr><td><b>Code Region: Getting curves from an instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetAndTransformCurve</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app</span><span>,</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>,</span><span> </span><span>Options</span><span> geoOptions</span><span>)</span><span>
</span><span>{</span><span>
   </span><span>// Get geometry element of the selected element</span><span>
   </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> element</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>

   </span><span>// Get geometry object</span><span>
   </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
   </span><span>{</span><span>
      </span><span>// Get the geometry instance which contains the geometry information</span><span>
      </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> instance </span><span>=</span><span>
             geoObject </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
      </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> instance</span><span>)</span><span>
      </span><span>{</span><span>
         </span><span>GeometryElement</span><span> instanceGeometryElement </span><span>=</span><span> instance</span><span>.</span><span>GetInstanceGeometry</span><span>();</span><span>
         </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> o </span><span>in</span><span> instanceGeometryElement</span><span>)</span><span>
         </span><span>{</span><span>
            </span><span>// Try to find curves</span><span>
            </span><span>Curve</span><span> curve </span><span>=</span><span> o </span><span>as</span><span> </span><span>Curve</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>curve </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
               </span><span>// The curve is already transformed into the project coordinate system</span><span>
            </span><span>}</span><span>
         </span><span>}</span><span>
      </span><span>}</span><span>
   </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

In this sample, the solids are obtained from an instance using GetSymbolGeometry(). The constituent points are then transformed into the project coordinate system using the GeometryInstance.Transform.

<table summary="" id="GUID-B4F83374-0DF6-4737-91EB-900E676E862B__TABLE_30A437E3589144C3AFC1AADEB2F10DB2"><tbody><tr><td><b>Code Region: Getting solid information from an instance</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetAndTransformSolidInfo</span><span>(</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Element</span><span> element</span><span>,</span><span> </span><span>Options</span><span> geoOptions</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get geometry element of the selected element</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> element</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>

        </span><span>// Get geometry object</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Get the geometry instance which contains the geometry information</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span> instance </span><span>=</span><span>
      geoObject </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryInstance</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> instance</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>GeometryElement</span><span> instanceGeometryElement </span><span>=</span><span> instance</span><span>.</span><span>GetSymbolGeometry</span><span>();</span><span>
                    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> instObj </span><span>in</span><span> instanceGeometryElement</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>Solid</span><span> solid </span><span>=</span><span> instObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> solid </span><span>||</span><span> </span><span>0</span><span> </span><span>==</span><span> solid</span><span>.</span><span>Faces</span><span>.</span><span>Size</span><span> </span><span>||</span><span> </span><span>0</span><span> </span><span>==</span><span> solid</span><span>.</span><span>Edges</span><span>.</span><span>Size</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>continue</span><span>;</span><span>
                                </span><span>}</span><span>

                                </span><span>Transform</span><span> instTransform </span><span>=</span><span> instance</span><span>.</span><span>Transform</span><span>;</span><span>
                                </span><span>// Get the faces and edges from solid, and transform the formed points</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>Mesh</span><span> mesh </span><span>=</span><span> face</span><span>.</span><span>Triangulate</span><span>();</span><span>
                                        </span><span>foreach</span><span> </span><span>(</span><span>XYZ ii </span><span>in</span><span> mesh</span><span>.</span><span>Vertices</span><span>)</span><span>
                                        </span><span>{</span><span>
                                                XYZ point </span><span>=</span><span> ii</span><span>;</span><span>
                                                XYZ transformedPoint </span><span>=</span><span> instTransform</span><span>.</span><span>OfPoint</span><span>(</span><span>point</span><span>);</span><span>
                                        </span><span>}</span><span>
                                </span><span>}</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> edge </span><span>in</span><span> solid</span><span>.</span><span>Edges</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>foreach</span><span> </span><span>(</span><span>XYZ ii </span><span>in</span><span> edge</span><span>.</span><span>Tessellate</span><span>())</span><span>
                                        </span><span>{</span><span>
                                                XYZ point </span><span>=</span><span> ii</span><span>;</span><span>
                                                XYZ transformedPoint </span><span>=</span><span> instTransform</span><span>.</span><span>OfPoint</span><span>(</span><span>point</span><span>);</span><span>
                                        </span><span>}</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
