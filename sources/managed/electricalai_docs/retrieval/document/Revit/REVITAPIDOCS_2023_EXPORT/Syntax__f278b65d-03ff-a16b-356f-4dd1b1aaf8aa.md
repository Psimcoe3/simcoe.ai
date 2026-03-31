[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConditionName Method

---



|  |
| --- |
| [FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)   [See Also](#seeAlsoToggle) |

Gets the name of the specified condition on the fabrication service button.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public string GetConditionName( 	int condition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConditionName ( _ 	condition As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetConditionName( 	int condition ) ``` |

#### Parameters

condition
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The condition index.

#### Return Value

The name of the specified condition on the fabrication service button.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index condition is not larger or equal to 0 and less than ConditionCount |

# See Also

[FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)