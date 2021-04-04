package com.employee.employee_demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@EnableSwagger2
@Configuration
public class EmployeeSwaggerConfig {
	
	
@Bean
public Docket EmployeeAPI(){
	return new Docket(DocumentationType.SWAGGER_2)
			.select()
			.apis(RequestHandlerSelectors.basePackage("com.employee.employee_demo"))
			.paths(PathSelectors.regex("/employee.*"))
			.build()
			.apiInfo(EmployeeInfo());
			
	
}

private static final String SWAGGER_API_VERSION = "1.0";
private static final String LICENSE_TEXT = "App Ver:1.0";
private static final String title = "Employee Details";
private static final String description = "RESTful API for Employees";

private ApiInfo EmployeeInfo() {
    return new ApiInfoBuilder()
            .title(title)
            .description(description)
            .license(LICENSE_TEXT)
            .version(SWAGGER_API_VERSION)
            .build();
}

/*private ApiInfo EmployeeInfo() {
	
	ApiInfo apiInfo = new ApiInfo(
			"Employee Details",
			"Swager Example",
			"1.0", 
			"terms of Service",
			"manidharreddy41@gmail.com",
			"Apache License version 2.0",
			"Done"
			
			);
	return apiInfo;
}*/
}
