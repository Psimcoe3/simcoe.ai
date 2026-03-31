[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLayerTable Class

---



|  |
| --- |
| [Members](26273ccb-19e1-1f31-edf1-627595253daa.htm)   [See Also](#seeAlsoToggle) |

A table supporting a mapping of category and subcategory to layer name and other layer properties that will be set in the target export format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportLayerTable : IEnumerable<KeyValuePair<ExportLayerKey, ExportLayerInfo>>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportLayerTable _ 	Implements IEnumerable(Of KeyValuePair(Of ExportLayerKey, ExportLayerInfo)),  _ 	IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportLayerTable : IEnumerable<KeyValuePair<ExportLayerKey^, ExportLayerInfo^>>,  	IDisposable ``` |

# Remarks

This table is structured as a mapping from  [ExportLayerKey](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)  to  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  members. The  [ExportLayerKey](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)  contains the identification information for the layer table: the Revit category and subcategory names. In addition, the key contains a  [SpecialType](c4dd5703-709a-729c-7ec5-c7f16c77cf38.htm)  member used only to represent non-Revit categories that can be assigned specific layer information on export. The  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  contains the exported layer name, color name, and layer modifiers for standard and cut representations.

The table can be accessed via direct iteration as a collection of KeyValuePairs, or by traversal of the stored keys obtained from GetKeys(), or via specific lookup of a key constructed externally. In all cases, the  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  returned will be a copy of the  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  from the table. In order to make changes to the  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  and use those settings during export, set the modified  [ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)  back into the table using the same key.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ExportLayerTable

# See Also

[ExportLayerTable Members](26273ccb-19e1-1f31-edf1-627595253daa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)