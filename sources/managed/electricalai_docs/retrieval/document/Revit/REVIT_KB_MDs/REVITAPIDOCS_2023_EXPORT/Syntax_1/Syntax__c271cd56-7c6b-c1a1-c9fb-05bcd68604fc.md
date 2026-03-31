[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MakeNonReporting Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Set the reporting family parameter as a regular/driving parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void MakeNonReporting( 	FamilyParameter familyParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MakeNonReporting ( _ 	familyParameter As FamilyParameter _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MakeNonReporting( 	FamilyParameter^ familyParameter ) ``` |

#### Parameters

familyParameter
:   Type:  [Autodesk.Revit.DB FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"familyParameter"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when attempting to make a parameter which is labeled to an arc length dimension non-reporting. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)