[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, String, Guid, String, ElementId, IList(ConnectionInputPointInfo))

---



|  |
| --- |
| [StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)   [See Also](#seeAlsoToggle) |

Creates a new StructuralConnectionHandlerType object.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static StructuralConnectionHandlerType Create( 	Document pADoc, 	string name, 	Guid guid, 	string familyName, 	ElementId categoryId, 	IList<ConnectionInputPointInfo> inputPointsInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	pADoc As Document, _ 	name As String, _ 	guid As Guid, _ 	familyName As String, _ 	categoryId As ElementId, _ 	inputPointsInfo As IList(Of ConnectionInputPointInfo) _ ) As StructuralConnectionHandlerType ``` |

 

| Visual C++ |
| --- |
| ``` public: static StructuralConnectionHandlerType^ Create( 	Document^ pADoc,  	String^ name,  	Guid guid,  	String^ familyName,  	ElementId^ categoryId,  	IList<ConnectionInputPointInfo^>^ inputPointsInfo ) ``` |

#### Parameters

pADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

name
:   Type:  System String    
     The type name.

guid
:   Type:  System Guid    
     Connection GUID.

familyName
:   Type:  System String    
     Name of system family which created type will belong to.

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Category identity of connection type.

inputPointsInfo
:   Type:  System.Collections.Generic IList   [ConnectionInputPointInfo](1a44f5bf-0f28-e1f6-0085-e35bec49d5c6.htm)    
     List of description information used for the selection of input points.

#### Return Value

The newly created instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)

[Create Overload](e8bc4ab9-de41-ec75-fff0-0339c734bd5d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)