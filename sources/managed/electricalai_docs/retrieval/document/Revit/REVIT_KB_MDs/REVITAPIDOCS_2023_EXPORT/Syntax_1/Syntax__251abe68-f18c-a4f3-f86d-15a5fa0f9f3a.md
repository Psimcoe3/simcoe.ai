[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCDataPrimitiveType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Used in operations to specify the primitive type of an IFCData.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum IFCDataPrimitiveType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration IFCDataPrimitiveType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class IFCDataPrimitiveType ``` |

# Members

| Member name | Description |
| --- | --- |
| Integer | Integer. |
| Double | Double. |
| Boolean | Boolean. |
| Logical | IFCLogical type. |
| String | String. |
| Binary | Binary. When reading or writing an IFCData of primitive type Binary, the value will be the string representation of the binary value as seen in the IFC specification. |
| Enumeration | Enumeration. When reading or writing an IFCData of primitive type Enumeration, the value will be the string representation of the enumeration value as seen in the IFC specification. |
| Instance | Represents IFCAnyHandle. |
| Aggregate | Represents IFCAggregate. |
| Unknown | Unknown. |

# See Also

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)