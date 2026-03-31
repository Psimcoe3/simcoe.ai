[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTangentLock Method

---



|  |
| --- |
| [CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)   [See Also](#seeAlsoToggle) |

Sets a new status for an existing tangent join with another curve element at the given end-point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetTangentLock( 	int end, 	ElementId other, 	bool state ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetTangentLock ( _ 	end As Integer, _ 	other As ElementId, _ 	state As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetTangentLock( 	int end,  	ElementId^ other,  	bool state ) ``` |

#### Parameters

end
:   Type:  System Int32    
     Index of one of the curve's ends. Values '0' and '1' indicate the start or end point, respectively.

other
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of another Curve Element from the same document.

state
:   Type:  System Boolean    
     Requested new state of the lock; True to lock it, False to unlock it.

# Remarks

The input status indicates whether the tangent join is to be locked or unlocked. Note that the status can be set only if this and the other curve element are currently joined and tangent at the given point.

Locking a tangent join between elements of a family will make the family parametric. A parametric family needs to utilize a geometry solver in order to determine final shapes of its instances. Using the solver in families which contain large sketches may cause regenerations of such families to become significantly slower. To determine whether a particular family falls into such a category, programmers can query  [IsParametric](1d4166dd-057d-9d9b-e28f-7bd250bbe587.htm)  property and  [!:Autodesk::Revit::DB::Family::DoesContainLargeSketches()]  method of the  [Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)  class.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given Id does not represent any of the two end-points of a curve element. A valid value of either '0' or '1' is expected. -or- The given ElementId (%elementId) is not of a valid Curve Element. A valid Curve Element must be in the same document and must be diferent than this curve elements self. -or- This element has no tangent join with the input element at the given end-point. -or- The element other does not exist in the document containing this CurveElement |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This curve element does not support tangent joins with other elements. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | This CurveElement is an internal element, such as a component of a loaded family or a group type. -or- The document containing this CurveElement is in Group Edit Mode, Sketch Edit Mode, or Paste Mode, and the element is not a member of the group, sketch, or clipboard. -or- This CurveElement is a member of a group or sketch, and the document is not currently editing the group or sketch. -or- other is an internal element, such as a component of a loaded family or a group type. -or- The document containing other is in Group Edit Mode, Sketch Edit Mode, or Paste Mode, and the element is not a member of the group, sketch, or clipboard. -or- other is a member of a group or sketch, and the document is not currently editing the group or sketch. |

# See Also

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)