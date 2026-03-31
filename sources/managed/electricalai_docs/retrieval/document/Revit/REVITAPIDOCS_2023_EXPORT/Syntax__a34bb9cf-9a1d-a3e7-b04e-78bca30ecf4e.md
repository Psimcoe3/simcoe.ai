[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNonControlledTemplateParameterIds Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Returns a list of parameters that are not marked as included when this view is used as a template.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetNonControlledTemplateParameterIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNonControlledTemplateParameterIds As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetNonControlledTemplateParameterIds() ``` |

#### Return Value

The parameter ids that are not marked to be included.

# Remarks

This is a subset of the parameters returned by  [GetTemplateParameterIds](64761c8c-ed01-65b6-2b05-ebd7b02acd77.htm)  .

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)