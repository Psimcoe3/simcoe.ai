[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFormula Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Set the formula of a family parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetFormula( 	FamilyParameter familyParameter, 	string formula ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFormula ( _ 	familyParameter As FamilyParameter, _ 	formula As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFormula( 	FamilyParameter^ familyParameter,  	String^ formula ) ``` |

#### Parameters

familyParameter
:   Type:  [Autodesk.Revit.DB FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)    
     The family parameter.

formula
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The formula string, input    a null reference (  Nothing  in Visual Basic)  to clean the formula of the parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"familyParameter"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when there is no valid family type, or the parameter cannot be assigned a formula, or the operation make a circular chain of references among the formulas. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)