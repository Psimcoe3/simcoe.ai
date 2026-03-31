---
created: 2026-01-28T21:03:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_Management_html
author: 
---

# Help | Material Management | Autodesk

> ## Excerpt
> You can use filtering to retrieve all materials in the document. Every Material object in the Document is identified by a unique name.

---
You can use filtering to retrieve all materials in the document. Every Material object in the Document is identified by a unique name.

The following example illustrates how to use the material name to get material.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_1F839372D0694C90BCB0F8EC95D5B6D8"><tbody><tr><td><b>Code Region 19-5: Getting a material by name</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MaterialByName</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> elementCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    elementCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Material</span><span>)));</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> materials </span><span>=</span><span> elementCollector</span><span>.</span><span>ToElements</span><span>();</span><span>

    </span><span>Material</span><span> floorMaterial </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>string</span><span> floorMaterialName </span><span>=</span><span> </span><span>"Default Floor"</span><span>;</span><span>

    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> materialElement </span><span>in</span><span> materials</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Material</span><span> material </span><span>=</span><span> materialElement </span><span>as</span><span> </span><span>Material</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>floorMaterialName </span><span>==</span><span> material</span><span>.</span><span>Name</span><span>)</span><span>
        </span><span>{</span><span>
            floorMaterial </span><span>=</span><span> material</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> floorMaterial</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Material found."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre><p><span>Note:</span> To run the sample code, make sure the material name exists in your document. All material names for the current document are located under the Manage tab (Project Settings panel &gt; Materials.)</p></td></tr></tbody></table>

### Creating Materials

There are two ways to create a new Material object in the API.

-   Duplicate an existing Material
    
-   Add a new Material.
    

When using the Duplicate() method, the returned Material object is the same type as the original.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_654837E6A6BE4A2FB4C0B2CE908A1CAE"><tbody><tr><td><b>Code Region 19-6: Duplicating a material</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>bool</span><span> </span><span>DuplicateMaterial</span><span>(</span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>bool</span><span> duplicated </span><span>=</span><span> </span><span>false</span><span>;</span><span>
        </span><span>//try to duplicate a new instance of Material class using duplicate method</span><span>
        </span><span>//make sure the name of new material is unique in MaterailSet</span><span>
        </span><span>string</span><span> newName </span><span>=</span><span> </span><span>"new"</span><span> </span><span>+</span><span> material</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>Material</span><span> myMaterial </span><span>=</span><span> material</span><span>.</span><span>Duplicate</span><span>(</span><span>newName</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> myMaterial</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Failed to duplicate a material!"</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                duplicated </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> duplicated</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Use the static method Material.Create() to add a new Material directly. No matter how it is applied, it is necessary to specify a unique name for the material and any assets belonging to the material. The unique name is the Material object key.

<table summary="" id="GUID-8928F399-9E98-4C5B-A778-1E5E8DADF5AF__TABLE_20E15F95752D446CB62CE19BA3BC5220"><tbody><tr><td><b>Code Region 19-7: Adding a new Material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateMaterial</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>//Create the material</span><span>
    </span><span>ElementId</span><span> materialId </span><span>=</span><span> </span><span>Material</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"My Material"</span><span>);</span><span>
    </span><span>Material</span><span> material </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>materialId</span><span>)</span><span> </span><span>as</span><span> </span><span>Material</span><span>;</span><span>

    </span><span>//Create a new property set that can be used by this material</span><span>
    </span><span>StructuralAsset</span><span> strucAsset </span><span>=</span><span> </span><span>new</span><span> </span><span>StructuralAsset</span><span>(</span><span>"My Property Set"</span><span>,</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Concrete</span><span>);</span><span>
    strucAsset</span><span>.</span><span>Behavior</span><span> </span><span>=</span><span> </span><span>StructuralBehavior</span><span>.</span><span>Isotropic</span><span>;</span><span>
    strucAsset</span><span>.</span><span>Density</span><span> </span><span>=</span><span> </span><span>232.0</span><span>;</span><span>

    </span><span>//Assign the property set to the material.</span><span>
    </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> </span><span>PropertySetElement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> strucAsset</span><span>);</span><span>
    material</span><span>.</span><span>SetMaterialAspectByPropertySet</span><span>(</span><span>MaterialAspect</span><span>.</span><span>Structural</span><span>,</span><span> pse</span><span>.</span><span>Id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Deleting Materials

To delete a material use:

-   Document.Delete()

Document.Delete() is a generic method. See [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) for details.
