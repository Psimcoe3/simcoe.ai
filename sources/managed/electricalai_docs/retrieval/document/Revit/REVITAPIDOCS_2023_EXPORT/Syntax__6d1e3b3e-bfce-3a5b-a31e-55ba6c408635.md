[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFlags Method (Int32, Int32)

---



|  |
| --- |
| [ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)   [See Also](#seeAlsoToggle) |

Sets the flags associated to a given measurement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetFlags( 	int flags, 	int measurement ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFlags ( _ 	flags As Integer, _ 	measurement As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFlags( 	int flags,  	int measurement ) ``` |

#### Parameters

flags
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The value of the flags to set. Flags values are defined in the enumerated class ValueAtPointFlags and are combined into the int value.

measurement
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Measurement for which to set flags.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for measurement is negative. |

# See Also

[ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)

[SetFlags Overload](dff6d4fa-7c12-ca4e-0439-75b1e4f80b9e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)