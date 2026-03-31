[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPartMakerMethodToDivideVolumeFW Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Obtains the object allowing access to the divided volume properties of the PartMaker.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static PartMakerMethodToDivideVolumes GetPartMakerMethodToDivideVolumeFW( 	PartMaker partMaker ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPartMakerMethodToDivideVolumeFW ( _ 	partMaker As PartMaker _ ) As PartMakerMethodToDivideVolumes ``` |

 

| Visual C++ |
| --- |
| ``` public: static PartMakerMethodToDivideVolumes^ GetPartMakerMethodToDivideVolumeFW( 	PartMaker^ partMaker ) ``` |

#### Parameters

partMaker
:   Type:  [Autodesk.Revit.DB PartMaker](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)    
     The PartMaker.

#### Return Value

The object handle. Returns    a null reference (  Nothing  in Visual Basic)  if the PartMaker does not represent divided volumes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)