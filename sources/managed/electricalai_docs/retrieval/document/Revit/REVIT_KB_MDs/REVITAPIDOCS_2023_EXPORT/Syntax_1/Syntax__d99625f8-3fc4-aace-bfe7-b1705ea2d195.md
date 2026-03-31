[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSplittingCurves Method (Document, ElementId)

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Identifies the curves that were used to create the part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public static IList<Curve> GetSplittingCurves( 	Document document, 	ElementId partId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetSplittingCurves ( _ 	document As Document, _ 	partId As ElementId _ ) As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<Curve^>^ GetSplittingCurves( 	Document^ document,  	ElementId^ partId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The source document of the part.

partId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The part id.

#### Return Value

The curves that created the part. Empty if partId is not a Part or Part is not divided.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetCurveDividers(Part part)
{
   StringBuilder message = new StringBuilder();

   // Get curve dividers.
   IList<Curve> divisionCurves = PartUtils.GetSplittingCurves(part.Document, part.Id);

   if (divisionCurves.Count == 0)
      message.AppendLine("Part is not divided.");
   else
   {
      message.AppendLine("The dividers are : ");
      if (divisionCurves.Count > 0)
         message.AppendLine(divisionCurves.Count.ToString() + " division curves");
   }

   TaskDialog.Show("Revit", message.ToString());
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetCurveDividers(ByVal part As Part)
    Dim message As StringBuilder = New StringBuilder
    ' Get curve dividers.
    Dim divisionCurves As IList(Of Curve) = PartUtils.GetSplittingCurves(part.Document, part.Id)
    If (divisionCurves.Count = 0) Then
        message.AppendLine("Part is not divided.")
    Else
        message.AppendLine("The dividers are : ")
        If (divisionCurves.Count > 0) Then
            message.AppendLine((divisionCurves.Count.ToString + " division curves"))
        End If

    End If

    TaskDialog.Show("Revit", message.ToString)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[GetSplittingCurves Overload](52e5fb58-36d6-5f45-2380-c96674ced907.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)