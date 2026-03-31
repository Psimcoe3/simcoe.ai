[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, String)

---



|  |
| --- |
| [EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new EndTreatmentType in a document and adds the input string to the endTreatment parameter.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static EndTreatmentType Create( 	Document doc, 	string strTreatment ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	strTreatment As String _ ) As EndTreatmentType ``` |

 

| Visual C++ |
| --- |
| ``` public: static EndTreatmentType^ Create( 	Document^ doc,  	String^ strTreatment ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

strTreatment
:   Type:  System String

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void NewEndTreatmentForCouplerType(Document doc, ElementId couplerTypeId)
{
    EndTreatmentType treatmentType = EndTreatmentType.Create(doc, "Custom");
    FamilySymbol couplerType = doc.GetElement(couplerTypeId) as FamilySymbol;
    Parameter param = couplerType.get_Parameter(BuiltInParameter.COUPLER_MAIN_ENDTREATMENT);
    param.Set(treatmentType.Id);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub NewEndTreatmentForCouplerType(doc As Document, couplerTypeId As ElementId)
    Dim treatmentType As EndTreatmentType = EndTreatmentType.Create(doc, "Custom")
    Dim couplerType As FamilySymbol = TryCast(doc.GetElement(couplerTypeId), FamilySymbol)
    Dim param As Parameter = couplerType.Parameter(BuiltInParameter.COUPLER_MAIN_ENDTREATMENT)
    param.[Set](treatmentType.Id)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)

[Create Overload](bfa0b5ed-b4e3-dcba-67f9-7ea73bf408b2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)