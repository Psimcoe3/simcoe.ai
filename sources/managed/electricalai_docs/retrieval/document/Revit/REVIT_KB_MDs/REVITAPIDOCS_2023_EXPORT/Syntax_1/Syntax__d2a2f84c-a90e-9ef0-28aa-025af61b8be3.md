[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetRevealObstaclesMode Method

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

Sets Reveal Obstacles mode for the given view.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public static PathOfTravelCalculationStatus SetRevealObstaclesMode( 	View DBView, 	bool newState ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function SetRevealObstaclesMode ( _ 	DBView As View, _ 	newState As Boolean _ ) As PathOfTravelCalculationStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: static PathOfTravelCalculationStatus SetRevealObstaclesMode( 	View^ DBView,  	bool newState ) ``` |

#### Parameters

DBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view to set Reveal Obstacles mode for.

newState
:   Type:  System Boolean    
     New state of Reveal Obstacles mode to be set for the view.

#### Return Value

Result status of the operation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element "DBView" is in a family document or a document in in-place edit mode. -or- View is not a floor plan view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document containing DBView is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The Path of Travel calculation service is not available |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document containing DBView is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document containing DBView is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document containing DBView has no open transaction. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)