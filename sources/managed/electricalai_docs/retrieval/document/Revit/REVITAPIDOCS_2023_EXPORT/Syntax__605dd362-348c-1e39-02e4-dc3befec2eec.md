[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidNonContinuousRailName Method

---



|  |
| --- |
| [NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)   [See Also](#seeAlsoToggle) |

Checks whether the input name is valid for a non-continuous rail in its associated railing type.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool IsValidNonContinuousRailName( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidNonContinuousRailName ( _ 	name As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidNonContinuousRailName( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     The name to be checked.

#### Return Value

True if the name is unique for the  [!:Autodesk::Revit::DB::Architecture::RailingType]  , false otherwise.

# Remarks

The name must be unique within the  [!:Autodesk::Revit::DB::Architecture::RailingType]  to which the non-continuous rail belongs.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)