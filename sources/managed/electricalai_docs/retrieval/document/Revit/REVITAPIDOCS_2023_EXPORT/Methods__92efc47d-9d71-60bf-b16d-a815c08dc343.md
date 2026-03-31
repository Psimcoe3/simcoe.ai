[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TessellatedBuildIssue Members

---



|  |
| --- |
| [TessellatedBuildIssue Class](123454f4-f295-c687-213b-da97c032aba6.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [TessellatedBuildIssue](123454f4-f295-c687-213b-da97c032aba6.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](af2ff164-3247-3a9f-6d84-a63d5dae899c.htm) | Releases all resources used by the  [TessellatedBuildIssue](123454f4-f295-c687-213b-da97c032aba6.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetIssueDescription](5588d9b9-bde0-98ba-1ed2-0003300db90d.htm) | Gets a string describing the issue. If the issue does not present a problem, then an empty string is returned. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsValidIssue](3d5943e5-deb3-2daf-e528-78d498e6b038.htm) | Reports whether the issue is well-formed, valid and does describe a real problem. |
| Public method | [MakesDataUnusable](60eedd37-6a15-9af4-cd05-d213748d06a0.htm) | Reports whether this issue makes some data unusable ('true') or is only shows that data format conventions were broken, but the data are still usable (false). |
| Public method | [ReportIssueToDataSource](e47fc5bf-bcf3-19a1-2045-b76cf01cd535.htm) | Reports whether this issue should be reported to the company which wrote the software which produced the face set data (true), or to Autodesk (false). |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](9b561318-6770-97fe-354f-2277745ae71e.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [NumberEncountered](a7f8c71f-786c-ce0a-29d5-71cc33cd060f.htm) | How many times this issue was encountered in its face set during the face set processing. This number can be less than the total number of such issues in the face set, as the face set processing could be aborted due to the presence of the issues which could not be handled. |

# See Also

[TessellatedBuildIssue Class](123454f4-f295-c687-213b-da97c032aba6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)