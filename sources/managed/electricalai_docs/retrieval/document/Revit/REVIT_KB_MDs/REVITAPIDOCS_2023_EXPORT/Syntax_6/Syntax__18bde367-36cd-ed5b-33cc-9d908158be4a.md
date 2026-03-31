[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayoutAsFixedNumber Method

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

Sets the Layout Rule property of rebar set to Fixed Number.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetLayoutAsFixedNumber( 	int numberOfBars ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayoutAsFixedNumber ( _ 	numberOfBars As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayoutAsFixedNumber( 	int numberOfBars ) ``` |

#### Parameters

numberOfBars
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The number of bars in set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarFreeFormAccessor doesn't contain a valid rebar reference. -or- This RebarFreeFormAccessor Rebar doesn't contain a valid server GUID. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)