[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWorksharingCentralGUID Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Gets the worksharing central GUID of the given server-based model.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public Guid GetWorksharingCentralGUID( 	ServerPath serverModelPath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWorksharingCentralGUID ( _ 	serverModelPath As ServerPath _ ) As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: Guid GetWorksharingCentralGUID( 	ServerPath^ serverModelPath ) ``` |

#### Parameters

serverModelPath
:   Type:  [Autodesk.Revit.DB ServerPath](c304ffcf-b3ae-46be-e361-a80bec83b5c0.htm)    
     The server-based model path.

#### Return Value

The worksharing central GUID.

# Remarks

The given server-based model saved in a release prior to Revit 2013 did not have this GUID. Only the given server-based model saved in Revit 2013 or later will be able to provide this value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | The central model is missing. -or- An internal error happened on the central model, please contact the server administrator. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | Thrown when the given model is not created in Revit 2013 or later release. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The server-based central model could not be accessed because of a network communication error. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | An internal error happened on the server, please contact the server administrator. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)