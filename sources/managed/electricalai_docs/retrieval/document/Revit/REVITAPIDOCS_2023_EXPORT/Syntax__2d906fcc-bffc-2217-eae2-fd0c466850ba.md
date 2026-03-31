[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLinkedConnectorElement Method

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Set the linked connector element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetLinkedConnectorElement( 	ConnectorElement otherConnector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLinkedConnectorElement ( _ 	otherConnector As ConnectorElement _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLinkedConnectorElement( 	ConnectorElement^ otherConnector ) ``` |

#### Parameters

otherConnector
:   Type:  [Autodesk.Revit.DB ConnectorElement](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)    
     The connector to link to.

# Remarks

Set the linked connector to    a null reference (  Nothing  in Visual Basic)  to remove the link.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The connector being linked to is a different domain than that of the calling connector. -or- The connector being linked to is the same as the calling connector. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This connector type does not support linked connectors. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)