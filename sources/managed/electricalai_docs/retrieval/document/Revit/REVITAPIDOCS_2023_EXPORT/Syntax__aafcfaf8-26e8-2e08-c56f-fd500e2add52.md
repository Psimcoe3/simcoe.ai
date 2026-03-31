[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCallingDocumentModelPath Method

---



|  |
| --- |
| [ExternalResourceLoadContext Class](225225cb-6161-4681-34f9-1da4a6d50856.htm)   [See Also](#seeAlsoToggle) |

Returns a copy of the ModelPath of the document that is requesting the external resource.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ModelPath GetCallingDocumentModelPath() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCallingDocumentModelPath As ModelPath ``` |

 

| Visual C++ |
| --- |
| ``` public: ModelPath^ GetCallingDocumentModelPath() ``` |

#### Return Value

A copy of the ModelPath of the document that is requesting the external resource.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document requesting the external resource does not have a ModelPath, either because it is detached, or because it has not been saved to disk yet. |

# See Also

[ExternalResourceLoadContext Class](225225cb-6161-4681-34f9-1da4a6d50856.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)