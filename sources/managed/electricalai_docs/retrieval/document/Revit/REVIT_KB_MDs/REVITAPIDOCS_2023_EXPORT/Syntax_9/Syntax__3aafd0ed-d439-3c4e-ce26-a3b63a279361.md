[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoincidentEnergyAnalyticalModelFaceReference Method

---



|  |
| --- |
| [MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)   [See Also](#seeAlsoToggle) |

Returns a Reference to a Face from the same or a different MassEnergyAnalyticalModel that is coincident with the input Face.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static Reference GetCoincidentEnergyAnalyticalModelFaceReference( 	Document document, 	Reference referenceToFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCoincidentEnergyAnalyticalModelFaceReference ( _ 	document As Document, _ 	referenceToFace As Reference _ ) As Reference ``` |

 

| Visual C++ |
| --- |
| ``` public: static Reference^ GetCoincidentEnergyAnalyticalModelFaceReference( 	Document^ document,  	Reference^ referenceToFace ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

referenceToFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A Reference to a Face of a MassEnergyAnalyticalModel.

# Remarks

The result is always a Reference to a Face. The Reference Type should report as REFERENCE\_TYPE\_SURFACE. Currently Revit improperly reports it as REFERENCE\_TYPE\_NONE.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The Reference is not a Face of a MassEnergyAnalyticalModel. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)