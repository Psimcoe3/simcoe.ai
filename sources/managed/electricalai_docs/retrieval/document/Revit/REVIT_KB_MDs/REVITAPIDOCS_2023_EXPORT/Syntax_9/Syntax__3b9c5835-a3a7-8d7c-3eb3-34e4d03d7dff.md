[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMassEnergyAnalyticalModelIdForMassInstance Method

---



|  |
| --- |
| [MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)   [See Also](#seeAlsoToggle) |

Get the ElementId of the MassEnergyAnalyticalModel for a mass instance.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ElementId GetMassEnergyAnalyticalModelIdForMassInstance( 	Document document, 	ElementId massInstanceId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetMassEnergyAnalyticalModelIdForMassInstance ( _ 	document As Document, _ 	massInstanceId As ElementId _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetMassEnergyAnalyticalModelIdForMassInstance( 	Document^ document,  	ElementId^ massInstanceId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

massInstanceId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of a mass instance.

#### Return Value

ElementId of a MassEnergyAnalyticalModel.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId massInstanceId is not a mass instance. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)