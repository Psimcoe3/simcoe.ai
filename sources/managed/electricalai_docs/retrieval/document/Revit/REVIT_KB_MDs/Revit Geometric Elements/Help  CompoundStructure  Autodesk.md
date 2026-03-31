---
created: 2026-01-28T21:05:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_CompoundStructure_html
author: 
---

# Help | CompoundStructure | Autodesk

> ## Excerpt
> Describes the internal structure of a wall, floor, roof or ceiling.

---
Describes the internal structure of a wall, floor, roof or ceiling.

Walls, floors, ceilings and roofs are all children of the API class HostObject. HostObject (and its related type class HostObjAttributes) provide read only access to the CompoundStructure. A compound structure consists a collection of ordered layers, proceeding from exterior to interior for a wall, or from top to bottom for a floor, roof or ceiling. The properties of these layers determine the thickness, material, and function of the overall structure of the associated wall, floor, roof or ceiling.

Layers can be accessed via the GetLayers() method and completely replaced using SetLayers().

Normally these layers are parallel and extend the entire host object with a fixed layer width. However, for walls the structure can also be “vertically compound”, where the layers vary at specified vertical distances from the top and bottom of the wall. Use CompoundStructure.IsVerticallyCompound to identify these. For vertically compound structures, the structure describes a vertical section via a rectangle which is divided into polygonal regions whose sides are all vertical or horizontal segments. A map associates each of these regions with the index of a layer in the CompoundStructure which determines the properties of that region.

It is possible to use the compound structure to find the geometric location of different layer boundaries. The method CompoundStructure.GetOffsetForLocationLine() provides the offset from the center location line to any of the location line options (core centerline, finish faces on either side, or core sides).

With the offset to the location line available, you can obtain the location of each layer boundary by starting from a known location and obtaining the widths of each bounding layer using CompoundStructure.GetLayerWidth().

Some notes about the use of CompoundStructure:

-   The total width of the element is the sum of each CompoundStructureLayer's widths. You cannot change the element's total width directly but you can change it via changing the CompoundStructureLayer width. The index of the designated variable length layer (if assigned) can be obtained from CompoundStructure.VariableLayerIndex.
    
-   You must set the CompoundStructure back to the HostObjAttributes instance (using the HostObjAttributes.SetCompoundStructure() method) in order for any change to be stored.
    
-   Changes to the HostObjAttributes affects every instance in the current document. If you need a new combination of layers,you will need to create a new HostObjAttributes (use ElementType.Duplicate()) and assign the new CompoundStructure to it.
    
-   The CompoundStructureLayer DeckProfileId, and DeckEmbeddingType, properties only work with Slab in the structural features of Revit. For more details, refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).
    
    ### Material
    

Each CompoundStructureLayer in HostObjAttributes is typically displayed with some type of material. If CompoundStructureLayer.MaterialId returns -1, it means the Material is Category-related. For more details, refer to [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html). Getting the CompoundStructureLayer Material is illustrated in the following sample code:

<table summary="" id="GUID-93FA05F8-0A12-430E-9988-D0D0595F8AAD__TABLE_82B43B7300BD450796CC03B312C78A95"><tbody><tr><td><b>Code Region 11-5: Getting the CompoundStructureLayer Material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWallLayerMaterial</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get WallType of wall</span><span>
        </span><span>WallType</span><span> aWallType </span><span>=</span><span> wall</span><span>.</span><span>WallType</span><span>;</span><span>
        </span><span>// Only Basic Wall has compoundStructure</span><span>
        </span><span>if</span><span> </span><span>(</span><span>WallKind</span><span>.</span><span>Basic</span><span> </span><span>==</span><span> aWallType</span><span>.</span><span>Kind</span><span>)</span><span>
        </span><span>{</span><span>

                </span><span>// Get CompoundStructure</span><span>
                </span><span>CompoundStructure</span><span> comStruct </span><span>=</span><span> aWallType</span><span>.</span><span>GetCompoundStructure</span><span>();</span><span>
                </span><span>Categories</span><span> allCategories </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>.</span><span>Categories</span><span>;</span><span>

                </span><span>// Get the category OST_Walls default Material; </span><span>
                </span><span>// use if that layer's default Material is &lt;By Category&gt;</span><span>
                </span><span>Category</span><span> wallCategory </span><span>=</span><span> allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Walls</span><span>);</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> wallMaterial </span><span>=</span><span> wallCategory</span><span>.</span><span>Material</span><span>;</span><span>

                </span><span>foreach</span><span> </span><span>(</span><span>CompoundStructureLayer</span><span> structLayer </span><span>in</span><span> comStruct</span><span>.</span><span>GetLayers</span><span>())</span><span>
                </span><span>{</span><span>
                        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> layerMaterial </span><span>=</span><span> 
                                document</span><span>.</span><span>GetElement</span><span>(</span><span>structLayer</span><span>.</span><span>MaterialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

                        </span><span>// If CompoundStructureLayer's Material is specified, use default</span><span>
                        </span><span>// Material of its Category</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> layerMaterial</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>switch</span><span> </span><span>(</span><span>structLayer</span><span>.</span><span>Function</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Finish1</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>                                       
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsFinish1</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Finish2</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>                                      
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsFinish2</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Membrane</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsMembrane</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Structure</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span>  
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsStructure</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Substrate</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span> 
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsSubstrate</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>case</span><span> </span><span>MaterialFunctionAssignment</span><span>.</span><span>Insulation</span><span>:</span><span>
                                                layerMaterial </span><span>=</span><span> 
                                                        allCategories</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_WallsInsulation</span><span>).</span><span>Material</span><span>;</span><span>
                                                </span><span>break</span><span>;</span><span>
                                        </span><span>default</span><span>:</span><span>
                                                </span><span>// It is impossible to reach here</span><span>
                                                </span><span>break</span><span>;</span><span>
                                </span><span>}</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> layerMaterial</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>// CompoundStructureLayer's default Material is its SubCategory</span><span>
                                        layerMaterial </span><span>=</span><span> wallMaterial</span><span>;</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Layer Material: "</span><span> </span><span>+</span><span> layerMaterial</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Sometimes just the material from the "structural" layer is needed. Rather than looking at each layer for the one whose function is MaterialFunctionAssignment.Structure, use the CompoundStructure.StructuralMaterialIndex property to find the index of the layer whose material defines the structural properties of the type for the purposes of analysis.

Note: When calling SetLayers(), the StructuralMaterialIndex value will be cleared and need to be reset.
