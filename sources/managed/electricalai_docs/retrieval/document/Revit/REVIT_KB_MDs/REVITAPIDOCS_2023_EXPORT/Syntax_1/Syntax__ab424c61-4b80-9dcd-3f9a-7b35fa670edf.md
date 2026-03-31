[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyInstanceReferenceType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Corresponds to the possible values of parameter "Is Reference" of reference planes and parameter "Reference" of reference lines in families. This enum is used to identify references of family instances corresponding to reference planes and reference lines in the family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public enum FamilyInstanceReferenceType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration FamilyInstanceReferenceType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class FamilyInstanceReferenceType ``` |

# Members

| Member name | Description |
| --- | --- |
| Left | Reference plane whose "Is Reference" parameter is set to "Left". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| CenterLeftRight | Reference plane whose "Is Reference" parameter is set to "Center (Left/Right)". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| Right | Reference plane whose "Is Reference" parameter is set to "Right". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| Front | Reference plane whose "Is Reference" parameter is set to "Front". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| CenterFrontBack | Reference plane whose "Is Reference" parameter is set to "Center (Front/Back)". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| Back | Reference plane whose "Is Reference" parameter is set to "Back". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| Bottom | Reference plane whose "Is Reference" parameter is set to "Bottom". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| CenterElevation | Reference plane whose "Is Reference" parameter is set to "Center (Elevation)". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| Top | Reference plane whose "Is Reference" parameter is set to "Top". There may be no more than one such reference plane in the family. This reference is stable: if there is a dimension to this reference of an instance, and the instance's type or family is replaced, the dimension will survive. |
| StrongReference | Reference plane whose "Is Reference" parameter is set to "Strong Reference", or reference line whose "Reference" parameter is set to "Strong Reference". There may be multiple such reference planes and lines in the family. These references are not stable: if there is a dimension to such reference, and the instance's family is replaced, the dimension is not guaranteed to survive. |
| WeakReference | Reference plane whose "Is Reference" parameter is set to "Weak Reference", or reference line whose "Reference" parameter is set to "Weak Reference". There may be multiple such reference planes and lines in the family. These references are not stable: if there is a dimension to such reference, and the instance's family is replaced, the dimension is not guaranteed to survive. |
| NotAReference | This value is returned from FamilyInstance::getReferenceType if the reference does not correspond to any reference plane or reference line in the family. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)