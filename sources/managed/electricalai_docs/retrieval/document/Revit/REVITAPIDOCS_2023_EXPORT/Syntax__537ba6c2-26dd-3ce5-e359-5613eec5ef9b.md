[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBendProfile Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns the profile (not including generated fillets) that defines the shape of the Fabric Sheet bending.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public CurveLoop GetBendProfile() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBendProfile As CurveLoop ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveLoop^ GetBendProfile() ``` |

#### Return Value

The profile that defines the shape of the fabric sheet bending for bent fabric sheet, for flat fabric sheet    a null reference (  Nothing  in Visual Basic)  will be returned.

# Remarks

The returned profile defines the center-curve of a wire. Note that bent Fabric Sheets can have planar geometry, but flat Fabric Sheets are always planar.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
#region Autodesk.Revit.DB.Structure.FabricSheet.SetBendProfile(Autodesk.Revit.DB.CurveLoop)
private void ModifyBentFabricSheet(Document document, FabricSheet bentFabricSheet)
{
   CurveLoop newBendingProfile = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, new XYZ(0, 0, -1));
   bentFabricSheet.SetBendProfile(newBendingProfile);

   // Give the user some information
   TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.ToString()));
}
#endregion
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
#Region "Autodesk.Revit.DB.Structure.FabricSheet.SetBendProfile(Autodesk.Revit.DB.CurveLoop)"
        Private Sub ModifyBentFabricSheet(document As Document, bentFabricSheet As FabricSheet)
            Dim newBendingProfile As CurveLoop = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, New XYZ(0, 0, -1))
            bentFabricSheet.SetBendProfile(newBendingProfile)

            ' Give the user some information
            TaskDialog.Show("Revit", String.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.ToString()))
        End Sub
#End Region
```

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)