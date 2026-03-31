[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReinforcementSettings Class

---



|  |
| --- |
| [Members](b640c189-ade8-22fc-6ca0-40ff2f9a327d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides access to project-wide reinforcement settings.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ReinforcementSettings : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ReinforcementSettings _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ReinforcementSettings : public Element ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private bool SetEndTreatmentType(Document doc, RebarShape rebarShape)
{
    bool set = false;
    // check if end treatments are defined by rebar shape
    ReinforcementSettings settings = ReinforcementSettings.GetReinforcementSettings(doc);
    if (!settings.RebarShapeDefinesEndTreatments)
    {
        try
        {
            // can only be changed if document contains no rebars, area reinforcement or path reinforcement
            settings.RebarShapeDefinesEndTreatments = true;
        }
        catch (Exception e)
        {
            // cannot change the settings value
            TaskDialog.Show("Revit", e.Message);
        }
    }
    if (settings.RebarShapeDefinesEndTreatments)
    {
        EndTreatmentType treatmentType = EndTreatmentType.Create(doc, "Flame Cut");
        rebarShape.SetEndTreatmentTypeId(treatmentType.Id, 0);

        ElementId treatmentTypeId = EndTreatmentType.CreateDefaultEndTreatmentType(doc);
        rebarShape.SetEndTreatmentTypeId(treatmentTypeId, 1);

        set = true;
    }

    return set;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function SetEndTreatmentType(doc As Document, rebarShape As RebarShape) As Boolean
    Dim [set] As Boolean = False
    ' check if end treatments are defined by rebar shape
    Dim settings As ReinforcementSettings = ReinforcementSettings.GetReinforcementSettings(doc)
    If Not settings.RebarShapeDefinesEndTreatments Then
        Try
            ' can only be changed if document contains no rebars, area reinforcement or path reinforcement
            settings.RebarShapeDefinesEndTreatments = True
        Catch e As Exception
            ' cannot change the settings value
            TaskDialog.Show("Revit", e.Message)
        End Try
    End If
    If settings.RebarShapeDefinesEndTreatments Then
        Dim treatmentType As EndTreatmentType = EndTreatmentType.Create(doc, "Flame Cut")
        rebarShape.SetEndTreatmentTypeId(treatmentType.Id, 0)

        Dim treatmentTypeId As ElementId = EndTreatmentType.CreateDefaultEndTreatmentType(doc)
        rebarShape.SetEndTreatmentTypeId(treatmentTypeId, 1)

        [set] = True
    End If

    Return [set]
End Function
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Structure ReinforcementSettings

# See Also

[ReinforcementSettings Members](b640c189-ade8-22fc-6ca0-40ff2f9a327d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)