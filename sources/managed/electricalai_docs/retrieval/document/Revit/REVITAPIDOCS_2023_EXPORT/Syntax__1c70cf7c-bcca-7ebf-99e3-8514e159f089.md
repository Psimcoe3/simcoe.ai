[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNearestLevelId Method (Document, Double)

---



|  |
| --- |
| [Level Class](577e5d4e-a558-118c-9dea-3b810b061775.htm)   [See Also](#seeAlsoToggle) |

Returns id of the Level which is closest to the specified elevation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ElementId GetNearestLevelId( 	Document document, 	double elevation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetNearestLevelId ( _ 	document As Document, _ 	elevation As Double _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetNearestLevelId( 	Document^ document,  	double elevation ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elevation
:   Type:  System Double    
     Target Elevation.

# Remarks

The level can be at, above or below the target elevation. If there is more than one Level at the same distance from the elevation, the Level with the lowest Id will be returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Level Class](577e5d4e-a558-118c-9dea-3b810b061775.htm)

[GetNearestLevelId Overload](c4b7e959-c26d-306f-e867-d8915b67a327.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)