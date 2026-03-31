[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomTag Class

---



|  |
| --- |
| [Members](c8eec458-15a9-9ef4-26db-277e0c13a9c3.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides access to the room tag in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class RoomTag : SpatialElementTag ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RoomTag _ 	Inherits SpatialElementTag ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RoomTag : public SpatialElementTag ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_RoomTag(RoomTag roomTag)
{
    string message = "Room Tag : ";
    //get the location of the roomtag
    LocationPoint location = roomTag.Location as LocationPoint;
    XYZ point = location.Point;
    message += "\nRoomTag location: (" + point.X + ", " +
                   point.Y + ", " + point.Z + ")";

    //get the name of the roomTag
    message += "\nName: " + roomTag.Name;

    //get the room that the tag is associated with
    Room room = roomTag.Room;
    message += "\nThe number of the room is : " + room.Number;

    //get the view in which the tag is placed
    Autodesk.Revit.DB.View view = roomTag.View;
    if (null != view)
    {
        message += "\nView Name: " + view.Name;
    }
    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_RoomTag(roomTag As RoomTag)
    Dim message As String = "Room Tag : "
    'get the location of the roomtag
    Dim location As LocationPoint = TryCast(roomTag.Location, LocationPoint)
    Dim point As XYZ = location.Point
    message += ((vbLf & "RoomTag location: (" + point.X & ", ") + point.Y & ", ") + point.Z & ")"

    'get the name of the roomTag
    message += vbLf & "Name: " & Convert.ToString(roomTag.Name)

    'get the room that the tag is associated with
    Dim room As Room = roomTag.Room
    message += vbLf & "The number of the room is : " + room.Number

    'get the view in which the tag is placed
    Dim view As Autodesk.Revit.DB.View = roomTag.View
    If view IsNot Nothing Then
        message += vbLf & "View Name: " + view.Name
    End If
    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB SpatialElementTag](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)    
  Autodesk.Revit.DB.Architecture RoomTag

# See Also

[RoomTag Members](c8eec458-15a9-9ef4-26db-277e0c13a9c3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)