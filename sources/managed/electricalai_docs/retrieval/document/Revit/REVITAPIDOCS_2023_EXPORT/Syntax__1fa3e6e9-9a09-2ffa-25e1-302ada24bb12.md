[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTemporaryViewPropertiesId Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

When Temporary View Properties mode is in progress it provides view id that overrode settings for current view. Outside Temporary View Properties mode InvalidElementId will be returned.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId GetTemporaryViewPropertiesId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTemporaryViewPropertiesId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetTemporaryViewPropertiesId() ``` |

# Remarks

Returned ElementId might refer to element that was deleted. It will happen when Temporary View Properties mode was applied basing on template that next was deleted.

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)