---
created: 2026-01-28T20:49:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Global_Parameters_Managing_Global_Parameters_html
author: 
---

# Help | Managing Global Parameters | Autodesk

> ## Excerpt
> The GlobalParametersManager class provides access to general information and data of Global Parameter elements in a particular model.

---
The GlobalParametersManager class provides access to general information and data of Global Parameter elements in a particular model.

GlobalParametersManager provides the main access point to managing global parameters in a project document. It provides static methods to access and reorder global parameters and to test for name uniqueness and Id validity.

## Accessing global parameters

Global parameters are only supported in project documents, not family documents. Even with a project document, however, global parameters may be disallowed under certain circumstances, either temporarily or permanently. The AreGlobalParametersAllowed() method will indicate whether global parameters are allowed within a specified document.

If global parameters are allowed in a project document, use the methods GetAllGlobalParameters() to get all global parameters in a specified document, or GetGlobalParametersOrdered() to get an ordered list of the global parameters. When retrieving an ordered list, the order of the items corresponds to the order in which global parameters appear in the standard Global Parameters dialog in the Revit user interface.

To get a global parameter by name, call FindByName(), which will return the ElementId of the named global parameter, or ElementId.InvalidElementId if no global parameter is found with the given name. Since global parameter names must be unique, the IsUniqueName() method should be called to check a name prior to creating a new GlobalParameter.

Given an ElementId for a GlobalParameter, the IsValidGlobalParameter() will confirm that the given ElementId is a valid global parameter id.

The following example demonstrates how to get all global parameters, if global parameters are allowed in the document.

<table summary="" id="GUID-9FDC35A5-C054-46CA-B2DC-E20958FD197F__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region: Getting global parameters</b></td></tr><tr><td><pre><code><span>/// &lt;summary&gt;</span><span>
</span><span>/// Returns all global parameter elements defined in the given document. </span><span>
</span><span>/// &lt;/summary&gt;</span><span>
</span><span>/// &lt;param name="document"&gt;Revit project document.&lt;/param&gt;</span><span>
</span><span>/// &lt;returns&gt;A set of ElementIds of global parameter elements&lt;/returns&gt;</span><span>
</span><span>public</span><span> </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>GetAllGlobalParameters</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Global parameters are not available in all documents.</span><span>
    </span><span>// They are available in projects, but not in families.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>GlobalParametersManager</span><span>.</span><span>AreGlobalParametersAllowed</span><span>(</span><span>document</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>GlobalParametersManager</span><span>.</span><span>GetAllGlobalParameters</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// return an empty set if global parameters are not available in the document</span><span>
    </span><span>return</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Reordering global parameters

GlobalParametersManager provides methods to change the given order of the global parameters in the project document. These operations have no effect on the global parameters themselves. The rearranged order is only visible in the standard Global Parameters dialog in Revit and reflected in the GetGlobalParametersOrdered() method.

-   SortParameters() - sorts the global parameters in either ascending or descending alphabetical order, but only within the range of their respective parameter group.
-   MoveParameterDownOrder() - moves a given parameter down in the current order.
-   MoveParameterUpOrder() - moves the given parameter up in the current order. A parameter can only be moved within its parameter group, so if a parameter can no longer move because it is at the boundary of its group, the MoveParameter methods will return False.
