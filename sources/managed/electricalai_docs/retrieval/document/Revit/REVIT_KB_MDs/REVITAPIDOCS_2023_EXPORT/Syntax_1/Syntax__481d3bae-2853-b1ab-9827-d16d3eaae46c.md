[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transformed Property

---



|  |
| --- |
| [Profile Class](7837da2e-456d-7ef2-d5d1-76d7d3e7f9b3.htm)   [See Also](#seeAlsoToggle) |

Transforms this profile and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Profile this[ 	Transform transform ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Transformed ( _ 	transform As Transform _ ) As Profile 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Profile^ Transformed[Transform^ transform] { 	Profile^ get (Transform^ transform); } ``` |

#### Parameters

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transformation used to transform the profile.

#### Return Value

The transformed profile.

# Remarks

Transforms all the curves that define the boundary of this profile.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the handle of the specified transformation is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when failed to transform a curve in the profile. |

# See Also

[Profile Class](7837da2e-456d-7ef2-d5d1-76d7d3e7f9b3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)