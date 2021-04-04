package com.employee.employee_demo;

import java.util.List;

public interface EmployeeService {

	public void createEmployee(Employee employee);

	public Employee getEmployee(int id);

	public Employee updateEmployee( Employee employee);

	public void deleteEmployee(int id);

	public List<Employee> getAllEmployees();

}
