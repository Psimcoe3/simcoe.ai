---
created: 2026-01-28T21:03:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_General_Material_Information_html
author: 
---

# Help | General Material Information | Autodesk

> ## Excerpt
> Before you begin the walkthrough, read through the following section for a better understanding of the Material class.

---
Before you begin the walkthrough, read through the following section for a better understanding of the Material class.

All Material objects can be retrieved using a Material class filter. Material objects are also available in Document, Category, Element, Face, and so on, and are discussed in the pertinent sections in this chapter. Wherever you get a material object, it is represented as the Material class.

### Properties

A material will have one or more aspects pertaining to rendering appearance, structure, or other major material category. Each aspect is represented by properties on the Material class itself or via one of its assets, structural or thermal. The StructuralAsset class represents the properties of a material pertinent to structural analysis. The ThermalAsset class represents the properties of a material pertinent to energy analysis.

<table summary="" id="GUID-F0C7BA6A-8C58-45B4-8639-1E08CBC6781D__TABLE_CEF5B6EF8B0D48DBB98774BC02AAC136"><tbody><tr><td><b>Code Region 19-3: Getting material properties</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ReadMaterialProps</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ElementId</span><span> strucAssetId </span><span>=</span><span> material</span><span>.</span><span>StructuralAssetId</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>strucAssetId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>PropertySetElement</span><span> pse </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>strucAssetId</span><span>)</span><span> </span><span>as</span><span> </span><span>PropertySetElement</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>pse </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>StructuralAsset</span><span> asset </span><span>=</span><span> pse</span><span>.</span><span>GetStructuralAsset</span><span>();</span><span>

            </span><span>// Check the material behavior and only read if Isotropic</span><span>
            </span><span>if</span><span> </span><span>(</span><span>asset</span><span>.</span><span>Behavior</span><span> </span><span>==</span><span> </span><span>StructuralBehavior</span><span>.</span><span>Isotropic</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// Get the class of material</span><span>
                </span><span>StructuralAssetClass</span><span> assetClass </span><span>=</span><span> asset</span><span>.</span><span>StructuralAssetClass</span><span>;</span><span> </span><span>// Get other material properties</span><span>

                </span><span>// Get other material properties</span><span>
                </span><span>double</span><span> poisson </span><span>=</span><span> asset</span><span>.</span><span>PoissonRatio</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> youngMod </span><span>=</span><span> asset</span><span>.</span><span>YoungModulus</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> thermCoeff </span><span>=</span><span> asset</span><span>.</span><span>ThermalExpansionCoefficient</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>double</span><span> unitweight </span><span>=</span><span> asset</span><span>.</span><span>Density</span><span>;</span><span>
                </span><span>double</span><span> shearMod </span><span>=</span><span> asset</span><span>.</span><span>ShearModulus</span><span>.</span><span>X</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>assetClass </span><span>==</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Metal</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>double</span><span> dMinStress </span><span>=</span><span> asset</span><span>.</span><span>MinimumYieldStress</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>assetClass </span><span>==</span><span> </span><span>StructuralAssetClass</span><span>.</span><span>Concrete</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>double</span><span> dConcComp </span><span>=</span><span> asset</span><span>.</span><span>ConcreteCompression</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Classification

The material classification relevant to structural analysis (i.e. steel, concrete, wood) can be obtained from the StructuralAssetClass property of the StructuralAsset associated with the material.

Note: The API does not provide access to the values of Concrete Type for Concrete material.

The material classification relevant to energy analysis (i.e. solid, liquid, gas) can be obtained from the ThermalMaterialType property of the ThermalAsset associated with the material.

### Other Properties

The material object properties identify a specific type of material including color, fill pattern, and more.

#### Properties and Parameter

Some Material properties are only available as a Parameter. A few, such as Color, are available as a property or as a Parameter using the BuiltInParameter MATERIAL\_PARAM\_COLOR.

#### Rendering Information

Collections of rendering data are organized into objects called Assets. You can obtain all available Appearance-related assets from the Application.Assets property. An appearance asset can be accessed from a material via the Material.AppearanceAssetId property.

The following figure shows the Appearance Library section of the Asset Browser dialog box, which shows how some rendering assets are displayed in the UI.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/AssetBrowser.jpg)**Figure 106: Appearance Library**

The Materials sample application included with the SDK shows how to set the RenderApperance property to a material selected in a dialog. The dialog is populated with all the Asset objects in Application.Assets.

#### Editing properties of an Appearance Asset

Editing properties in an appearance Asset requires establishment of an edit scope. The new class

```
Autodesk.Revit.DB.Visual.AppearanceAssetEditScope
```

allows an application to create and maintain an editing session for an appearance asset. The scope provides access to an editable Asset object whose properties may be changed. Once all of the desired changes have been made to the asset's properties, the edit scope should be committed, which causes the changes to be sent back into the document. (This is the only part of the process when a transaction must be opened).

The methods of this class are

-   AppearanceAssetEditScope.Start() – Starts the edit scope for the asset contained in a particular AppearanceAssetElement. The editable Asset is returned from this method.
-   AppearanceAssetEditScope.Commit() – Finishes the edit scope: all changes made during the edit scope will be committed. Provides an option to force the update of all open views.
-   AppearanceAssetEditScope.Cancel() – Cancels the edit scope and discards any changes.

##### Connected Assets

Connected assets are associated to properties in appearance assets, and represent subordinate objects encapsulating a collection of related properties. One example of a connected asset is the "Unified Bitmap" representing an image and its mapping parameters and values. AssetProperty offers methods to provide the ability to modify, add or delete the asset connected to a property:

-   AssetProperty.GetSingleConnectedAsset() – Gets the single connected asset of this property
-   AssetProperty.RemoveConnectedAsset() – Removes the single connected asset of this property
-   AssetProperty.AddConnectedAsset (String schemaId) – Create a new default asset of schema type and connects it to this property
-   AssetProperty.AddCopyAsConnectedAsset() – Connects the property to a copy of the asset

##### Schemas & Property names

Appearance asset properties are aligned with specific schemas. Each schema contains necessary properties which define how the appearance of the material will be generated. There are 14 standard material schemas:

-   Ceramic
-   Concrete
-   Generic
-   Glazing
-   Hardwood
-   MasonryCMU
-   Metal
-   MetallicPaint
-   Mirror
-   PlasticVinyl
-   SolidGlass
-   Stone
-   WallPaint
-   Water

In addition, there are 5 schemas representing "advanced" materials - these may be encountered as a result of import from other Autodesk products:

-   AdvancedLayered
-   AdvancedMetal
-   AdvancedOpaque
-   AdvancedTransparent
-   AdvancedWood

Finally, there are 10 schemas used for the aspects of the connected assets:

-   BumpMap
-   Checker
-   Gradient
-   Marble
-   Noise
-   Speckle
-   Tile
-   UnifiedBitmap
-   Wave
-   Wood

The method:

```
 AssetProperty.IsValidSchemaIdentifier(String schemaName)
```

identifies if the input name is a valid name for a supported schema.

To assist in creating code accessing and manipulating the properties of a given schema, predefined properties have been introduced to allow a compile-time reference to a property name without requiring you to transcribe it as a string in your code. These predefined property names are available in static classes named similar to the schema names, above, e.g. Autodesk.Revit.DB.Visual.Ceramic.

##### Asset Utilities

The method:

-   Application.GetAssets(AssetType)

returns a list of assets available to the session.

The method:

-   AppearanceAssetElement.Duplicate()

creates a copy of an appearance asset element and the asset contained by it.

The operator:

-   Asset.operator\[ \]

accesses a particular AssetProperty associated to the given asset.

#### FillPattern

All FillPatterns in a document are available using a FilteredElementCollector filtering on class FillPatternElement. A FillPatternElement is an element that contains a FillPattern while the FillPattern class provides access to the pattern name and the set of FillGrids that make up the pattern.

There are two kinds of FillPatterns: Drafting and Model. In the UI, you can only set Drafting fill patterns to Material.CutForegroundPatternId or Material.CutBackgroundPatternId. The fill pattern type is exposed via the FillPattern.Target property. The following example shows how to change the material FillPattern.

<table summary="" id="GUID-F0C7BA6A-8C58-45B4-8639-1E08CBC6781D__TABLE_DF5D0D5974C541FE8D1B4A77E88879FE"><tbody><tr><td><b>Code Region 19-4: Setting the fill pattern</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetFillPattern</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Material</span><span> material</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> fillPatternElements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FillPatternElement</span><span>)).</span><span>ToElementIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> fillPatternId </span><span>in</span><span> fillPatternElements</span><span>)</span><span>
    </span><span>{</span><span>
        material</span><span>.</span><span>CutForegroundPatternId</span><span> </span><span>=</span><span> fillPatternId</span><span>;</span><span>
        material</span><span>.</span><span>SurfaceForegroundPatternId</span><span> </span><span>=</span><span> fillPatternId</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
