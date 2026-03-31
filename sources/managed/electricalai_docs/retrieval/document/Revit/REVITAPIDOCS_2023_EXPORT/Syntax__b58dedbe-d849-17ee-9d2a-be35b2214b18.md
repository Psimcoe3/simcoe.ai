[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Delete Method

---



|  |
| --- |
| [ViewSheetSetting Class](e85ce148-ef47-7640-1864-6035b6773411.htm)   [See Also](#seeAlsoToggle) |

Delete the current view sheet set, and make the In-Session set as the current one.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Delete() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Delete As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Delete() ``` |

#### Return Value

False if Delete operation fails, otherwise True.

# Remarks

If the current view sheet set is In-Session, an InvalidOperationException will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the current view sheet set is In-Session. |

# See Also

[ViewSheetSetting Class](e85ce148-ef47-7640-1864-6035b6773411.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)