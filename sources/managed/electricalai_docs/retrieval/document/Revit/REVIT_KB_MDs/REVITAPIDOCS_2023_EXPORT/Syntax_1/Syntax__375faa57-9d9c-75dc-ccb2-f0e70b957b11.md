[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCenterPointsForConnectedGridCellsInSpaceVolume Method

---



|  |
| --- |
| [BuildingEnvelopeAnalyzer Class](7f7ccb3f-75e2-6e4d-021c-85718ea2f30b.htm)   [See Also](#seeAlsoToggle) |

Returns the collection of connected cells in an enclosed space volume.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<XYZ> GetCenterPointsForConnectedGridCellsInSpaceVolume( 	int spaceVolume ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCenterPointsForConnectedGridCellsInSpaceVolume ( _ 	spaceVolume As Integer _ ) As IList(Of XYZ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<XYZ^>^ GetCenterPointsForConnectedGridCellsInSpaceVolume( 	int spaceVolume ) ``` |

#### Parameters

spaceVolume
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

#### Return Value

The center points for the connected analytical grid cells in the enclosed space volume.

# Remarks

This method requires the building envelope analyzer method created with the option set to compute enclosed space volumes.

# See Also

[BuildingEnvelopeAnalyzer Class](7f7ccb3f-75e2-6e4d-021c-85718ea2f30b.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)