[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of an Analytical Panel within the project.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static AnalyticalPanel Create( 	Document aDoc, 	CurveLoop curveLoop ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	curveLoop As CurveLoop _ ) As AnalyticalPanel ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalyticalPanel^ Create( 	Document^ aDoc,  	CurveLoop^ curveLoop ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Revit document.

curveLoop
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     CurveLoop for the Analytical Panel.

#### Return Value

The newly created AnalyticalPanel instance.

# Remarks

CurveLoop must be planar and not self-intersecting.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One of the following requirements is not satisfied : - curve loop curveLoop is not planar - curve loop curveLoop is self-intersecting - curve loop curveLoop contains zero length curves |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AnalyticalPanel Class](b88181d3-743b-8cca-8fb3-0cc13e5d70aa.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)