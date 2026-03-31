[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetIndexStreamLine Method

---



|  |
| --- |
| [IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.htm)   [See Also](#seeAlsoToggle) |

Gets a stream that can be used to write  [IndexLine](3b22e25e-f934-3931-6f22-e451ffcc11b0.htm)  segment primitives into the buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IndexStreamLine GetIndexStreamLine() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetIndexStreamLine As IndexStreamLine ``` |

 

| Visual C++ |
| --- |
| ``` public: IndexStreamLine^ GetIndexStreamLine() ``` |

#### Return Value

The stream that can be used to write into this buffer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the buffer is not mapped. -or- Thrown if the buffer has insufficient space. |

# See Also

[IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)