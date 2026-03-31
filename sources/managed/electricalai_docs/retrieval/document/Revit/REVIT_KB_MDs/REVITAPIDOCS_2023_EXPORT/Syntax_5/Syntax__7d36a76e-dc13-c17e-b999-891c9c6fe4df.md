[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cancel Method

---



|  |
| --- |
| [EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)   [See Also](#seeAlsoToggle) |

Cancels the edit scope.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Cancel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Cancel ``` |

 

| Visual C++ |
| --- |
| ``` public: void Cancel() ``` |

# Remarks

All the changes made after starting the EditScope will be rolled back.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | EditScope is not active. EditScope can only be committed or cancelled when it is active. -or- EditScope cannot be closed, for there is a transaction or transaction group still open in the document. |

# See Also

[EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)