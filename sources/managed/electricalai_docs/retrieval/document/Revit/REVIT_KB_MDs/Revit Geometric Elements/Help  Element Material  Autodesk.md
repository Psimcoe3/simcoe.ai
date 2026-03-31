---
created: 2026-01-28T21:03:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html
author: 
---

# Help | Element Material | Autodesk

> ## Excerpt
> One element can have several elements and components. For example, FamilyInstance has SubComponents and Wall has CompoundStructure which contain several CompoundStructureLayers. (For more details about SubComponents refer to the Family Instances section and refer to Walls, Floors, Roofs and Openings for more information about CompoundStructure.)

---
One element can have several elements and components. For example, FamilyInstance has SubComponents and Wall has CompoundStructure which contain several CompoundStructureLayers. (For more details about SubComponents refer to the Family Instances section and refer to [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html) for more information about CompoundStructure.)

In the Revit Platform API, get an element's materials using the following guidelines:

-   If the element contains elements, get the materials separately.
-   If the element contains components, get the material for each component from the parameters or in specific way (see [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html) section in [Walls, Floors, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html)).
-   If the component's material returns null, get the material from the corresponding Element.Category sub Category.
    
    ### Material in a Parameter
    

If the Element object has a Parameter with a Definition whose GetDataType() method returns SpecTypeId.Reference.Material, you can get the element material from the Parameter. For example, a structural column FamilySymbol (a FamilyInstance whose Category is BuiltInCategory.OST\_StructuralColumns) has the Structural Material parameter. Get the Material using the ElementId. The following code example illustrates how to get the structural column Material that has one component.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_31045170AC5541C0B8B41E6A6586AB36"><tbody><tr><td><b>Code Region: Getting an element material from a parameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetMaterialFromParameter</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> familyInstance</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Definition</span><span> definition </span><span>=</span><span> parameter</span><span>.</span><span>Definition</span><span>;</span><span>
        </span><span>// material is stored as element id</span><span>
        </span><span>if</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>StorageType</span><span> </span><span>==</span><span> </span><span>StorageType</span><span>.</span><span>ElementId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>definition</span><span>.</span><span>ParameterGroup</span><span> </span><span>==</span><span> </span><span>BuiltInParameterGroup</span><span>.</span><span>PG_MATERIALS </span><span>&amp;&amp;</span><span>
                definition</span><span>.</span><span>GetDataType</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Reference</span><span>.</span><span>Material</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> material </span><span>=</span><span> </span><span>null</span><span>;</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> materialId </span><span>=</span><span> parameter</span><span>.</span><span>AsElementId</span><span>();</span><span>
                </span><span>if</span><span> </span><span>(-</span><span>1</span><span> </span><span>==</span><span> materialId</span><span>.</span><span>IntegerValue</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>//Invalid ElementId, assume the material is "By Category"</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyInstance</span><span>.</span><span>Category</span><span>)</span><span>
                    </span><span>{</span><span>
                        material </span><span>=</span><span> familyInstance</span><span>.</span><span>Category</span><span>.</span><span>Material</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span>
                </span><span>{</span><span>
                    material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>}</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Element material: "</span><span> </span><span>+</span><span> material</span><span>.</span><span>Name</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: If the material property is set to By Category in the UI, the ElementId for the material is ElementId.InvalidElementId and cannot be used to retrieve the Material object as shown in the sample code. Try retrieving the Material from Category as described in the next section.

Some material properties contained in other compound parameters are not accessible from the API. As an example, in the following figure, for System Family: Railing, the Rail Structure parameter's StorageType is StorageType.None. As a result, you cannot get material information in this situation.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ByCategory.jpg)

**Figure 107: Rail structure property**

### Material and FamilyInstance

Beam, Column and Foundation FamilyInstances have another way to get their material using their StructuralMaterialId property. This property returns an ElementId which identifies the material that defines the instance's structural analysis properties.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_8B5ABF07F2E64065B30704FA6E86C2BD"><tbody><tr><td><b>Code Region: Getting an element material from a family instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Material</span><span> </span><span>GetFamilyInstanceMaterial</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Material</span><span> material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>beam</span><span>.</span><span>StructuralMaterialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>return</span><span> material</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Material and Category

Only model elements can have material.

From the Revit Manage tab, click Settings![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ac.menuaro.gif)Object Styles to display the Object Styles dialog box. Elements whose category is listed in the Model Objects tab have material information.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ModelObjectsMaterial.jpg)**Figure 108: Category material**

Only Model elements can have the Material property assigned. Querying Material for a category that corresponds to other than Model elements (e.g. Annotations or Imported) will therefore always result in a null. For more details about the Element and Category classifications, refer to [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html).

If an element has more than one component, some of the Category.Subcategories correspond to the components.

In the previous Object Styles dialog box, the Windows Category and the Frame/Mullion and Glass subcategories are mapped to components in the windows element. In the following picture, it seems the window symbol Glass Pane Material parameter is the only way to get the window pane material. However, the value is By Category and the corresponding Parameter returns ElementId.InvalidElementId.

In this case, the pane's Material is not null and it depends on the Category OST\_WindowsFrameMullionProjection's Material property which is a subcategory of the window's category, OST\_Windows. If it returns null as well, the pane's Material is determined by the parent category OST\_Windows. For more details, refer to [Element Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Element_Material_html).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E345BF1-1837-41C7-BF9C-A89A1A76539F-low.png)**Figure 109: Window material**

### CompoundStructureLayer Material

You can get the CompoundStructureLayer object from HostObjAttributes. For more details, refer to [Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html).

### Retrieve Element Materials

The following diagram shows the workflow to retrieve Element Materials:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-64D41480-87CE-454E-8B14-1EFEFEC8BF09-low.png)**Figure 110: Getting Element Material workflow**

This workflow illustrates the following process:

-   The workflow shows how to get the Material object (not Autodesk.Revit.DB.Structure.StructuralMaterialType enumerated type) that belongs to the element.
-   There are two element classifications when retrieving the Material:
    -   HostObject with CompoundStructure - Get the Material object from the CompoundStructureLayer class MaterialId property.
    -   Others - Get the Material from the Parameters.
-   When you get a null Material object or an invalid ElementId with a value of ElementId.InvalidElementId, try the Material from the corresponding category. Note that a FamilyInstance and its FamilySymbol usually have the same category.
-   The more you know about the Element object, the easier it is to get the material. For example:
    -   If you know the Element is a beam, you can get the instance parameter Structural Material
    -   If you know the element is a window, you can cast it to a FamilyInstance and get the FamilySymbol.
-   After that you can get the Parameters such as Frame Exterior Material or Frame Interior Material to get the Material object. If you get null try to get the Material object from the FamilySymbol Category.
-   Not all Element Materials are available in the API.
    
    ### Walkthrough: Get Window Materials
    

The following code illustrates how to get the Window Materials.

<table summary="" id="GUID-FD067FA5-623D-474B-98FB-686C096F0165__TABLE_FA4B8EFD22EE42ABB74FEB91E3A6A11C"><tbody><tr><td><b>Code Region: Getting window materials walkthrough</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWindowMaterial</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> window</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FamilySymbol</span><span> windowSymbol </span><span>=</span><span> window</span><span>.</span><span>Symbol</span><span>;</span><span>
    </span><span>Category</span><span> category </span><span>=</span><span> windowSymbol</span><span>.</span><span>Category</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> frameExteriorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> frameInteriorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Material</span><span> sashMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// Check the parameters first</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> windowSymbol</span><span>.</span><span>Parameters</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>switch</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>Definition</span><span>.</span><span>Name</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>case</span><span> </span><span>"Frame Exterior Material"</span><span>:</span><span>
                frameExteriorMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>"Frame Interior Material"</span><span>:</span><span>
                frameInteriorMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>"Sash"</span><span>:</span><span>
                sashMaterial </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>parameter</span><span>.</span><span>AsElementId</span><span>())</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>default</span><span>:</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>// Try category if the material is set by category</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> frameExteriorMaterial</span><span>)</span><span>
        frameExteriorMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> frameInteriorMaterial</span><span>)</span><span>
        frameInteriorMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> sashMaterial</span><span>)</span><span>
        sashMaterial </span><span>=</span><span> category</span><span>.</span><span>Material</span><span>;</span><span>
    </span><span>// Show the result because the category may have a null Material,</span><span>
    </span><span>// the Material objects need to be checked.</span><span>
    </span><span>string</span><span> materialsInfo </span><span>=</span><span> </span><span>"Frame Exterior Material: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> frameExteriorMaterial </span><span>?</span><span> frameExteriorMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    materialsInfo </span><span>+=</span><span> </span><span>"Frame Interior Material: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> frameInteriorMaterial </span><span>?</span><span> frameInteriorMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    materialsInfo </span><span>+=</span><span> </span><span>"Sash: "</span><span> </span><span>+</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> sashMaterial </span><span>?</span><span> sashMaterial</span><span>.</span><span>Name</span><span> </span><span>:</span><span> </span><span>"null"</span><span>)</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>materialsInfo</span><span>);</span><span>
</span><span>}</span><span> </span></code></pre></td></tr></tbody></table>
