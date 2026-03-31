[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetEndTreatmentTypeId Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sets the EndTreatmentType id at the specified rebar shape end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetEndTreatmentTypeId( 	ElementId endTreatmentId, 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetEndTreatmentTypeId ( _ 	endTreatmentId As ElementId, _ 	iEnd As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetEndTreatmentTypeId( 	ElementId^ endTreatmentId,  	int iEnd ) ``` |

#### Parameters

endTreatmentId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of an EndTreatmentType element, or invalidElementId if the rebar shape should have no end treatment at the specified end.

iEnd
:   Type:  System Int32    
     0 for the start end treatment, 1 for the end end treatment.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
#region Autodesk.Revit.DB.Structure.ReinforcementSettings
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
#endregion
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
#Region "Autodesk.Revit.DB.Structure.ReinforcementSettings"
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
#End Region
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iEnd not a valid shape end -or- the parameter endTreatmentId is not an EndTreatmentType element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)