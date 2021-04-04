package com.employee.employee_demo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

@RestController
//@RequestMapping(path = "/employee")
//@Api(value = "EmployeeControllerAPI",produces = MediaType.APPLICATION_JSON_VALUE)
public class EmployeeController {

	@Autowired
	private EmployeeService employeeService;

	public EmployeeController() {
		System.out.println("EmployeeController()");
	}

	@RequestMapping(value = "/employee", method = RequestMethod.POST)//,consumes = MediaType.APPLICATION_JSON_VALUE)
	void create(@RequestBody Employee employee) {
		employeeService.createEmployee(employee);

	}
	@RequestMapping(value = "/employee/{id}", method = RequestMethod.DELETE)
	void delete(@PathVariable("id") int id) {
		employeeService.deleteEmployee(id);

	}

	@RequestMapping(value = "/employee", method = RequestMethod.GET)
	@ApiOperation("gets employee details")
	 @ApiResponses(value = {@ApiResponse(code = 200, message = "OK", response = Employee.class)})
	List<Employee> findAll() {

		return employeeService.getAllEmployees();
	}

	@RequestMapping(value = "/employee/{id}", method = RequestMethod.GET)
	Employee findById(@PathVariable("id") int id) throws EmployeeNotFoundException {

		/*
		 * EmployeeExceptionThrower eT = new EmployeeExceptionThrower();
		 * eT.throwCustomException();
		 */
		Employee e = employeeService.getEmployee(id);

		if (e != null) {
			return e;
		}
		throw new EmployeeNotFoundException("Employee not found");

	}

	@RequestMapping(value = "/employee", method = RequestMethod.PUT)//,consumes = MediaType.APPLICATION_JSON_VALUE)
	Employee update(@RequestBody Employee employee) {
		return employeeService.updateEmployee(employee);

	}

}