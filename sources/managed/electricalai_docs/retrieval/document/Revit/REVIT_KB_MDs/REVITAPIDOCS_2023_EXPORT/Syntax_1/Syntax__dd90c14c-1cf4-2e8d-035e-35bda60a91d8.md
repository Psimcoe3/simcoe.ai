[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateNoteBlock Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a note block.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ViewSchedule CreateNoteBlock( 	Document document, 	ElementId familyId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateNoteBlock ( _ 	document As Document, _ 	familyId As ElementId _ ) As ViewSchedule ``` |

 

| Visual C++ |
| --- |
| ``` public: static ViewSchedule^ CreateNoteBlock( 	Document^ document,  	ElementId^ familyId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new schedule will be added.

familyId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the family whose elements will be included in the schedule.

#### Return Value

The newly created schedule.

# Remarks

A note block is a schedule of the Generic Annotations category that shows elements of a single family rather than all elements in the category.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
ViewSchedule noteBlockSchedule = null;

using (Transaction transaction = new Transaction(doc, "Creating Note BLock"))
{
    //Get first ElementId of a Note Block family.
    ICollection<ElementId> noteblockFamilies = ViewSchedule.GetValidFamiliesForNoteBlock(doc);
    ElementId symbolId = noteblockFamilies.First<ElementId>();

    if (!symbolId.Equals(ElementId.InvalidElementId))
    {
        transaction.Start();

        //Create a note-block view schedule.
        noteBlockSchedule = ViewSchedule.CreateNoteBlock(doc, symbolId);
    }

    if (null != areaSchedule)
    {
        transaction.Commit();
    }
    else
    {
        transaction.RollBack();
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim noteBlockSchedule As ViewSchedule = Nothing

Using transaction As New Transaction(doc, "Creating Note BLock")
    'Get first ElementId of a Note Block family.
    Dim noteblockFamilies As ICollection(Of ElementId) = ViewSchedule.GetValidFamiliesForNoteBlock(doc)
    Dim symbolId As ElementId = noteblockFamilies.First()

    If Not symbolId.Equals(ElementId.InvalidElementId) Then
        transaction.Start()

        'Create a note-block view schedule.
        noteBlockSchedule = ViewSchedule.CreateNoteBlock(doc, symbolId)
    End If

    If areaSchedule IsNot Nothing Then
        transaction.Commit()
    Else
        transaction.RollBack()
    End If
End Using
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- familyId is not a valid family for a note block. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)