[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMinimum Method

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Calculates the minimum value for all primitives

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double GetMinimum( 	int resultIndex, 	bool rawValue ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMinimum ( _ 	resultIndex As Integer, _ 	rawValue As Boolean _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetMinimum( 	int resultIndex,  	bool rawValue ) ``` |

#### Parameters

resultIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of result schema

rawValue
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     If true returned value is NOT multiplied by the current result's units multiplier, otherwise it IS

#### Return Value

Resulting minimum value

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | Thrown when current measurement is >= the number of measurements for at least one primitive |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)