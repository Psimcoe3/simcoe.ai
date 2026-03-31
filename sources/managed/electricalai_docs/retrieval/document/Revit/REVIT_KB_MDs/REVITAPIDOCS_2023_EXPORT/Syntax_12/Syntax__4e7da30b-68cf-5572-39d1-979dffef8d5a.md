[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Finish Method

---



|  |
| --- |
| [BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)   [See Also](#seeAlsoToggle) |

Complete construction of the geometry. The geometry will be validated and, if valid, stored in this Builder. Otherwise it will be deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public BRepBuilderOutcome Finish() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Finish As BRepBuilderOutcome ``` |

 

| Visual C++ |
| --- |
| ``` public: BRepBuilderOutcome Finish() ``` |

#### Return Value

BRepBuilderOutcome.Success if successful, BRepBuilderOutcome.Failure otherwise.

# Remarks

If this function returned anything but BRepBuilderOutcome.Success, this BrepBuilder object should be discarded. An attempt to retrieve the built b-rep via GetBRep() will cause an exception to be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This BRepBuilder object isn't accepting new data, either because it has already been used to build geometry, or because of an error. Consult the State property of the BRepBuilder object for more details. -or- BRep doesn't have enough faces. -or- FinishFace() must be called on all the faces of the BRepBuilder. |

# See Also

[BRepBuilder Class](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)