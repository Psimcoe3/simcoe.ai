[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ISet(ElementId))

---



|  |
| --- |
| [DeleteElements Class](f8d66e28-6e49-7b79-42e5-aa92ee9e536f.htm)   [See Also](#seeAlsoToggle) |

Creates an instance of the DeleteElements resolution.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FailureResolution Create( 	Document document, 	ISet<ElementId> ids ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	ids As ISet(Of ElementId) _ ) As FailureResolution ``` |

 

| Visual C++ |
| --- |
| ``` public: static FailureResolution^ Create( 	Document^ document,  	ISet<ElementId^>^ ids ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document which owns the elements to delete.

ids
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ids of the elements that will be deleted when this resolution is chosen.

#### Return Value

The instance of the DeleteElements resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input ids is empty or contains an invalid element id. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DeleteElements Class](f8d66e28-6e49-7b79-42e5-aa92ee9e536f.htm)

[Create Overload](4aca5a57-87fa-cd4b-b6fb-135abc4851e7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)