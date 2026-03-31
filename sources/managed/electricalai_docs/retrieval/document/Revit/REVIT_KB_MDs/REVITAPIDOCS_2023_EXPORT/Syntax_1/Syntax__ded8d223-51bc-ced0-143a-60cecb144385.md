[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveCurtainGrid Method

---



|  |
| --- |
| [CurtainSystem Class](49847a7a-35e9-09f3-e723-5f906a14b0e3.htm)   [See Also](#seeAlsoToggle) |

Remove CurtainGrid from the specified face for the CurtainSystem.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void RemoveCurtainGrid( 	Reference face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveCurtainGrid ( _ 	face As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveCurtainGrid( 	Reference^ face ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The face CurtainGrid will be removed from.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input parameter face is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the CurtainGrid cannot be removed from the specified face or regenerate fails. |

# See Also

[CurtainSystem Class](49847a7a-35e9-09f3-e723-5f906a14b0e3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)