[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFlow Method

---



|  |
| --- |
| [MEPAnalyticalConnection Class](5564555f-89fd-9348-33f2-f8d1d68cafe5.htm)   [See Also](#seeAlsoToggle) |

Gets the flow value of this analytical connection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

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

#### Return Value

The flow value.

# Remarks

If the network flow is asynchronously calculated, this method would wait until the calculation is completed. This ensures the returned flow value is always up to date.

# See Also

[MEPAnalyticalConnection Class](5564555f-89fd-9348-33f2-f8d1d68cafe5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)