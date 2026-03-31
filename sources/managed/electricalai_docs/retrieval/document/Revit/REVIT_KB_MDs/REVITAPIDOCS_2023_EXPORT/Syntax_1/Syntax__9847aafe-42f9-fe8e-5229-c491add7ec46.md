[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewRoomTag Method

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new RoomTag referencing a room in the host model or in a Revit link.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public RoomTag NewRoomTag( 	LinkElementId roomId, 	UV point, 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewRoomTag ( _ 	roomId As LinkElementId, _ 	point As UV, _ 	viewId As ElementId _ ) As RoomTag ``` |

 

| Visual C++ |
| --- |
| ``` public: RoomTag^ NewRoomTag( 	LinkElementId^ roomId,  	UV^ point,  	ElementId^ viewId ) ``` |

#### Parameters

roomId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The HostOrLinkElementId of the Room.

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     A 2D point that defines the tag location on the level of the room.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the view where the tag will be shown. If    a null reference (  Nothing  in Visual Basic)  and the room in not in a Revit link, the view of the room will be used.

#### Return Value

If successful a RoomTag object will be returned, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
RoomTag CreateRoomTag(Autodesk.Revit.DB.Document document, Room room)
{
    // Create a UV structure which determine the room tag location
   UV roomTagLocation = new UV(0, 0); 

    // Create a new room tag in the created room
    LinkElementId roomId = new LinkElementId(room.Id);
    RoomTag roomTag = document.Create.NewRoomTag(roomId, roomTagLocation, ElementId.InvalidElementId);
    if (null == roomTag)
    {
        throw new Exception("Create a new room tag failed.");
    }

    // Give the user some information
    TaskDialog.Show("Revit","Room tag created successfully.");

    return roomTag;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreateRoomTag(document As Autodesk.Revit.DB.Document, room As Room) As RoomTag
    ' Create a UV structure which determine the room tag location
    Dim roomTagLocation As New UV(0, 0)

    ' Create a new room tag in the created room
    Dim roomId As New LinkElementId(room.Id)
    Dim roomTag As RoomTag = document.Create.NewRoomTag(roomId, roomTagLocation, ElementId.InvalidElementId)
    If roomTag Is Nothing Then
        Throw New Exception("Create a new room tag failed.")
    End If

    ' Give the user some information
    TaskDialog.Show("Revit", "Room tag created successfully.")

    Return roomTag
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | viewId is not associated with a plan view or section view. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | viewId is null and the room is in a linked file. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)