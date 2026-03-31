---
created: 2026-01-28T20:49:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Definition_File_html
author: 
---

# Help | Definition File | Autodesk

> ## Excerpt
> The DefinitionFile object represents a shared parameter file which is a common text file.

---
The DefinitionFile object represents a shared parameter file which is a common text file.

## Format

The shared parameter definition file is a text file (.txt) with three blocks: META, GROUP and PARAM. The GROUP and PARAM blocks are relevant to the shared parameter functionality in the Revit API. Do not edit the definition file directly; instead, edit it using the UI or the API.

Although the Revit API takes care of reading and writing this file, the following section provides information the format of the file, which closely corresponds to the API objects and methods used to access shared parameters. The file uses tabs to separate fields and can be difficult to read in a text editor. The code region below shows the contents of a sample shared parameter text file.

<table summary="" id="GUID-9C7F6E02-05C2-4F72-8108-60F2175FB9E3__TABLE_4C1829695A954DB2A85684E526336D06"><tbody><tr><td><b>Code Region 22-1: Parameter definition file example</b></td></tr><tr><td><pre><code><span># This is a Revit shared parameter file.</span><span>
</span><span># Do not edit manually.</span><span>
</span><span>*</span><span>META    VERSION    MINVERSION
META    </span><span>2</span><span>    </span><span>1</span><span>
</span><span>*</span><span>GROUP    ID    NAME
GROUP    </span><span>1</span><span>    </span><span>MyGroup</span><span>
GROUP    </span><span>2</span><span>    </span><span>AnotherGroup</span><span>
</span><span>*</span><span>PARAM    GUID    NAME    DATATYPE    DATACATEGORY    GROUP    VISIBLE    DESCRIPTION    USERMODIFIABLE
PARAM    bb7f0005</span><span>-</span><span>9692</span><span>-</span><span>4b76</span><span>-</span><span>8fa3</span><span>-</span><span>30cec8aecf74</span><span>    </span><span>Price</span><span>    INTEGER        </span><span>2</span><span>    </span><span>1</span><span>    </span><span>Enter</span><span> price </span><span>in</span><span> USD    </span><span>1</span><span>
PARAM    b7ea2654</span><span>-</span><span>b206</span><span>-</span><span>4694</span><span>-</span><span>a087</span><span>-</span><span>756359b52e7f</span><span>    areaTags    FAMILYTYPE    </span><span>-</span><span>2005020</span><span>    </span><span>1</span><span>    </span><span>1</span><span>        </span><span>1</span><span>
PARAM    d1a5439d</span><span>-</span><span>dc8d</span><span>-</span><span>4053</span><span>-</span><span>99fa</span><span>-</span><span>2f33804bae0e</span><span>    </span><span>MyParam</span><span>    TEXT        </span><span>1</span><span>    </span><span>1</span><span>        </span><span>1</span></code></pre></td></tr></tbody></table>

-   The GROUP block contains group entries that associate every parameter definition with a group. The following fields appear in the GROUP block:
    
    -   ID - Uniquely identifies the group and associates the parameter definition with a group.
    -   Name - The group name displayed in the UI.
-   The PARAM block contains parameter definitions. The following fields appear in the PARAM block:
    
    -   GUID - Identifies the parameter definition.
        
    -   NAME - Parameter definition name.
        
    -   DATATYPE - Parameter type. This field can be a common type (TEXT, INTEGER, etc.), structural type (FORCE, MOMENT, etc.) or common family type (Area Tags, etc). Common type and structural type parameters are specified in the text file directly (e.g.: TEXT, FORCE). If the value of the DATATYPE field is FAMILYTYPE, an extra number is added. For example, FAMILYTYPE followed by -2005020 represents Family type: Area Tags.
        
    -   DATACATEGORY - An optional field for parameters whose DATATYPE is FAMILYTYPE.
        
    -   GROUP - A group ID used to identify the group that includes the current parameter definition.
        
    -   VISIBLE - Identifies whether the parameter is visible. The value of this field is 0 or 1.0 = invisible
        
        1 = visible
        
    -   DESCRIPTION - An optional field for a tooltip for this parameter.
        
    -   USERMODIFIABLE - Identifies whether the parameter is editable by the user.0 = user cannot edit the parameter and it is greyed out in the UI
        
        1 = user can edit the parameter value in the UI
        

In the sample definition file, there are two groups:

-   MyGroup - ID 1 - Contains the parameter definition for MyParam which is a Text type parameter, and the definition for areaTags which is a FamilyType parameter.
-   AnotherGroup - ID 2 - Contains the parameter definition for Price which is an Integer type parameter.

Of the 3 parameters in the sample file, only Price has a description. All of the parameters are visible and user modifiable.
