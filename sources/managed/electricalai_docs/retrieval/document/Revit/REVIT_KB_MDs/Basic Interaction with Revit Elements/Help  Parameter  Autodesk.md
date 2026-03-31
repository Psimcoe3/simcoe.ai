---
created: 2026-01-28T20:49:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html
author: 
---

# Help | Parameter | Autodesk

> ## Excerpt
> The Parameter class contains the value for the given parameter.

---
The Parameter class contains the value for the given parameter.

All Elements within Autodesk Revit contain Parameters, which can be retrieved as a set or individually. An individual parameter object can be obtained from any Element using either a BuiltInParameter enumeration, a Definition object or a Shared Parameter GUID.

The data contained within the parameter can be either a Double, Integer, String or ElementId, as indicated by its StorageType property. For value types, the DisplayUnitType property will indicate the display unit used for the parameter value. The Parameter object also contains a [Definition](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Definition_html "The Definition object describes the data type, name, and other Parameter details.") object that describes the data type, name and other details of the parameter.

## StorageType

StorageType describes the type of parameter values stored internally.

Based on the property value, use the corresponding get and set methods to retrieve and set the parameter data value.

The StorageType is an enumerated type that lists all internal parameter data storage types supported by Revit:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_CC5D594BCB2B441FA238B6B3BB9061B8"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>_String_</td><td>Internal data is stored as a string of characters.</td></tr><tr><td>_ElementId_</td><td>Data type represents an element and is stored as an Element ID.</td></tr><tr><td>_Double_</td><td>Data is stored internally as an 8-byte floating point number.</td></tr><tr><td>_Integer_</td><td>Internal data is stored as a signed 32-bit integer.</td></tr><tr><td>_None_</td><td>None represents an invalid storage type. For internal use only.</td></tr></tbody></table>

In most cases, the ElementId value is a positive number. However, it can be a negative number. When the ElementId value is negative, it does not represent an Element but has another meaning. For example, the storage type parameter for a beam's Vertical Projection is ElementId. When the parameter value is Level 1 or Level 2, the ElementId value is positive and corresponds to the ElementId of that level. However, when the parameter value is set to Auto-detect, Center of Beam or Top of Beam, the ElementId value is negative.

The following code sample shows how to check whether a parameter's value can be set to a double value, based on its StorageType:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_E19B02276D564884B2EB427762713A30"><tbody><tr><td><b>Code Region: Checking a parameter's StorageType</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>SetParameter</span><span>(</span><span>Parameter</span><span> parameter</span><span>,</span><span> </span><span>double</span><span> value</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> result </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>//if the parameter is readonly, you can't change the value of it</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> parameter </span><span>&amp;&amp;</span><span> </span><span>!</span><span>parameter</span><span>.</span><span>IsReadOnly</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StorageType</span><span> storageType </span><span>=</span><span> parameter</span><span>.</span><span>StorageType</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>StorageType</span><span>.</span><span>Double</span><span> </span><span>!=</span><span> storageType</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"The storagetypes of value and parameter are different!"</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>//If successful, the result is true</span><span>
        result </span><span>=</span><span> parameter</span><span>.</span><span>Set</span><span>(</span><span>value</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> result</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The Set() method return value indicates that the Parameter value was changed. The Set() method returns true if the Parameter value was changed, otherwise it returns false.

Not all Parameters are writable. An Exception is thrown if the Parameter is read-only.

## AsValueString() and SetValueString()

These two Parameter class methods only apply to value type parameters, which are double or integer parameters representing a measured quantity.

Use the AsValueString() method to get the parameter value as a string with the unit of measure. For example, the Base Offset value, a wall parameter, is a Double value. Usually the value is shown as a string like -20'0" in the Element Properties. Using the AsValueString() method, you get the -20'0" string value directly. Using the AsDouble() method, you get a double value like -20 without the units of measure.

Use the SetValueString() method to change the value of a value type parameter instead of using the Set() method. The following code sample illustrates how to change the parameter value using the SetValueString() method:

<table summary="" id="GUID-FEA13CF3-85D2-4D19-978B-0A5BCD0D710A__TABLE_0AC674B655AF45A885ABE785167F4713"><tbody><tr><td><b>Code Region: Using Parameter.SetValueString()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>SetWithValueString</span><span>(</span><span>Parameter</span><span> foundParameter</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> result </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>foundParameter</span><span>.</span><span>IsReadOnly</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>//If successful, the result is true</span><span>
        result </span><span>=</span><span> foundParameter</span><span>.</span><span>SetValueString</span><span>(</span><span>"-22\'3\""</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> result</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Global parameter associations

The Parameter class has several methods for maintaining associations between element parameters and global parameters. The method GetAssociatedGlobalParameter() returns the ElementId of a global parameter, if any, currently associated with a parameter. InvalidElementId is returned in case this parameter is not associated with any global parameter. InvalidElementId is also returned if called for a parameter that cannot even be associated with a global parameters (i.e. a non-parameterizable parameter or a parameter with a formula).

There are two methods to determine if a parameter can be associated with global parameters. Parameter.CanBeAssociatedWithGlobalParameters() tests wether a parameter can be associated with any global parameter. Only properties defined as parametrizable can be associated with global parameters. That excludes any read-only and formula-driven parameters, as well as those that have other explicit or implicit restrictions imposed by Revit. To test whether a specific global parameter can be associated with this parameter, use Parameter.CanBeAssociatedWithGlobalParameter(). Keep in mind that the parameter's value type must match the type of the global parameter to create an association.

For parameters that can be associated with a global parameter, use AssociateWithGlobalParameter() to create the association. Once associated, the parameter can be later dissociated by calling the DissociateFromGlobalParameter() method

## ParameterUtils

ParameterUtils is a class with static utility functions related to ForgeTypeId parameter identifiers:

-   ParameterUtils.GetAllBuiltInGroups()
-   ParameterUtils.GetAllBuiltInParameters()
-   ParameterUtils.IsBuiltInGroup(ForgeTypeId)
-   ParameterUtils.IsBuiltInParameter(ForgeTypeId)

The ParameterUtils class contains several methods new in Revit 2022 but also deprecated. They are offered only to assist in migrating code from the BuiltInParameter and BuiltInParameterGroup enumerations to the ForgeTypeId class.

-   ParameterUtils.GetBuiltInParameter(ForgeTypeId)
-   ParameterUtils.GetBuiltInParameterGroup(ForgeTypeId)
-   ParameterUtils.GetParameterGroupTypeId(BuiltInParameterGroup)
-   ParameterUtils.GetParameterTypeId(BuiltInParameter)

## Multiple Values

The `MultipleValuesIndicationSettings` class allows access to the custom value used in instances of the Properties dialog, Tags, and Schedules when multiple elements are referenced and the value of the parameter is differs among those elements
