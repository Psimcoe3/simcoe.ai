[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllExternalResourceReferences Method (Document)

---



|  |
| --- |
| [ExternalResourceUtils Class](1d4d9853-ab61-8a7f-06eb-2c79032b47d3.htm)   [See Also](#seeAlsoToggle) |

Gets the ids of all elements which refer to external resources.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static ISet<ElementId> GetAllExternalResourceReferences( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAllExternalResourceReferences ( _ 	document As Document _ ) As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ISet<ElementId^>^ GetAllExternalResourceReferences( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Revit Document containing the external resource references.

#### Return Value

The ids of all elements which refer to external resources.

# Remarks

This function will not return the ids of nested Revit links; it only returns top-level references.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalResourceUtils Class](1d4d9853-ab61-8a7f-06eb-2c79032b47d3.htm)

[GetAllExternalResourceReferences Overload](3b6f0931-48f3-6fd9-dfa1-0354d202b833.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)