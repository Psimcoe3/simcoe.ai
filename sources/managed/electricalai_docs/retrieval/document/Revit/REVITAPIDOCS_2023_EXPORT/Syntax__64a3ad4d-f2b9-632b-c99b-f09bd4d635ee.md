[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Set Method (Int32)

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Sets the parameter to a new integer value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Set( 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Set ( _ 	value As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Set( 	int value ) ``` |

#### Parameters

value
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The new integer value to which the parameter is to be set.

#### Return Value

The Set method will return True if the parameter was successfully set to the new value, otherwise false.

# Remarks

You should only use this method if the StorageType property reports the type of the parameter as an integer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The parameter is read-only. |

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Set Overload](906458f5-cc02-5972-1272-a59f27739c12.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)