[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveOriginToHostOrigin Method

---



|  |
| --- |
| [RevitLinkInstance Class](a3a27c39-75bf-67d1-ae78-4cadd49a9c8e.htm)   [See Also](#seeAlsoToggle) |

Moves this link instance so that the internal origin of the linked document is aligned to the internal origin of the host document. This is a one-time movement and does not set up any shared coordinates relationship.

If the rotation angle of the link instance was changed after insertion, the rotation angle can be preserved or reset to the original insertion angle.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016 SubscriptionUpdate

# Syntax

| C# |
| --- |
| ``` public void MoveOriginToHostOrigin( 	bool resetToOriginalRotation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MoveOriginToHostOrigin ( _ 	resetToOriginalRotation As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MoveOriginToHostOrigin( 	bool resetToOriginalRotation ) ``` |

#### Parameters

resetToOriginalRotation
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    

    Sets to true if:

    * restoring the original insertion angle of the link instance after it is moved if there was a rotation \ mirror transform on the link instance.
    * there was no a rotation \ mirror transform on the link instance.

    Sets to false to retain the current angle of the link instance after it is moved if there was a rotation \ mirror transform on the link instance.

# Remarks

This operation can only be performed on instances of top-level links. The internal origin is not necessarily the same location as the Project Base Point. See  [MoveBasePointToHostBasePoint(Boolean)](052feb8e-e569-ddcd-30b8-a2373d1466f8.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RevitLinkInstance is not an instance of a loaded RevitLinkType. -or- This RevitLinkInstance is not an instance of a top-level RevitLinkType. -or- The operation is not permitted because the element is pinned. |

# See Also

[RevitLinkInstance Class](a3a27c39-75bf-67d1-ae78-4cadd49a9c8e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)