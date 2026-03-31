[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSymbolId Method

---



|  |
| --- |
| [GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.htm)   [See Also](#seeAlsoToggle) |

The Id of the symbol associated with the node. This property is deprecated in Revit 2023 and may be removed in a future version of Revit. For an InstanceNode please use the GetSymbolGeometryId().SymbolId. For a LinkNode please use SymbolId property. In Revit 2023 we introduced instance nodes that point to a part of the symbol's geometry. For comparing if two such nodes point to the same geometry, the SymbolId isn't enough. SymbolGeometryId can be used to identify a piece of geometry managed by a symbol element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute] public ElementId GetSymbolId() ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute> _ Public Function GetSymbolId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute] public: ElementId^ GetSymbolId() ``` |

# See Also

[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)