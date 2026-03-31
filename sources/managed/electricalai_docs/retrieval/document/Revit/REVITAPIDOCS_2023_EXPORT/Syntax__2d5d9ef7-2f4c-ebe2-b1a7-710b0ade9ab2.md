[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFlow Method

---



|  |
| --- |
| [MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)   [See Also](#seeAlsoToggle) |

Gets the flow of this mechanical system.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double GetFlow() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFlow As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetFlow() ``` |

# Remarks

The system flow is calculated in the non-blocking evaluation framework. The caller may set up callbacks that react to the asynchronous calculation results. If no callback is set up (e.g, called from third-party applications), the calculation is automatically switched to synchronous calculation so the caller can access the up-to-date result. Similarly, the public method get\_ParameterValue(BuiltInParameter.RBS\_DUCT\_FLOW\_PARAM) has the same behavior. Due to this change, the parameter RBS\_DUCT\_FLOW\_PARAM no longer supports dynamic model update.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The flow can not be calculated for this system. |

# See Also

[MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)