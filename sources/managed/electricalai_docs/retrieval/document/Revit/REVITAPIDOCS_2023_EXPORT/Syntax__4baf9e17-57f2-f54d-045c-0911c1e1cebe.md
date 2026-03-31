[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (View, XYZ, XYZ)

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

Creates a new path of travel between two points.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static PathOfTravel Create( 	View DBView, 	XYZ pathStart, 	XYZ pathEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	DBView As View, _ 	pathStart As XYZ, _ 	pathEnd As XYZ _ ) As PathOfTravel ``` |

 

| Visual C++ |
| --- |
| ``` public: static PathOfTravel^ Create( 	View^ DBView,  	XYZ^ pathStart,  	XYZ^ pathEnd ) ``` |

#### Parameters

DBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The floor plan view to use when computing the shortest distance.

pathStart
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The start point of the path. The input Z coordinates are ignored and set to the view's level elevation.

pathEnd
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The end point of the path. The input Z coordinates are ignored and set to the view's level elevation.

#### Return Value

The newly created path of travel element, or    a null reference (  Nothing  in Visual Basic)  if no path between the two points is found.

# Remarks

InvalidOperationException is thrown if PathOfTravel cannot be created for the following conditions:

* View has crop box active and crop box is split
* View has crop box active and start or end point lies outside of the crop
* View model outline area is larger than the current limit (2,000,000 sq.ft.)
* View export contains too much geometry (more than 200,000 lines)
* Start and end points are too close

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element "DBView" is in a family document or a document in in-place edit mode. -or- View is not a floor plan view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document containing DBView is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- This operation cannot be performed while the document is in edit mode. -or- The Path of Travel calculation service is not available -or- This functionality is not available in Revit LT. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document containing DBView is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document containing DBView is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document containing DBView has no open transaction. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Create Overload](0237a26d-1900-4d52-89fc-c6c6562e4763.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)