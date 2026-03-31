---
created: 2026-01-28T22:17:19 (UTC -05:00)
tags: []
source: https://api.gtpstratus.com/index.html
author: Authorize
---

# Stratus API

> ## Excerpt
> Activity NameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:14.821Z",
      "createdById": "string",
      "createdByName": "string",
      "divisionId": "string",
      "divisionName": "string",
      "route": "string",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "projectColor": "string",
      "modelId": "string",
      "modelName": "string",
      "reference": "0 = Unspecified",
      "referenceId": "string",
      "referenceName": "string",
      "action": "0 = Unspecified",
      "actionName": "string",
      "name": "string",
      "value": "string",
      "trackingStatusId": "string",
      "trackingStatusName": "string",
      "trackingStatusColor": "string",
      "stationId": "string",
      "stationName": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Package NameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 200)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "assemblyIds": [
        "string"
      ],
      "bimAreaId": "string",
      "bimAreaName": "string",
      "cadIdsBySequence": [
        "string"
      ],
      "categoryId": "string",
      "createdBy": "string",
      "createdDT": "2026-01-29T03:17:14.855Z",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "description": "string",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "hoursEstimatedField": 0,
      "hoursEstimatedOffice": 0,
      "hoursEstimatedPurchasing": 0,
      "hoursEstimatedShop": 0,
      "id": "string",
      "installedDT": "2026-01-29T03:17:14.855Z",
      "modelId": "string",
      "modifiedBy": "string",
      "modifiedDT": "2026-01-29T03:17:14.855Z",
      "name": "string",
      "number": "string",
      "officeDuration": 0,
      "officeStartDT": "2026-01-29T03:17:14.855Z",
      "partCadIds": [
        "string"
      ],
      "projectId": "string",
      "purchasingDuration": 0,
      "purchasingStartDT": "2026-01-29T03:17:14.855Z",
      "qrCodeUrl": "string",
      "requiredDT": "2026-01-29T03:17:14.855Z",
      "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "shopDuration": 0,
      "startDT": "2026-01-29T03:17:14.855Z",
      "status": "0 = Active",
      "statusName": "string",
      "viewId": "string",
      "isViewIdOverridden": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:14.869Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:14.869Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:14.869Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:14.869Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:14.869Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:14.869Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:14.869Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "id": "string",
    "projectId": "string",
    "modelId": "string",
    "stratusDimensionType": "0 = AliasTag",
    "orderId": "string",
    "assemblyId": "string",
    "partCadIds": [
      "string"
    ],
    "colorIndex": 0,
    "dimensionLineType": "0 = LabelOnly",
    "connectedAssemblyId": "string",
    "distance": 0,
    "label": "string",
    "lineVertices": [
      {
        "x": 0,
        "y": 0,
        "z": 0
      }
    ],
    "location": {
      "x": 0,
      "y": 0,
      "z": 0
    },
    "gridlineAnnotation": "string",
    "dimensionAnchorTypes": [
      {
        "location": {
          "x": 0,
          "y": 0,
          "z": 0
        },
        "partPointType": "0 = Unspecified"
      }
    ]
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdById": "string",
      "createdDT": "2026-01-29T03:17:14.906Z",
      "projectId": "string",
      "modelId": "string",
      "referenceType": "0 = Unspecified",
      "referenceName": "string",
      "referenceId": "string",
      "role": "0 = Unspecified",
      "roleName": "string",
      "fileType": "0 = Unspecified",
      "fileTypeName": "string",
      "localFilePath": "string",
      "fileName": "string",
      "overriddenRemoteFolder": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "divisionId": "string",
  "projectId": "string",
  "modelId": "string",
  "packageId": "string",
  "requiredDT": "2026-01-29T03:17:14.919Z",
  "isLocked": true,
  "generatedDT": "2026-01-29T03:17:14.919Z",
  "generatedByName": "string",
  "lockedDT": "2026-01-29T03:17:14.919Z",
  "lockedByName": "string",
  "unlockedDT": "2026-01-29T03:17:14.919Z",
  "unlockedByName": "string",
  "lineItems": [
    {
      "groupedPartCadIds": [
        "string"
      ],
      "sequence": 0,
      "isModeled": true,
      "isReportable": true,
      "isConsolidated": true,
      "manufacturer": "string",
      "quantity": 0,
      "size": "string",
      "description": "string",
      "material": "string",
      "productCode": "string",
      "diameter": "string",
      "width": "string",
      "length": "string",
      "isLengthNestable": true,
      "nominalStockLength": "string",
      "additionalProperty": "string",
      "unitOfMeasure": "0 = Bundle",
      "unitOfMeasureName": "string",
      "comment": "string",
      "notPurchased": true,
      "isAncillary": true,
      "serviceName": "string",
      "serviceCode": "string",
      "possibleSupplierCodes": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ]
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idreportid *string(path)STRATUS Company Report IdCodeDescriptionLinks200OKMedia typeControls Accept header."string"No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links429Too Many RequestsNo links500Internal Server ErrorNo linksNameDescriptionpackageIdstring(query)Package Id. Empty=all (def).Default value :projectIdstring(query)Project Id. Empty=all (def).modelIdstring(query)Model Id. Empty=all (def).reportIdstring(query)Id of report to run. Empty=dashboard.businessUnitsstring(query)Project Business Units. Empty=all (def). Semicolon separated list of values as filter.divisionsstring(query)Division Names or Ids. Empty=all (def). Semicolon separated list of values as filter.packageCategoriesstring(query)Package Category Names or Ids. Empty=all (def). Semicolon separated list of values as filter.activeboolean(query)Active packages. true is def.Default value : truearchivedboolean(query)Archived packages. false is def.Default value : falseCodeDescriptionLinks200OKMedia typeControls Accept header.stringNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links429Too Many RequestsNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:14.980Z",
      "modifiedDT": "2026-01-29T03:17:14.980Z",
      "projectId": "string",
      "modelId": "string",
      "cadId": "string",
      "sheetId": "string",
      "viewId": "string",
      "isViewIdOverridden": true,
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "assemblyType": "0 = Unspecified",
      "assemblyTypeLabel": "string",
      "excludedCadIds": [
        "string"
      ],
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "name": "string",
      "nameLabel": "string",
      "partIds": [
        "string"
      ],
      "instanceIndex": "string",
      "lastUsedAssembliesPartsTableReportIds": [
        "string"
      ],
      "qrCodeUrl": "string",
      "notes": [
        {
          "isPartialData": true,
          "isReadOnly": true,
          "id": "string",
          "createdDT": "2026-01-29T03:17:14.980Z",
          "createdById": "string",
          "modifiedDT": "2026-01-29T03:17:14.980Z",
          "modifiedById": "string",
          "name": "string"
        }
      ],
      "defaultOrientationForReportTemplatesForgeViewerViewJson": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdincludeAssemblyPartsboolean(query)OPTIONALDefault value : falseincludeStratusPropertiesboolean(query)Pass true to this optional query parameter if you want to generate STRATUS.Part.* properties and have them returned for the parts.Default value : falseexcludeNullAndEmptyboolean(query)Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.Default value : falseinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 100)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.007Z",
      "modifiedDT": "2026-01-29T03:17:15.007Z",
      "cutDT": "2026-01-29T03:17:15.007Z",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "modelId": "string",
      "modelName": "string",
      "bimAreaId": "string",
      "bimArea": "string",
      "cadId": "string",
      "cadType": "string",
      "webId": "string",
      "description": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "properties": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "propertiesGtp": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "points": [
        {
          "pointType": "0 = Unspecified",
          "cadId": "string",
          "location": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "direction": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "upVector": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "width": 0,
          "height": 0,
          "matingElementUniqueId": "string"
        }
      ],
      "cutLengthAdjustment": 0,
      "cutLength2Adjustment": 0,
      "lockLength": true,
      "lockLocation": true,
      "qrCodeUrl": "string",
      "partUrl": "string",
      "patternNumber": "string",
      "source": "0 = PublishedModel",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionqrcode *string(path)The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.include(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.024Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.024Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.024Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.024Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.024Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.024Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.024Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdtrackingLogEntryIdstring(query)Optional TrackingLogEntry Id to associate Attachment with a TrackingLogEntryCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdById": "string",
  "createdDT": "2026-01-29T03:17:15.040Z",
  "projectId": "string",
  "modelId": "string",
  "referenceType": "0 = Unspecified",
  "referenceName": "string",
  "referenceId": "string",
  "role": "0 = Unspecified",
  "roleName": "string",
  "fileType": "0 = Unspecified",
  "fileTypeName": "string",
  "localFilePath": "string",
  "fileName": "string",
  "overriddenRemoteFolder": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdREQUIRED: CutListDataApi - minimum json includes material, size, and cutListItems list with at least one entry containing lengthInInches{
  "id": "string",
  "completedDT": "2026-01-29T03:17:15.055Z",
  "createdDT": "2026-01-29T03:17:15.055Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.055Z",
  "modifiedById": "string",
  "cutListItems": [
    {
      "area": "string",
      "assemblyId": "string",
      "assemblyName": "string",
      "index": 0,
      "cadId": "string",
      "cutDateTime": "2026-01-29T03:17:15.055Z",
      "description": "string",
      "itemNumber": "string",
      "lengthInInches": 0,
      "lengthInFeetAndInches": "string",
      "level": "string",
      "preFabId": "string",
      "qrCode": "string",
      "userData1": "string",
      "userData2": "string",
      "userData3": "string",
      "userData4": "string",
      "userData5": "string",
      "userData6": "string",
      "userData7": "string",
      "userData8": "string",
      "userData9": "string",
      "userData10": "string",
      "userData11": "string",
      "userData12": "string",
      "userData13": "string",
      "userData14": "string",
      "userData15": "string"
    }
  ],
  "cutListItemCount": 0,
  "cutListStatus": "0 = New",
  "cutListStatusLabel": "string",
  "cutListStatusName": "string",
  "isAutoGeneratedCutList": true,
  "material": "string",
  "modelId": "string",
  "name": "string",
  "packageId": "string",
  "projectId": "string",
  "requestedDT": "2026-01-29T03:17:15.055Z",
  "requestedUserId": "string",
  "size": "string",
  "startedDT": "2026-01-29T03:17:15.055Z",
  "stationId": "string",
  "totalLengthInInches": 0,
  "totalLengthInFeetAndInches": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "completedDT": "2026-01-29T03:17:15.059Z",
  "createdDT": "2026-01-29T03:17:15.059Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.059Z",
  "modifiedById": "string",
  "cutListItems": [
    {
      "area": "string",
      "assemblyId": "string",
      "assemblyName": "string",
      "index": 0,
      "cadId": "string",
      "cutDateTime": "2026-01-29T03:17:15.059Z",
      "description": "string",
      "itemNumber": "string",
      "lengthInInches": 0,
      "lengthInFeetAndInches": "string",
      "level": "string",
      "preFabId": "string",
      "qrCode": "string",
      "userData1": "string",
      "userData2": "string",
      "userData3": "string",
      "userData4": "string",
      "userData5": "string",
      "userData6": "string",
      "userData7": "string",
      "userData8": "string",
      "userData9": "string",
      "userData10": "string",
      "userData11": "string",
      "userData12": "string",
      "userData13": "string",
      "userData14": "string",
      "userData15": "string"
    }
  ],
  "cutListItemCount": 0,
  "cutListStatus": "0 = New",
  "cutListStatusLabel": "string",
  "cutListStatusName": "string",
  "isAutoGeneratedCutList": true,
  "material": "string",
  "modelId": "string",
  "name": "string",
  "packageId": "string",
  "percentComplete": 0,
  "projectId": "string",
  "requestedDT": "2026-01-29T03:17:15.059Z",
  "requestedUserId": "string",
  "size": "string",
  "startedDT": "2026-01-29T03:17:15.059Z",
  "stationId": "string",
  "totalLengthInInches": 0,
  "totalLengthInFeetAndInches": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdREQUIRED: TrackingStatusId{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.074Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.076Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdArray of Assembly CadIds to add.CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.091Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.091Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.091Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.091Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.091Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.091Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.091Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdArray of Assembly CadIds used to replace existing.CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.108Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.108Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.108Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.108Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.108Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.108Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.108Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdArray of Part CadIds used to replace existing.CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.126Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.126Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.126Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.126Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.126Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.126Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.126Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdExample JSON KeyValuePair: {
  "key": "string",
  "value": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "key": "string",
  "value": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdExample JSON Array of KeyValuePair: [,,...][
  {
    "key": "string",
    "value": "string"
  }
]CodeDescriptionLinks200OKMedia typeControls Accept header.0No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Package IdArray of Part CadIds to add.CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.171Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.171Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.171Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.171Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.171Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.171Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.171Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksId is required.
Status: 0 = Active, 1 = Archived.{
  "categoryId": "string",
  "description": "string",
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.184Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.184Z",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.184Z",
  "requiredDT": "2026-01-29T03:17:15.184Z",
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.184Z",
  "status": 0
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.186Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.186Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.186Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.186Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.186Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.186Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.186Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Part NameDescriptionincludeStratusPropertiesboolean(query)Pass true to this optional query parameter if you want to generate STRATUS.Part.* properties and have them returned for the parts.  When in use, query must be limited to a single model id.Default value : falseexcludeNullAndEmptyboolean(query)Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.Default value : falseinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 100)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.210Z",
      "modifiedDT": "2026-01-29T03:17:15.210Z",
      "cutDT": "2026-01-29T03:17:15.210Z",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "modelId": "string",
      "modelName": "string",
      "bimAreaId": "string",
      "bimArea": "string",
      "cadId": "string",
      "cadType": "string",
      "webId": "string",
      "description": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "properties": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "propertiesGtp": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "points": [
        {
          "pointType": "0 = Unspecified",
          "cadId": "string",
          "location": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "direction": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "upVector": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "width": 0,
          "height": 0,
          "matingElementUniqueId": "string"
        }
      ],
      "cutLengthAdjustment": 0,
      "cutLength2Adjustment": 0,
      "lockLength": true,
      "lockLocation": true,
      "qrCodeUrl": "string",
      "partUrl": "string",
      "patternNumber": "string",
      "source": "0 = PublishedModel",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionqrcode *string(path)The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.includeStratusPropertiesboolean(query)Pass true to this optional query parameter if you want to generate STRATUS.Part.* properties and have them returned for the parts.  When in use, query must be limited to a single model id.Default value : falseexcludeNullAndEmptyboolean(query)Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.Default value : falseinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.228Z",
  "modifiedDT": "2026-01-29T03:17:15.228Z",
  "cutDT": "2026-01-29T03:17:15.228Z",
  "projectId": "string",
  "projectName": "string",
  "projectNumber": "string",
  "modelId": "string",
  "modelName": "string",
  "bimAreaId": "string",
  "bimArea": "string",
  "cadId": "string",
  "cadType": "string",
  "webId": "string",
  "description": "string",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "properties": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "propertiesGtp": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "points": [
    {
      "pointType": "0 = Unspecified",
      "cadId": "string",
      "location": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "direction": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "upVector": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "width": 0,
      "height": 0,
      "matingElementUniqueId": "string"
    }
  ],
  "cutLengthAdjustment": 0,
  "cutLength2Adjustment": 0,
  "lockLength": true,
  "lockLocation": true,
  "qrCodeUrl": "string",
  "partUrl": "string",
  "patternNumber": "string",
  "source": "0 = PublishedModel",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdincludeStratusPropertiesboolean(query)Pass true to this optional query parameter if you want to generate STRATUS.Part.* properties and have them returned for the parts.Default value : falseexcludeNullAndEmptyboolean(query)Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.Default value : falseinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.246Z",
  "modifiedDT": "2026-01-29T03:17:15.246Z",
  "cutDT": "2026-01-29T03:17:15.246Z",
  "projectId": "string",
  "projectName": "string",
  "projectNumber": "string",
  "modelId": "string",
  "modelName": "string",
  "bimAreaId": "string",
  "bimArea": "string",
  "cadId": "string",
  "cadType": "string",
  "webId": "string",
  "description": "string",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "properties": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "propertiesGtp": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "points": [
    {
      "pointType": "0 = Unspecified",
      "cadId": "string",
      "location": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "direction": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "upVector": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "width": 0,
      "height": 0,
      "matingElementUniqueId": "string"
    }
  ],
  "cutLengthAdjustment": 0,
  "cutLength2Adjustment": 0,
  "lockLength": true,
  "lockLocation": true,
  "qrCodeUrl": "string",
  "partUrl": "string",
  "patternNumber": "string",
  "source": "0 = PublishedModel",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptioncsvIdsstring(header)List of STRATUS Part IdsCodeDescriptionLinks200OKMedia typeControls Accept header.stringNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdtrackingLogEntryIdstring(query)Optional TrackingLogEntry Id to associate Attachment with a TrackingLogEntryCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdById": "string",
  "createdDT": "2026-01-29T03:17:15.273Z",
  "projectId": "string",
  "modelId": "string",
  "referenceType": "0 = Unspecified",
  "referenceName": "string",
  "referenceId": "string",
  "role": "0 = Unspecified",
  "roleName": "string",
  "fileType": "0 = Unspecified",
  "fileTypeName": "string",
  "localFilePath": "string",
  "fileName": "string",
  "overriddenRemoteFolder": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdisCutboolean(query)DEFAULT: true. If set to false, will not mark the part as cut.Default value : trueREQUIRED: TrackingStatusId{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.288Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.290Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdExample JSON KeyValuePair: {
  "key": "string",
  "value": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "key": "string",
  "value": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksExample List of PartPropertiesDataApi JSON: [},}][
  {
    "id": "string",
    "properties": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  }
]CodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdExample JSON KeyValuePair: {
  "key": "string",
  "value": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "key": "string",
  "value": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Part IdExample JSON Array of KeyValuePair: [,,...][
  {
    "key": "string",
    "value": "string"
  }
]CodeDescriptionLinks200OKMedia typeControls Accept header.0No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Ping NameDescriptionapp-idstring(header)(optional) Partner App IdCodeDescriptionLinks200OKNo links401UnauthorizedNo links Project NameDescriptionid *string(path)STRATUS Project IdCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.365Z",
  "modifiedDT": "2026-01-29T03:17:15.365Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.365Z",
  "actualStartDate": "2026-01-29T03:17:15.365Z",
  "targetEndDate": "2026-01-29T03:17:15.365Z",
  "actualEndDate": "2026-01-29T03:17:15.365Z",
  "color": "string",
  "isTaxExempt": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project IdasFlatListboolean(query)if true, results will be list of areas instead of hierarchy data structure using children, where ParentId can be used to understand hierarchyDefault value : falseCodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "abbreviation": "string",
    "children": [
      "string"
    ],
    "code": "string",
    "color": "string",
    "createdById": "string",
    "createdDT": "2026-01-29T03:17:15.379Z",
    "elevation": 0,
    "id": "string",
    "levelBottomOffset": 0,
    "levelTopOffset": 0,
    "modifiedById": "string",
    "modifiedDT": "2026-01-29T03:17:15.379Z",
    "name": "string",
    "parentId": "string"
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.397Z",
      "modifiedDT": "2026-01-29T03:17:15.397Z",
      "projectId": "string",
      "modelId": "string",
      "cadId": "string",
      "sheetId": "string",
      "viewId": "string",
      "isViewIdOverridden": true,
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "assemblyType": "0 = Unspecified",
      "assemblyTypeLabel": "string",
      "excludedCadIds": [
        "string"
      ],
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "name": "string",
      "nameLabel": "string",
      "partIds": [
        "string"
      ],
      "instanceIndex": "string",
      "lastUsedAssembliesPartsTableReportIds": [
        "string"
      ],
      "qrCodeUrl": "string",
      "notes": [
        {
          "isPartialData": true,
          "isReadOnly": true,
          "id": "string",
          "createdDT": "2026-01-29T03:17:15.397Z",
          "createdById": "string",
          "modifiedDT": "2026-01-29T03:17:15.397Z",
          "modifiedById": "string",
          "name": "string"
        }
      ],
      "defaultOrientationForReportTemplatesForgeViewerViewJson": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "length": "string",
      "width": "string",
      "height": "string",
      "location": "string",
      "containerTypeName": "string",
      "parentContainerId": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "qrCodeUrl": "string",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "partIds": [
        "string"
      ],
      "assemblyCadIds": [
        "string"
      ],
      "packageIds": [
        "string"
      ],
      "containerIds": [
        "string"
      ],
      "contents": [
        {
          "projectId": "string",
          "referenceId": "string",
          "referenceType": "0 = Unspecified"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "a360FolderId": "string",
      "createdDT": "2026-01-29T03:17:15.441Z",
      "databaseUnits": "0 = Imperial",
      "defaultViewId": "string",
      "id": "string",
      "isFieldOrderz": true,
      "lastPublishedDT": "2026-01-29T03:17:15.441Z",
      "modelName": "string",
      "modelType": "0 = Unspecified",
      "modifiedDT": "2026-01-29T03:17:15.441Z",
      "name": "string",
      "projectId": "string",
      "publishStatus": "0 = Published",
      "releaseVersion": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project Idpage(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "name": "string",
      "number": "string",
      "description": "string",
      "statusName": "string",
      "supplierName": "string",
      "supplierResponseNumber": "string",
      "tax": 0,
      "freight": 0,
      "totalAmount": 0,
      "projectId": "string",
      "lineItems": [
        {
          "additionalProperty": "string",
          "ancillaryType": "string",
          "ancillaryUsageType": "string",
          "backorderedQTY": 0,
          "comment": "string",
          "description": "string",
          "diameter": "string",
          "isAncillary": true,
          "isModeled": true,
          "length": "string",
          "lineNumber": 0,
          "manufacturer": "string",
          "material": "string",
          "nominalStockLength": "string",
          "orderedQTY": 0,
          "partTemplateName": "string",
          "productCode": "string",
          "quotedQTY": 0,
          "serviceCode": "string",
          "serviceName": "string",
          "shippedQTY": 0,
          "size": "string",
          "totalPrice": 0,
          "unitOfMeasure": "string",
          "unitPrice": "string",
          "width": "string"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Project Idpage(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "source": "1 = STRATUS",
      "name": "string",
      "code": "string",
      "abbreviation": "string",
      "group": "string",
      "fabConfigId": "string",
      "fabServiceId": "string",
      "fabServiceSpecId": "string",
      "fabServiceInsulationSpecId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionnonStratusProjectsOnlyboolean(query)If true, returns only projects which have not been synced to Stratus, otherwise all projects (which takes longer).CodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "id": "string",
    "createdDT": "2026-01-29T03:17:15.488Z",
    "modifiedDT": "2026-01-29T03:17:15.488Z",
    "status": "0 = New",
    "statusName": "string",
    "a360Id": "string",
    "a360RootFolderId": "string",
    "companyId": "string",
    "category": "string",
    "number": "string",
    "name": "string",
    "phase": "string",
    "description": "string",
    "imageAttachmentId": "string",
    "address1": "string",
    "address2": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "targetStartDate": "2026-01-29T03:17:15.488Z",
    "actualStartDate": "2026-01-29T03:17:15.488Z",
    "targetEndDate": "2026-01-29T03:17:15.488Z",
    "actualEndDate": "2026-01-29T03:17:15.488Z",
    "color": "string",
    "isTaxExempt": true
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.507Z",
      "modifiedDT": "2026-01-29T03:17:15.507Z",
      "status": "0 = New",
      "statusName": "string",
      "a360Id": "string",
      "a360RootFolderId": "string",
      "companyId": "string",
      "category": "string",
      "number": "string",
      "name": "string",
      "phase": "string",
      "description": "string",
      "imageAttachmentId": "string",
      "address1": "string",
      "address2": "string",
      "city": "string",
      "state": "string",
      "zip": "string",
      "targetStartDate": "2026-01-29T03:17:15.507Z",
      "actualStartDate": "2026-01-29T03:17:15.507Z",
      "targetEndDate": "2026-01-29T03:17:15.507Z",
      "actualEndDate": "2026-01-29T03:17:15.507Z",
      "color": "string",
      "isTaxExempt": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionqrcode *string(path)The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.include(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.522Z",
  "modifiedDT": "2026-01-29T03:17:15.522Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.522Z",
  "actualStartDate": "2026-01-29T03:17:15.522Z",
  "targetEndDate": "2026-01-29T03:17:15.522Z",
  "actualEndDate": "2026-01-29T03:17:15.522Z",
  "color": "string",
  "isTaxExempt": true
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionuserid *string(path)User Id specified for Project Role filtering.include(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.543Z",
      "modifiedDT": "2026-01-29T03:17:15.543Z",
      "status": "0 = New",
      "statusName": "string",
      "a360Id": "string",
      "a360RootFolderId": "string",
      "companyId": "string",
      "category": "string",
      "number": "string",
      "name": "string",
      "phase": "string",
      "description": "string",
      "imageAttachmentId": "string",
      "address1": "string",
      "address2": "string",
      "city": "string",
      "state": "string",
      "zip": "string",
      "targetStartDate": "2026-01-29T03:17:15.543Z",
      "actualStartDate": "2026-01-29T03:17:15.543Z",
      "targetEndDate": "2026-01-29T03:17:15.543Z",
      "actualEndDate": "2026-01-29T03:17:15.543Z",
      "color": "string",
      "isTaxExempt": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionaddDefaultUserProjectRolesboolean(query)if true, default user project roles will be added to the new projectsetActiveboolean(query)if true, project will be set to Active status, otherwise set to NewPass Project object in request body.
Project object returned by call to available-autodesk-projects can be passed into this method.
Project object must contain valid A360Id and Name.
Resulting ProjectDataApi will be returned with new Stratus Project Id if successful, otherwise null.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.560Z",
  "modifiedDT": "2026-01-29T03:17:15.560Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.560Z",
  "actualStartDate": "2026-01-29T03:17:15.560Z",
  "targetEndDate": "2026-01-29T03:17:15.560Z",
  "actualEndDate": "2026-01-29T03:17:15.560Z",
  "color": "string",
  "isTaxExempt": true
}CodeDescriptionLinks200OKNo links QRCode NameDescriptionurlSubstringstring(query)Optional: Returns all ShortURL records that have the given sub-string inside the URL field.where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "url": "string",
      "projectId": "string",
      "modelId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Tables NameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)CodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "companyTableId": "string",
    "createdById": "string",
    "createdByName": "string",
    "createdDT": "2026-01-29T03:17:15.598Z",
    "csvData": "string",
    "headers": [
      "string"
    ],
    "id": "string",
    "isCloneToProjectTableEnabled": true,
    "modifiedById": "string",
    "modifiedByName": "string",
    "modifiedDT": "2026-01-29T03:17:15.598Z",
    "name": "string",
    "notes": "string",
    "projectId": "string",
    "referencesCount": 0
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.609Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.609Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDCodeDescriptionLinks200OKMedia typeControls Accept header.No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)CodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "companyTableId": "string",
    "createdById": "string",
    "createdByName": "string",
    "createdDT": "2026-01-29T03:17:15.634Z",
    "csvData": "string",
    "headers": [
      "string"
    ],
    "id": "string",
    "isCloneToProjectTableEnabled": true,
    "modifiedById": "string",
    "modifiedByName": "string",
    "modifiedDT": "2026-01-29T03:17:15.634Z",
    "name": "string",
    "notes": "string",
    "projectId": "string",
    "referencesCount": 0
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDid *string(path)Table IDinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.648Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.648Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDid *string(path)Table IDCodeDescriptionLinks200OKMedia typeControls Accept header.No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksTable data{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.673Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.673Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.675Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.675Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDColumn operation details{
  "columnMappings": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "columnName": "string",
  "defaultValue": "string",
  "index": 0,
  "operation": "1 = Add"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.691Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.691Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDindexinteger($int32)(query)Index where to insert the columncolumnNamestring(query)Name of the new columndefaultValuestring(query)Default value for the new columnDefault value :CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.706Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.706Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDTable data{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.720Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.720Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.721Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.721Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksUpdated table data{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.735Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.735Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.737Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.737Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDindex *integer($int32)(path)Index of the column to renamenewColumnNamestring(query)New name for the columnCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.750Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.750Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDColumn mappings (new index -> old index){
  "additionalProp1": 0,
  "additionalProp2": 0,
  "additionalProp3": 0
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.766Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.766Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDUpdated table data{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.780Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.780Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.782Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.782Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)Table IDindex *integer($int32)(path)Index of the column to removeCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.807Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.807Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDCodeDescriptionLinks200OKMedia typeControls Accept header.0No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionprojectId *string(path)Project IDid *string(path)Table IDCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Task NameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.847Z",
      "createdById": "string",
      "modifiedDT": "2026-01-29T03:17:15.847Z",
      "modifiedById": "string",
      "projectId": "string",
      "modelId": "string",
      "packageId": "string",
      "taskWorkflowId": "string",
      "taskDefinitionId": "string",
      "description": "string",
      "referenceType": "0 = Unspecified",
      "referenceTypeName": "string",
      "referenceId": "string",
      "referenceCadId": "string",
      "taskStatus": "string",
      "assignedUserId": "string",
      "assignedStationId": "string",
      "logEntries": [
        {
          "createdById": "string",
          "createdDT": "2026-01-29T03:17:15.847Z",
          "taskStatus": "string",
          "stationId": "string"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Task IdCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.860Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.860Z",
  "modifiedById": "string",
  "projectId": "string",
  "modelId": "string",
  "packageId": "string",
  "taskWorkflowId": "string",
  "taskDefinitionId": "string",
  "description": "string",
  "referenceType": "0 = Unspecified",
  "referenceTypeName": "string",
  "referenceId": "string",
  "referenceCadId": "string",
  "taskStatus": "string",
  "assignedUserId": "string",
  "assignedStationId": "string",
  "logEntries": [
    {
      "createdById": "string",
      "createdDT": "2026-01-29T03:17:15.860Z",
      "taskStatus": "string",
      "stationId": "string"
    }
  ]
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS Task IdstationIdstring(query)Optional Station Id to associate with Status updatetaskStatusIdstring(query)Required Task Status Id to assign to TaskCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptiontoolIdstring(query)STRATUS Tool IdmodelIdstring(query)STRATUS Model IdpartCadIdstring(query)STRATUS Part CadIdtaskDefinitionIdstring(query)STRATUS Task Definition IdCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptiontoolIdstring(query)STRATUS Tool IdmodelIdstring(query)STRATUS Model IdpartCadIdstring(query)STRATUS Part CadIdtaskDefinitionIdstring(query)STRATUS Task Definition IdCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links TimeSession NameDescriptionwhere(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "isPartialData": true,
      "isReadOnly": true,
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.921Z",
      "createdById": "string",
      "modifiedDT": "2026-01-29T03:17:15.921Z",
      "modifiedById": "string",
      "activityType": "0 = None",
      "activityTypeName": "string",
      "divisionId": "string",
      "divisionName": "string",
      "email": "string",
      "employeeId": "string",
      "firstName": "string",
      "isLocked": true,
      "lastName": "string",
      "modelId": "string",
      "modelName": "string",
      "packageCategoryId": "string",
      "packageCategoryName": "string",
      "packageDivisionId": "string",
      "packageDivisionName": "string",
      "packageId": "string",
      "packageName": "string",
      "packageNumber": "string",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "shiftTypeId": "string",
      "startDT": "2026-01-29T03:17:15.921Z",
      "stationDivisionId": "string",
      "stationDivisionName": "string",
      "stationId": "string",
      "stationName": "string",
      "stopDT": "2026-01-29T03:17:15.921Z",
      "taskDefinitionId": "string",
      "userTypeName": "string",
      "workerId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links{
  "isLocked": true,
  "timeSessionIds": [
    "string"
  ]
}CodeDescriptionLinks200OKNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links TrackingLog NameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:16.051Z",
      "currentDivisionId": "string",
      "modifiedDT": "2026-01-29T03:17:16.051Z",
      "modelId": "string",
      "referenceType": "0 = Unspecified",
      "referenceName": "string",
      "referenceId": "string",
      "currentTrackingStatusId": "string",
      "totalHours": 0,
      "trackingLogEntries": [
        {
          "trackingStatusId": "string",
          "createdById": "string",
          "createdDT": "2026-01-29T03:17:16.051Z",
          "divisionId": "string",
          "id": "string",
          "origin": "0 = Unknown",
          "comment": "string",
          "hours": 0,
          "costTypeId": "string",
          "hoursCost": 0
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "additionalProp1": "string",
  "additionalProp2": "string",
  "additionalProp3": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "additionalProp1": "string",
  "additionalProp2": "string",
  "additionalProp3": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links User NameDescriptionid *string(path)STRATUS User Idinclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS User IdCodeDescriptionLinks200OKMedia typeControls Accept header.{
  "userId": "string",
  "firstName": "string",
  "lastName": "string",
  "shortUrl": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS User IdCodeDescriptionLinks200OKMedia typeControls Accept header.[
  {
    "projectId": "string",
    "projectRoleTypeId": "string"
  }
]No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptioninclude(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]where(query)Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)page(query)Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)pagesize(query)Optional: defines the number of elements per page (default (and max) is 1000)disabletotal(query)Optional: disable total calculation to improve performance (default is false)CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "data": [
    {
      "cellPhone": "string",
      "companyId": "string",
      "companyName": "string",
      "dateFormat": "string",
      "email": "string",
      "firstName": "string",
      "hourFormat": "string",
      "id": "string",
      "isCheckedIn": true,
      "isTimeTrackingEnabled": true,
      "lastName": "string",
      "lastViewedDateTimeForAssemblyId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "lastViewedDateTimeForModelId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "lastViewedDateTimeForPackageId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "longDateFormat": "string",
      "profileImageUrl": "string",
      "profileImageBase64": "string",
      "status": "1 = Active",
      "timeFormat": "string",
      "timeZoneInfoId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionemail *string(path)include(query)A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties["Family"], propertiesGtp["Material"]CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS User Id{
  "projectId": "string",
  "projectRoleTypeId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "projectId": "string",
  "projectRoleTypeId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS User Id{
  "projectId": "string",
  "projectRoleTypeId": "string"
}CodeDescriptionLinks200OKMedia typeControls Accept header.{
  "projectId": "string",
  "projectRoleTypeId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path){
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}CodeDescriptionLinks202AcceptedMedia typeControls Accept header.{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo linksNameDescriptionid *string(path)STRATUS User IdprojectId *string(path)STRATUS Project IdCodeDescriptionLinks200OKMedia typeControls Accept header.trueNo links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links Version CodeDescriptionLinks200OKMedia typeControls Accept header."string"No links400Bad RequestNo links401UnauthorizedNo links404Not FoundNo links500Internal Server ErrorNo links API Health CodeDescriptionLinks200Health descriptionMedia typeControls Accept header.{
  "status": "string",
  "totalDuration": "string",
  "entries": 
}No links

---
### Activity

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:14.821Z",
      "createdById": "string",
      "createdByName": "string",
      "divisionId": "string",
      "divisionName": "string",
      "route": "string",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "projectColor": "string",
      "modelId": "string",
      "modelName": "string",
      "reference": "0 = Unspecified",
      "referenceId": "string",
      "referenceName": "string",
      "action": "0 = Unspecified",
      "actionName": "string",
      "name": "string",
      "value": "string",
      "trackingStatusId": "string",
      "trackingStatusName": "string",
      "trackingStatusColor": "string",
      "stationId": "string",
      "stationName": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Package

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 200)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "assemblyIds": [
        "string"
      ],
      "bimAreaId": "string",
      "bimAreaName": "string",
      "cadIdsBySequence": [
        "string"
      ],
      "categoryId": "string",
      "createdBy": "string",
      "createdDT": "2026-01-29T03:17:14.855Z",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "description": "string",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "hoursEstimatedField": 0,
      "hoursEstimatedOffice": 0,
      "hoursEstimatedPurchasing": 0,
      "hoursEstimatedShop": 0,
      "id": "string",
      "installedDT": "2026-01-29T03:17:14.855Z",
      "modelId": "string",
      "modifiedBy": "string",
      "modifiedDT": "2026-01-29T03:17:14.855Z",
      "name": "string",
      "number": "string",
      "officeDuration": 0,
      "officeStartDT": "2026-01-29T03:17:14.855Z",
      "partCadIds": [
        "string"
      ],
      "projectId": "string",
      "purchasingDuration": 0,
      "purchasingStartDT": "2026-01-29T03:17:14.855Z",
      "qrCodeUrl": "string",
      "requiredDT": "2026-01-29T03:17:14.855Z",
      "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "shopDuration": 0,
      "startDT": "2026-01-29T03:17:14.855Z",
      "status": "0 = Active",
      "statusName": "string",
      "viewId": "string",
      "isViewIdOverridden": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:14.869Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:14.869Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:14.869Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:14.869Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:14.869Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:14.869Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:14.869Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "id": "string",
    "projectId": "string",
    "modelId": "string",
    "stratusDimensionType": "0 = AliasTag",
    "orderId": "string",
    "assemblyId": "string",
    "partCadIds": [
      "string"
    ],
    "colorIndex": 0,
    "dimensionLineType": "0 = LabelOnly",
    "connectedAssemblyId": "string",
    "distance": 0,
    "label": "string",
    "lineVertices": [
      {
        "x": 0,
        "y": 0,
        "z": 0
      }
    ],
    "location": {
      "x": 0,
      "y": 0,
      "z": 0
    },
    "gridlineAnnotation": "string",
    "dimensionAnchorTypes": [
      {
        "location": {
          "x": 0,
          "y": 0,
          "z": 0
        },
        "partPointType": "0 = Unspecified"
      }
    ]
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdById": "string",
      "createdDT": "2026-01-29T03:17:14.906Z",
      "projectId": "string",
      "modelId": "string",
      "referenceType": "0 = Unspecified",
      "referenceName": "string",
      "referenceId": "string",
      "role": "0 = Unspecified",
      "roleName": "string",
      "fileType": "0 = Unspecified",
      "fileTypeName": "string",
      "localFilePath": "string",
      "fileName": "string",
      "overriddenRemoteFolder": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "divisionId": "string",
  "projectId": "string",
  "modelId": "string",
  "packageId": "string",
  "requiredDT": "2026-01-29T03:17:14.919Z",
  "isLocked": true,
  "generatedDT": "2026-01-29T03:17:14.919Z",
  "generatedByName": "string",
  "lockedDT": "2026-01-29T03:17:14.919Z",
  "lockedByName": "string",
  "unlockedDT": "2026-01-29T03:17:14.919Z",
  "unlockedByName": "string",
  "lineItems": [
    {
      "groupedPartCadIds": [
        "string"
      ],
      "sequence": 0,
      "isModeled": true,
      "isReportable": true,
      "isConsolidated": true,
      "manufacturer": "string",
      "quantity": 0,
      "size": "string",
      "description": "string",
      "material": "string",
      "productCode": "string",
      "diameter": "string",
      "width": "string",
      "length": "string",
      "isLengthNestable": true,
      "nominalStockLength": "string",
      "additionalProperty": "string",
      "unitOfMeasure": "0 = Bundle",
      "unitOfMeasureName": "string",
      "comment": "string",
      "notPurchased": true,
      "isAncillary": true,
      "serviceName": "string",
      "serviceCode": "string",
      "possibleSupplierCodes": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ]
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

reportid \*

string

(path)

 | 

STRATUS Company Report Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
"string"
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 429 | 

Too Many Requests



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
packageId

string

(query)

 | 

Package Id. Empty=all (def).

_Default value_ :

 |
| 

projectId

string

(query)

 | 

Project Id. Empty=all (def).

 |
| 

modelId

string

(query)

 | 

Model Id. Empty=all (def).

 |
| 

reportId

string

(query)

 | 

Id of report to run. Empty=dashboard.

 |
| 

businessUnits

string

(query)

 | 

Project Business Units. Empty=all (def). Semicolon separated list of values as filter.

 |
| 

divisions

string

(query)

 | 

Division Names or Ids. Empty=all (def). Semicolon separated list of values as filter.

 |
| 

packageCategories

string

(query)

 | 

Package Category Names or Ids. Empty=all (def). Semicolon separated list of values as filter.

 |
| 

active

boolean

(query)

 | 

Active packages. true is def.

_Default value_ : true

 |
| 

archived

boolean

(query)

 | 

Archived packages. false is def.

_Default value_ : false

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
string
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 429 | 

Too Many Requests



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:14.980Z",
      "modifiedDT": "2026-01-29T03:17:14.980Z",
      "projectId": "string",
      "modelId": "string",
      "cadId": "string",
      "sheetId": "string",
      "viewId": "string",
      "isViewIdOverridden": true,
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "assemblyType": "0 = Unspecified",
      "assemblyTypeLabel": "string",
      "excludedCadIds": [
        "string"
      ],
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "name": "string",
      "nameLabel": "string",
      "partIds": [
        "string"
      ],
      "instanceIndex": "string",
      "lastUsedAssembliesPartsTableReportIds": [
        "string"
      ],
      "qrCodeUrl": "string",
      "notes": [
        {
          "isPartialData": true,
          "isReadOnly": true,
          "id": "string",
          "createdDT": "2026-01-29T03:17:14.980Z",
          "createdById": "string",
          "modifiedDT": "2026-01-29T03:17:14.980Z",
          "modifiedById": "string",
          "name": "string"
        }
      ],
      "defaultOrientationForReportTemplatesForgeViewerViewJson": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

includeAssemblyParts

boolean

(query)

 | 

OPTIONAL

_Default value_ : false

 |
| 

includeStratusProperties

boolean

(query)

 | 

Pass true to this optional query parameter if you want to generate STRATUS.Part.\* properties and have them returned for the parts.

_Default value_ : false

 |
| 

excludeNullAndEmpty

boolean

(query)

 | 

Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.

_Default value_ : false

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 100)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.007Z",
      "modifiedDT": "2026-01-29T03:17:15.007Z",
      "cutDT": "2026-01-29T03:17:15.007Z",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "modelId": "string",
      "modelName": "string",
      "bimAreaId": "string",
      "bimArea": "string",
      "cadId": "string",
      "cadType": "string",
      "webId": "string",
      "description": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "properties": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "propertiesGtp": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "points": [
        {
          "pointType": "0 = Unspecified",
          "cadId": "string",
          "location": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "direction": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "upVector": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "width": 0,
          "height": 0,
          "matingElementUniqueId": "string"
        }
      ],
      "cutLengthAdjustment": 0,
      "cutLength2Adjustment": 0,
      "lockLength": true,
      "lockLocation": true,
      "qrCodeUrl": "string",
      "partUrl": "string",
      "patternNumber": "string",
      "source": "0 = PublishedModel",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
qrcode \*

string

(path)

 | 

The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.024Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.024Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.024Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.024Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.024Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.024Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.024Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |
| 

trackingLogEntryId

string

(query)

 | 

Optional TrackingLogEntry Id to associate Attachment with a TrackingLogEntry

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdById": "string",
  "createdDT": "2026-01-29T03:17:15.040Z",
  "projectId": "string",
  "modelId": "string",
  "referenceType": "0 = Unspecified",
  "referenceName": "string",
  "referenceId": "string",
  "role": "0 = Unspecified",
  "roleName": "string",
  "fileType": "0 = Unspecified",
  "fileTypeName": "string",
  "localFilePath": "string",
  "fileName": "string",
  "overriddenRemoteFolder": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

REQUIRED: CutListDataApi - minimum json includes material, size, and cutListItems list with at least one entry containing lengthInInches

```
{
  "id": "string",
  "completedDT": "2026-01-29T03:17:15.055Z",
  "createdDT": "2026-01-29T03:17:15.055Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.055Z",
  "modifiedById": "string",
  "cutListItems": [
    {
      "area": "string",
      "assemblyId": "string",
      "assemblyName": "string",
      "index": 0,
      "cadId": "string",
      "cutDateTime": "2026-01-29T03:17:15.055Z",
      "description": "string",
      "itemNumber": "string",
      "lengthInInches": 0,
      "lengthInFeetAndInches": "string",
      "level": "string",
      "preFabId": "string",
      "qrCode": "string",
      "userData1": "string",
      "userData2": "string",
      "userData3": "string",
      "userData4": "string",
      "userData5": "string",
      "userData6": "string",
      "userData7": "string",
      "userData8": "string",
      "userData9": "string",
      "userData10": "string",
      "userData11": "string",
      "userData12": "string",
      "userData13": "string",
      "userData14": "string",
      "userData15": "string"
    }
  ],
  "cutListItemCount": 0,
  "cutListStatus": "0 = New",
  "cutListStatusLabel": "string",
  "cutListStatusName": "string",
  "isAutoGeneratedCutList": true,
  "material": "string",
  "modelId": "string",
  "name": "string",
  "packageId": "string",
  "projectId": "string",
  "requestedDT": "2026-01-29T03:17:15.055Z",
  "requestedUserId": "string",
  "size": "string",
  "startedDT": "2026-01-29T03:17:15.055Z",
  "stationId": "string",
  "totalLengthInInches": 0,
  "totalLengthInFeetAndInches": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "completedDT": "2026-01-29T03:17:15.059Z",
  "createdDT": "2026-01-29T03:17:15.059Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.059Z",
  "modifiedById": "string",
  "cutListItems": [
    {
      "area": "string",
      "assemblyId": "string",
      "assemblyName": "string",
      "index": 0,
      "cadId": "string",
      "cutDateTime": "2026-01-29T03:17:15.059Z",
      "description": "string",
      "itemNumber": "string",
      "lengthInInches": 0,
      "lengthInFeetAndInches": "string",
      "level": "string",
      "preFabId": "string",
      "qrCode": "string",
      "userData1": "string",
      "userData2": "string",
      "userData3": "string",
      "userData4": "string",
      "userData5": "string",
      "userData6": "string",
      "userData7": "string",
      "userData8": "string",
      "userData9": "string",
      "userData10": "string",
      "userData11": "string",
      "userData12": "string",
      "userData13": "string",
      "userData14": "string",
      "userData15": "string"
    }
  ],
  "cutListItemCount": 0,
  "cutListStatus": "0 = New",
  "cutListStatusLabel": "string",
  "cutListStatusName": "string",
  "isAutoGeneratedCutList": true,
  "material": "string",
  "modelId": "string",
  "name": "string",
  "packageId": "string",
  "percentComplete": 0,
  "projectId": "string",
  "requestedDT": "2026-01-29T03:17:15.059Z",
  "requestedUserId": "string",
  "size": "string",
  "startedDT": "2026-01-29T03:17:15.059Z",
  "stationId": "string",
  "totalLengthInInches": 0,
  "totalLengthInFeetAndInches": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

REQUIRED: TrackingStatusId

```
{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.074Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.076Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Array of Assembly CadIds to add.

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.091Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.091Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.091Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.091Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.091Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.091Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.091Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Array of Assembly CadIds used to replace existing.

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.108Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.108Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.108Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.108Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.108Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.108Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.108Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Array of Part CadIds used to replace existing.

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.126Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.126Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.126Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.126Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.126Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.126Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.126Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Example JSON KeyValuePair: {"key":"fieldId","value":"fieldValue"}

```
{
  "key": "string",
  "value": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "key": "string",
  "value": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Example JSON Array of KeyValuePair: \[{"key":"field1Id","value":"field1Value"},{"key":"field2Id","value":"field2Value"},...\]

```
[
  {
    "key": "string",
    "value": "string"
  }
]
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
0
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Package Id

 |

Array of Part CadIds to add.

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.171Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.171Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.171Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.171Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.171Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.171Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.171Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

Id is required. Status: 0 = Active, 1 = Archived.

```
{
  "categoryId": "string",
  "description": "string",
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.184Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.184Z",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.184Z",
  "requiredDT": "2026-01-29T03:17:15.184Z",
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.184Z",
  "status": 0
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "assemblyIds": [
    "string"
  ],
  "bimAreaId": "string",
  "bimAreaName": "string",
  "cadIdsBySequence": [
    "string"
  ],
  "categoryId": "string",
  "createdBy": "string",
  "createdDT": "2026-01-29T03:17:15.186Z",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "description": "string",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "hoursEstimatedField": 0,
  "hoursEstimatedOffice": 0,
  "hoursEstimatedPurchasing": 0,
  "hoursEstimatedShop": 0,
  "id": "string",
  "installedDT": "2026-01-29T03:17:15.186Z",
  "modelId": "string",
  "modifiedBy": "string",
  "modifiedDT": "2026-01-29T03:17:15.186Z",
  "name": "string",
  "number": "string",
  "officeDuration": 0,
  "officeStartDT": "2026-01-29T03:17:15.186Z",
  "partCadIds": [
    "string"
  ],
  "projectId": "string",
  "purchasingDuration": 0,
  "purchasingStartDT": "2026-01-29T03:17:15.186Z",
  "qrCodeUrl": "string",
  "requiredDT": "2026-01-29T03:17:15.186Z",
  "selectedTaskWorkflowIdsForAssemblyAndPartCadIds": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "shopDuration": 0,
  "startDT": "2026-01-29T03:17:15.186Z",
  "status": "0 = Active",
  "statusName": "string",
  "viewId": "string",
  "isViewIdOverridden": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Part

| Name | Description |
| --- | --- |
| 
includeStratusProperties

boolean

(query)

 | 

Pass true to this optional query parameter if you want to generate STRATUS.Part.\* properties and have them returned for the parts. When in use, query must be limited to a single model id.

_Default value_ : false

 |
| 

excludeNullAndEmpty

boolean

(query)

 | 

Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.

_Default value_ : false

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 100)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.210Z",
      "modifiedDT": "2026-01-29T03:17:15.210Z",
      "cutDT": "2026-01-29T03:17:15.210Z",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "modelId": "string",
      "modelName": "string",
      "bimAreaId": "string",
      "bimArea": "string",
      "cadId": "string",
      "cadType": "string",
      "webId": "string",
      "description": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "properties": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "propertiesGtp": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "points": [
        {
          "pointType": "0 = Unspecified",
          "cadId": "string",
          "location": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "direction": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "upVector": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "width": 0,
          "height": 0,
          "matingElementUniqueId": "string"
        }
      ],
      "cutLengthAdjustment": 0,
      "cutLength2Adjustment": 0,
      "lockLength": true,
      "lockLocation": true,
      "qrCodeUrl": "string",
      "partUrl": "string",
      "patternNumber": "string",
      "source": "0 = PublishedModel",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
qrcode \*

string

(path)

 | 

The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.

 |
| 

includeStratusProperties

boolean

(query)

 | 

Pass true to this optional query parameter if you want to generate STRATUS.Part.\* properties and have them returned for the parts. When in use, query must be limited to a single model id.

_Default value_ : false

 |
| 

excludeNullAndEmpty

boolean

(query)

 | 

Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.

_Default value_ : false

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.228Z",
  "modifiedDT": "2026-01-29T03:17:15.228Z",
  "cutDT": "2026-01-29T03:17:15.228Z",
  "projectId": "string",
  "projectName": "string",
  "projectNumber": "string",
  "modelId": "string",
  "modelName": "string",
  "bimAreaId": "string",
  "bimArea": "string",
  "cadId": "string",
  "cadType": "string",
  "webId": "string",
  "description": "string",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "properties": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "propertiesGtp": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "points": [
    {
      "pointType": "0 = Unspecified",
      "cadId": "string",
      "location": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "direction": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "upVector": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "width": 0,
      "height": 0,
      "matingElementUniqueId": "string"
    }
  ],
  "cutLengthAdjustment": 0,
  "cutLength2Adjustment": 0,
  "lockLength": true,
  "lockLocation": true,
  "qrCodeUrl": "string",
  "partUrl": "string",
  "patternNumber": "string",
  "source": "0 = PublishedModel",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |
| 

includeStratusProperties

boolean

(query)

 | 

Pass true to this optional query parameter if you want to generate STRATUS.Part.\* properties and have them returned for the parts.

_Default value_ : false

 |
| 

excludeNullAndEmpty

boolean

(query)

 | 

Pass true to this optional query parameter if you want empty or null values removed from the part's Properties and PropertiesGtp collections to improve performance.

_Default value_ : false

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.246Z",
  "modifiedDT": "2026-01-29T03:17:15.246Z",
  "cutDT": "2026-01-29T03:17:15.246Z",
  "projectId": "string",
  "projectName": "string",
  "projectNumber": "string",
  "modelId": "string",
  "modelName": "string",
  "bimAreaId": "string",
  "bimArea": "string",
  "cadId": "string",
  "cadType": "string",
  "webId": "string",
  "description": "string",
  "currentTrackingStatusId": "string",
  "currentDivisionId": "string",
  "properties": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "propertiesGtp": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "points": [
    {
      "pointType": "0 = Unspecified",
      "cadId": "string",
      "location": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "direction": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "upVector": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "width": 0,
      "height": 0,
      "matingElementUniqueId": "string"
    }
  ],
  "cutLengthAdjustment": 0,
  "cutLength2Adjustment": 0,
  "lockLength": true,
  "lockLocation": true,
  "qrCodeUrl": "string",
  "partUrl": "string",
  "patternNumber": "string",
  "source": "0 = PublishedModel",
  "fieldIdToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "fieldNameToValueMap": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
csvIds

string

(header)

 | 

List of STRATUS Part Ids

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
string
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |
| 

trackingLogEntryId

string

(query)

 | 

Optional TrackingLogEntry Id to associate Attachment with a TrackingLogEntry

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdById": "string",
  "createdDT": "2026-01-29T03:17:15.273Z",
  "projectId": "string",
  "modelId": "string",
  "referenceType": "0 = Unspecified",
  "referenceName": "string",
  "referenceId": "string",
  "role": "0 = Unspecified",
  "roleName": "string",
  "fileType": "0 = Unspecified",
  "fileTypeName": "string",
  "localFilePath": "string",
  "fileName": "string",
  "overriddenRemoteFolder": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |
| 

isCut

boolean

(query)

 | 

DEFAULT: true. If set to false, will not mark the part as cut.

_Default value_ : true

 |

REQUIRED: TrackingStatusId

```
{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.288Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "comment": "string",
  "costTypeId": "string",
  "createdDT": "2026-01-29T03:17:15.290Z",
  "divisionId": "string",
  "hours": 0,
  "trackingLogEntryIdResult": "string",
  "trackingStatusId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |

Example JSON KeyValuePair: {"key":"propertyKey","value":"propertyValue"}

```
{
  "key": "string",
  "value": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "key": "string",
  "value": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

Example List of PartPropertiesDataApi JSON: \[{"Id":"Part1.Id","Properties":{"Property1Key":"Property1Value","Property2Key":"Property2Value"}},{"Id":"Part2.Id","Properties":{"Property1Key":"Property1Value","Property2Key":"Property2Value"}}\]

```
[
  {
    "id": "string",
    "properties": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  }
]
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |

Example JSON KeyValuePair: {"key":"fieldId","value":"fieldValue"}

```
{
  "key": "string",
  "value": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "key": "string",
  "value": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Part Id

 |

Example JSON Array of KeyValuePair: \[{"key":"field1Id","value":"field1Value"},{"key":"field2Id","value":"field2Value"},...\]

```
[
  {
    "key": "string",
    "value": "string"
  }
]
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
0
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Ping

| Name | Description |
| --- | --- |
| 
app-id

string

(header)

 | 

(optional) Partner App Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |

### Project

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.365Z",
  "modifiedDT": "2026-01-29T03:17:15.365Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.365Z",
  "actualStartDate": "2026-01-29T03:17:15.365Z",
  "targetEndDate": "2026-01-29T03:17:15.365Z",
  "actualEndDate": "2026-01-29T03:17:15.365Z",
  "color": "string",
  "isTaxExempt": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

asFlatList

boolean

(query)

 | 

if true, results will be list of areas instead of hierarchy data structure using children, where ParentId can be used to understand hierarchy

_Default value_ : false

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "abbreviation": "string",
    "children": [
      "string"
    ],
    "code": "string",
    "color": "string",
    "createdById": "string",
    "createdDT": "2026-01-29T03:17:15.379Z",
    "elevation": 0,
    "id": "string",
    "levelBottomOffset": 0,
    "levelTopOffset": 0,
    "modifiedById": "string",
    "modifiedDT": "2026-01-29T03:17:15.379Z",
    "name": "string",
    "parentId": "string"
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.397Z",
      "modifiedDT": "2026-01-29T03:17:15.397Z",
      "projectId": "string",
      "modelId": "string",
      "cadId": "string",
      "sheetId": "string",
      "viewId": "string",
      "isViewIdOverridden": true,
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "assemblyType": "0 = Unspecified",
      "assemblyTypeLabel": "string",
      "excludedCadIds": [
        "string"
      ],
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "fieldNameToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "name": "string",
      "nameLabel": "string",
      "partIds": [
        "string"
      ],
      "instanceIndex": "string",
      "lastUsedAssembliesPartsTableReportIds": [
        "string"
      ],
      "qrCodeUrl": "string",
      "notes": [
        {
          "isPartialData": true,
          "isReadOnly": true,
          "id": "string",
          "createdDT": "2026-01-29T03:17:15.397Z",
          "createdById": "string",
          "modifiedDT": "2026-01-29T03:17:15.397Z",
          "modifiedById": "string",
          "name": "string"
        }
      ],
      "defaultOrientationForReportTemplatesForgeViewerViewJson": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "length": "string",
      "width": "string",
      "height": "string",
      "location": "string",
      "containerTypeName": "string",
      "parentContainerId": "string",
      "currentTrackingStatusId": "string",
      "currentDivisionId": "string",
      "qrCodeUrl": "string",
      "fieldIdToValueMap": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "partIds": [
        "string"
      ],
      "assemblyCadIds": [
        "string"
      ],
      "packageIds": [
        "string"
      ],
      "containerIds": [
        "string"
      ],
      "contents": [
        {
          "projectId": "string",
          "referenceId": "string",
          "referenceType": "0 = Unspecified"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "a360FolderId": "string",
      "createdDT": "2026-01-29T03:17:15.441Z",
      "databaseUnits": "0 = Imperial",
      "defaultViewId": "string",
      "id": "string",
      "isFieldOrderz": true,
      "lastPublishedDT": "2026-01-29T03:17:15.441Z",
      "modelName": "string",
      "modelType": "0 = Unspecified",
      "modifiedDT": "2026-01-29T03:17:15.441Z",
      "name": "string",
      "projectId": "string",
      "publishStatus": "0 = Published",
      "releaseVersion": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "name": "string",
      "number": "string",
      "description": "string",
      "statusName": "string",
      "supplierName": "string",
      "supplierResponseNumber": "string",
      "tax": 0,
      "freight": 0,
      "totalAmount": 0,
      "projectId": "string",
      "lineItems": [
        {
          "additionalProperty": "string",
          "ancillaryType": "string",
          "ancillaryUsageType": "string",
          "backorderedQTY": 0,
          "comment": "string",
          "description": "string",
          "diameter": "string",
          "isAncillary": true,
          "isModeled": true,
          "length": "string",
          "lineNumber": 0,
          "manufacturer": "string",
          "material": "string",
          "nominalStockLength": "string",
          "orderedQTY": 0,
          "partTemplateName": "string",
          "productCode": "string",
          "quotedQTY": 0,
          "serviceCode": "string",
          "serviceName": "string",
          "shippedQTY": 0,
          "size": "string",
          "totalPrice": 0,
          "unitOfMeasure": "string",
          "unitPrice": "string",
          "width": "string"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Project Id

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "source": "1 = STRATUS",
      "name": "string",
      "code": "string",
      "abbreviation": "string",
      "group": "string",
      "fabConfigId": "string",
      "fabServiceId": "string",
      "fabServiceSpecId": "string",
      "fabServiceInsulationSpecId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
nonStratusProjectsOnly

boolean

(query)

 | 

If true, returns only projects which have not been synced to Stratus, otherwise all projects (which takes longer).

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "id": "string",
    "createdDT": "2026-01-29T03:17:15.488Z",
    "modifiedDT": "2026-01-29T03:17:15.488Z",
    "status": "0 = New",
    "statusName": "string",
    "a360Id": "string",
    "a360RootFolderId": "string",
    "companyId": "string",
    "category": "string",
    "number": "string",
    "name": "string",
    "phase": "string",
    "description": "string",
    "imageAttachmentId": "string",
    "address1": "string",
    "address2": "string",
    "city": "string",
    "state": "string",
    "zip": "string",
    "targetStartDate": "2026-01-29T03:17:15.488Z",
    "actualStartDate": "2026-01-29T03:17:15.488Z",
    "targetEndDate": "2026-01-29T03:17:15.488Z",
    "actualEndDate": "2026-01-29T03:17:15.488Z",
    "color": "string",
    "isTaxExempt": true
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.507Z",
      "modifiedDT": "2026-01-29T03:17:15.507Z",
      "status": "0 = New",
      "statusName": "string",
      "a360Id": "string",
      "a360RootFolderId": "string",
      "companyId": "string",
      "category": "string",
      "number": "string",
      "name": "string",
      "phase": "string",
      "description": "string",
      "imageAttachmentId": "string",
      "address1": "string",
      "address2": "string",
      "city": "string",
      "state": "string",
      "zip": "string",
      "targetStartDate": "2026-01-29T03:17:15.507Z",
      "actualStartDate": "2026-01-29T03:17:15.507Z",
      "targetEndDate": "2026-01-29T03:17:15.507Z",
      "actualEndDate": "2026-01-29T03:17:15.507Z",
      "color": "string",
      "isTaxExempt": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
qrcode \*

string

(path)

 | 

The decoded text from a STRATUS QR Code -- being a URL or just the last eight characters of the URL.

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.522Z",
  "modifiedDT": "2026-01-29T03:17:15.522Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.522Z",
  "actualStartDate": "2026-01-29T03:17:15.522Z",
  "targetEndDate": "2026-01-29T03:17:15.522Z",
  "actualEndDate": "2026-01-29T03:17:15.522Z",
  "color": "string",
  "isTaxExempt": true
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
userid \*

string

(path)

 | 

User Id specified for Project Role filtering.

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.543Z",
      "modifiedDT": "2026-01-29T03:17:15.543Z",
      "status": "0 = New",
      "statusName": "string",
      "a360Id": "string",
      "a360RootFolderId": "string",
      "companyId": "string",
      "category": "string",
      "number": "string",
      "name": "string",
      "phase": "string",
      "description": "string",
      "imageAttachmentId": "string",
      "address1": "string",
      "address2": "string",
      "city": "string",
      "state": "string",
      "zip": "string",
      "targetStartDate": "2026-01-29T03:17:15.543Z",
      "actualStartDate": "2026-01-29T03:17:15.543Z",
      "targetEndDate": "2026-01-29T03:17:15.543Z",
      "actualEndDate": "2026-01-29T03:17:15.543Z",
      "color": "string",
      "isTaxExempt": true
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
addDefaultUserProjectRoles

boolean

(query)

 | 

if true, default user project roles will be added to the new project

 |
| 

setActive

boolean

(query)

 | 

if true, project will be set to Active status, otherwise set to New

 |

Pass Project object in request body. Project object returned by call to available-autodesk-projects can be passed into this method. Project object must contain valid A360Id and Name. Resulting ProjectDataApi will be returned with new Stratus Project Id if successful, otherwise null.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.560Z",
  "modifiedDT": "2026-01-29T03:17:15.560Z",
  "status": "0 = New",
  "statusName": "string",
  "a360Id": "string",
  "a360RootFolderId": "string",
  "companyId": "string",
  "category": "string",
  "number": "string",
  "name": "string",
  "phase": "string",
  "description": "string",
  "imageAttachmentId": "string",
  "address1": "string",
  "address2": "string",
  "city": "string",
  "state": "string",
  "zip": "string",
  "targetStartDate": "2026-01-29T03:17:15.560Z",
  "actualStartDate": "2026-01-29T03:17:15.560Z",
  "targetEndDate": "2026-01-29T03:17:15.560Z",
  "actualEndDate": "2026-01-29T03:17:15.560Z",
  "color": "string",
  "isTaxExempt": true
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK



 | _No links_ |

### QRCode

| Name | Description |
| --- | --- |
| 
urlSubstring

string

(query)

 | 

Optional: Returns all ShortURL records that have the given sub-string inside the URL field.

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "url": "string",
      "projectId": "string",
      "modelId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Tables

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "companyTableId": "string",
    "createdById": "string",
    "createdByName": "string",
    "createdDT": "2026-01-29T03:17:15.598Z",
    "csvData": "string",
    "headers": [
      "string"
    ],
    "id": "string",
    "isCloneToProjectTableEnabled": true,
    "modifiedById": "string",
    "modifiedByName": "string",
    "modifiedDT": "2026-01-29T03:17:15.598Z",
    "name": "string",
    "notes": "string",
    "projectId": "string",
    "referencesCount": 0
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.609Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.609Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "companyTableId": "string",
    "createdById": "string",
    "createdByName": "string",
    "createdDT": "2026-01-29T03:17:15.634Z",
    "csvData": "string",
    "headers": [
      "string"
    ],
    "id": "string",
    "isCloneToProjectTableEnabled": true,
    "modifiedById": "string",
    "modifiedByName": "string",
    "modifiedDT": "2026-01-29T03:17:15.634Z",
    "name": "string",
    "notes": "string",
    "projectId": "string",
    "referencesCount": 0
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |
| 

id \*

string

(path)

 | 

Table ID

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.648Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.648Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |
| 

id \*

string

(path)

 | 

Table ID

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

Table data

```
{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.673Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.673Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.675Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.675Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |

Column operation details

```
{
  "columnMappings": {
    "additionalProp1": 0,
    "additionalProp2": 0,
    "additionalProp3": 0
  },
  "columnName": "string",
  "defaultValue": "string",
  "index": 0,
  "operation": "1 = Add"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.691Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.691Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |
| 

index

integer($int32)

(query)

 | 

Index where to insert the column

 |
| 

columnName

string

(query)

 | 

Name of the new column

 |
| 

defaultValue

string

(query)

 | 

Default value for the new column

_Default value_ :

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.706Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.706Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |

Table data

```
{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.720Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.720Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.721Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.721Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

Updated table data

```
{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.735Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.735Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.737Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.737Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |
| 

index \*

integer($int32)

(path)

 | 

Index of the column to rename

 |
| 

newColumnName

string

(query)

 | 

New name for the column

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.750Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.750Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |

Column mappings (new index -> old index)

```
{
  "additionalProp1": 0,
  "additionalProp2": 0,
  "additionalProp3": 0
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.766Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.766Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |

Updated table data

```
{
  "isReadOnly": true,
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.780Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.780Z",
  "modifiedById": "string",
  "companyTableId": "string",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "isCloneToProjectTableEnabled": true,
  "name": "string",
  "notes": "string",
  "projectId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.782Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.782Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

Table ID

 |
| 

index \*

integer($int32)

(path)

 | 

Index of the column to remove

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "companyTableId": "string",
  "createdById": "string",
  "createdByName": "string",
  "createdDT": "2026-01-29T03:17:15.807Z",
  "csvData": "string",
  "headers": [
    "string"
  ],
  "id": "string",
  "isCloneToProjectTableEnabled": true,
  "modifiedById": "string",
  "modifiedByName": "string",
  "modifiedDT": "2026-01-29T03:17:15.807Z",
  "name": "string",
  "notes": "string",
  "projectId": "string",
  "referencesCount": 0
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
0
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
projectId \*

string

(path)

 | 

Project ID

 |
| 

id \*

string

(path)

 | 

Table ID

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Task

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.847Z",
      "createdById": "string",
      "modifiedDT": "2026-01-29T03:17:15.847Z",
      "modifiedById": "string",
      "projectId": "string",
      "modelId": "string",
      "packageId": "string",
      "taskWorkflowId": "string",
      "taskDefinitionId": "string",
      "description": "string",
      "referenceType": "0 = Unspecified",
      "referenceTypeName": "string",
      "referenceId": "string",
      "referenceCadId": "string",
      "taskStatus": "string",
      "assignedUserId": "string",
      "assignedStationId": "string",
      "logEntries": [
        {
          "createdById": "string",
          "createdDT": "2026-01-29T03:17:15.847Z",
          "taskStatus": "string",
          "stationId": "string"
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Task Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "id": "string",
  "createdDT": "2026-01-29T03:17:15.860Z",
  "createdById": "string",
  "modifiedDT": "2026-01-29T03:17:15.860Z",
  "modifiedById": "string",
  "projectId": "string",
  "modelId": "string",
  "packageId": "string",
  "taskWorkflowId": "string",
  "taskDefinitionId": "string",
  "description": "string",
  "referenceType": "0 = Unspecified",
  "referenceTypeName": "string",
  "referenceId": "string",
  "referenceCadId": "string",
  "taskStatus": "string",
  "assignedUserId": "string",
  "assignedStationId": "string",
  "logEntries": [
    {
      "createdById": "string",
      "createdDT": "2026-01-29T03:17:15.860Z",
      "taskStatus": "string",
      "stationId": "string"
    }
  ]
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS Task Id

 |
| 

stationId

string

(query)

 | 

Optional Station Id to associate with Status update

 |
| 

taskStatusId

string

(query)

 | 

Required Task Status Id to assign to Task

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
toolId

string

(query)

 | 

STRATUS Tool Id

 |
| 

modelId

string

(query)

 | 

STRATUS Model Id

 |
| 

partCadId

string

(query)

 | 

STRATUS Part CadId

 |
| 

taskDefinitionId

string

(query)

 | 

STRATUS Task Definition Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
toolId

string

(query)

 | 

STRATUS Tool Id

 |
| 

modelId

string

(query)

 | 

STRATUS Model Id

 |
| 

partCadId

string

(query)

 | 

STRATUS Part CadId

 |
| 

taskDefinitionId

string

(query)

 | 

STRATUS Task Definition Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### TimeSession

| Name | Description |
| --- | --- |
| 
where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "isPartialData": true,
      "isReadOnly": true,
      "id": "string",
      "createdDT": "2026-01-29T03:17:15.921Z",
      "createdById": "string",
      "modifiedDT": "2026-01-29T03:17:15.921Z",
      "modifiedById": "string",
      "activityType": "0 = None",
      "activityTypeName": "string",
      "divisionId": "string",
      "divisionName": "string",
      "email": "string",
      "employeeId": "string",
      "firstName": "string",
      "isLocked": true,
      "lastName": "string",
      "modelId": "string",
      "modelName": "string",
      "packageCategoryId": "string",
      "packageCategoryName": "string",
      "packageDivisionId": "string",
      "packageDivisionName": "string",
      "packageId": "string",
      "packageName": "string",
      "packageNumber": "string",
      "projectId": "string",
      "projectName": "string",
      "projectNumber": "string",
      "shiftTypeId": "string",
      "startDT": "2026-01-29T03:17:15.921Z",
      "stationDivisionId": "string",
      "stationDivisionName": "string",
      "stationId": "string",
      "stationName": "string",
      "stopDT": "2026-01-29T03:17:15.921Z",
      "taskDefinitionId": "string",
      "userTypeName": "string",
      "workerId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

```
{
  "isLocked": true,
  "timeSessionIds": [
    "string"
  ]
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK



 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### TrackingLog

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "id": "string",
      "createdDT": "2026-01-29T03:17:16.051Z",
      "currentDivisionId": "string",
      "modifiedDT": "2026-01-29T03:17:16.051Z",
      "modelId": "string",
      "referenceType": "0 = Unspecified",
      "referenceName": "string",
      "referenceId": "string",
      "currentTrackingStatusId": "string",
      "totalHours": 0,
      "trackingLogEntries": [
        {
          "trackingStatusId": "string",
          "createdById": "string",
          "createdDT": "2026-01-29T03:17:16.051Z",
          "divisionId": "string",
          "id": "string",
          "origin": "0 = Unknown",
          "comment": "string",
          "hours": 0,
          "costTypeId": "string",
          "hoursCost": 0
        }
      ]
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "additionalProp1": "string",
  "additionalProp2": "string",
  "additionalProp3": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "additionalProp1": "string",
  "additionalProp2": "string",
  "additionalProp3": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### User

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.081Z",
    "additionalProp2": "2026-01-29T03:17:16.081Z",
    "additionalProp3": "2026-01-29T03:17:16.081Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "userId": "string",
  "firstName": "string",
  "lastName": "string",
  "shortUrl": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
[
  {
    "projectId": "string",
    "projectRoleTypeId": "string"
  }
]
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |
| 

where

(query)

 | 

Filter on JSON property values. Example: To filter on two JSON properties: length eq '10' AND description == "truck". To get the last 30 days of data, use: createdDT ge DateTime.Now.AddDays(-30)

 |
| 

page

(query)

 | 

Offset retrieves a given page of data, where 0 is the 1st page, etc (number of elements per page is set by PageSize below)

 |
| 

pagesize

(query)

 | 

Optional: defines the number of elements per page (default (and max) is 1000)

 |
| 

disabletotal

(query)

 | 

Optional: disable total calculation to improve performance (default is false)

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "data": [
    {
      "cellPhone": "string",
      "companyId": "string",
      "companyName": "string",
      "dateFormat": "string",
      "email": "string",
      "firstName": "string",
      "hourFormat": "string",
      "id": "string",
      "isCheckedIn": true,
      "isTimeTrackingEnabled": true,
      "lastName": "string",
      "lastViewedDateTimeForAssemblyId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "lastViewedDateTimeForModelId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "lastViewedDateTimeForPackageId": {
        "additionalProp1": "2026-01-29T03:17:16.122Z",
        "additionalProp2": "2026-01-29T03:17:16.122Z",
        "additionalProp3": "2026-01-29T03:17:16.122Z"
      },
      "longDateFormat": "string",
      "profileImageUrl": "string",
      "profileImageBase64": "string",
      "status": "1 = Active",
      "timeFormat": "string",
      "timeZoneInfoId": "string"
    }
  ],
  "pageOffset": 0,
  "pageLimit": 0,
  "pageCount": 0,
  "total": 0,
  "truncatedResults": true,
  "truncatedReason": "string",
  "filterOptions": [
    {
      "isValueConcatenated": true,
      "data": "string",
      "options": [
        "string"
      ]
    }
  ],
  "links": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
email \*

string

(path)

 |  |
| 

include

(query)

 | 

A comma delimited list of JSON properties to return. All remaining JSON properties will removed from the JSON response. Example: id, description, cutListItems. Specific dictionary keys can be included as follows: properties\["Family"\], propertiesGtp\["Material"\]

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.135Z",
    "additionalProp2": "2026-01-29T03:17:16.135Z",
    "additionalProp3": "2026-01-29T03:17:16.135Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |

```
{
  "projectId": "string",
  "projectRoleTypeId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "projectId": "string",
  "projectRoleTypeId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |

```
{
  "projectId": "string",
  "projectRoleTypeId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
{
  "projectId": "string",
  "projectRoleTypeId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 |  |

```
{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.177Z",
    "additionalProp2": "2026-01-29T03:17:16.177Z",
    "additionalProp3": "2026-01-29T03:17:16.177Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}
```

| Code | Description | Links |
| --- | --- | --- |
| 202 | 
Accepted

Media type

Controls `Accept` header.

```
{
  "cellPhone": "string",
  "companyId": "string",
  "companyName": "string",
  "dateFormat": "string",
  "email": "string",
  "firstName": "string",
  "hourFormat": "string",
  "id": "string",
  "isCheckedIn": true,
  "isTimeTrackingEnabled": true,
  "lastName": "string",
  "lastViewedDateTimeForAssemblyId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "lastViewedDateTimeForModelId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "lastViewedDateTimeForPackageId": {
    "additionalProp1": "2026-01-29T03:17:16.181Z",
    "additionalProp2": "2026-01-29T03:17:16.181Z",
    "additionalProp3": "2026-01-29T03:17:16.181Z"
  },
  "longDateFormat": "string",
  "profileImageUrl": "string",
  "profileImageBase64": "string",
  "status": "1 = Active",
  "timeFormat": "string",
  "timeZoneInfoId": "string"
}
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

| Name | Description |
| --- | --- |
| 
id \*

string

(path)

 | 

STRATUS User Id

 |
| 

projectId \*

string

(path)

 | 

STRATUS Project Id

 |

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
true
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### Version

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
OK

Media type

Controls `Accept` header.

```
"string"
```





 | _No links_ |
| 400 | 

Bad Request



 | _No links_ |
| 401 | 

Unauthorized



 | _No links_ |
| 404 | 

Not Found



 | _No links_ |
| 500 | 

Internal Server Error



 | _No links_ |

### API Health

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
Health description

Media type

Controls `Accept` header.

```
{
  "status": "string",
  "totalDuration": "string",
  "entries": {}
}
```





 | _No links_ |

integer($int32)Enum:  

{

<table><tbody><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdByName</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>divisionName</td><td><span><span></span></span></td></tr><tr><td>route</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>projectName</td><td><span><span></span></span></td></tr><tr><td>projectNumber</td><td><span><span></span></span></td></tr><tr><td>projectColor</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>modelName</td><td><span><span></span></span></td></tr><tr><td>reference</td><td><span><span></span></span></td></tr><tr><td>referenceId</td><td><span><span></span></span></td></tr><tr><td>referenceName</td><td><span><span></span></span></td></tr><tr><td>action</td><td><span><span></span></span></td></tr><tr><td>actionName</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>value</td><td><span><span></span></span></td></tr><tr><td>trackingStatusId</td><td><span><span></span></span></td></tr><tr><td>trackingStatusName</td><td><span><span></span></span></td></tr><tr><td>trackingStatusColor</td><td><span><span></span></span></td></tr><tr><td>stationId</td><td><span><span></span></span></td></tr><tr><td>stationName</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>stratusDimensionType</td><td><span><span></span></span></td></tr><tr><td>orderId</td><td><span><span></span></span></td></tr><tr><td>assemblyId</td><td><span><span></span></span></td></tr><tr><td>partCadIds</td><td><span><span></span></span></td></tr><tr><td>colorIndex</td><td><span><span></span></span></td></tr><tr><td>dimensionLineType</td><td><span><span></span></span></td></tr><tr><td>connectedAssemblyId</td><td><span><span></span></span></td></tr><tr><td>distance</td><td><span><span></span></span></td></tr><tr><td>label</td><td><span><span></span></span></td></tr><tr><td>lineVertices</td><td><span><span></span></span></td></tr><tr><td>location</td><td><span><span></span></span></td></tr><tr><td>gridlineAnnotation</td><td><span><span></span></span></td></tr><tr><td>dimensionAnchorTypes</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>abbreviation</td><td><span><span></span></span></td></tr><tr><td>children</td><td><span><span></span></span></td></tr><tr><td>code</td><td><span><span></span></span></td></tr><tr><td>color</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>elevation</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>levelBottomOffset</td><td><span><span></span></span></td></tr><tr><td>levelTopOffset</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>parentId</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>cadId</td><td><span><span></span></span></td></tr><tr><td>sheetId</td><td><span><span></span></span></td></tr><tr><td>viewId</td><td><span><span></span></span></td></tr><tr><td>isViewIdOverridden</td><td><span><span></span></span></td></tr><tr><td>currentTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>currentDivisionId</td><td><span><span></span></span></td></tr><tr><td>assemblyType</td><td><span><span></span></span></td></tr><tr><td>assemblyTypeLabel</td><td><span><span></span></span></td></tr><tr><td>excludedCadIds</td><td><span><span></span></span></td></tr><tr><td>fieldIdToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>fieldNameToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>nameLabel</td><td><span><span></span></span></td></tr><tr><td>partIds</td><td><span><span></span></span></td></tr><tr><td>instanceIndex</td><td><span><span></span></span></td></tr><tr><td>lastUsedAssembliesPartsTableReportId</td><td><span><span></span></span></td></tr><tr><td>lastUsedAssembliesPartsTableReportIds</td><td><span><span></span></span></td></tr><tr><td>qrCodeUrl</td><td><span><span></span></span></td></tr><tr><td>notes</td><td><span><span></span></span></td></tr><tr><td>defaultOrientationForReportTemplatesForgeViewerViewJson</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>cadId</td><td><span><span></span></span></td></tr><tr><td>createdByUserEmail</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>initialTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>name<span>*</span></td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>isPartialData</td><td><span><span></span></span></td></tr><tr><td>isReadOnly</td><td><span><span></span></span></td></tr><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>fabConfigName</td><td><span><span></span></span></td></tr><tr><td>fabFileGroupId</td><td><span><span></span></span></td></tr><tr><td>fabLocaleId</td><td><span><span></span></span></td></tr><tr><td>fabProfileName</td><td><span><span></span></span></td></tr><tr><td>fabUnitType</td><td><span><span></span></span></td></tr><tr><td>fileByteCount</td><td><span><span></span></span></td></tr><tr><td>fileName<span>*</span></td><td><span><span></span></span></td></tr><tr><td>fileType</td><td><span><span></span></span></td></tr><tr><td>fileUploadTimeInSeconds</td><td><span><span></span></span></td></tr><tr><td>isCollaboration</td><td><span><span></span></span></td></tr><tr><td>isMarkups</td><td><span><span></span></span></td></tr><tr><td>isPrimaryModel</td><td><span><span></span></span></td></tr><tr><td>itemIdBase64URN</td><td><span><span></span></span></td></tr><tr><td>itemId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>itemLink<span>*</span></td><td><span><span></span></span></td></tr><tr><td>localFilePath</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>overriddenRemoteFolder</td><td><span><span></span></span></td></tr><tr><td>parentAttachmentId</td><td><span><span></span></span></td></tr><tr><td>previewImageFileId</td><td><span><span></span></span></td></tr><tr><td>previousVersions</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>projectId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>referenceId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>referenceType<span>*</span></td><td><span><span></span></span></td></tr><tr><td>role</td><td><span><span></span></span></td></tr><tr><td>totalTransformationMatrix</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>referenceType</td><td><span><span></span></span></td></tr><tr><td>referenceName</td><td><span><span></span></span></td></tr><tr><td>referenceId</td><td><span><span></span></span></td></tr><tr><td>role</td><td><span><span></span></span></td></tr><tr><td>roleName</td><td><span><span></span></span></td></tr><tr><td>fileType</td><td><span><span></span></span></td></tr><tr><td>fileTypeName</td><td><span><span></span></span></td></tr><tr><td>localFilePath</td><td><span><span></span></span></td></tr><tr><td>fileName</td><td><span><span></span></span></td></tr><tr><td>overriddenRemoteFolder</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>bytes</td><td><span><span></span></span></td></tr><tr><td>contentType</td><td><span><span></span></span></td></tr><tr><td>fileName</td><td><span><span></span></span></td></tr><tr><td>localPath</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>packageId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>requiredDT</td><td><span><span></span></span></td></tr><tr><td>isLocked</td><td><span><span></span></span></td></tr><tr><td>generatedDT</td><td><span><span></span></span></td></tr><tr><td>generatedByName</td><td><span><span></span></span></td></tr><tr><td>lockedDT</td><td><span><span></span></span></td></tr><tr><td>lockedByName</td><td><span><span></span></span></td></tr><tr><td>unlockedDT</td><td><span><span></span></span></td></tr><tr><td>unlockedByName</td><td><span><span></span></span></td></tr><tr><td>lineItems</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>groupedPartCadIds</td><td><span><span></span></span></td></tr><tr><td>sequence</td><td><span><span></span></span></td></tr><tr><td>isModeled</td><td><span><span></span></span></td></tr><tr><td>isReportable</td><td><span><span></span></span></td></tr><tr><td>isConsolidated</td><td><span><span></span></span></td></tr><tr><td>manufacturer</td><td><span><span></span></span></td></tr><tr><td>quantity</td><td><span><span></span></span></td></tr><tr><td>size</td><td><span><span></span></span></td></tr><tr><td>description<span>*</span></td><td><span><span></span></span></td></tr><tr><td>material</td><td><span><span></span></span></td></tr><tr><td>productCode</td><td><span><span></span></span></td></tr><tr><td>diameter</td><td><span><span></span></span></td></tr><tr><td>width</td><td><span><span></span></span></td></tr><tr><td>length</td><td><span><span></span></span></td></tr><tr><td>isLengthNestable</td><td><span><span></span></span></td></tr><tr><td>nominalStockLength</td><td><span><span></span></span></td></tr><tr><td>additionalProperty</td><td><span><span></span></span></td></tr><tr><td>unitOfMeasure</td><td><span><span></span></span></td></tr><tr><td>unitOfMeasureName</td><td><span><span></span></span></td></tr><tr><td>comment</td><td><span><span></span></span></td></tr><tr><td>notPurchased</td><td><span><span></span></span></td></tr><tr><td>isAncillary</td><td><span><span></span></span></td></tr><tr><td>serviceName</td><td><span><span></span></span></td></tr><tr><td>serviceCode</td><td><span><span></span></span></td></tr><tr><td>possibleSupplierCodes</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>abbreviation</td><td><span><span></span></span></td></tr><tr><td>useAssemblies</td><td><span><span></span></span></td></tr><tr><td>useContainers</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>length</td><td><span><span></span></span></td></tr><tr><td>width</td><td><span><span></span></span></td></tr><tr><td>height</td><td><span><span></span></span></td></tr><tr><td>location</td><td><span><span></span></span></td></tr><tr><td>containerTypeName</td><td><span><span></span></span></td></tr><tr><td>parentContainerId</td><td><span><span></span></span></td></tr><tr><td>currentTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>currentDivisionId</td><td><span><span></span></span></td></tr><tr><td>qrCodeUrl</td><td><span><span></span></span></td></tr><tr><td>fieldIdToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>partIds</td><td><span><span></span></span></td></tr><tr><td>assemblyCadIds</td><td><span><span></span></span></td></tr><tr><td>packageIds</td><td><span><span></span></span></td></tr><tr><td>containerIds</td><td><span><span></span></span></td></tr><tr><td>contents</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>referenceId</td><td><span><span></span></span></td></tr><tr><td>referenceType</td><td><span><span></span></span></td></tr></tbody></table>

}

{}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>code</td><td><span><span></span></span></td></tr><tr><td>color</td><td><span><span></span></span></td></tr><tr><td>hourlyRate</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>containerTypeId</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>length</td><td><span><span></span></span></td></tr><tr><td>width</td><td><span><span></span></span></td></tr><tr><td>height</td><td><span><span></span></span></td></tr><tr><td>location</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>completedDT</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>cutListItems</td><td><span><span></span></span></td></tr><tr><td>cutListItemCount</td><td><span><span></span></span></td></tr><tr><td>cutListStatus</td><td><span><span></span></span></td></tr><tr><td>cutListStatusLabel</td><td><span><span></span></span></td></tr><tr><td>cutListStatusName</td><td><span><span></span></span></td></tr><tr><td>isAutoGeneratedCutList</td><td><span><span></span></span></td></tr><tr><td>material</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>packageId</td><td><span><span></span></span></td></tr><tr><td>percentComplete</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>requestedDT</td><td><span><span></span></span></td></tr><tr><td>requestedUserId</td><td><span><span></span></span></td></tr><tr><td>size</td><td><span><span></span></span></td></tr><tr><td>startedDT</td><td><span><span></span></span></td></tr><tr><td>stationId</td><td><span><span></span></span></td></tr><tr><td>totalLengthInInches</td><td><span><span></span></span></td></tr><tr><td>totalLengthInFeetAndInches</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>area</td><td><span><span></span></span></td></tr><tr><td>assemblyId</td><td><span><span></span></span></td></tr><tr><td>assemblyName</td><td><span><span></span></span></td></tr><tr><td>index</td><td><span><span></span></span></td></tr><tr><td>cadId</td><td><span><span></span></span></td></tr><tr><td>cutDateTime</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>itemNumber</td><td><span><span></span></span></td></tr><tr><td>lengthInInches</td><td><span><span></span></span></td></tr><tr><td>lengthInFeetAndInches</td><td><span><span></span></span></td></tr><tr><td>level</td><td><span><span></span></span></td></tr><tr><td>preFabId</td><td><span><span></span></span></td></tr><tr><td>qrCode</td><td><span><span></span></span></td></tr><tr><td>userData1</td><td><span><span></span></span></td></tr><tr><td>userData2</td><td><span><span></span></span></td></tr><tr><td>userData3</td><td><span><span></span></span></td></tr><tr><td>userData4</td><td><span><span></span></span></td></tr><tr><td>userData5</td><td><span><span></span></span></td></tr><tr><td>userData6</td><td><span><span></span></span></td></tr><tr><td>userData7</td><td><span><span></span></span></td></tr><tr><td>userData8</td><td><span><span></span></span></td></tr><tr><td>userData9</td><td><span><span></span></span></td></tr><tr><td>userData10</td><td><span><span></span></span></td></tr><tr><td>userData11</td><td><span><span></span></span></td></tr><tr><td>userData12</td><td><span><span></span></span></td></tr><tr><td>userData13</td><td><span><span></span></span></td></tr><tr><td>userData14</td><td><span><span></span></span></td></tr><tr><td>userData15</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

integer($int32)Enum:  

{}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>trackingStatusGroupId</td><td><span><span></span></span></td></tr><tr><td>trackingStatusGroupName</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>dataType</td><td><span><span></span></span></td></tr><tr><td>dataTypeName</td><td><span><span></span></span></td></tr><tr><td>defaultValue</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>displayName</td><td><span><span></span></span></td></tr><tr><td>expression</td><td><span><span></span></span></td></tr><tr><td>filterId</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>isEditable</td><td><span><span></span></span></td></tr><tr><td>isExpression</td><td><span><span></span></span></td></tr><tr><td>isTotal</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>possibleValues</td><td><span><span></span></span></td></tr><tr><td>unit</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{}

{

<table><tbody><tr><td>isValueConcatenated</td><td><span><span></span></span></td></tr><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>options</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>gridIntersections</td><td><span><span></span></span></td></tr><tr><td>gridLines</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>horizontalAnnotation</td><td><span><span></span></span></td></tr><tr><td>horizontalDirection</td><td><span><span></span></span></td></tr><tr><td>horizontalGridLineId</td><td><span><span></span></span></td></tr><tr><td>intersectionPoint</td><td><span><span></span></span></td></tr><tr><td>verticalAnnotation</td><td><span><span></span></span></td></tr><tr><td>verticalDirection</td><td><span><span></span></span></td></tr><tr><td>verticalGridLineId</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>annotation</td><td><span><span></span></span></td></tr><tr><td>gridLineType</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>linePoints</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>status</td><td><span><span></span></span></td></tr><tr><td>totalDuration</td><td><span><span></span></span></td></tr><tr><td>entries</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>isPartialData</td><td><span><span></span></span></td></tr><tr><td>isReadOnly</td><td><span><span></span></span></td></tr><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>companyTableId</td><td><span><span></span></span></td></tr><tr><td>csvData</td><td><span><span></span></span></td></tr><tr><td>headers</td><td><span><span></span></span></td></tr><tr><td>isCloneToProjectTableEnabled</td><td><span><span></span></span></td></tr><tr><td>name<span>*</span></td><td><span><span></span></span></td></tr><tr><td>notes</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>a360FolderId</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>databaseUnits</td><td><span><span></span></span></td></tr><tr><td>defaultViewId</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>isFieldOrderz</td><td><span><span></span></span></td></tr><tr><td>lastPublishedDT</td><td><span><span></span></span></td></tr><tr><td>modelName</td><td><span><span></span></span></td></tr><tr><td>modelType</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>publishStatus</td><td><span><span></span></span></td></tr><tr><td>releaseVersion</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>viewRole</td><td><span><span></span></span></td></tr><tr><td>autodeskViewId</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>assemblyName</td><td><span><span></span></span></td></tr><tr><td>packageName</td><td><span><span></span></span></td></tr><tr><td>packageNumber</td><td><span><span></span></span></td></tr><tr><td>purchaseNumber</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>employeeId</td><td><span><span></span></span></td></tr><tr><td>firstName</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>isCheckedIn</td><td><span><span></span></span></td></tr><tr><td>isTimeTrackingEnabled</td><td><span><span></span></span></td></tr><tr><td>lastName</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>status</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>isPartialData</td><td><span><span></span></span></td></tr><tr><td>isReadOnly</td><td><span><span></span></span></td></tr><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>assemblyIds</td><td><span><span></span></span></td></tr><tr><td>bimAreaId</td><td><span><span></span></span></td></tr><tr><td>bimAreaName</td><td><span><span></span></span></td></tr><tr><td>assemblyCadIds</td><td><span><span></span></span></td></tr><tr><td>cadIdsBySequence</td><td><span><span></span></span></td></tr><tr><td>categoryId</td><td><span><span></span></span></td></tr><tr><td>createdBy</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>currentTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>currentDivisionId</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>fieldIdToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>fieldNameToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>hoursEstimatedField</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedOffice</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedPurchasing</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedShop</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>installedDT</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>modifiedBy</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>number</td><td><span><span></span></span></td></tr><tr><td>officeDuration</td><td><span><span></span></span></td></tr><tr><td>officeStartDT</td><td><span><span></span></span></td></tr><tr><td>partCadIds</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>purchasingDuration</td><td><span><span></span></span></td></tr><tr><td>purchasingStartDT</td><td><span><span></span></span></td></tr><tr><td>qrCodeUrl</td><td><span><span></span></span></td></tr><tr><td>requiredDT</td><td><span><span></span></span></td></tr><tr><td>selectedTaskWorkflowIdsForAssemblyAndPartCadIds</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>shopDuration</td><td><span><span></span></span></td></tr><tr><td>startDT</td><td><span><span></span></span></td></tr><tr><td>status</td><td><span><span></span></span></td></tr><tr><td>statusName</td><td><span><span></span></span></td></tr><tr><td>viewId</td><td><span><span></span></span></td></tr><tr><td>isViewIdOverridden</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>categoryId</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedField</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedOffice</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedPurchasing</td><td><span><span></span></span></td></tr><tr><td>hoursEstimatedShop</td><td><span><span></span></span></td></tr><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>installedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>number</td><td><span><span></span></span></td></tr><tr><td>officeDuration</td><td><span><span></span></span></td></tr><tr><td>officeStartDT</td><td><span><span></span></span></td></tr><tr><td>purchasingDuration</td><td><span><span></span></span></td></tr><tr><td>purchasingStartDT</td><td><span><span></span></span></td></tr><tr><td>requiredDT</td><td><span><span></span></span></td></tr><tr><td>shopDuration</td><td><span><span></span></span></td></tr><tr><td>startDT</td><td><span><span></span></span></td></tr><tr><td>status</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>areaId</td><td><span><span></span></span></td></tr><tr><td>categoryId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdByUserEmail</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>initialTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>name<span>*</span></td><td><span><span></span></span></td></tr><tr><td>number</td><td><span><span></span></span></td></tr><tr><td>orderNameFOZ</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>cutDT</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>projectName</td><td><span><span></span></span></td></tr><tr><td>projectNumber</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>modelName</td><td><span><span></span></span></td></tr><tr><td>bimAreaId</td><td><span><span></span></span></td></tr><tr><td>bimArea</td><td><span><span></span></span></td></tr><tr><td>cadId</td><td><span><span></span></span></td></tr><tr><td>cadType</td><td><span><span></span></span></td></tr><tr><td>webId</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>currentTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>currentDivisionId</td><td><span><span></span></span></td></tr><tr><td>properties</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>propertiesGtp</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>points</td><td><span><span></span></span></td></tr><tr><td>cutLengthAdjustment</td><td><span><span></span></span></td></tr><tr><td>cutLength2Adjustment</td><td><span><span></span></span></td></tr><tr><td>lockLength</td><td><span><span></span></span></td></tr><tr><td>lockLocation</td><td><span><span></span></span></td></tr><tr><td>qrCodeUrl</td><td><span><span></span></span></td></tr><tr><td>partUrl</td><td><span><span></span></span></td></tr><tr><td>patternNumber</td><td><span><span></span></span></td></tr><tr><td>source</td><td><span><span></span></span></td></tr><tr><td>fieldIdToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>fieldNameToValueMap</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>pointType</td><td><span><span></span></span></td></tr><tr><td>cadId</td><td><span><span></span></span></td></tr><tr><td>location</td><td><span><span></span></span></td></tr><tr><td>direction</td><td><span><span></span></span></td></tr><tr><td>upVector</td><td><span><span></span></span></td></tr><tr><td>width</td><td><span><span></span></span></td></tr><tr><td>height</td><td><span><span></span></span></td></tr><tr><td>matingElementUniqueId</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>properties</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>status</td><td><span><span></span></span></td></tr><tr><td>statusName</td><td><span><span></span></span></td></tr><tr><td>a360Id</td><td><span><span></span></span></td></tr><tr><td>a360RootFolderId</td><td><span><span></span></span></td></tr><tr><td>companyId</td><td><span><span></span></span></td></tr><tr><td>category</td><td><span><span></span></span></td></tr><tr><td>number</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>phase</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>imageAttachmentId</td><td><span><span></span></span></td></tr><tr><td>address1</td><td><span><span></span></span></td></tr><tr><td>address2</td><td><span><span></span></span></td></tr><tr><td>city</td><td><span><span></span></span></td></tr><tr><td>state</td><td><span><span></span></span></td></tr><tr><td>zip</td><td><span><span></span></span></td></tr><tr><td>targetStartDate</td><td><span><span></span></span></td></tr><tr><td>actualStartDate</td><td><span><span></span></span></td></tr><tr><td>targetEndDate</td><td><span><span></span></span></td></tr><tr><td>actualEndDate</td><td><span><span></span></span></td></tr><tr><td>color</td><td><span><span></span></span></td></tr><tr><td>isTaxExempt</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>projectRoleTypeId</td><td><span><span></span></span></td></tr></tbody></table>

}

{}

{

<table><tbody><tr><td>source</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>code</td><td><span><span></span></span></td></tr><tr><td>abbreviation</td><td><span><span></span></span></td></tr><tr><td>group</td><td><span><span></span></span></td></tr><tr><td>fabConfigId</td><td><span><span></span></span></td></tr><tr><td>fabServiceId</td><td><span><span></span></span></td></tr><tr><td>fabServiceSpecId</td><td><span><span></span></span></td></tr><tr><td>fabServiceInsulationSpecId</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>number</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>statusName</td><td><span><span></span></span></td></tr><tr><td>supplierName</td><td><span><span></span></span></td></tr><tr><td>supplierResponseNumber</td><td><span><span></span></span></td></tr><tr><td>tax</td><td><span><span></span></span></td></tr><tr><td>freight</td><td><span><span></span></span></td></tr><tr><td>totalAmount</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>lineItems</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>additionalProperty</td><td><span><span></span></span></td></tr><tr><td>ancillaryType</td><td><span><span></span></span></td></tr><tr><td>ancillaryUsageType</td><td><span><span></span></span></td></tr><tr><td>backorderedQTY</td><td><span><span></span></span></td></tr><tr><td>comment</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>diameter</td><td><span><span></span></span></td></tr><tr><td>isAncillary</td><td><span><span></span></span></td></tr><tr><td>isModeled</td><td><span><span></span></span></td></tr><tr><td>length</td><td><span><span></span></span></td></tr><tr><td>lineNumber</td><td><span><span></span></span></td></tr><tr><td>manufacturer</td><td><span><span></span></span></td></tr><tr><td>material</td><td><span><span></span></span></td></tr><tr><td>nominalStockLength</td><td><span><span></span></span></td></tr><tr><td>orderedQTY</td><td><span><span></span></span></td></tr><tr><td>partTemplateName</td><td><span><span></span></span></td></tr><tr><td>productCode</td><td><span><span></span></span></td></tr><tr><td>quotedQTY</td><td><span><span></span></span></td></tr><tr><td>serviceCode</td><td><span><span></span></span></td></tr><tr><td>serviceName</td><td><span><span></span></span></td></tr><tr><td>shippedQTY</td><td><span><span></span></span></td></tr><tr><td>size</td><td><span><span></span></span></td></tr><tr><td>totalPrice</td><td><span><span></span></span></td></tr><tr><td>unitOfMeasure</td><td><span><span></span></span></td></tr><tr><td>unitPrice</td><td><span><span></span></span></td></tr><tr><td>width</td><td><span><span></span></span></td></tr></tbody></table>

}

{}

{}

{

<table><tbody><tr><td>userId</td><td><span><span></span></span></td></tr><tr><td>firstName</td><td><span><span></span></span></td></tr><tr><td>lastName</td><td><span><span></span></span></td></tr><tr><td>shortUrl</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>formatTypeName</td><td><span><span></span></span></td></tr><tr><td>itemTypeName</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>toolId</td><td><span><span></span></span></td></tr><tr><td>imageFileId</td><td><span><span></span></span></td></tr><tr><td>managedMaterials</td><td><span><span></span></span></td></tr><tr><td>managedMaterialsValues</td><td><span><span></span></span></td></tr><tr><td>taskDefinitionIds</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{}

{

<table><tbody><tr><td>columnMappings</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>columnName</td><td><span><span></span></span></td></tr><tr><td>defaultValue</td><td><span><span></span></span></td></tr><tr><td>index</td><td><span><span></span></span></td></tr><tr><td>operation</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>companyTableId</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdByName</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>csvData</td><td><span><span></span></span></td></tr><tr><td>headers</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>isCloneToProjectTableEnabled</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>modifiedByName</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>notes</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>referencesCount</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>packageId</td><td><span><span></span></span></td></tr><tr><td>taskWorkflowId</td><td><span><span></span></span></td></tr><tr><td>taskDefinitionId</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>referenceType</td><td><span><span></span></span></td></tr><tr><td>referenceTypeName</td><td><span><span></span></span></td></tr><tr><td>referenceId</td><td><span><span></span></span></td></tr><tr><td>referenceCadId</td><td><span><span></span></span></td></tr><tr><td>taskStatus</td><td><span><span></span></span></td></tr><tr><td>assignedUserId</td><td><span><span></span></span></td></tr><tr><td>assignedStationId</td><td><span><span></span></span></td></tr><tr><td>logEntries</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>applyToPackageCategoryId</td><td><span><span></span></span></td></tr><tr><td>autoComplete</td><td><span><span></span></span></td></tr><tr><td>color</td><td><span><span></span></span></td></tr><tr><td>costCategoryId</td><td><span><span></span></span></td></tr><tr><td>costTypeId</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>filterIds</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>initiatedByTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>isEnabled</td><td><span><span></span></span></td></tr><tr><td>isJoin</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>referenceType</td><td><span><span></span></span></td></tr><tr><td>reportId</td><td><span><span></span></span></td></tr><tr><td>separateTaskPerFilter</td><td><span><span></span></span></td></tr><tr><td>sequenceNumber</td><td><span><span></span></span></td></tr><tr><td>taskCategoryId</td><td><span><span></span></span></td></tr><tr><td>trackingStatusApplyToAssembly</td><td><span><span></span></span></td></tr><tr><td>trackingStatusApplyToOrder</td><td><span><span></span></span></td></tr><tr><td>trackingStatusApplyToPart</td><td><span><span></span></span></td></tr><tr><td>trackingStatusBypassDialog</td><td><span><span></span></span></td></tr><tr><td>trackingStatusId</td><td><span><span></span></span></td></tr><tr><td>unitOfMeasureFieldId</td><td><span><span></span></span></td></tr><tr><td>unitVelocity</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>taskStatus</td><td><span><span></span></span></td></tr><tr><td>stationId</td><td><span><span></span></span></td></tr></tbody></table>

}

{}

integer($int32)Enum:  

{

<table><tbody><tr><td>isPartialData</td><td><span><span></span></span></td></tr><tr><td>isReadOnly</td><td><span><span></span></span></td></tr><tr><td>id<span>*</span></td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modifiedById</td><td><span><span></span></span></td></tr><tr><td>activityType</td><td><span><span></span></span></td></tr><tr><td>activityTypeName</td><td><span><span></span></span></td></tr><tr><td>divisionId<span>*</span></td><td><span><span></span></span></td></tr><tr><td>divisionName</td><td><span><span></span></span></td></tr><tr><td>email</td><td><span><span></span></span></td></tr><tr><td>employeeId</td><td><span><span></span></span></td></tr><tr><td>firstName</td><td><span><span></span></span></td></tr><tr><td>isLocked</td><td><span><span></span></span></td></tr><tr><td>lastName</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>modelName</td><td><span><span></span></span></td></tr><tr><td>packageCategoryId</td><td><span><span></span></span></td></tr><tr><td>packageCategoryName</td><td><span><span></span></span></td></tr><tr><td>packageDivisionId</td><td><span><span></span></span></td></tr><tr><td>packageDivisionName</td><td><span><span></span></span></td></tr><tr><td>packageId</td><td><span><span></span></span></td></tr><tr><td>packageName</td><td><span><span></span></span></td></tr><tr><td>packageNumber</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>projectName</td><td><span><span></span></span></td></tr><tr><td>projectNumber</td><td><span><span></span></span></td></tr><tr><td>shiftTypeId</td><td><span><span></span></span></td></tr><tr><td>startDT</td><td><span><span></span></span></td></tr><tr><td>stationDivisionId</td><td><span><span></span></span></td></tr><tr><td>stationDivisionName</td><td><span><span></span></span></td></tr><tr><td>stationId</td><td><span><span></span></span></td></tr><tr><td>stationName</td><td><span><span></span></span></td></tr><tr><td>stopDT</td><td><span><span></span></span></td></tr><tr><td>taskDefinitionId</td><td><span><span></span></span></td></tr><tr><td>userTypeName<span>*</span></td><td><span><span></span></span></td></tr><tr><td>workerId<span>*</span></td><td><span><span></span></span></td></tr></tbody></table>

}

{}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>location</td><td><span><span></span></span></td></tr><tr><td>toolType</td><td><span><span></span></span></td></tr><tr><td>toolTypeName</td><td><span><span></span></span></td></tr><tr><td>enabled</td><td><span><span></span></span></td></tr><tr><td>newStatusWhenDoneId</td><td><span><span></span></span></td></tr><tr><td>newTaskDefinitionWhenDoneId</td><td><span><span></span></span></td></tr><tr><td>labelTemplate</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>toolId</td><td><span><span></span></span></td></tr><tr><td>messageJson</td><td><span><span></span></span></td></tr><tr><td>messageType</td><td><span><span></span></span></td></tr><tr><td>projectId</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>packageId</td><td><span><span></span></span></td></tr><tr><td>assemblyId</td><td><span><span></span></span></td></tr><tr><td>toolType</td><td><span><span></span></span></td></tr><tr><td>toolTypeName</td><td><span><span></span></span></td></tr><tr><td>toolName</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>currentDivisionId</td><td><span><span></span></span></td></tr><tr><td>modifiedDT</td><td><span><span></span></span></td></tr><tr><td>modelId</td><td><span><span></span></span></td></tr><tr><td>referenceType</td><td><span><span></span></span></td></tr><tr><td>referenceName</td><td><span><span></span></span></td></tr><tr><td>referenceId</td><td><span><span></span></span></td></tr><tr><td>currentTrackingStatusId</td><td><span><span></span></span></td></tr><tr><td>totalHours</td><td><span><span></span></span></td></tr><tr><td>trackingLogEntries</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>trackingStatusId</td><td><span><span></span></span></td></tr><tr><td>createdById</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>origin</td><td><span><span></span></span></td></tr><tr><td>comment</td><td><span><span></span></span></td></tr><tr><td>hours</td><td><span><span></span></span></td></tr><tr><td>costTypeId</td><td><span><span></span></span></td></tr><tr><td>hoursCost</td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>name</td><td><span><span></span></span></td></tr><tr><td>description</td><td><span><span></span></span></td></tr><tr><td>color</td><td><span><span></span></span></td></tr><tr><td>sequenceNumber</td><td><span><span></span></span></td></tr><tr><td>canAddToAssembly</td><td><span><span></span></span></td></tr><tr><td>canAddToOrder</td><td><span><span></span></span></td></tr><tr><td>canRenumberItems</td><td><span><span></span></span></td></tr><tr><td>canAddToBOM</td><td><span><span></span></span></td></tr><tr><td>canGenerateCutList</td><td><span><span></span></span></td></tr><tr><td>appliedAtOrder</td><td><span><span></span></span></td></tr><tr><td>appliedAtAssembly</td><td><span><span></span></span></td></tr><tr><td>appliedAtPart</td><td><span><span></span></span></td></tr><tr><td>appliedAtContainer</td><td><span><span></span></span></td></tr><tr><td>onHold</td><td><span><span></span></span></td></tr><tr><td>trackingStatusGroupIds</td><td><span><span></span></span></td></tr><tr><td>trackingStatusGroups</td><td><span><span></span></span></td></tr><tr><td>trackingStatusGroupPercentageMapping</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>comment</td><td><span><span></span></span></td></tr><tr><td>costTypeId</td><td><span><span></span></span></td></tr><tr><td>createdDT</td><td><span><span></span></span></td></tr><tr><td>divisionId</td><td><span><span></span></span></td></tr><tr><td>hours</td><td><span><span></span></span></td></tr><tr><td>trackingLogEntryIdResult</td><td><span><span></span></span></td></tr><tr><td>trackingStatusId<span>*</span></td><td><span><span></span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{

<table><tbody><tr><td>cellPhone</td><td><span><span></span></span></td></tr><tr><td>companyId</td><td><span><span></span></span></td></tr><tr><td>companyName</td><td><span><span></span></span></td></tr><tr><td>dateFormat</td><td><span><span></span></span></td></tr><tr><td>email</td><td><span><span></span></span></td></tr><tr><td>firstName</td><td><span><span></span></span></td></tr><tr><td>hourFormat</td><td><span><span></span></span></td></tr><tr><td>id</td><td><span><span></span></span></td></tr><tr><td>isCheckedIn</td><td><span><span></span></span></td></tr><tr><td>isTimeTrackingEnabled</td><td><span><span></span></span></td></tr><tr><td>lastName</td><td><span><span></span></span></td></tr><tr><td>lastViewedDateTimeForAssemblyId</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>lastViewedDateTimeForModelId</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>lastViewedDateTimeForPackageId</td><td><span><span></span><span><br>nullable: true</span></span></td></tr><tr><td>longDateFormat</td><td><span><span></span></span></td></tr><tr><td>profileImageUrl</td><td><span><span></span></span></td></tr><tr><td>profileImageBase64</td><td><span><span></span></span></td></tr><tr><td>status</td><td><span><span></span></span></td></tr><tr><td>timeFormat</td><td><span><span></span></span></td></tr><tr><td>timeZoneInfoId</td><td><span><span></span></span></td></tr></tbody></table>

}

{

<table><tbody><tr><td>data</td><td><span><span></span></span></td></tr><tr><td>pageOffset</td><td><span><span></span></span></td></tr><tr><td>pageLimit</td><td><span><span></span></span></td></tr><tr><td>pageCount</td><td><span><span></span></span></td></tr><tr><td>total</td><td><span><span></span></span></td></tr><tr><td>truncatedResults</td><td><span><span></span></span></td></tr><tr><td>truncatedReason</td><td><span><span></span></span></td></tr><tr><td>filterOptions</td><td><span><span></span></span></td></tr><tr><td>links</td><td><span><span></span><span><br>nullable: true</span></span></td></tr></tbody></table>

}

integer($int32)Enum:  

{}
