[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, IList(Curve), SketchPlane, XYZ, Boolean)

---



|  |
| --- |
| [BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)   [See Also](#seeAlsoToggle) |

Creates a new BeamSystem with specified profile curves.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static BeamSystem Create( 	Document document, 	IList<Curve> profile, 	SketchPlane sketchPlane, 	XYZ direction, 	bool is3d ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	profile As IList(Of Curve), _ 	sketchPlane As SketchPlane, _ 	direction As XYZ, _ 	is3d As Boolean _ ) As BeamSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static BeamSystem^ Create( 	Document^ document,  	IList<Curve^>^ profile,  	SketchPlane^ sketchPlane,  	XYZ^ direction,  	bool is3d ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the new BeamSystem is created.

profile
:   Type:  System.Collections.Generic IList   [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The profile of the BeamSystem.

sketchPlane
:   Type:  [Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm)    
     The work-plane for the BeamSystem.

direction
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The direction is the direction of the BeamSystem.

is3d
:   Type:  System Boolean    
     Whether the BeamSystem is 3D. If the BeamSystem is 3D, the sketchPlane must be a level, otherwise an exception will be thrown.

#### Return Value

If successful, a new BeamSystem object will be returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | SketchPlane is not valid for BeamSystem creation. -or- The input profile contains at least one helical curve and is not supported for this operation. -or- The profile curves must be in the sketch plane. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The BeamSystem is 3D, but the SketchPlane is not a level. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)

[Create Overload](38e7211c-d61b-01fb-7c66-0fca146684a2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)