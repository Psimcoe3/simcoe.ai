[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AcquireCoordinates Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Acquires coordinates from the specified link instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void AcquireCoordinates( 	ElementId linkInstanceId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AcquireCoordinates ( _ 	linkInstanceId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AcquireCoordinates( 	ElementId^ linkInstanceId ) ``` |

#### Parameters

linkInstanceId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The  ElementId  of the link instance (such as  RevitLinkInstance  or  ImportInstance  ) from which the coordinates would be acquired.

# Remarks

When you acquire coordinates from the linked model, the shared coordinates of the linked model become the shared coordinates of the host model, based on the position of the linked model instance in the host model. There is no change to the host model's internal coordinates.

The host model also acquires True North from the linked model. The origin of the linked model's shared coordinates becomes the origin of the host model's shared coordinates.

When a Revit model acquires coordinates from a linked DWG file, the World Coordinate System (WCS) of the selected linked DWG file becomes the shared coordinate system of the host Revit model, based on the position of the linked DWG instance. The Y axis of the DWG becomes True North, and the origin of the DWG becomes the origin of the shared coordinate system of the Revit model.

On acquiring coordinates from a geo-referenced model, the geolocation information will be pulled from the linked model to the host model.

Unlike UI operation Acquire Coordinates, calling the API would always overwrite the geolocation information in the host model even if it is different from the one in the linked model, or the linked model has empty geolocation information (in which case the geolocation information in the host model would be removed).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element linkInstanceId does not exist in the document |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Document is not a project document. -or- This Document is in an edit mode. -or- The coordinate system of the selected model are the same as the host model. -or- Cannot acquire coordinates from a model placed multiple times. -or- Failed to acquire coordinates from the link instance. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)