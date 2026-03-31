---
created: 2026-01-28T20:49:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Definition_html
author: 
---

# Help | Definition | Autodesk

> ## Excerpt
> The Definition object describes the data type, name, and other Parameter details.

---
The Definition object describes the data type, name, and other Parameter details.

There are two kinds of definition objects derived from this object.

-   InternalDefinition represents all kinds of definitions existing entirely in the Revit database.
-   ExternalDefinition represents definitions stored on disk in a shared parameter file.

You should write the code to use the Definition base class so that the code is applicable to both internal and external parameter Definitions. The following code sample shows how to find a specific parameter using the definition type.

<table summary="" id="GUID-13EE268E-DEAC-4245-A192-E14BFA63E382__TABLE_E2A463303AAA4F09B5BAB775B1171CEF"><tbody><tr><td><b>Code Region 8-2: Finding a parameter based on definition type</b></td></tr><tr><td><pre><code><span>//Find parameter using the Parameter's definition type.</span><span>
</span><span>public</span><span> </span><span>Parameter</span><span> </span><span>FindParameter</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Parameter</span><span> foundParameter </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>// This will find the first parameter that measures length</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Parameter</span><span> parameter </span><span>in</span><span> element</span><span>.</span><span>Parameters</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>parameter</span><span>.</span><span>Definition</span><span>.</span><span>GetDataType</span><span>()</span><span> </span><span>==</span><span> </span><span>SpecTypeId</span><span>.</span><span>Length</span><span>)</span><span>
                </span><span>{</span><span>
                        foundParameter </span><span>=</span><span> parameter</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> foundParameter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Parameter Data Type

For parameters associated with units of measurement, `GetDataType()` returns a measurable spec identifier. Use `UnitUtils.IsMeasurableSpec(ForgeTypeId)` to detect a measurable spec identifier.

For Family Type parameters, `GetDataType()` returns a category identifier. Use `Category.IsBuiltInCategory(ForgeTypeId)` to detect a category identifier.

For all other parameters, `GetDataType()` returns a spec identifier. Use `Parameter.IsSpec(ForgeTypeId)` to detect a spec identifier, including measurable specs.

### GetGroupTypeId()

The Definition class GetGroupTypeId() method returns a ForgeTypeId. The members of the GroupTypeId class list all value supported by Revit. The GroupTypeId is used to sort parameters in the Element Properties dialog box.

## InternalDefinition

Every Parameter object has an InternalDefinition, which can be obtained from the Definition property. The InternalDefinition represents the parameter definition in the Revit document. In addition to the properties it inherits from Definition, it also has some other key properties.

### BuiltInParameter

This property tests whether this definition identifies a built-in parameter or not. For a built-in parameter, this property returns one of the BuiltInParameter enumerated values. For custom-defined parameters, such as shared, global, or family parameters the value will be BuiltInParameter.INVALID.

### Id

This property returns the id for the associated ParameterElement if the parameter is not built-in.

### VariesAcrossGroups

This property, and the corresponding SetAllowVaryBetweenGroups() method, determine whether the values of this parameter can vary across the related members of group instances. If False, the values will be consistent across the related members in group instances. This can only be set for non-built-in parameters.

### Visible

The visible property indicates whether a shared parameter is hidden from the user. This is useful if you wish to add data to an element that is only meaningful to your application and not to the user. This value can only be set when the shared parameter definition is created.
