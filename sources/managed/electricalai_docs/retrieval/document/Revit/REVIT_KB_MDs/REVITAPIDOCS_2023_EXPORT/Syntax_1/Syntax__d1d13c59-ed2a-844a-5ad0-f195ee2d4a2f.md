[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create3DOrthographic Method

---



|  |
| --- |
| [AssemblyViewUtils Class](4c839bed-9f56-c255-afba-8152c9171a22.htm)   [See Also](#seeAlsoToggle) |

Creates a new orthographic 3D assembly view for the assembly instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static View3D Create3DOrthographic( 	Document document, 	ElementId assemblyInstanceId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create3DOrthographic ( _ 	document As Document, _ 	assemblyInstanceId As ElementId _ ) As View3D ``` |

 

| Visual C++ |
| --- |
| ``` public: static View3D^ Create3DOrthographic( 	Document^ document,  	ElementId^ assemblyInstanceId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the view will be added.

assemblyInstanceId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the assembly instance that owns the new view.

#### Return Value

A new orthographic 3D assembly view.

# Remarks

The view will have the same orientation as the Default 3D view. The document must be regenerated before using the 3D view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | assemblyInstanceId is not an AssemblyInstance. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AssemblyViewUtils Class](4c839bed-9f56-c255-afba-8152c9171a22.htm)

[Create3DOrthographic Overload](d749ec99-f1dd-8979-0869-89c02c394cec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)