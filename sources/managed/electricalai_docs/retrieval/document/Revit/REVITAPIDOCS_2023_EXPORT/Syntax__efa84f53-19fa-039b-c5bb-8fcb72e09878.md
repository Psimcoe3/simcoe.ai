[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsType Class

---



|  |
| --- |
| [Members](03e9941e-aa3e-64e9-125a-5d94d319e673.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A type element containing the properties for a component-based stair.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class StairsType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StairsType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StairsType : public ElementType ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void GetStairsType(Stairs stairs)
{
    StairsType stairsType = stairs.Document.GetElement(stairs.GetTypeId()) as StairsType;

    // Format stairs type info for display
    string info = "Stairs Type:  " + stairsType.Name;
    info += "\nLeft Lateral Offset:  " + stairsType.LeftLateralOffset;
    info += "\nRight Lateral Offset:  " + stairsType.RightLateralOffset;
    info += "\nMax Riser Height:  " + stairsType.MaxRiserHeight;
    info += "\nMin Run Width:  " + stairsType.MinRunWidth;



    TaskDialog.Show("Revit", info);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetStairsType(stairs As Stairs)
    Dim stairsType As StairsType = TryCast(stairs.Document.GetElement(stairs.GetTypeId()), StairsType)

    ' Format stairs type info for display
    Dim info As String = "Stairs Type:  " + stairsType.Name
    info += vbLf & "Left Lateral Offset:  " + stairsType.LeftLateralOffset
    info += vbLf & "Right Lateral Offset:  " + stairsType.RightLateralOffset
    info += vbLf & "Max Riser Height:  " + stairsType.MaxRiserHeight
    info += vbLf & "Min Run Width:  " + stairsType.MinRunWidth



    TaskDialog.Show("Revit", info)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Architecture StairsType

# See Also

[StairsType Members](03e9941e-aa3e-64e9-125a-5d94d319e673.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)