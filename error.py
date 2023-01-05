class SchemaValidationError:
    def __new__(cls, validation_error):
        try:
            error_details=validation_error.details

            default_message=error_details.get("errmsg")
            
            schema_rules_not_satisfied=error_details.get("errInfo",{}).get("details", {}).get("schemaRulesNotSatisfied",[])
            rules_not_satisfied_error=[]

            for item in schema_rules_not_satisfied:

                properties_not_satisfied=item.get("propertiesNotSatisfied",[])
                
                if not properties_not_satisfied: 
                    print(f"{default_message} : {str(item)}")
                    continue

                for property in properties_not_satisfied:
                    rules_not_satisfied_error.append(property.get("description"))    
            
            if rules_not_satisfied_error:
                return rules_not_satisfied_error[0]
            else:
                return default_message
        except:
            return "Internal Server Error"
