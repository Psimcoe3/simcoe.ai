[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorType Class

---



|  |
| --- |
| [Members](a066bc01-6e5e-0bb6-a08b-3c55c6cde5bf.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An object that specifies the type of a floor in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class FloorType : HostObjAttributes ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FloorType _ 	Inherits HostObjAttributes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FloorType : public HostObjAttributes ``` |

# Remarks

The structural layers of the floor can be accessed via this object.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfo_FloorType(FloorType floorType)
{
    string message;
    // Get whether FloorType is a foundation slab
    message = "If is foundation slab : " + floorType.IsFoundationSlab;
    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfo_FloorType(floorType As FloorType)
    Dim message As String
    ' Get whether FloorType is a foundation slab
    message = "If is foundation slab : " & Convert.ToString(floorType.IsFoundationSlab)
    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB HostObjAttributes](a3d349c5-d457-3b56-eec4-c2fa2757c860.htm)    
  Autodesk.Revit.DB FloorType

# See Also

[FloorType Members](a066bc01-6e5e-0bb6-a08b-3c55c6cde5bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)