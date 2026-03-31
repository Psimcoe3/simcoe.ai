---
created: 2026-01-28T20:49:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Built_In_Parameters_html
author: 
---

# Help | Built-In Parameters | Autodesk

> ## Excerpt
> The Revit Platform API has a large number of built-in parameters.

---
The Revit Platform API has a large number of built-in parameters.

Built-in parameters are defined in the Autodesk.Revit.Parameters.BuiltInParameter enumeration (see the RevitAPI Help.chm file for the definition of this enumeration). This enumeration has generated documentation visible from Visual Studio intellisense as shown below. The documentation for each id includes the parameter name, as found in the Element Properties dialog in the English version of Autodesk Revit. Note that multiple distinct parameter ids may map to the same English name; in those cases you must examine the parameters associated with a specific element to determine which parameter id to use.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/BuiltInParameter-76164.jpg)

The parameter ID is used to retrieve the specific parameter from an element, if it exists, using the Element.Parameter property. However, not all parameters can be retrieved using the ID. For example, family parameters are not exposed in the Revit Platform API, therefore, you cannot get them using the built-in parameter ID.

The following code sample shows how to get the specific parameter using the BuiltInParameter Id:

<table summary="" id="GUID-C0D9C62F-1BEB-412E-B5B4-E70E2EF4F378__TABLE_7B05D97002E64C939B306A59D69E43DE"><tbody><tr><td><b>Code Region 8-3: Getting a parameter based on BuiltInParameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Parameter</span><span> </span><span>FindWithBuiltinParameterID</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use the WALL_BASE_OFFSET paramametId</span><span>
        </span><span>// to get the base offset parameter of the wall.</span><span>
        </span><span>BuiltInParameter</span><span> paraIndex </span><span>=</span><span> </span><span>BuiltInParameter</span><span>.</span><span>WALL_BASE_OFFSET</span><span>;</span><span>
        </span><span>Parameter</span><span> parameter </span><span>=</span><span> wall</span><span>.</span><span>get_Parameter</span><span>(</span><span>paraIndex</span><span>);</span><span>

        </span><span>return</span><span> parameter</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Getting localized parameter names

The method `LabelUtils.GetLabelFor Method (BuiltInParameter, LanguageType)` returns the localized string name for the built-in parameter. If the corresponding resource DLL cannot be found, the US-English name will be returned.
